#coding:utf-8
from slackbot.bot import respond_to, listen_to
import sys
sys.path.append('../')
from switch import trun
from getLux import get_lux , switch_status , room_status
import re

@respond_to(u'(エアコン)+.*(つけ|付け|点け|突け)+')
def on_order(message,*someting):
    bright=get_lux()
    with open('/home/pi/slackbot/bot_status.txt',mode=mode = 'r') as f:
        for row in f:
            hoge=int(row.strip())
            bot_status=hoge
        if bot_status == 0:
            message.reply('botが監視をしています。')
        else:
            if bright[0] > switch_status: #電源ランプがついてるときの値
                message.reply('既に電源が入っているようです。')
            else :
                message.reply('電源を入れます。')
                trun()

@respond_to(u'(エアコン)+.*(消し|けし)+')
def off_order(message,*something):
    bright=get_lux()
    with open('/home/pi/slackbot/bot_status.txt',mode = 'r') as f:
        for row in f:
            hoge=int(row.strip())
            bot_status=hoge
        if bot_status == 0:
            message.reply('botが監視をしています。')
        else:
            if bright[0] > switch_status: #電源ランプがついてるときの値
                message.reply('電源を消します。')
                trun()
            else :
                message.reply('既に電源が入っていないようです。')

@respond_to(u'(誰か|だれか|ダレカ)+.*(いる|居る|イル)+')
def room_check_order(message,*something):
    bright = getLux()
    if bright[1] > room_status:
        message.reply('部屋の明るさ:'+str(bright[1])+'(lx)\n誰かいるようですね。')

    else:
        message.reply('部屋の明るさ:'+str(bright[1])+'(lx)\n誰もいないようです。')

@respond_to(u'(調子|ちょうし)+.*(どう)+')
def switch_check_order(message,*something):
    bright = getLux()
    with open('/home/pi/slackbot/bot_status.txt',mode = 'r') as f:
        for row in f:
            hoge=int(row.strip())
            bot_status=hoge

        if bot_status == 0:
            message.reply('電源を監視しています。\n'+'電源:'+str(bright[0])+'(lx)部屋:'+str(bright[1])+'(lx)\nって感じですね。')
        else:
            message.reply('仕事してないです。\n'+'電源:'+str(bright[0])+'(lx)部屋:'+str(bright[1])+'\n(lx)って感じですね。')

@respond_to('bot activate')
def bot_active(message):
    with open('/home/pi/slackbot/bot_status.txt',mode = 'r') as f:
        for row in f:
            hoge=int(row.strip())
            bot_status=hoge
        if bot_status == 0:
            with open('lock.txt','w') as f:
                f.write('1')
            message.reply('bot active!')

        else:
            message.reply('already active')

@respond_to('bot deactivate')
def bot_deactive(message):
    with open('/home/pi/slackbot/bot_status.txt',mode = 'r') as f:
        for row in f:
            hoge=int(row.strip())
            bot_status=hoge
        if bot_status == 1:
            with open('lock.txt','w') as f:
                f.write('0')
            message.reply('bot deactive!')

        else:
            message.reply('already deactive')
