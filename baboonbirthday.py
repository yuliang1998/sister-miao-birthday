# !/usr/bin/env python
# -*- coding:utf-8 -*-
#                                                           #
#                      _oo0oo_                              #
#                     o8888888o                             #
#                     88" . "88                             #
#                     (| -_- |)                             #
#                      0\ = /0                              #
#                  ____/'---'\____                          #
#                .   ' \\| |// '   .                        #
#               /   \\||| : |||//   \                       #
#              /  _||||| -:- |||||_  \                      #
#                 | | \\\ - /// | |                         #
#              |  \_| ''\---/'' | |                         #
#               \  .-\__ '-' ___/-.  /                      #
#             ___'. .' /--.--\ '. . __                      #
#          ."" '< '.___\_<|>_/___.' >'""                    #
#         | | : '- \'.;'\ _ /';.'/ - ' : | |                #
#           \ \ '-. \_ __\ /__ _/  .-' / /                  #
#   ======'-.____'-.___\_____/___.-'____.-'======           #
#                      '=---='                              #
#.....................................................      #
#    佛祖镇楼                       BUG辟易                 #
#   佛曰：                                                  #
#       写字楼里写字间，写字间里程序员；                    #
#       程序人员写程序，又拿程序换酒钱。                    #
#       酒醒只在网上坐，酒醉还来网下眠；                    #
#       酒醉酒醒日复日，网上网下年复年。                    #
#       但愿老死电脑间，不愿鞠躬老板前；                    #
#       奔驰宝马贵者趣，公交自行程序员。                    #
#       别人笑我忒疯癫，我笑自己命太贱；                    #
#       不见满街漂亮妹，哪个归得程序员？                    #
#                                                           #

import turtle
import datetime
import time


def birthday():
    def func(x, y):
        main()

    turtle.title('喵姐姐生日快乐')
    baboon = turtle.Turtle()
    baboon.hideturtle()
    baboon.getscreen().bgcolor('light blue')
    baboon.color('purple', 'red')
    baboon.pensize(1)
    baboon.speed(1)
    baboon.up()
    baboon.goto(0, -150)
    baboon.down()
    baboon.begin_fill()
    baboon.goto(0, -150)
    baboon.goto(-175.12, -8.59)
    baboon.left(140)
    pos = []
    for i in range(19):
        baboon.right(10)
        baboon.forward(20)
        pos.append((-baboon.pos()[0], baboon.pos()[1]))
    for item in pos[::-1]:
        baboon.goto(item)
    baboon.goto(175.12, -8.59)
    baboon.goto(0, -150)
    baboon.left(50)
    baboon.end_fill()
    baboon.up()
    baboon.goto(0, 80)
    baboon.down()
    baboon.write("喵姐姐", font=(u"方正舒体", 36, "normal"), align="center")
    baboon.up()
    baboon.goto(0, 0)
    baboon.down()
    baboon.write("生日快乐！", font=(u"方正舒体", 48, "normal"), align="center")
    baboon.up()
    baboon.goto(100, -210)
    baboon.down()
    turtle.reset()
    turtle.hideturtle()
    baboon.color('red', 'black')
    baboon.pensize(1)
    baboon.speed(1)
    baboon.up()
    baboon.goto(0, -150)
    baboon.down()
    baboon.begin_fill()
    baboon.goto(0, -150)
    baboon.goto(-175.12, -8.59)
    baboon.left(140)
    pos = []
    for i in range(19):
        baboon.right(10)
        baboon.forward(20)
        pos.append((-baboon.pos()[0], baboon.pos()[1]))
    for item in pos[::-1]:
        baboon.goto(item)
    baboon.goto(175.12, -8.59)
    baboon.goto(0, -150)
    baboon.left(50)
    baboon.end_fill()
    baboon.up()
    baboon.goto(0, 80)
    baboon.down()
    baboon.write("喵姐姐", font=(u"方正舒体", 36, "normal"), align="center")
    baboon.up()
    baboon.goto(0, 0)
    baboon.down()
    baboon.write("生日快乐！", font=(u"方正舒体", 48, "normal"), align="center")
    baboon.up()
    baboon.goto(100, -210)
    baboon.down()
    a = turtle.Pen()
    turtle.bgcolor("black")
    sides = 7
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    for x in range(360):
        a.pencolor(colors[x % sides])
        a.forward(x * 3 / sides + x)
        a.left(360 / sides + 1)
        a.width(x * sides / 200)


def main():
    pass


if __name__ == '__main__':
    if datetime.date.today() == datetime.date(2018, 11, 2):
        birthday()
    else:
        main()

