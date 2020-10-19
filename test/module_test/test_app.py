import pytest
import os
import pathlib

from app import App

TEST_REJECT_FILE_PATH = './../test/module_test/reject/reject_by_country.gcsh_'


@pytest.fixture()
def instance():
    instance = App()
    return instance


@pytest.fixture()
def make_reject_file():
    if os.path.exists(TEST_REJECT_FILE_PATH):
        pass
    else:
        pathlib.Path(TEST_REJECT_FILE_PATH).touch()


def test_fetch_country_name(instance):
    assert instance.fetch_country_name() == ['test1', 'test2', 'test3']


# 関数を実行し、ファイルを削除した後に存在を確認する
def test_remove_reject_file(instance):
    # ファイルが存在したら削除する
    if os.path.exists(TEST_REJECT_FILE_PATH):
        pass
    else:
        pathlib.Path(TEST_REJECT_FILE_PATH).touch()
    assert os.path.exists(TEST_REJECT_FILE_PATH) is True
    instance.remove_reject_file()
    assert os.path.exists(TEST_REJECT_FILE_PATH) is False


def test_main(instance):
    instance.main()
    with open(TEST_REJECT_FILE_PATH) as f:
        line = f.readline()
    assert line == \
        'gcloud compute firewall-rules create foreign-reject-test1-000 \
--action=DENY --rules=ALL --priority=100 --source-ranges=\
1.0.1.0/24,1.0.2.0/23,1.0.8.0/21\n'
