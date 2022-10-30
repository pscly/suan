import requests
import time
import os


def get_pc_name():
    return os.getenv('COMPUTERNAME') 
def get_pc_user_name():
    return os.getenv('USERNAME') 
def get_pc_time():
    return time.strftime("%Y-%m-%d")
def get_pc_all():
    return get_pc_name()+'-'+get_pc_user_name()

def send1(file='log.txt', to_file_name='a1.txt'):
    """ 
    args:
        file: 要发送的文件
        to_file_name: 发送到的文件名(会自动拼接)
    """ 
    url = 'http://pscly.cn:31002/files/up'
    if not os.path.isfile(file):
        open(file, 'w')
    file = open(file=file, mode='rb')
    s_data = {
        'file_name': f'tosuan_{get_pc_all()}{to_file_name}',
    }
    r = requests.post(url, data=s_data, files={'file': file})

if __name__ == '__main__':
    send1('main.py', 'main.py')
