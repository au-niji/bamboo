import pathlib
from os import (getenv, path, remove)

from module.read_country_ip import ReadCountryIP
from module.write_reject_command import WriteRejectCommand


COUNTRY_FILE_PATH = './ipv4/'
REJECT_FILE_PATH = './reject/reject_by_country.gcsh_'
TEST_COUNTRY_FILE_PATH = './../test/module_test/ipv4'
TEST_REJECT_FILE_PATH = './../test/module_test/reject/reject_by_country.gcsh_'

read_country_ip = ReadCountryIP()
write_rejcet_command = WriteRejectCommand()


class App():
    def __init__(self):
        env = getenv('ENV')
        if env == 'DEV' or env == 'test':
            self.c_path = TEST_COUNTRY_FILE_PATH
            self.r_path = TEST_REJECT_FILE_PATH
        elif env == 'PROD':
            self.c_path = COUNTRY_FILE_PATH
            self.r_path = REJECT_FILE_PATH
        else:
            raise EnvironmentError('モードが正しくありません。 ENV:{}'.format(env))

    # 国別ファイルの名前を取得
    def fetch_country_name(self):
        l_country_name = []
        files = pathlib.Path(self.c_path).glob('*')
        for file in files:
            l_country_name.append(file.stem)
        return l_country_name

    # rejectファイルが存在していたら削除
    def remove_reject_file(self):
        if path.exists(self.r_path):
            remove(self.r_path)

    def main(self):
        self.remove_reject_file()
        l_coiuntry_name = self.fetch_country_name()
        for c_name in l_coiuntry_name:
            l_ip = read_country_ip.read_file(c_name)
            write_rejcet_command.write_file(l_ip, c_name)


if __name__ == '__main__':
    instance = App()
    instance.main()
