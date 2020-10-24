# 本番では make [cmd] e=prod とする

# test or prod
ENV:=test
# testで実行する時にフォルダかファイルを指定
TEST_FILE:=../test/module_test/
APP_NAME:=app
EXEC_COMMAND:=bash

pre:
# e: ステージ設定(デフォルトだとtest)
ifdef e
ENV=${e}
endif

# f: ユニットテストを行うファイル名指定(デフォルトだとフォルダーごと指定)
ifdef f
TEST_FILE:=$(join $(TEST_FILE), $(f))
endif

# n: コンテナ名を指定(デフォルトだとapp)
ifdef n
APP_NAME=$(n)
endif

# c: コマンドを指定(デフォルトだとbash)
ifdef c
EXEC_COMMAND=$(c)
endif

# これよりmakeの後ろにつける引数によって変わる
# ENVの値によって実行する環境を変える
up: pre
ifeq ($(ENV), prod)
	docker-compose -f docker-compose.yml -f docker-compose.$(ENV).yml up -d
endif
ifeq ($(ENV), test)
	TEST_FILE=$(TEST_FILE) docker-compose -f docker-compose.yml -f docker-compose.$(ENV).yml up
endif

down: pre
	docker-compose down

rebuild: pre
	docker-compose build --no-cache

exec: pre
	docker-compose exec $(APP_NAME) $(EXEC_COMMAND)
