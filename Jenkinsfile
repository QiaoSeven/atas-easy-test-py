#!/bin/groovy

// CHANGEME
// Change flow as you like
// env: Virtual environment name. You can define any number of enviroments
// clusterId: CaaS cluster ID to which you want to deploy
// namespace: Kubernetes namespace. By default get from job URL
// image: build => build new image, promote => promote image from previous environment
def FLOW = [
  [env: "beta",    clusterId: "jpe1-caas1-dev1", namespace: "${env.JOB_NAME.split('/')[3]}", image: "build"],
  [env: "release", clusterId: "jpe1-caas1-prod1", namespace: "${env.JOB_NAME.split('/')[3]}", image: "promote"]
]
def ENV_LIST = FLOW.collect{ it.env }
def flow

pipeline {
  agent {
    label 'slave'
  }
  options {
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '20'))
    timeout(time: 30, unit: 'MINUTES')
    timestamps()
  }
  parameters {
    choice(choices: ENV_LIST, description: 'Please choose environment you want to deploy!', name: 'ENVIRONMENT')
  }
  environment {
    // Get app name from Jenkins job url.
    // e.g, /Tenant/caas-pipeline/Namespace/caas-jenkins/Apps/nginx/ => APP_NAME=nginx
    APP_NAME = "${env.JOB_NAME.split('/')[5]}"

    // CHANGEME "image: nginx" in a deployment.yaml is replaced with built image url by kustomize dynamically.
    // If you want to replace different image name in a deployment.yaml, please use same image name in a deployment yaml.
    IMAGE_NAME = 'registry-jpe1.r-local.net/atas-auto-execution/python:3.9.13.1'

    MANIFEST_FILE = 'resource.yaml'
  }
  stages {
    stage('Initialization') {
      steps {
        script {
          flow = new com.rakuten.cpd.Flow(this, FLOW)
          flow.setCurrentEnv(params.ENVIRONMENT)
          env.K8S_CLUSTER_ID = flow.getClusterId()
          env.K8S_NAMESPACE  = flow.getNamespace()
        }
      }
    }

    // If you want to use USER toekn instead of ServiceAccount token, please remove following comment.
    // stage('Retrieve IAM token from user session') {
    //   steps {
    //     script {
    //       env.K8S_TOKEN = cpd.getIAMToken()
    //     }
    //   }
    // }

    // Docker file exists in same repository as manifests repository
    stage('Build and Push image') {
      when {
        expression { flow.isBuildImage() }
      }
      steps {
        script {
          // BUILD_TIMESTAMP comes from https://plugins.jenkins.io/build-timestamp/ plugin
          // If you want to use different tag, change this logic please
          def tag = "${env.BUILD_TIMESTAMP}-${env.GIT_COMMIT[0..6]}-${params.ENVIRONMENT}"

          cpd.withDockerRegistry(env.K8S_CLUSTER_ID, env.K8S_NAMESPACE) {
            // Build docker image with method of Jenkins docker plugin
            // https://jenkins.io/doc/book/pipeline/docker/
            def img = docker.build("${env.K8S_NAMESPACE}/${APP_NAME}:${tag}")
            img.push()
            env.DOCKER_IMAGE = img.imageName()
          }
        }
      }
    }

    stage('Promote image') {
      when {
        expression { flow.isPromoteImage() }
      }
      steps {
        script {
          // Retag target tag with new env name suffix
          // promoteImage method expects that your docker image tag ends with environment name
          env.DOCKER_IMAGE = cpd.promoteImage(flow, env.APP_NAME)
        }
      }
    }

    stage ('Build resource yaml') {
      steps {
        script {
          // Update image url with built image url in above stage
          sh label: 'build resource.yaml with kustomize', script: """
            ${KUSTOMIZE_HOME}/kustomize edit set image ${IMAGE_NAME}=${env.DOCKER_IMAGE}
            ${KUSTOMIZE_HOME}/kustomize build --output ${MANIFEST_FILE}
          """

          // cpd.getNameFromManifest only support single resource
          // If you want to check rollout status of multiple deployments, please set DEPLOY_NAME statically and call kubectl rollout status twice.
          env.DEPLOY_NAME = cpd.getNameFromManifest(file: env.MANIFEST_FILE, kind: 'Deployment')
        }
      }
      post {
        success {
          archiveArtifacts env.MANIFEST_FILE
        }
      }
    }

    stage ('Apply manifests') {
      steps {
        script {
          def APPLY_STATUS = cpd.kubectl("apply -f ${MANIFEST_FILE}")
          if (APPLY_STATUS > 0) {
            error("\u001B[31m Applyment is failed. Please check syntax of resource yaml, your permission or try to logout/login Jenkins to refresh token.\u001B[0m ")
          }
        }
      }
    }

    stage('Watch the status of the rollout') {
      when { expression { return env.DEPLOY_NAME } }
      steps {
        script {
          // Wait until deployment become ready
          def ROLLOUT_STATUS = cpd.kubectl("rollout status deployment ${DEPLOY_NAME}")
          if (ROLLOUT_STATUS > 0) {
            error("\u001B[31m Rollout deployment ${DEPLOY_NAME} is failed.\nref \u001B[0m https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/ ")
            cpd.kubectl("get events | grep ${DEPLOY_NAME}")
          }
        }
      }
      post {
        aborted {
          script {
            echo "\u001B[31m Rollout deployment ${DEPLOY_NAME} is timeout.\nref \u001B[0m https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/ "
            cpd.kubectl("get events | grep ${DEPLOY_NAME}")
          }
        }
      }
    }

    stage ('Automation-pull code') {
      steps {
        script {
//           def POD_NAME = cpd.executeCommand("kubectl get pods | grep ${DEPLOY_NAME} | awk '{print \$1}' | head -n 1")
          def POD_NAME = cpd.kubeGetKey(name:"auto-env", kind:"pod", "name")
          cpd.kubectl("exec -it ${POD_NAME} -- git clone ssh://git@git.rakuten-it.com:7999/poc-atas/atas-easy-test-py.git /root/atas-easy-test-py")
        }
      }
    }
    stage ('Automation-install dependence') {
      steps {
        script {
          cpd.kubectl("pip3 install -r /root/atas-easy-test-py/requirements.txt")
          cpd.kubectl("sed -i 's/10.13.71.101:7108/stg-acntdatas102z.stg.jp.local:8080/g' /root/atas-easy-test-py/pytest.ini")
          cpd.kubectl("sed -i 's/ATAS_AUTO_PROJECT/ATAS_PROJ_STG/g' /root/atas-easy-test-py/pytest.ini")
          cpd.kubectl("sed -i 's/312d7764-37cc-42b6-964d-53fa4500c63e/3aafadca-b911-41b3-9508-48f86ef9b0f3/g' /root/atas-easy-test-py/pytest.ini")
          cpd.kubectl("ln -s /usr/local/python3.9.13/bin/pytest /usr/bin/pytest")
        }
      }
    }
    stage ('Automation-execution') {
      steps {
        script {
          cpd.kubectl("sh /root/atas-easy-test-py/shell/py-selenium-run-ui-docker-stg.sh cloud")
        }
      }
    }
  }
  post {
    always {
      // Clean up workspace to avoid mixing with the results of previous builds
      // If you want to debug, comment out following line please
      cleanWs()
    }
  }
}