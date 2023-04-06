#!/bin/bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=dev
fi

export ATAS_CONF=${ENV}
pytest -n 2 /Users/tao.ding/PycharmProjects/atas-easy-test-py/testcase/mobile --reportportal
