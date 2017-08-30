# -*- coding:utf-8 -*-

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def adbkeyevent(keyword):
    dict1 = {0: 7,
             1: 8,
             2: 9,
             3: 10,
             4: 11,
             5: 12,
             6: 13,
             7: 14,
             8: 15,
             9: 16,
             "A": 29,
             "B": 30,
             "C": 31,
             "D": 32,
             "E": 33,
             "F": 34,
             "G": 35,
             "H": 36,
             "I": 37,
             "J": 38,
             "K": 39,
             "L": 40,
             "M": 41,
             "N": 42,
             "O": 43,
             "P": 44,
             "Q": 45,
             "R": 46,
             "S": 47,
             "T": 48,
             "U": 49,
             "V": 50,
             "W": 51,
             "X": 52,
             "Y": 53,
             "Z": 54}

    keywords = list(keyword)  # 将字符串转换为以单个元素为单位的数组

    for x in keywords:
        if x.isdigit():  # 判断是否为数字
            b = dict1[int(x)]
            os.popen("adb shell input keyevent " + str(b))
        else:
            a = x.upper()  # 小写转大写
            if dict1.has_key(a):  # 判断字典是否包含参数，比如@不包含，即执行else # a in dict1.keys()方法也可用
                b = dict1[a]
                os.popen("adb shell input keyevent " + str(b))
            else:
                os.popen("adb shell input text " + str(a))


def adbtap(x, y):
    os.popen("adb shell input tap " + str(x) + " " + str(y))


def adbswipe(x1, y1, x2, y2):
    os.popen("adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))

# adbtap(376,1718)
# adbkeyenent("qwea@sd123")
# adbswipe(666,1460,666,500)
