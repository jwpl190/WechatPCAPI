# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 14:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    : 
# @Software: PyCharm

from WechatPCAPI import WechatPCAPI
import time


# 接收消息的回调函数，可自行定义
def on_message(message):
    print(message)


def main():
    # 初始化wx实例
    wx_inst = WechatPCAPI(on_message=on_message)

    # 启动微信 目前仅支持微信V2.7.1.82
    wx_inst.start_wechat(block=True)

    # 等待登陆成功，此时需要人为扫码登录微信
    while not wx_inst.get_myself():
        time.sleep(5)

    # 登录成功了
    print(wx_inst.get_myself())

    # 以下尝试发送各类消息给文件传输助手，可以换成任何人的wx_id
    wx_inst.send_text(to_user='filehelper', msg='777888999')
    wx_inst.send_link_card(
        to_user='filehelper',
        title='我的博客',
        desc='我的博客，红领巾技术分享网站',
        target_url='http://www.honglingjin.online/',
        img_url=''
    )
    wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    wx_inst.send_file(to_user='filehelper', file_abspath=r'C:\Users\Leon\Desktop\1.txt')
    wx_inst.send_gif(to_user='filehelper', gif_abspath=r'C:\Users\Leon\Desktop\08.gif')
    wx_inst.send_card(to_user='filehelper', wx_id=wx_inst.wx_id)

    time.sleep(10)
    # 更新所有好友信息，数据会通过上面的回调函数返回
    wx_inst.update_frinds()


if __name__ == '__main__':
    main()
