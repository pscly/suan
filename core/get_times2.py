""" 
此处返回的是特殊时间

子时——晚11点钟到凌晨1点钟
丑时——1点钟至3点钟
寅时——3点钟至5点钟
卯辰——5点钟至7点钟
辰时——7点钟至9点钟
巳时——9点钟至11点钟
午时——11点钟至下午1点钟
未时——13点钟至15点钟
申时——下午3点钟至5点钟
酉时——下午5点钟至7点钟
戌时——下午7点钟至晚9点钟
亥时——晚9点钟至11点钟。

"""
import time
import datetime
import cnlunar
# from get_times import get

if __name__ == '__main__':
    
    a = cnlunar.Lunar(datetime.datetime(2001, 9, 8, 6, 58))
    a = cnlunar.Lunar()
    dic = {
        '日期': a.date,
        '农历数字': (a.lunarYear, a.lunarMonth, a.lunarDay, '闰' if a.isLunarLeapMonth else ''),
        # '农历': '%s %s[%s]年 %s%s' % (a.lunarYearCn, a.year8Char, a.chineseYearZodiac, a.lunarMonthCn, a.lunarDayCn),
        # '星期': a.weekDayCn,
        # # 未增加除夕
        # '今日节日': (a.get_legalHolidays(), a.get_otherHolidays(), a.get_otherLunarHolidays()),
        # '八字': ' '.join([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char]),
        # '今日节气': a.todaySolarTerms,
        # '下一节气': (a.nextSolarTerm, a.nextSolarTermDate, a.nextSolarTermYear),
        # # '今年节气表': a.thisYearSolarTermsDic,
        # '季节': a.lunarSeason,
        '今日时辰': a.twohour8CharList,
        # '时辰凶吉': a.get_twohourLuckyList(),
        # '生肖冲煞': a.chineseZodiacClash,
        # '星座': a.starZodiac,
        # '星次': a.todayEastZodiac,
        # '彭祖百忌': a.get_pengTaboo(),
        # '彭祖百忌精简': a.get_pengTaboo(long=4, delimit='<br>'),
        # '十二神': a.get_today12DayOfficer(),
        # '廿八宿': a.get_the28Stars(),
        # '今日三合': a.zodiacMark3List,
        # '今日六合': a.zodiacMark6,
        # '今日五行': a.get_today5Elements(),
        # '纳音': a.get_nayin(),
        # '九宫飞星': a.get_the9FlyStar(),
        # '吉神方位': a.get_luckyGodsDirection(),
        # '今日胎神': a.get_fetalGod(),
        # '神煞宜忌': a.angelDemon,
        # '今日吉神': a.goodGodName,
        # '今日凶煞': a.badGodName,
        # '宜': a.goodThing,
        # '忌': a.badThing,
        # '时辰经络': a.meridians
    }
    print(dic)
