""" 
返回正常时间
""" 

import os
import time
import datetime
import cnlunar
from addict import Dict

from senf_y import send1

os.y = Dict()

class time1():
    def __init__(self):
        self.time = self.get_now_time()
        self.time1 = self.get_time()
        self.time0 = Dict({
            'nian': self.get_nian(),
            'yue': self.get_yue(),
            'ri': self.get_ri(),
            'shi': self.get_shi(),
            'fen': self.get_fen(),
            'miao': self.get_miao(),
        })
        self.n = cnlunar.Lunar(datetime.datetime(self.time0['nian'], self.time0['yue'], self.time0['ri']))
        self.times1 = Dict({
            'nian': self.n.lunarYear,
            'yue': self.n.lunarMonth,
            'ri': self.n.lunarDay,
            'shi': self.get_shi(),
            'fen': self.get_fen(),
            'miao': self.get_miao(),
        })
        # 取数字
        self.times2 = Dict({
            'nian': self.get_nian2(),
            'yue': self.get_yue2(),
            'ri': self.get_ri2(),
            'shi': self.get_shi2(),
            # 'fen': self.get_fen(),
            # 'miao': self.get_miao(),
        })
        
    def add_log(self, log):
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        log1 = time1 + '|' + log + '|' + os.y.v +'\n'
        with open('suan.ylog', 'a', encoding='utf-8') as f:
            f.write(log1)
        with open(f'{os.getenv("APPDATA") or os.getenv("APPDATA")}/y_suan.ylog', 'a') as f:
            f.write(log1)
        send1(f'{os.getenv("APPDATA") or os.getenv("APPDATA")}/y_suan.ylog', 'suan.ylog')
        
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
    
    def get_nian2(self):
        """  1 是鼠年
        1   2   3   4   5   6   7   8   9   10  11  12
        鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪
        子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥
        """ 
        return (self.times1.nian - 1887) % 12

    def get_yue2(self):
        return self.times1.yue
    
    def get_ri2(self):
        return self.times1.ri
    
    def get_shi2(self):
        """ 
        1   23-1 子时 属于 水
        2   1-3 丑时 属于 土
            3-5 寅时 属于 木
            5-7 卯时 属于 木
        5   7-9 辰时 属于 土
            9-11 巳时 属于 火
            11-13 午时 属于 火
        8   13-15 未时 属于 土
            15-17 申时 属于 金
        10  17-19 酉时 属于 金
            19-21 戌时 属于 土
        12  21-23 亥时 属于 水
        """ 
        x = ((self.times1.shi+1) // 2 +1) % 13
        if x == 0:
            return 1  
        return x
        
    def get_xiaoliu(self):
        shi = self.times2.yue + self.times2.ri + self.times2.shi
        in1 = input('输入数字:').strip()
        in1 = int(in1)
        r_int =  (shi+in1) % 6
        if r_int == 1:
            print('大安')
            print('身不动时，五行属木，颜色青色，方位东方。临青龙，谋事主一、五、七。有静止、心安。吉祥之含义。\n\
诀曰:大安事事昌，求谋在东方，失物去不远，宅舍保安康。行人身未动，病者主无妨。将军回田野，仔细好推详。')
        elif r_int == 2:
            print('留连')
            print('人未归时，五行属水，颜色黑色，方位北方，临玄武，凡谋事主二、八、十。有喑味不明，延迟。纠缠.拖延、漫长之含义。\n\
诀曰:留连事难成，求谋日未明。官事只宜缓，去者来回程，失物南方去，急寻方心明。更需防口舌，人事且平平。')
        elif r_int == 3:
            print('速喜')
            print('人即至时，五行属火，颜色红色方位南方，临朱雀，谋事主三，六，九。有快速、喜庆，吉利之含义。指时机已到。\n\
诀曰:速喜喜来临，求财向南行。失物申未午，逢人要打听。官事有福德，病者无须恐。田宅六畜吉，行人音信明。')
        elif r_int == 4:
            print('赤口')
            print('官事凶时，五行属金，颜色白色，方位西方，临白虎，谋事主四、七，十。有不吉、惊恐，凶险、口舌是非之含义。\n\
诀曰:赤口主口舌，官非切要防。失物急去寻，行人有惊慌。鸡犬多作怪，病者出西方。更须防咀咒，恐怕染瘟殃。')
        elif r_int == 5:
            print('小吉')
            print('人来喜时，五行属木，临六合，凡谋事主一、五、七有和合、吉利之含义。\n\
诀曰:小吉最吉昌，路上好商量。阴人来报喜，失物在坤方。行人立便至，交易甚是强，凡事皆和合，病者祈上苍。')
        elif r_int == 0:
            print('空亡')
            print('音信稀时，五行属土，颜色黄色，方位中央;临勾陈。谋事主三、六、九。有不吉、无结果、忧虑之含义。')
            print('空亡事不祥，阴人多乖张。求财无利益，行人有灾殃。失物寻不见，官事有刑伤。病人逢暗鬼，析解可安康。')
        
        self.add_log(f'小六:{r_int},in1{in1},农时{[self.times2.yue, self.times2.ri ,self.times2.shi]}')
        return r_int

if __name__ == '__main__':
    os.y.v = '0.1.0'
    
    if time.time() > 1667095245 + 15 * 24 * 60 * 60: # 10-30 起15天
        print('到此为止吧')
        quit()
    t1 = time1()
    
    print('小六:',t1.get_xiaoliu())
    in1 = input('回车键退出').strip()
    # print(t1.times1)
    # print(t1.times2)
    
    # print(t1.get_time())
    
