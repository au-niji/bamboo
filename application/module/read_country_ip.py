from os import getenv
import re

TEST_PATH = './../test/module_test/ipv4/'
PROD_PATH = './ipv4/'


class ReadCountryIP():
    def __init__(self, country):
        env = getenv('ENV')
        if env == 'DEV' or env == 'test':
            self.path = TEST_PATH + country + '.txt'
        elif env == 'PROD':
            self.path = PROD_PATH + country + '.txt'
        else:
            raise EnvironmentError('モードが正しくありません。 ENV:{}'.format(env))

    # 同じIP address があった場合削除する
    def remove_duplicate(self, l_ip):
        l_unique_ip = sorted(set(l_ip[:]), key=l_ip.index)
        return l_unique_ip

    # 特定の国名のファイルを読み込みモードで開く
    def read_file(self):
        try:
            with open(self.path) as f:
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
