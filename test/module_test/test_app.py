import pytest
from os import getenv, path
import pathlib

from app import App


@pytest.fixture()
def instance():
    instance = App()
    return instance


@pytest.fixture()
def reject_file_path():
    reject_folder_path = getenv('REJECT_FOLDER_PATH')
    reject_file_name = getenv('REJECT_FILE_NAME')
    reject_file_full_path = str(reject_folder_path) + str(reject_file_name)
    return reject_file_full_path


@pytest.fixture()
def make_reject_file(reject_file_path):
    if path.exists(reject_file_path):
        pass
    else:
        pathlib.Path(reject_file_path).touch()


def test_fetch_country_name(instance):
    assert instance.fetch_country_name() == ['test1', 'test2', 'test3']


# 関数を実行し、ファイルを削除した後に存在を確認する
def test_remove_reject_file(instance, reject_file_path, make_reject_file):
    # ファイルが存在したら削除する
    if path.exists(reject_file_path):
        pass
    else:
        pathlib.Path(reject_file_path).touch()
    assert path.exists(reject_file_path) is True
    instance.remove_reject_file()
    assert path.exists(reject_file_path) is False


def test_main(instance, reject_file_path):
    instance.main()
    with open(reject_file_path) as f:
        line = f.readline()
    assert line == \
        'gcloud compute firewall-rules create foreign-reject-test1-000 \
--action=DENY --rules=ALL --priority=100 --source-ranges=\
1.0.1.0/24,1.0.2.0/23,1.0.8.0/21\n'
