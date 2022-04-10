import nextcord
from nextcord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from nextcord.utils import get
from nextcord import FFmpegPCMAudio
import asyncio
import time
import pandas as pd

TOKENVALUE = open(r'C:\Users\c\Desktop\discordTOKEN.txt','r')
TOKEN = TOKENVALUE.read()
TOKENVALUE.close()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succeseful')
    game = nextcord.Game('음악 연구')
    await bot.change_presence(status=nextcord.Status.online, activity = game)

@bot.command()
async def 들어와(ctx):
    try:
        try:
            global vc
            vc = await ctx.message.author.voice.channel.connect()
        except:
            await ctx.send('이미 채널에 속해있습니다.')
                
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('채널어 유저가 접속해있지 않네요..')
    

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send('이미 그 채널에 속해있지 않아요.')

@bot.command()
async def 링크재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = nextcord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command()
async def 재생(ctx, *, msg):
    if not vc.is_playing():

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        chromedriver_dir = (r'C:\Users\c\Desktop\chromedriver.exe')
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = nextcord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command()
async def 지금노래(ctx):
    if not vc.is_playing():
        await ctx.send("지금은 노래가 재생되지 않네요..")
    else:
        await ctx.send(embed = nextcord.Embed(title = "지금노래", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))

@bot.command()
async def 멜론차트(ctx):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = (r"C:\Users\c\Desktop\chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = nextcord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command()
async def 명령어(ctx):
    await ctx.send('모든 명령어 앞에는 !를 붙입니다\n' + '들어와 : 봇을 음성채팅 서버에 참여시킵니다\n' + 
    '나가 : 봇을 음성채팅 서버에서 추방시킵니다\n' + '재생[제목] : 제목을 입력하면 해당하는 노래를 재생합니다\n'+
    '링크재생 : 링크를 입력하면 해당하는 동영상을 재생합니다\n' + '멜론차트 : 멜론차트를 재생합니다\n' +
    '지금노래 : 현재 재생되고있는 노래제목을 알려줍니다')
    
bot.run(TOKEN)