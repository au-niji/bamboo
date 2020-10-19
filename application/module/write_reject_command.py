from os import getenv


TEST_PATH = './../test/module_test/reject/reject_by_country.gcsh_'
PROD_PATH = './reject/reject_by_country.gcsh_'
BEGINNING_COMMAND = 'gcloud compute firewall-rules create foreign-reject-'
INTERMEDIATE_COMMAND = ' --action=DENY --rules=ALL --priority=100 --source-ranges='
SPLIT_NUM = 250


class WriteRejectCommand():
    def __init__(self):
        env = getenv('ENV')
        if env == 'DEV' or env == 'test':
            self.path = TEST_PATH
        elif env == 'PROD':
            self.path = PROD_PATH
        else:
            raise EnvironmentError('モードが正しくありません。 ENV:{}'.format(env))

    # 冒頭のコマンドを作る
    def make_command(self, country, i, l_split_ip):
        command = BEGINNING_COMMAND + country + '-' + str(i).zfill(3) + INTERMEDIATE_COMMAND
        command += ','.join(l_split_ip)
        return command

    # n個ずつのリストに分割する
    def split_list(self, l_ip, n):
        for i in range(0, len(l_ip), n):
            yield l_ip[i:i + n]

    # 特定のファイルに書き込む
    def write_file(self, l_ip, country):
        l_split_ip = list(self.split_list(l_ip, SPLIT_NUM))
        with open(self.path, mode='a') as f:
            for split_i in range(len(l_split_ip)):
                write_command = self.make_command(country, split_i, l_split_ip[split_i])
                f.writelines(write_command + '\n')
