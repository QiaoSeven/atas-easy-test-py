#!/bin/bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=''
fi

export ATAS_CONF=${ENV}
pytest -s /root/atas-easy-test-py/testcase/atas-smoking/ --reportportal
echo 'This execution is completed!'
export ATAS_CONF=''