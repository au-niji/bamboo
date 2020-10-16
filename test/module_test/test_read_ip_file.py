import pytest

from module.read_country_ip import ReadCountryIP

DATA_LIST = [
    '1.0.1.0/24',
    '1.0.2.0/23',
    '1.0.8.0/21'
]
# 重複するIP addressを持つリスト
DUPLICATING_DATA_LIST = [
    '1.0.1.0/24',
    '1.0.2.0/23',
    '1.0.2.0/23',
    '1.0.8.0/21'
]


@pytest.fixture()
def instance():
    instance = ReadCountryIP('test')
    return instance


@pytest.fixture()
def instance2():
    instance2 = ReadCountryIP('test2')
    return instance2


def test_read_file(instance, instance2):
    assert instance.read_file() == DATA_LIST
    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError


def test_remove_duplicate(instance):
    assert instance.remove_duplicate(DATA_LIST) == DATA_LIST
    assert instance.remove_duplicate(DUPLICATING_DATA_LIST) == DATA_LIST
