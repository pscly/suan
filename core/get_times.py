""" 
返回正常时间
""" 

import time
import datetime
import cnlunar
from addict import Dict

class time1():
    def __init__(self):
        self.time = self.get_now_time()
        self.time2 = self.get_time()
        self.times = Dict({
            'nian': self.get_nian(),
            'yue': self.get_yue(),
            'ri': self.get_ri(),
            'shi': self.get_shi(),
            'fen': self.get_fen(),
            'miao': self.get_miao(),
            # 2 代表取数字
            'nian2': self.get_nian(),
            'yue2': self.get_yue(),
            'ri2': self.get_ri(),
            'shi2': self.get_shi(),
            'fen2': self.get_fen(),
            'miao2': self.get_miao(),
        })
    
    def get_now_time(self):
        in_time = input('请输入时间 (2022-10-27-19-11)(年月日时分) \n 如果是当前时间就请输入空\n>:').strip()
        if in_time == '':
            return time.time()
        if in_time.count('-') != 4:
            print('输入错误')
            return self.get_now_time()
        return time.mktime(time.strptime(in_time, '%Y-%m-%d-%H-%M')) - 60*60    # 成都地域的原因 
        
    def get_time(self):
        """ 
        返回年月时分秒
        return 2022,09,04,21,13,31
        """
        return self.get_nian(), self.get_yue(), self.get_ri(), self.get_shi(), self.get_fen(), self.get_miao()


    def get_nian(self):
        """ 
        返回年
        return 2022
        """
        t1 = int(time.strftime('%Y', time.localtime(self.time)))
        return t1


    def get_yue(self):
        """ 
        返回月
        return 09
        """
        t1 = int(time.strftime('%m', time.localtime(self.time)))
        return t1


    def get_ri(self):
        """ 
        返回日
        return 04
        """
        t1 = int(time.strftime('%d', time.localtime(self.time)))
        return t1

    def get_shi(self):
        """ 
        返回时
        return 21
        """
        t1 = int(time.strftime('%H', time.localtime(self.time)))
        return t1

    def get_fen(self):
        """ 
        返回分
        return 13
        """
        t1 = int(time.strftime('%M', time.localtime(self.time)))
        return t1

    def get_miao(self):
        """ 
        返回秒
        return 31
        """
        t1 = int(time.strftime('%S', time.localtime(self.time)))
        return t1



if __name__ == '__main__':
    t1 = time1()
    print(t1.get_time())
    
