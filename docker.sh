#!/usr/bin/bash

TEST_FOLDER_PATH=../test/module_test/
COMMAND=$1 # up か downを指定する
ENV=${2:-prod} # prod、testを指定する。デフォルトではprod
TEST_FILE=$3 # テストするファイル名

case $1 in
    up )
        if [ $ENV = test ]; then
            TEST_FILE=$TEST_FOLDER_PATH$TEST_FILE docker-compose -f docker-compose.yml -f docker-compose.$ENV.yml up
        elif [ $ENV = prod ]; then
            docker-compose -f docker-compose.yml -f docker-compose.$ENV.yml up
        fi
        ;;
    down )
        docker-compose down;;
esac
