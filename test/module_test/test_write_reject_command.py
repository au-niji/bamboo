import os

import pytest

from module.read_country_ip import ReadCountryIP
from module.write_reject_command import WriteRejectCommand


@pytest.fixture()
def instance():
    instance = WriteRejectCommand()
    return instance


@pytest.fixture()
def data():
    read_country_ip = ReadCountryIP()
    data = read_country_ip.read_file("test3")
    return data


# 3個ずつ分けられた状態のファイル
@pytest.fixture()
def data2(instance):
    read_country_ip = ReadCountryIP()
    l_ip = read_country_ip.read_file("test1")
    data2 = list(instance.split_list(l_ip, 3))
    return data2


def test_make_command(instance, data2):
    assert instance.make_command(country='test1', i=0, l_split_ip=data2[0]) == \
'gcloud compute firewall-rules create foreign-reject-test1-000 \
--action=DENY --rules=ALL --priority=100 --source-ranges=\
1.0.1.0/24,1.0.2.0/23,1.0.8.0/21'


# 253個のデータを使う
def test_split_list(instance, data):
    assert len(data) == 253
    assert len(list(instance.split_list(data, 250))[0]) == 250
    assert len(list(instance.split_list(data, 250))[1]) == 3
    assert list(instance.split_list(data, 250))[0][0] == '1.0.1.0/24'


def test_write_file(instance, data):
    path = './../test/module_test/reject/reject_by_country.gcsh_'
    # ファイルが既に存在していたら削除
    if os.path.exists(path):
        os.remove(path)
    assert os.path.exists(path) == False
    instance.write_file(data, country='test3')
    assert os.path.exists(path) == True
    # 書き込まれたファイルの中身を確認
    with open(path) as f:
        assert f.readlines()[1] == \
'gcloud compute firewall-rules create foreign-reject-test3-001 \
--action=DENY --rules=ALL --priority=100 --source-ranges=\
43.225.140.0/22,43.225.172.0/22,43.225.180.0/22\n'
