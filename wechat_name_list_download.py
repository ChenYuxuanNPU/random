import time

import numpy as np
import pandas as pd
import psutil
import pywinauto
from pywinauto.application import Application


def get_wechat_pid():
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == 'WeChat.exe':
            return pid
    return None


def get_name_list(pid):
    print('>>> WeChat.exe pid: {}'.format(pid))
    print('>>> 请打开【微信=>目标群聊=>聊天成员=>查看更多】，尤其是【查看更多】，否则查找不全！')
    for i in range(30):
        print('\r({:2d} 秒)'.format(30 - i), end='')
        time.sleep(1)
    app = Application(backend='uia').connect(process=pid)
    win_main_dialog = app.window(class_name='WeChatMainWndForPC')
    chat_list = win_main_dialog.child_window(control_type='List', title='聊天成员')
    name_list = []
    all_members = []
    for i in chat_list.items():
        p = i.descendants()
        if p and len(p) > 5:
            if p[5].texts() and p[5].texts()[0].strip() != '' and (
                    p[5].texts()[0].strip() != '添加' and p[5].texts()[0].strip() != '移出'):
                name_list.append(p[5].texts()[0].strip())
                all_members.append([p[5].texts()[0].strip(), p[3].texts()[0].strip()])
    pd.DataFrame(np.array(all_members)).to_csv('all_members.csv', header=['群昵称', '微信昵称'])
    print('\r>>> 群成员共 {} 人，结果已保存至all_members.csv'.format(len(name_list)))
    return name_list


def match():
    pid = get_wechat_pid()
    if pid is None:
        print('>>> 找不到WeChat.exe，请先打开WeChat.exe再运行此脚本！')
        return
    try:
        member_list = get_name_list(pid)
    except pywinauto.findwindows.ElementNotFoundError as e:
        print('\r>>> 未找到【聊天成员】窗口，程序终止！')
        print('>>> 若已开启【聊天成员】窗口但仍报错，请重启微信（原因：可能存在多个WeChat进程）')
        return


if __name__ == '__main__':
    match()
