# coding: utf-8
import time
import threading

from requests_oauthlib import OAuth1Session
from slacker import Slacker
from slackbot.bot import Bot
from datetime import datetime

from getLux import get_lux ,switch_status ,room_status
from slackbot.settings import API_TOKEN

#
# API token
token = API_TOKEN

# 投稿するチャンネル名
c_name = 'test'

# 投稿
slacker = Slacker(token)

try:
    with open('/home/pi/slackbot/bot_status.txt', mode='x') as f:
        f.write('1')
except FileExistsError:
    pass

global bot_status

time_stamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def check_lux():
    """
    Threadで定期的に明るさをチェックしてしきい値を下回ったらステータスをOFFにする
    """
    # 初期化
    set_away()
    while True:

        bright = get_lux()
        # 電源ランプによってステータスを変更
        if bright[1] > room_status:
            set_active()

        else:
            set_away()

        # 最後のbotの状態を取得
        with open('/home/pi/slackbot/bot_status.txt', mode='r') as f:
            for row in f:
                hoge = int(row.strip())
                global bot_status
                bot_status = hoge

        if bot_status == 1:
            print("bot active!")
            # 部屋が明るくなった
            if bright[1] > room_status and bright[0] <= switch_status:
                turn()

            # 部屋が暗くなった
            elif bright[1] <= room_status and bright[0] > switch_status:
                turn()

            else:
                pass

        else:
            print("bot deactive")

        time.sleep(10)


def main():
    bot = Bot()
    # 照度監視用のスレッドを起動する
    th_me = threading.Thread(target=check_lux, name="th_check_lux")
    th_me.setDaemon(True)
    th_me.start()
    try:
        slacker.chat.post_message(c_name, '起動しました', as_user=True)
        with open('/home/pi/slackbot/bot_status.txt', mode='r') as f:
            for row in f:
                hoge = int(row.strip())
                global bot_status
                bot_status = hoge
        if bot_status == 0:
            slacker.chat.post_message(c_name, 'botが監視をしていないようです。\n"bot activate"で監視を開始してください。', as_user=True)
        # botを起動する
        bot.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    slacker.chat.post_message(c_name, '起動しました。', as_user=True)
    print('start slackbot')
    main()
