# WechatPCAPI
微信PC版的API接口，可通过Python调用微信获取好友、群、公众号列表，并收发消息等功能。可用于二次开发在线微信机器人、微信消息监控、群控软件、开发界面作多个微信控制软件等用途。

当前版本:@钊@

如果帮到你，帮我点个star。

## 功能列表

目前支持：

1. 微信多开
2. 获取好友、群、公众号列表
3. 接收消息（包括好友、群、公众号消息）
4. 发送消息（支持文本、图片、分享链接、文件、名片等格式）

待完成：

1. 公众号关注
2. 群控功能（建群、拉人进群、退群、踢人、@某人、发布群公告等功能）
3. 加好友、删好友
4. 反消息撤回等


## 怎么用？

目前提供pyd和依赖的相关文件，通过python直接import即可使用，如下：

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

## 环境支持情况

windows 7/10 测试通过

python 3.7.4 理论上支持python3.6以后所有版本

微信版本 目前仅支持V2.7.1.82版本，后续会考虑兼容其他版本，目录包里有该微信版本，直接下载安装即可。

## 函数文档注释

不知道怎么调用的话，可以使用``help(类名)``查看函数文档，如下：

    Help on class WechatPCAPI in module WechatPCAPI:

    class WechatPCAPI(builtins.object)
     |  WechatPCAPI(on_message=None, on_wx_exit_handle=None, log=None)
     |
     |  微信PC版的API接口--当前版本:@钊@
     |
     |  Methods defined here:
     |
     |  __init__(self, on_message=None, on_wx_exit_handle=None, log=None)
     |      类初始化函数
     |      :param on_message: 收到微信消息时的回调函数
     |      :param on_wx_exit_handle: 微信退出的回调函数，可空
     |      :param log: 日志句柄
     |
     |  get_myself(self)
     |      获取我的信息，即所登录账号的信息
     |      :return: 尚未登陆成功时为None, 登陆成功后为dict格式返回
     |
     |  send_card(self, to_user, wx_id)
     |      发送名片
     |      :param to_user: 发给谁（wx_id）
     |      :param wx_id: 要发送谁的名片（wx_id）
     |      :return: 无
     |
     |  send_file(self, to_user, file_abspath)
     |      发送文件
     |      :param to_user: 发给谁（wx_id）
     |      :param file_abspath: 文件在本地的绝对路径
     |      :return: 无
     |
     |  send_gif(self, to_user, gif_abspath)
     |      发送gif表情
     |      :param to_user: 发给谁（wx_id）
     |      :param gif_abspath: gif在本地的绝对路径
     |      :return: 无
     |
     |  send_img(self, to_user, img_abspath)
     |      发送图片
     |      :param to_user: 发给谁（wx_id）
     |      :param img_abspath: 图片在本地的绝对路径
     |      :return: 无
     |
     |  send_link_card(self, to_user, title, desc, target_url, img_url='')
     |      发送链接分享
     |      :param to_user: 发给谁（wx_id）
     |      :param title: 链接标题
     |      :param desc: 链接描述
     |      :param target_url: 链接URL
     |      :param img_url: 显示图片的URL
     |      :return: 无
     |
     |  send_text(self, to_user, msg)
     |      发送文本消息
     |      :param to_user: 发给谁（wx_id）
     |      :param msg: 文本消息内容
     |      :return: 无
     |
     |  start_wechat(self, block=True)
     |      启动微信，目前仅支持微信版本v2.7.1.82
     |      :param block: 是否阻塞，默认阻塞
     |      :return: 无
     |
     |  update_frinds(self)
     |      :return: 无
     |
     |  ----------------------------------------------------------------------


## 联系我

关注微信公众号“燕幕自安”，即可获取我的联系方式。

## 赞赏我

支持作者继续更新，请我喝杯咖啡

<img src="https://github.com/Mocha-L/findtheone/blob/master/pic/ali.png" width="230px" /><img src="https://github.com/Mocha-L/findtheone/blob/master/pic/wechat.png" width="230px" />

## 声明

**本项目仅供技术研究，请勿用于非法用途，如有任何人凭此做何非法事情，均于作者无关，特此声明。**
