from khl import *
from yumemiBot import yumemi as bot
import dndice
import random
import requests
import json
from tools.ffxiv_arcana import FFArcana

@bot.command(name='hello')
async def hello(msg: Message):
    '''
    /hello: return a designated string.
    '''
    # print(msg)    # <khl.message.PrivateMessage object at 0xaddress>
    # await msg.reply('') # quote reply
    await msg.ctx.channel.send('欢迎光临星象馆，这里有无论何时都不会消失，美丽的无穷光辉，漫天繁星在等待您的到来。') # direct output in the channel


@bot.command(name='r')
async def roll(msg: Message, dices: str):
    '''
    /roll: simple dice roller command.
    '''
    try:
        result = dndice.basic(dices)
    except Exception:
        result = 'an error rolling dices'
    finally:
        await msg.reply(f'you got: {result}')
    pass


@bot.command(name='jrrp')
async def jrrp(msg: Message):
    '''
    /jrrp: Shows the luckiness of current user on today.
     - the user is variant but the datetime is fixed.
     - same user on same day get same rp, but different user varies.
     - bot should fetch current user of the command then use it to generate seeds.
    '''
    # await msg.ctx.channel.send(f'aa今天的人品是0，下楼拿夜宵的时候小心踩到乐高哦')
    pass

    
@bot.command(name='draw')
async def draw(msg: Message, cat: str):
    '''
    /draw: draw a card, its random all the time.
    Tarot API: https://github.com/ekelen/tarot-api
    Its currently not a Chinese Translated Version
    '''
    if cat == '单张塔罗牌':
        cardno = random.randint(0, 21)
        cardpos = random.choice(['meaning_up', 'meaning_rev'])
        url = 'https://rws-cards-api.herokuapp.com/api/v1/cards/ar' + str(cardno).zfill(2)
        print(url)
        response = requests.get(url)
        card = json.loads(response.content)['card']
        
        reply = '你抽到的卡是' + card['value'] + '. ' + card['name'] + '。\n含义为' + card[cardpos]
        # reply += # additional info
        await msg.reply(reply)
    elif cat == '奥秘卡占卜':
        cardno = random.randint(0,11)
        card = FFArcana.deck[cardno]
        print(card)
        if cardno < 6 :
            pos = '正位（星极' + card['attribute'] + '）'
        else:
            pos =  '逆位（灵极' + card['attribute'] + '）'
        if card['meaning'] == '':
            desc = '<暂缺>'
        else:
            desc = card['meaning']
        # TODO: fill in the meaning and desc zone of ffxiv arcana
        reply = '你抽到的卡是' + card['card'] + ', ' + pos + ', 对应十二神中的' + card['deity'] + '。\n含义为' + desc
        await msg.reply(reply)
    else:
        pass