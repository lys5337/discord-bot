from gc import callbacks
from http.client import NON_AUTHORITATIVE_INFORMATION
from logging import StrFormatStyle
from tkinter import Button
from unittest import result
import nextcord
from nextcord.ui import Button, View
from nextcord import Intents, User, user_command
from nextcord.ext import commands
from nextcord.utils import get
from selenium.webdriver.chrome.options import Options
from numpy import number
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from nextcord import Embed, FFmpegPCMAudio, Interaction
import asyncio
import time
import pandas as pd
import random

TOKENVALUE = open(r'C:\Users\c\Desktop\bot_TOKEN\discord_TOKEN.txt','r')
TOKEN = TOKENVALUE.read()
TOKENVALUE.close()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)
client = nextcord.Client()

class musicbot:
    user = []
    musictitle = []
    song_queue = []
    musicnow = []

    def title(msg):
        global music

        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        chromedriver_dir = r"C:\Users\c\Desktop\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        music = entireNum.text.strip()
        
        musicbot.musictitle.append(music)
        musicbot.musicnow.append(music)
        test1 = entireNum.get('href')
        url = 'https://www.youtube.com'+test1
        with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']

        driver.quit()
        
        return music, URL

    def play(ctx):
        global vc
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        URL = musicbot.song_queue[0]
        del musicbot.user[0]
        del musicbot.musictitle[0]
        del musicbot.song_queue[0]
        vc = get(bot.voice_clients, guild=ctx.guild)
        if not vc.is_playing():
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: musicbot.play_next(ctx)) 

    def play_next(ctx):
        if len(musicbot.musicnow) - len(musicbot.user) >= 2:
            for i in range(len(musicbot.musicnow) - len(musicbot.user) - 1):
                del musicbot.musicnow[0]
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        if len(musicbot.user) >= 1:
            if not vc.is_playing():
                del musicbot.musicnow[0]
                URL = musicbot.song_queue[0]
                del musicbot.user[0]
                del musicbot.musictitle[0]
                del musicbot.song_queue[0]
                vc.play(nextcord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: musicbot.play_next(ctx))
    
    def again(ctx, url):
        global number
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        if number:
            with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            if not vc.is_playing():
                vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: musicbot.again(ctx, url))
                    


    @bot.command()
    async def 들어와(ctx):
        try:
            global vc
            vc = await ctx.message.author.voice.channel.connect()
                    
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
            musicbot.musicnow.insert(0, entireText)
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            await ctx.send(embed = nextcord.Embed(title= "노래 재생", description = "현재 " + musicbot.musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        else:
            musicbot.user.append(msg)
            result, URLTEST = musicbot.title(msg)
            musicbot.song_queue.append(URLTEST)
            await ctx.send('이미 노래가 재생중이라' + result + '을(를) 대기열로 추가시켰습니다')

    @bot.command()
    async def 지금노래(ctx):
        if not vc.is_playing():
            await ctx.send("지금은 노래가 재생되지 않네요..")
        else:
            await ctx.send(embed = nextcord.Embed(title = "지금노래", description = "현재 " + musicbot.musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))

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
            await ctx.send(embed = nextcord.Embed(title= "노래 재생", description = "현재 " + musicbot.musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        else:
            await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

    @bot.command()
    async def 일시정지(ctx):
        if vc.is_playing():
            vc.pause()
            await ctx.send(embed = nextcord.Embed(title = '일시정지', discription = musicbot.musicnow[0] + '을(를) 일시정지 했습니다', color = 0x00ff00))
        else:
            await ctx.send('지금 노래가 재생되지 않네요')

    @bot.command()
    async def 다시재생(ctx):
        try:
            vc.resume()
            await ctx.send(embed = nextcord.Embed(title = '일시정지', discription = musicbot.musicnow[0] + '을(를) 다시 재생했습니다', color = 0x00ff00))
        except:
            await ctx.send('지금 노래가 재생되지 않네요')

    @bot.command()
    async def 노래끄기(ctx):
        if vc.is_playing():
            vc.stop()
            global number
            number = 0
            await ctx.send(embed = nextcord.Embed(title = '노래끄기', discription = musicbot.musicnow[0] + '을(를) 종료했습니다', color = 0x00ff00))
        else:
            await ctx.send('지금 노래가 재생되지 않네요')

    @bot.command()
    async def 반복재생(ctx, *, msg):

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        global vc
        if not vc.is_playing():
            try:
                vc = await ctx.message.author.voice.channel.connect()   
            except:
                try:
                    await vc.move_to(ctx.message.author.voice.channel)
                except:
                    pass
            
            global entireText
            global number
            number = 1
            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
            if len(musicbot.musicnow) - len(musicbot.user) >= 1:
                for i in range(len(musicbot.musicnow) - len(musicbot.user)):
                    del musicbot.musicnow[0]
                    
            chromedriver_dir = (r"C:\Users\c\Desktop\chromedriver.exe")
            driver = webdriver.Chrome(chromedriver_dir, options = options)
            driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
            source = driver.page_source
            bs = bs4.BeautifulSoup(source, 'lxml')
            entire = bs.find_all('a', {'id': 'video-title'})
            entireNum = entire[0]
            entireText = entireNum.text.strip()
            musicbot.musicnow.insert(0, entireText)
            test1 = entireNum.get('href')
            url = 'https://www.youtube.com'+test1
            await ctx.send(embed = nextcord.Embed(title= "반복재생", description = "현재 " + musicbot.musicnow[0] + "을(를) 반복재생하고 있습니다.", color = 0x00ff00))
            musicbot.again(ctx, url)
        else : 
            await ctx.send('현재 노래가 재생중이라 반복재생 할 수 없네요.. 노래를 끄거나 일시정지 한 후 사용해주세요')

    @bot.command()
    async def 추가(ctx, *, msg):
        musicbot.user.append(msg)
        result, URLTEST = musicbot.title(msg)
        musicbot.song_queue.append(URLTEST)
        await ctx.send(result + "를 재생목록에 추가했어요!")

    @bot.command()
    async def 삭제(ctx, *, number):
        try:
            ex = len(musicbot.musicnow) - len(musicbot.user)
            del musicbot.user[int(number) - 1]
            del musicbot.musictitle[int(number) - 1]
            del musicbot.song_queue[int(number)-1]
            del musicbot.musicnow[int(number)-1+ex]
                
            await ctx.send("대기열이 정상적으로 삭제되었습니다.")
        except:
            if len(list) == 0:
                await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
            else:
                if len(list) < int(number):
                    await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
                else:
                    await ctx.send("숫자를 입력해주세요!")

    @bot.command()
    async def 스킵(ctx):
        if len(musicbot.user) >= 1:
            if vc.is_playing():
                vc.stop()
                global number
                number = 0
                await ctx.send(embed = nextcord.Embed(title = '스킵', description = musicbot.musicnow[1] 
                + '을(를) 다음에 재생합니다', color = 0x00ff00))

    @bot.command()
    async def 목록(ctx):
        if len(musicbot.musictitle) == 0:
            await ctx.send("아직 아무노래도 등록하지 않았어요.")
        else:
            global Text
            Text = ""
            for i in range(len(musicbot.musictitle)):
                Text = Text + "\n" + str(i + 1) + ". " + str(musicbot.musictitle[i])
                
            await ctx.send(embed = nextcord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

    @bot.command()
    async def 목록초기화(ctx):
        try:
            ex = len(musicbot.musicnow) - len(musicbot.user)
            del musicbot.user[:]
            del musicbot.musictitle[:]
            del musicbot.song_queue[:]
            while True:
                try:
                    del musicbot.musicnow[ex]
                except:
                    break
            await ctx.send(embed = nextcord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
        except:
            await ctx.send("아직 아무노래도 등록하지 않았어요.")
    
    @bot.command()
    async def 목록섞기(ctx):
        try:
            global musicnow, user, musictitle, song_queue
            numbershuffle = len(musicbot.musicnow) - len(musicbot.user)
            for i in range(numbershuffle):
                random.shuffle.append(musicbot.musicnow[0])
                del musicbot.musicnow[0]
            combine = list(zip(musicbot.user, musicbot.musicnow, musicbot.musictitle, musicbot.song_queue))
            random.shuffle(combine)
            a,b,c,d = list(zip(*combine))

            musicbot.user = list(a)
            musicbot.musicnow = list(b)
            musicbot.musictitle = list(c)
            musicbot.song_queue = list(d)

            for i in range(numbershuffle):
                musicbot.musicnow.insert(0, random.shuffle[i])

            await ctx.send('목록을 정상적으로 섞었습니다')
        except:
            await ctx.send('섞을 목록이 없습니다')

    @bot.command()
    async def 목록재생(ctx):

        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        
        if len(musicbot.user) == 0:
            await ctx.send("아직 아무노래도 등록하지 않았어요.")
        else:
            if len(musicbot.musicnow) - len(musicbot.user) >= 1:
                for i in range(len(musicbot.musicnow) - len(musicbot.user)):
                    del musicbot.musicnow[0]
            if not vc.is_playing():
                musicbot.play(ctx)
            else:
                await ctx.send("노래가 이미 재생되고 있어요!")

    @bot.command()
    async def 명령어(ctx):
        detail_command = Button(label="자세히", style = nextcord.ButtonStyle.green)
        simple_command = Button(label="간단히", style = nextcord.ButtonStyle.green)

        async def detail_command_callback(interaction):
            await ctx.send('모든 명령어 앞에는 !를 붙입니다\n\n' + 
            '들어와 : 봇을 음성채팅 서버에 참여시킵니다\n' + 
            '나가 : 봇을 음성채팅 서버에서 추방시킵니다\n' + 
            '재생[제목] : 제목을 입력하면 해당하는 노래를 재생합니다\n'+ 
            '멜론차트 : 멜론차트를 재생합니다\n' +
            '노래반복[제목] : [제목]의 노래를 반복합니다\n' +
            '지금노래 : 현재 재생되고있는 노래제목을 알려줍니다\n' + 
            '추가/삭제 : 대기열에 노래를 추가/삭제 합니다\n' +
            '목록/목록재생 : 재생목록을 보여줍니다/재생합니다\n' + 
            '일시정지/다시재생 : 노래를 정지/다시재생 시킵니다\n' + 
            '노래끄기 : 노래를 종료하고 바로 다음곡을 재생합니다\n')

        async def simple_command_callback(interaction):
            await ctx.send('모든 명령어 앞에는 !를 붙입니다\n'+
            '들어와               '+'나가                 '+'재생[제목]          '+'노래반복[제목]\n'+
            '멜론차트           '+'지금노래         '+'추가/삭제           '+'목록\n'+
            '목록재생           '+'일시정지         '+'다시재생             '+'노래끄기\n')

        detail_command.callback = detail_command_callback
        simple_command.callback = simple_command_callback

        view = View()
        view.add_item(detail_command)
        view.add_item(simple_command)
    
        await ctx.send(embed = nextcord.Embed(title='명령어 설명',description="원하시는 버튼을 클릭해주세요", colour=nextcord.Colour.blue()), view=view)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succeseful')
    game = nextcord.Game('음악 연구')
    await bot.change_presence(status=nextcord.Status.online, activity = game)
    
bot.run(TOKEN)