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
        ipv4_folder_path = getenv('IPv4_FOLDER_PATH')
        reject_folder_path = getenv('REJECT_FOLDER_PATH')
        self.country_directory_path = ipv4_folder_path
        self.reject_file_path = reject_folder_path

    # 国別ファイルの名前を取得
    def fetch_country_name(self):
        l_country_name = []
        files = pathlib.Path(self.country_directory_path).glob('*')
        for file in files:
            l_country_name.append(file.stem)
        return l_country_name

    # rejectファイルが存在していたら削除
    def remove_reject_file(self):
        if path.exists(self.reject_file_path):
            remove(self.reject_file_path)

    def main(self):
        self.remove_reject_file()
        l_coiuntry_name = self.fetch_country_name()
        for country_name in l_coiuntry_name:
            l_ip = read_country_ip.read_file(country_name)
            write_rejcet_command.write_file(l_ip, country_name)


if __name__ == '__main__':
    instance = App()
    instance.main()
