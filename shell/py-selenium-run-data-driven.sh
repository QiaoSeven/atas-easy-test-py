#!/bin/bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=dev
fi

export ATAS_CONF=${ENV}
pytest -s /Users/tao.ding/PycharmProjects/atas-easy-test-py/testcase/data-driven/ --reportportal
