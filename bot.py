import discord
from discord.ext import commands
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def control(ctx):
    if ctx.message.attachments :
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(IMAGE_DIR,file_name)
            await attachment.save(file_path)
            await ctx.send('Görsel Kayıt Olundu, Sonucun cevabını bekleyin')
            class_name,score = get_class(file_path)
            await ctx.send(f'Görsel Teması: {class_name}, Ortalama Düşüncem:{score}')
            if class_name == 'PS':
                await ctx.send('Bu görsel PS Yani Prehistoric Survival temasına benziyor, Etrafdaki Canavar veya dinazorlara dikkat etsen iyi olur!')
            elif class_name == 'Backrooms':
                await ctx.send('Bu Görsel Backrooms u andırıyor. Uzun koridorlar ve sonsuz mekanlar var,Orada iken nereye gittiğine dikkat et daha tehlikeli bir bölüme yada bir canavarla karşılaştırabilir. Bol şans!')
            else:
                await ctx.send('Bu Görsel Climbing Temasına benziyor. Bu tip oyunlar genellikle bir yerlere tırmanmak ve tırmanırken hayatta kalmakla geçer.. En kötü ne olabilirki?')
                
                

    else:
        await ctx.send('Görsel Göndermediniz.')

bot.run("TOKEN")