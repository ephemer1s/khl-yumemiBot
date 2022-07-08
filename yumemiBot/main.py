from khl import *
from yumemiBot import yumemi as bot
import dndice

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
