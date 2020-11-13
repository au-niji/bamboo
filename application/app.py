import pathlib
from os import (getenv, path, remove)

from module.read_country_ip import ReadCountryIP
from module.write_reject_command import WriteRejectCommand

ipv4_folder_path = getenv('IPv4_FOLDER_PATH')
reject_folder_path = getenv('REJECT_OUTPUT_FOLDER_PATH')
reject_file_name = getenv('REJECT_FILE_NAME')
reject_file_path = str(reject_folder_path) + str(reject_file_name)
country_folder_path = str(ipv4_folder_path)

read_country_ip = ReadCountryIP(country_folder_path)
write_rejcet_command = WriteRejectCommand(reject_file_path)


class App():
    def __init__(self):
        self.country_directory_path = str(ipv4_folder_path)
        self.reject_file_full_path = reject_file_path

    # 国別ファイルの名前を取得
    def fetch_country_name(self):
        l_country_name = []
        files = pathlib.Path(self.country_directory_path).glob('*')
        for file in files:
            l_country_name.append(file.stem)
        return l_country_name

    # rejectファイルが存在していたら削除
    def remove_reject_file(self):
        if path.exists(self.reject_file_full_path):
            remove(self.reject_file_full_path)

    def main(self):
        self.remove_reject_file()
        l_coiuntry_name = self.fetch_country_name()
        for country_name in l_coiuntry_name:
            l_ip = read_country_ip.read_file(country_name)
            write_rejcet_command.write_file(l_ip, country_name)


if __name__ == '__main__':
    instance = App()
    instance.main()
