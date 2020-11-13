#!/usr/bin/bash

TEST_FOLDER_PATH=../test/module_test/
TEST_FILE=$1 # テストするファイル名

TEST_FILE=$TEST_FOLDER_PATH$TEST_FILE docker-compose -f docker-compose.yml -f docker-compose.test.yml up
