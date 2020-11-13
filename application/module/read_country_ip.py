from os import getenv
import re


class ReadCountryIP():
    def __init__(self, ipv4_folder_path):
        self.path = ipv4_folder_path

    # 同じIP address があった場合削除する
    def remove_duplicate(self, l_ip):
        l_unique_ip = sorted(set(l_ip[:]), key=l_ip.index)
        return l_unique_ip

    # 特定の国名のファイルを読み込みモードで開く
    def read_file(self, country):
        file_path = self.path + country + '.txt'
        try:
            with open(file_path) as f:
                match_pattern = r'^\s*(#.*|)$'
                line = f.readline()
                l_strip = []
                while line:
                    match = re.match(match_pattern, line)
                    if not match:
                        l_strip.append(line.rstrip())
                    line = f.readline()
                l_ip = self.remove_duplicate(l_strip)
                return l_ip
        except FileNotFoundError:
            raise FileNotFoundError('ファイルが見つかりません。PATH:{}'.format(self.path))
