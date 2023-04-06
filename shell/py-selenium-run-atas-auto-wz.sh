#!/bin/bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=''
fi

export ATAS_CONF=${ENV}
pytest -s /Users/zhuo.b.wang/atas-easy-test-py/testcase/auto-test --reportportal
export ATAS_CONF=''