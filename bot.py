from gc import callbacks
from http.client import NON_AUTHORITATIVE_INFORMATION
from logging import StrFormatStyle
from sqlite3 import enable_shared_cache
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
from urllib.request import urlopen, Request
import urllib
import urllib.request
import numpy as np
import maple_cube
import lol_info

TOKENVALUE = open(r'C:\Users\c\Desktop\bot_TOKEN\discord_TOKEN.txt','r')
TOKEN = TOKENVALUE.read()
TOKENVALUE.close()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)
client = nextcord.Client(enable_debug_events = True)

#00
@bot.command()
async def 명령어(ctx):
    command_music = Button(label="음악봇", style = nextcord.ButtonStyle.green)
    command_game = Button(label="게임봇", style = nextcord.ButtonStyle.green)
    channel = ctx.channel
    
    async def command_music_callback(interaction):
        embed = nextcord.Embed(title = '명령어목록',
        description = '모든 명령어 앞에는 !를 붙입니다',
        colour = nextcord.Colour.blue())
        #class musicbot
        embed.add_field(name = '!들어와', value = '봇이 음성채널에 참가합니다(사용자가 있을경우에만)',inline = True) #01
        embed.add_field(name = '!나가', value = '봇이 음성채널에서 나갑니다', inline = True) #02
        embed.add_field(name = '!재생[제목/링크]', value = '제목/링크를 입력하면 재생합니다, 이미 재생중이라면 목록에 추가합니다', inline = True) #03
        embed.add_field(name = '!반복재생[제목/링크]', value = '제목/링크를 입력하면 그 노래를 반복재생합니다.', inline = True) #04
        embed.add_field(name = '!멜론차트', value = '최신 주의 멜론차트를 재생합니다', inline = True) #05
        embed.add_field(name = '!지금노래', value = '현재 재생중인 곡의 제목을 알려줍니다', inline = True) #06
        embed.add_field(name = '!목록', value = '앞으로 재생할 곡의 리스트를 보여줍니다.', inline = True) #07
        embed.add_field(name = '!추가/삭제[제목,링크]', value = '목록에있는 리스트에 추가/삭제 합니다', inline = True) #08
        embed.add_field(name = '!목록재생', value = '목록에 등록되어있는 리스트를 재생합니다', inline = True) #09
        embed.add_field(name = '!목록초기화', value = '현재 목록에 등록된 모든 노래를 초기화시킵니다', inline = True) #10
        embed.add_field(name = '!목록섞기', value = '현재 목록에 등록된 모든 노래의 순서를 랜덤하게 섞습니다', inline = True) #11
        embed.add_field(name = '!일시정지', value = '현재 재생중인 곡을 일시정지 시킵니다.', inline = True) #12
        embed.add_field(name = '!다시재생', value = '일시정지중인 곡을 다시 재생시킵니다', inline = True) #13
        embed.add_field(name = '!노래끄기', value = '현재 재생중인 곡을 즉시종료시킵니다', inline = True) #14
        embed.add_field(name = '!스킵', value = '현재 재생중인 곡을 스킵하고 다음곡을 재생합니다', inline = True) #15
        embed.add_field(name = '!즐겨찾기', value = '유저별로 플레이리스트를 저장하여 보여줍니다', inline = True) #16
        embed.add_field(name = '!즐겨찾기추가 / 즐겨찾기삭제', value = '유저별 즐겨찾기 목록에 곡을 추가/삭제 합니다', inline = True) #17
        embed.add_field(name = '!정밀검색', value = '검색한 내용의 유튜브영상을 최대 5개까지 보여줍니다') #18

        embed.add_field(name = '----------------------------------↑음악----------------------------------', 
                        value = '----------------------------------↓기타----------------------------------', inline = False)
        #class lotto
        embed.add_field(name = '!복권', value = '복권번호를 랜덤추첨 합니다', inline = True) #21
        #class weather
        embed.add_field(name = '!날씨[지역]', value = '해당하는 지역의 오늘의 날씨정보와 내일의 날씨정보를 알려줍니다', inline = True) #19
        embed.add_field(name = '!해외날씨[지역]', value = '해당하는 지역의 오늘의 날씨정보와 내일의 날씨정보를 알려줍니다', inline = True) #20

        await ctx.send(channel, embed = embed)

    async def command_game_callback(interaction):
        embed = nextcord.Embed(title = '명령어목록',
        description = '모든 명령어 앞에는 !를 붙입니다',
        colour = nextcord.Colour.blue())

        #class maplestory
        embed.add_field(name = '!메소시세', value = '전날의 메소시세를 알려줍니다', inline = True) #22
        embed.add_field(name = '!유저정보[닉네임]', value = '해당하는 닉네임의 유저정보를 제공합니다', inline = True) #23
        embed.add_field(name = '!강화공식', value = '주문의 흔적, 스타포스의 강화수치를 제공합니다', inline = True) #24
        embed.add_field(name = '!무기추옵', value = '파프니르, 앱솔랩스, 아케인셰이드, 제네시스 무기의 추가옵션을 제공합니다', inline = True) #25
        embed.add_field(name = '!레드큐브[횟수]', value = '레드큐브를 [횟수] 만큼 시뮬레이션 해줍니다.', inline = True) #26
        embed.add_field(name = '!블랙큐브[횟수]', value = '블랙큐브를 [횟수] 만큼 시뮬레이션 해줍니다.', inline = True) #27
        embed.add_field(name = '!에디셔널[횟수]', value = '에디셔널큐브를 [횟수] 만큼 시뮬레이션 해줍니다.', inline = True) #28

        embed.add_field(name = '----------------------------------↑메이플----------------------------------', 
                        value = '----------------------------------↓롤----------------------------------', inline = False)
        #class lol
        embed.add_field(name = '!룬[챔피언 이름]', value = '해당 챔피언의 포지션별 룬을 알려줍니다', inline = True) #29
        
        await ctx.send(channel, embed = embed)

    command_music.callback = command_music_callback
    command_game.callback = command_game_callback

    view = View()
    view.add_item(command_music)
    view.add_item(command_game)


    await ctx.send(embed = nextcord.Embed(title='명령어 설명',description="원하시는 버튼을 클릭해주세요", colour=nextcord.Colour.blue()), view=view)

class musicbot:

    user = []           #유저가 입력한 노래 정보
    musictitle = []     #가공된 정보의 노래 제목
    song_queue = []     #가공된 정보의 노래 링크
    musicnow = []       #현재 출력되는 노래 정보

    userF = []          #유저 정보 저장 배열
    userFlist = []      #유저 개인 노래 저장 배열
    allplaylist = []    #플레이리스트 배열

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

    def URLPLAY(ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        if not vc.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                client.loop.create_task(musicbot.subtitle_song(ctx, URL))

    #01
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
    #02        
    @bot.command()
    async def 나가(ctx):
        try:
            await vc.disconnect()
        except:
            await ctx.send('이미 그 채널에 속해있지 않아요.')
    #03
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
    #04
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
    #05    
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
            await ctx.send(embed = nextcord.Embed(title = "노래 재생", description = "현재 " + "멜론차트" + "을(를) 재생하고 있습니다.", color = 0x00ff00))
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        else:
            await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")
    #06
    @bot.command()
    async def 지금노래(ctx):
        if not vc.is_playing():
            await ctx.send("지금은 노래가 재생되지 않네요..")
        else:
            await ctx.send(embed = nextcord.Embed(title = "지금노래", description = "현재 " + musicbot.musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    #07            
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
    #08
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
    #09
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
    #10
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
    #11                
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
    #12
    @bot.command()
    async def 일시정지(ctx):
        if vc.is_playing():
            vc.pause()
            await ctx.send(embed = nextcord.Embed(title = '일시정지', discription = musicbot.musicnow[0] + '을(를) 일시정지 했습니다', color = 0x00ff00))
        else:
            await ctx.send('지금 노래가 재생되지 않네요')
    #13
    @bot.command()
    async def 다시재생(ctx):
        try:
            vc.resume()
            await ctx.send(embed = nextcord.Embed(title = '일시정지', discription = musicbot.musicnow[0] + '을(를) 다시 재생했습니다', color = 0x00ff00))
        except:
            await ctx.send('지금 노래가 재생되지 않네요')
    #14
    @bot.command()
    async def 노래끄기(ctx):
        if vc.is_playing():
            vc.stop()
            global number
            number = 0
            await ctx.send(embed = nextcord.Embed(title = '노래끄기', discription = musicbot.musicnow[0] + '을(를) 종료했습니다', color = 0x00ff00))
        else:
            await ctx.send('지금 노래가 재생되지 않네요')
    #15
    @bot.command()
    async def 스킵(ctx):
        if len(musicbot.user) >= 1:
            if vc.is_playing():
                vc.stop()
                global number
                number = 0
                await ctx.send(embed = nextcord.Embed(title = '스킵', description = musicbot.musicnow[1] 
                + '을(를) 다음에 재생합니다', color = 0x00ff00))
    #16
    @bot.command()
    async def 즐겨찾기(ctx):
        global Ftext
        Ftext = ""
        correct = 0
        global Flist
        for i in range(len(musicbot.userF)):
            if musicbot.userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
                correct = 1 #있으면 넘김
        if correct == 0:
            musicbot.userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
            musicbot.userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듬.
            musicbot.userFlist[len(musicbot.userFlist)-1].append(str(ctx.message.author.name))
            
        for i in range(len(musicbot.userFlist)):
            if musicbot.userFlist[i][0] == str(ctx.message.author.name):
                if len(musicbot.userFlist[i]) >= 2: # 노래가 있다면
                    for j in range(1, len(musicbot.userFlist[i])):
                        Ftext = Ftext + "\n" + str(j) + ". " + str(musicbot.userFlist[i][j])
                    titlename = str(ctx.message.author.name) + "님의 즐겨찾기"
                    embed = nextcord.Embed(title = titlename, description = Ftext.strip(), color = 0x00ff00)
                    embed.add_field(name = "목록에 추가\U0001F4E5", value = "즐겨찾기에 모든 곡들을 목록에 추가합니다.", inline = False)
                    embed.add_field(name = "플레이리스트로 추가\U0001F4DD", value = "즐겨찾기에 모든 곡들을 새로운 플레이리스트로 저장합니다.", inline = False)
                    Flist = await ctx.send(embed = embed)
                    await Flist.add_reaction("\U0001F4E5")
                    await Flist.add_reaction("\U0001F4DD")
                else:
                    await ctx.send("아직 등록하신 즐겨찾기가 없어요.")
    #17
    @bot.command()
    async def 즐겨찾기추가(ctx, *, msg):
        correct = 0
        for i in range(len(musicbot.userF)):
            if musicbot.userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
                correct = 1 #있으면 넘김
        if correct == 0:
            musicbot.userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
            musicbot.userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듦.
            musicbot.userFlist[len(musicbot.userFlist)-1].append(str(ctx.message.author.name))

        for i in range(len(musicbot.userFlist)):
            if musicbot.userFlist[i][0] == str(ctx.message.author.name):
                
                options = webdriver.ChromeOptions()
                options.add_argument("headless")

                chromedriver_dir = (r"C:\Users\c\Desktop\chromedriver.exe")
                driver = webdriver.Chrome(chromedriver_dir, options = options)
                driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
                source = driver.page_source
                bs = bs4.BeautifulSoup(source, 'lxml')
                entire = bs.find_all('a', {'id': 'video-title'})
                entireNum = entire[0]
                music = entireNum.text.strip()

                driver.quit()

                musicbot.userFlist[i].append(music)
                await ctx.send(music + "(이)가 정상적으로 등록되었어요!")

    @bot.command()
    async def 즐겨찾기삭제(ctx, *, number):
        correct = 0
        for i in range(len(musicbot.userF)):
            if musicbot.userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
                correct = 1 #있으면 넘김
        if correct == 0:
            musicbot.userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
            musicbot.userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듦.
            musicbot.userFlist[len(musicbot.userFlist)-1].append(str(ctx.message.author.name))

        for i in range(len(musicbot.userFlist)):
            if musicbot.userFlist[i][0] == str(ctx.message.author.name):
                if len(musicbot.userFlist[i]) >= 2: # 노래가 있다면
                    try:
                        del musicbot.userFlist[i][int(number)]
                        await ctx.send("정상적으로 삭제되었습니다.")
                    except:
                        await ctx.send("입력한 숫자가 잘못되었거나 즐겨찾기의 범위를 초과하였습니다.")
                else:
                    await ctx.send("즐겨찾기에 노래가 없어서 지울 수 없어요!")

    @bot.event
    async def on_reaction_add(ctx, reaction, users):

        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        chromedriver_dir = (r"C:\Users\c\Desktop\chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        
        if users.bot == 1:
            pass
        else:
            try:
                await Flist.delete()
            except:
                pass
            else:
                if str(reaction.emoji) == '\U0001F4E5':
                    await reaction.message.channel.send("잠시만 기다려주세요. (즐겨찾기 갯수가 많으면 지연될 수 있습니다.)")
                    print(users.name)
                    for i in range(len(musicbot.userFlist)):
                        if musicbot.userFlist[i][0] == str(users.name):
                            for j in range(1, len(musicbot.userFlist[i])):
                                try:
                                    driver.close()
                                except:
                                    print("NOT CLOSED")

                                musicbot.user.append(musicbot.userFlist[i][j])
                                result, URLTEST = musicbot.title(musicbot.userFlist[i][j])
                                musicbot.song_queue.append(URLTEST)
                                await reaction.message.channel.send(musicbot.userFlist[i][j] + "를 재생목록에 추가했어요!")

                elif str(reaction.emoji) == '\u0031\uFE0F\u20E3':                  
                    musicbot.URLPLAY(musicbot.rinklist[0])
                    await ctx.send("정상적으로 진행되었습니다.")
                elif str(reaction.emoji) == '\u0032\uFE0F\u20E3':
                    musicbot.URLPLAY(musicbot.rinklist[1])
                    await ctx.send("정상적으로 진행되었습니다.")
                elif str(reaction.emoji) == '\u0033\uFE0F\u20E3':
                    musicbot.URLPLAY(musicbot.rinklist[2])
                    await ctx.send("정상적으로 진행되었습니다.")
                elif str(reaction.emoji) == '\u0034\uFE0F\u20E3':
                    musicbot.URLPLAY(musicbot.rinklist[3])
                    await ctx.send("정상적으로 진행되었습니다.")
                elif str(reaction.emoji) == '\u0035\uFE0F\u20E3':
                    musicbot.URLPLAY(musicbot.rinklist[4])
                    await ctx.send("정상적으로 진행되었습니다.")
    #18
    @bot.command()
    async def 정밀검색(ctx, *, msg):
        Text = ""
        global rinklist
        global Alist
        rinklist = [0,0,0,0,0]

        try:
            global vc
            vc = await ctx.message.author.voice.channel.connect()
        except:
            try:
                await vc.move_to(ctx.message.author.voice.channel)
            except:
                await ctx.send("채널에 유저가 접속해있지 않네요..")

        YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        chromedriver_dir = r"C:\Users\c\Desktop\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)

        driver.get("https://www.youtube.com/results?search_query="+msg)
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        for i in range(0, 5):
            entireNum = entire[i]
            entireText = entireNum.text.strip()  # 영상제목
            test1 = entireNum.get('href')  # 하이퍼링크
            rinklist[i] = 'https://www.youtube.com'+test1
            Text = Text + str(i+1)+'번째 영상 : ' + entireText +'\n링크 : '+ rinklist[i] + '\n'
        
        await ctx.send(embed = nextcord.Embed(title= "검색한 영상들입니다.", description = Text.strip(), color = 0x00ff00))
        Alist = await ctx.send(embed = Embed)

        await Alist.add_reaction("\u0031\uFE0F\u20E3")
        await Alist.add_reaction("\u0032\uFE0F\u20E3")
        await Alist.add_reaction("\u0033\uFE0F\u20E3")
        await Alist.add_reaction("\u0034\uFE0F\u20E3")
        await Alist.add_reaction("\u0035\uFE0F\u20E3")

class weather:

    location = []
    #19
    @bot.command()
    async def 날씨(ctx, *,msg):
        weather.location.append(msg)
        enc_location = urllib.parse.quote(str(weather.location[0]) + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        today_Base = bsObj.find('div', {'class': 'weather_info'})
        tommorrow_Base = bsObj.find('ul', {'class': 'weather_info_list'})

        today_Temp1 = today_Base.find('div', {'class': 'temperature_text'})
        today_Temp2 = today_Temp1.find('strong')
        today_Temp = today_Temp2.text.strip()  # 온도

        thanYesturday1 = today_Base.find('div', {'class':'temperature_info'})
        than_Yesturday = thanYesturday1.text.strip() #현재상태

        today_Dust1 = today_Base.find('ul', {'class': 'today_chart_list'})
        today_Dust = today_Dust1.text.strip() #대기상태

        tommorrow_Temp = []
        tommorrow_Temp = tommorrow_Base.find_all('div', {'class': 'inner'})
        tommorrow_Morning = tommorrow_Temp[0].text.strip() #내일오전
        tommorrow_Afternoon = tommorrow_Temp[1].text.strip() #내일오후

        embed = nextcord.Embed(
            title = str(weather.location) + ' 날씨 정보',
            description = str(weather.location) + '날씨 정보입니다.',
            colour = nextcord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=str(today_Temp), inline=False)  # 현재온도
        embed.add_field(name='현재상태', value=str(than_Yesturday), inline=False)  # 현재상태
        embed.add_field(name='대기상태', value=str(today_Dust), inline=False)  # 대기상태
        embed.add_field(
            name='**----------------------------------↑오늘----------------------------------**',
            value='**----------------------------------↓내일----------------------------------**', 
            inline=False)  # 구분선
        embed.add_field(name='내일오전', value=str(tommorrow_Morning), inline=False) #내일오전
        embed.add_field(name='내일오후', value=str(tommorrow_Afternoon), inline=False) #내일오후

        await ctx.send(ctx.channel,embed=embed)

        del weather.location[0]
    #20
    @bot.command()
    async def 해외날씨(ctx, *,msg):
        weather.location.append(msg)
        enc_location = urllib.parse.quote(str(weather.location[0]) + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        todayBase = bsObj.find('div', {'class': 'info_data'})
        today = todayBase.text.strip() #오늘날씨

        tommorrow_Base = bsObj.find('div', {'class' : 'tomorrow_area _mainTabContent'})

        tommorrow = tommorrow_Base.find_all('div', {'class' : 'main_info morning_box'})
        tommorrow_Morning = tommorrow[0].text.strip() #내일오전
        tommorrow_Afternoon = tommorrow[1].text.strip() #내일오후

        embed = nextcord.Embed(
            title = str(weather.location) + ' 날씨 정보',
            description = str(weather.location) + '날씨 정보입니다.',
            colour = nextcord.Colour.gold()
        )
        embed.add_field(name='현재상태', value=str(today), inline=False)  #오늘날씨
        embed.add_field(
            name='**----------------------------------↑오늘----------------------------------**',
            value='**----------------------------------↓내일----------------------------------**', 
            inline=False)  # 구분선
        embed.add_field(name='내일오전', value=str(tommorrow_Morning), inline=False) #내일오전
        embed.add_field(name='내일오후', value=str(tommorrow_Afternoon), inline=False) #내일오후

        await ctx.send(ctx.channel,embed=embed)

class lotto:

    #21
    @bot.command()
    async def 복권(ctx):

        number = []

        for i in range (1, 47):
            number.append(i)

        lotto_number = random.sample(number, 6)

        embed = nextcord.Embed(
            title="복권 숫자!",
            description=lotto_number,
            colour=nextcord.Color.red()
        )
        await ctx.send(ctx.channel, embed=embed)

class maplestory:

    username = []

    #22
    @bot.command()
    async def 메소시세(ctx):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = ('https://talk.gamemarket.kr/maple/graph/')
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        mesoBase = bsObj.find('div', {'class':'v-data-table__wrapper'})
        mesotitle1 = mesoBase.find_all('th', {'class':'text-center'})
        mesotitle = '왼쪽 ' + mesotitle1[1].text.strip() + ', 오른쪽 ' + mesotitle1[2].text.strip()

        meso = mesoBase.find_all('td', {'class':'text-center'})
        meso1 = meso[1].text.strip() +'원    ' + meso[2].text.strip() +'원'
        meso2 = meso[4].text.strip() +'원    ' + meso[5].text.strip() +'원'
        meso3 = meso[7].text.strip() +'원    ' + meso[8].text.strip() +'원'
        meso4 = meso[10].text.strip() +'원    ' + meso[11].text.strip() +'원'
        meso5 = meso[13].text.strip() +'원    ' + meso[14].text.strip() +'원'
        meso6 = meso[16].text.strip() +'원    ' + meso[17].text.strip() +'원'
        meso7 = meso[19].text.strip() +'원    ' + meso[20].text.strip() +'원'
        meso8 = meso[22].text.strip() +'원    ' + meso[23].text.strip() +'원'
        meso9 = meso[25].text.strip() +'원    ' + meso[26].text.strip() +'원'
        meso10 = meso[28].text.strip() +'원    ' + meso[29].text.strip() +'원'
        meso11 = meso[31].text.strip() +'원    ' + meso[32].text.strip() +'원'
        meso12 = meso[34].text.strip() +'원    ' + meso[35].text.strip() +'원'

        embed = nextcord.Embed(
            title = '메이플 메소시세',
            description = '어제자 메이플 메소 시세입니다',
            colour = nextcord.Colour.orange()
        )
        embed.add_field(name='서버별 시세',value=str(mesotitle), inline=False)
        embed.add_field(name='스카니아', value=str(meso1), inline=True)  
        embed.add_field(name='베라', value=str(meso2), inline=True)
        embed.add_field(name='루나', value=str(meso3), inline=True)
        embed.add_field(name='제니스', value=str(meso4), inline=True)
        embed.add_field(name='크로아', value=str(meso5), inline=True)
        embed.add_field(name='유니온', value=str(meso6), inline=True)
        embed.add_field(name='엘리시움', value=str(meso7), inline=True)
        embed.add_field(name='이노시스', value=str(meso8), inline=True)
        embed.add_field(name='레드', value=str(meso9), inline=True)
        embed.add_field(name='오로라', value=str(meso10), inline=True)
        embed.add_field(name='아케인', value=str(meso11), inline=True)
        embed.add_field(name='노바', value=str(meso12), inline=True)
        embed.add_field(
            name='현재 오류상태로 가격 텍스트가 불러와지지 않습니다.',
            value='https://talk.gamemarket.kr/maple/graph 를 참고해주세요',
            inline=False)

        await ctx.send(ctx.channel, embed = embed)
    #23
    @bot.command()
    async def 유저정보(ctx, *, msg):
        maplestory.username.append(msg)
        try:
            enc_name = urllib.parse.quote(str(maplestory.username[0]))
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = ('https://maple.gg/u/' + enc_name)
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            maple_data_base = bsObj.find('div', {'class':'row text-center'})
            user_info_base = bsObj.find('div', {'class' : 'row row-normal user-additional'})

            maple_date_base = maple_data_base.find_all('div', {'class' : 'user-summary-date'})
            maple_rank_base = maple_data_base.find_all('div', {'class' : 'mb-2'})
            dojang_and_theseed = maple_data_base.find_all('div', {'class' : 'py-0 py-sm-4'})
            union_and_achievement = maple_data_base.find_all('div', {'class' : 'pt-3 pb-2 pb-sm-3'})
            user_info = user_info_base.find_all('div', {'class' : 'col-lg-2 col-md-4 col-sm-4 col-6 mt-3'})

            dojang = dojang_and_theseed[0].text.strip() #층수 / 기록
            dojang_date = maple_date_base[0].text.strip() #기준일
            dojang_rank = maple_rank_base[0].text.strip() #랭킹

            theseed = dojang_and_theseed[1].text.strip() #층수 / 기록
            theseed_date = maple_date_base[1].text.strip() #기준일
            theseed_rank = maple_rank_base[1].text.strip() #랭킹

            union = union_and_achievement[0].text.strip() #등급 / 레벨
            union_date = maple_date_base[2].text.strip() #기준일
            union_rank = maple_rank_base[2].text.strip() #랭킹

            achievement = union_and_achievement[1].text.strip() #등급 / 점수
            achievement_date = maple_date_base[3].text.strip() #기준일
            achievement_rank = maple_rank_base[3].text.strip() #랭킹
            
            userinfo = (user_info[0].text.strip() + '\n' + 
                        user_info[1].text.strip() + '\n' + 
                        user_info[2].text.strip() + '\n' + 
                        user_info[3].text.strip())

            embed = nextcord.Embed(
                title = '메이플 유저정보',
                description = str(maplestory.username[0]) + '의 정보입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='캐릭터 랭킹',value=str(userinfo), inline=False)

            embed.add_field(name='무릉',value=str(dojang), inline=True)
            embed.add_field(name='기준일',value=str(dojang_date), inline=True)
            embed.add_field(name='랭킹',value=str(dojang_rank), inline=True)

            embed.add_field(name='더시드',value=str(theseed), inline=True)
            embed.add_field(name='기준일',value=str(theseed_date), inline=True)
            embed.add_field(name='랭킹',value=str(theseed_rank), inline=True)

            embed.add_field(name='유니온',value=str(union), inline=True)
            embed.add_field(name='기준일',value=str(union_date), inline=True)
            embed.add_field(name='랭킹',value=str(union_rank), inline=True)

            embed.add_field(name='업적',value=str(achievement), inline=True)
            embed.add_field(name='기준일',value=str(achievement_date), inline=True)
            embed.add_field(name='랭킹',value=str(achievement_rank), inline=True)

            await ctx.send(ctx.channel, embed = embed)

            del maplestory.username[0]

        except:
            enc_name = urllib.parse.quote(str(maplestory.username[0]))
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = ('https://maple.gg/u/' + enc_name)
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            maple_data_base = bsObj.find('div', {'class':'row text-center'})
            user_info_base = bsObj.find('div', {'class' : 'row row-normal user-additional'})

            maple_date_base = maple_data_base.find_all('div', {'class' : 'user-summary-date'})
            maple_rank_base = maple_data_base.find_all('div', {'class' : 'mb-2'})
            dojang_and_theseed = maple_data_base.find_all('div', {'class' : 'py-0 py-sm-4'})
            union_and_achievement = maple_data_base.find_all('div', {'class' : 'pt-3 pb-2 pb-sm-3'})
            user_info = user_info_base.find_all('div', {'class' : 'col-lg-2 col-md-4 col-sm-4 col-6 mt-3'})

            dojang = dojang_and_theseed[0].text.strip() #층수 / 기록
            dojang_date = maple_date_base[0].text.strip() #기준일
            dojang_rank = maple_rank_base[0].text.strip() #랭킹

            union = union_and_achievement[0].text.strip() #등급 / 레벨
            union_date = maple_date_base[1].text.strip() #기준일
            union_rank = maple_rank_base[1].text.strip() #랭킹

            achievement = union_and_achievement[1].text.strip() #등급 / 점수
            achievement_date = maple_date_base[2].text.strip() #기준일
            achievement_rank = maple_rank_base[2].text.strip() #랭킹

            userinfo = (user_info[0].text.strip() + '\n' + 
                        user_info[1].text.strip() + '\n' + 
                        user_info[2].text.strip() + '\n' + 
                        user_info[3].text.strip())

            embed = nextcord.Embed(
                title = '메이플 유저정보',
                description = str(maplestory.username[0]) + '의 정보입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='캐릭터 랭킹',value=str(userinfo), inline=False)

            embed.add_field(name='무릉',value=str(dojang), inline=True)
            embed.add_field(name='기준일',value=str(dojang_date), inline=True)
            embed.add_field(name='랭킹',value=str(dojang_rank), inline=True)

            embed.add_field(name='더시드',value='기록이 없습니다', inline=True)
            embed.add_field(name='기준일',value='기록이 없습니다', inline=True)
            embed.add_field(name='랭킹',value='기록이 없습니다', inline=True)
            
            embed.add_field(name='유니온',value=str(union), inline=True)
            embed.add_field(name='기준일',value=str(union_date), inline=True)
            embed.add_field(name='랭킹',value=str(union_rank), inline=True)

            embed.add_field(name='업적',value=str(achievement), inline=True)
            embed.add_field(name='기준일',value=str(achievement_date), inline=True)
            embed.add_field(name='랭킹',value=str(achievement_rank), inline=True)

            await ctx.send(ctx.channel, embed = embed)
            del maplestory.username[0]
    #24
    @bot.command()
    async def 강화공식(ctx):
        jumun = Button(label="주문의 흔적", style = nextcord.ButtonStyle.green)
        star_force_140 = Button(label="스타포스(140)", style = nextcord.ButtonStyle.green)
        star_force_150 = Button(label="스타포스(150)", style = nextcord.ButtonStyle.green)
        star_force_160 = Button(label="스타포스(160)", style = nextcord.ButtonStyle.green)
        star_force_200 = Button(label="스타포스(200)", style = nextcord.ButtonStyle.green)

        async def jumun_callback(interaction):
            embed = nextcord.Embed(
                title = '강화수치',
                description = '주문의 흔적 강화수치입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='주문의 흔적', value='장비 레벨별 강화수치', inline=False)
            embed.add_field(name='0 ~ 70(무기)', 
                            value=
                            '100% : 공/마 + 1\n'+
                            '70% : 공/마 + 2\n' +
                            '30% : 공/마 + 3, 주스텟 + 1\n' +
                            '15% : 공/마 + 5, 주스텟 + 2\n', inline=True)
            embed.add_field(name='80 ~ 110(무기)', 
                            value=
                            '100% : 공/마 + 2\n'+
                            '70% : 공/마 + 3, 주스텟 + 1\n' +
                            '30% : 공/마 + 5, 주스텟 + 2\n' +
                            '15% : 공/마 + 7, 주스텟 + 3\n', inline=True)
            embed.add_field(name='120 ~ 200(무기)', 
                            value=
                            '100% : 공/마 + 3, 주스텟 + 1\n'+
                            '70% : 공/마 + 3, 주스텟 + 2\n' +
                            '30% : 공/마 + 7, 주스텟 + 3\n' +
                            '15% : 공/마 + 9, 주스텟 + 4\n', inline=True)
            embed.add_field(name='0 ~ 70(방어구)',
                            value=
                            '100% : 주스텟 + 1, 방어력 + 1, HP + 5\n' +
                            '70% : 주스텟 + 2, 방어력 + 2, HP + 15\n ' +
                            '30% : 주스텟 + 2, HP + 30\n ', inline=True)
            embed.add_field(name='80 ~ 110(방어구)',
                            value=
                            '100% : 주스텟 + 2, 방어력 + 2, HP + 20\n' +
                            '70% : 주스텟 + 3, 방어력 + 4, HP + 40\n ' +
                            '30% : 주스텟 + 5, 방어력 + 7,HP + 70\n ', inline=True)
            embed.add_field(name='120 ~ 200(방어구)',
                            value=
                            '100% : 주스텟 + 3, 방어력 + 3, HP + 30\n' +
                            '70% : 주스텟 + 4, 방어력 + 5, HP + 70\n ' +
                            '30% : 주스텟 + 7, 방어력 + 10, HP + 120\n ', inline=True)
            embed.add_field(name='0 ~ 70(장갑)',
                            value=
                            '100% : 방어력 + 3\n' +
                            '70% : 공/마 + 1\n ' +
                            '30% : 공/마 + 2\n ', inline=True)
            embed.add_field(name='80 ~ 200(장갑)',
                            value=
                            '100% : 공/마 + 1\n' +
                            '70% : 공/마 + 2\n ' +
                            '30% : 공/마 + 3\n ', inline=True)
            
            await ctx.send(ctx.channel, embed = embed)

        async def star_force_140_callback(interaction):
            embed = nextcord.Embed(
                title = '강화수치',
                description = '스타포스의 강화수치입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='140',
                            value=
                            '1 ~ 5성\n주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' + 
                            '6 ~ 15성\n주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' +
                            '16성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 8\n'
                            '17성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 9\n'
                            '18성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 10\n'
                            '19성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 11\n'
                            '20성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 12\n'
                            '21성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 13\n'
                            '22성\n주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 15\n',inline=True)
            
            await ctx.send(ctx.channel, embed = embed)

        async def star_force_150_callback(interaction):
            embed = nextcord.Embed(
                title = '강화수치',
                description = '스타포스의 강화수치입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='150',
                            value=
                            '1 ~ 5성\n주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' + 
                            '6 ~ 15성\n주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' +
                            '16성\n주스텟 + 11, 방어구 : 공/마 + 9, 무기 : 공/마 + 8\n'
                            '17성\n주스텟 + 11, 방어구 : 공/마 + 10, 무기 : 공/마 + 9\n'
                            '18성\n주스텟 + 11, 방어구 : 공/마 + 11, 무기 : 공/마 + 9\n'
                            '19성\n주스텟 + 11, 방어구 : 공/마 + 12, 무기 : 공/마 + 10\n'
                            '20성\n주스텟 + 11, 방어구 : 공/마 + 13, 무기 : 공/마 + 11\n'
                            '21성\n주스텟 + 11, 방어구 : 공/마 + 14, 무기 : 공/마 + 12\n'
                            '22성\n주스텟 + 11, 방어구 : 공/마 + 15, 무기 : 공/마 + 13\n',inline=True)
            
            await ctx.send(ctx.channel, embed = embed)
        
        async def star_force_160_callback(interaction):
            embed = nextcord.Embed(
                title = '강화수치',
                description = '스타포스의 강화수치입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='160',
                            value=
                            '1 ~ 5성\n주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' + 
                            '6 ~ 15성\n주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' +
                            '16성\n주스텟 + 13, 방어구 : 공/마 + 10, 무기 : 공/마 + 9\n'
                            '17성\n주스텟 + 13, 방어구 : 공/마 + 11, 무기 : 공/마 + 9\n'
                            '18성\n주스텟 + 13, 방어구 : 공/마 + 12, 무기 : 공/마 + 10\n'
                            '19성\n주스텟 + 13, 방어구 : 공/마 + 13, 무기 : 공/마 + 11\n'
                            '20성\n주스텟 + 13, 방어구 : 공/마 + 14, 무기 : 공/마 + 12\n'
                            '21성\n주스텟 + 13, 방어구 : 공/마 + 15, 무기 : 공/마 + 13\n'
                            '22성\n주스텟 + 13, 방어구 : 공/마 + 17, 무기 : 공/마 + 14\n',inline=True)
            
            await ctx.send(ctx.channel, embed = embed)

        async def star_force_200_callback(interaction):
            embed = nextcord.Embed(
                title = '강화수치',
                description = '스타포스의 강화수치입니다',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='200',
                            value=
                            '1 ~ 5성\n주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' + 
                            '6 ~ 15성\n주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동\n' +
                            '16성\n주스텟 + 15, 방어구 : 공/마 + 12, 무기 : 공/마 + 13\n'
                            '17성\n주스텟 + 15, 방어구 : 공/마 + 13, 무기 : 공/마 + 13\n'
                            '18성\n주스텟 + 15, 방어구 : 공/마 + 14, 무기 : 공/마 + 14\n'
                            '19성\n주스텟 + 15, 방어구 : 공/마 + 15, 무기 : 공/마 + 14\n'
                            '20성\n주스텟 + 15, 방어구 : 공/마 + 16, 무기 : 공/마 + 15\n'
                            '21성\n주스텟 + 15, 방어구 : 공/마 + 17, 무기 : 공/마 + 16\n'
                            '22성\n주스텟 + 15, 방어구 : 공/마 + 19, 무기 : 공/마 + 17\n',inline=True)
            
            await ctx.send(ctx.channel, embed = embed)

        jumun.callback = jumun_callback
        star_force_140.callback = star_force_140_callback
        star_force_150.callback = star_force_150_callback
        star_force_160.callback = star_force_160_callback
        star_force_200.callback = star_force_200_callback

        view = View()
        view.add_item(jumun)
        view.add_item(star_force_140)
        view.add_item(star_force_150)
        view.add_item(star_force_160)
        view.add_item(star_force_200)

        await ctx.send(embed = nextcord.Embed(title='강화수치',description="원하시는 버튼을 클릭해주세요", colour=nextcord.Colour.orange()), view=view)        
    #25
    @bot.command()
    async def 무기추옵(ctx):

        wapon_150 = Button(label='150제', style = nextcord.ButtonStyle.green)
        wapon_160 = Button(label='160제', style = nextcord.ButtonStyle.green)
        wapon_200_1 = Button(label='200제', style = nextcord.ButtonStyle.green)
        wapon_200_2 = Button(label='200제(제네시스)', style = nextcord.ButtonStyle.green)
            
        async def wapon_150_callback(Interaction):

            embed = nextcord.Embed(
                title = '추옵표',
                description = '150(파프니르) 무기의 추옵표 입니다\n왼쪽부터 1 ~ 5추옵',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='아대', value='36 28 21 16 11', inline=True)

            embed.add_field(name='건', value='52 40 31 23 16', inline=True)

            embed.add_field(name='너클', value='53 41 31 23 16', inline=True)
            embed.add_field(name='소울슈터', value='53 41 31 23 16', inline=True)
            embed.add_field(name='에너지소드', value='53 41 31 23 16', inline=True)
            embed.add_field(name='건틀렛 리볼버', value='53 41 31 23 16', inline=True)

            embed.add_field(name='폴암', value='63 49 38 27 19', inline=True)

            embed.add_field(name='활', value='66 52 39 29 20', inline=True)
            embed.add_field(name='듀얼보우건', value='66 52 39 29 20', inline=True)
            embed.add_field(name='에인션트 보우', value='66 52 39 29 20', inline=True)
            embed.add_field(name='제인', value='66 52 39 29 20', inline=True)
            embed.add_field(name='단검', value='66 52 39 29 20', inline=True)
            embed.add_field(name='부채', value='66 52 39 29 20', inline=True)

            embed.add_field(name='한손검', value='68 53 40 29 20', inline=True)
            embed.add_field(name='한손도끼', value='68 53 40 29 20', inline=True)
            embed.add_field(name='한손둔기', value='68 53 40 29 20', inline=True)
            embed.add_field(name='석궁', value='68 53 40 29 20', inline=True)
            embed.add_field(name='케인', value='68 53 40 29 20', inline=True)

            embed.add_field(name='두손검', value='71 55 42 31 21', inline=True)
            embed.add_field(name='데스페라도', value='71 55 42 31 21', inline=True)
            embed.add_field(name='튜너', value='71 55 42 31 21', inline=True)
            embed.add_field(name='두손도끼', value='71 55 42 31 21', inline=True)
            embed.add_field(name='두손둔기', value='71 55 42 31 21', inline=True)
            embed.add_field(name='창', value='71 55 42 31 21', inline=True)

            embed.add_field(name='핸드캐논', value='72 56 43 31 21', inline=True)

            embed.add_field(name='완드', value='83 65 49 36 25', inline=True)
            embed.add_field(name='샤이닝로드', value='83 65 49 36 25', inline=True)
            embed.add_field(name='ESP리미터', value='83 65 49 36 25', inline=True)
            embed.add_field(name='매직건틀렛', value='83 65 49 36 25', inline=True)
            
            embed.add_field(name='스태프', value='84 66 50 36 25', inline=True)
            

            await ctx.send(ctx.channel, embed = embed)
            
        async def wapon_160_callback(Interaction):

            embed = nextcord.Embed(
                title = '추옵표',
                description = '160제(앱솔랩스) 무기의 추옵표 입니다\n왼쪽부터 1 ~ 5추옵',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='아대', value='53 42 32 23 16', inline=True)

            embed.add_field(name='건', value='77 60 46 33 23', inline=True)

            embed.add_field(name='너클', value='79 62 47 34 24', inline=True)
            embed.add_field(name='소울슈터', value='79 62 47 34 24', inline=True)
            embed.add_field(name='에너지소드', value='79 62 47 34 24', inline=True)
            embed.add_field(name='건틀렛 리볼버', value='79 62 47 34 24', inline=True)

            embed.add_field(name='폴암', value='95 74 56 41 28', inline=True)

            embed.add_field(name='활', value='99 77 59 43 29', inline=True)
            embed.add_field(name='듀얼보우건', value='99 77 59 43 29', inline=True)
            embed.add_field(name='에인션트 보우', value='99 77 59 43 29', inline=True)
            embed.add_field(name='제인', value='99 77 59 43 29', inline=True)
            embed.add_field(name='단검', value='99 77 59 43 29', inline=True)
            embed.add_field(name='부채', value='99 77 59 43 29', inline=True)

            embed.add_field(name='한손검', value='101 79 60 44 30', inline=True)
            embed.add_field(name='한손도끼', value='101 79 60 44 30', inline=True)
            embed.add_field(name='한손둔기', value='101 79 60 44 30', inline=True)
            embed.add_field(name='석궁', value='101 79 60 44 30', inline=True)
            embed.add_field(name='케인', value='101 79 60 44 30', inline=True)

            embed.add_field(name='두손검', value='106 82 63 46 31', inline=True)
            embed.add_field(name='데스페라도', value='106 82 63 46 31', inline=True)
            embed.add_field(name='튜너', value='106 82 63 46 31', inline=True)
            embed.add_field(name='두손도끼', value='106 82 63 46 31', inline=True)
            embed.add_field(name='두손둔기', value='106 82 63 46 31', inline=True)
            embed.add_field(name='창', value='106 82 63 46 31', inline=True)

            embed.add_field(name='핸드캐논', value='108 84 64 47 32', inline=True)

            embed.add_field(name='완드', value='124 97 73 54 37', inline=True)
            embed.add_field(name='샤이닝로드', value='124 97 73 54 37', inline=True)
            embed.add_field(name='ESP리미터', value='124 97 73 54 37', inline=True)
            embed.add_field(name='매직건틀렛', value='124 97 73 54 37', inline=True)
            
            embed.add_field(name='스태프', value='126 98 75 54 37', inline=True)

            await ctx.send(ctx.channel, embed = embed)
            
        async def wapon_200_1_callback(Interaction):

            embed = nextcord.Embed(
                title = '추옵표',
                description = '200제(아케인셰이드) 무기의 추옵표 입니다\n왼쪽부터 1 ~ 5추옵',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='아대', value='92 72 55 40 27', inline=True)

            embed.add_field(name='건', value='133 104 79 58 39', inline=True)

            embed.add_field(name='너클', value='136 106 81 59 40', inline=True)
            embed.add_field(name='소울슈터', value='136 106 81 59 40', inline=True)
            embed.add_field(name='에너지소드', value='136 106 81 59 40', inline=True)
            embed.add_field(name='건틀렛 리볼버', value='136 106 81 59 40', inline=True)

            embed.add_field(name='폴암', value='163 127 96 70 48', inline=True)

            embed.add_field(name='활', value='170 133 101 73 50', inline=True)
            embed.add_field(name='듀얼보우건', value='170 133 101 73 50', inline=True)
            embed.add_field(name='에인션트 보우', value='170 133 101 73 50', inline=True)
            embed.add_field(name='제인', value='170 133 101 73 50', inline=True)
            embed.add_field(name='단검', value='170 133 101 73 50', inline=True)
            embed.add_field(name='부채', value='170 133 101 73 50', inline=True)

            embed.add_field(name='한손검', value='175 136 103 75 51', inline=True)
            embed.add_field(name='한손도끼', value='175 136 103 75 51', inline=True)
            embed.add_field(name='한손둔기', value='175 136 103 75 51', inline=True)
            embed.add_field(name='석궁', value='175 136 103 75 51', inline=True)
            embed.add_field(name='케인', value='175 136 103 75 51', inline=True)

            embed.add_field(name='두손검', value='182 142 108 78 54', inline=True)
            embed.add_field(name='데스페라도', value='182 142 108 78 54', inline=True)
            embed.add_field(name='튜너', value='182 142 108 78 54', inline=True)
            embed.add_field(name='두손도끼', value='182 142 108 78 54', inline=True)
            embed.add_field(name='두손둔기', value='182 142 108 78 54', inline=True)
            embed.add_field(name='창', value='182 142 108 78 54', inline=True)

            embed.add_field(name='핸드캐논', value='186 145 110 80 55', inline=True)

            embed.add_field(name='완드', value='214 167 126 92 63', inline=True)
            embed.add_field(name='샤이닝로드', value='214 167 126 92 63', inline=True)
            embed.add_field(name='ESP리미터', value='214 167 126 92 63', inline=True)
            embed.add_field(name='매직건틀렛', value='214 167 126 92 63', inline=True)
            
            embed.add_field(name='스태프', value='218 170 129 94 64', inline=True)

            await ctx.send(ctx.channel, embed = embed)
            
        async def wapon_200_2_callback(Interaction):

            embed = nextcord.Embed(
                title = '추옵표',
                description ='200제(제네시스) 무기의 추옵표 입니다\n왼쪽부터 1 ~ 5추옵',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='아대', value='106 83 63 46 31', inline=True)

            embed.add_field(name='건', value='154 120 91 66 45', inline=True)

            embed.add_field(name='너클', value='157 123 93 68 46', inline=True)
            embed.add_field(name='소울슈터', value='157 123 93 68 46', inline=True)
            embed.add_field(name='에너지소드', value='157 123 93 68 46', inline=True)
            embed.add_field(name='건틀렛 리볼버', value='157 123 93 68 46', inline=True)

            embed.add_field(name='폴암', value='187 146 111 81 55', inline=True)

            embed.add_field(name='활', value='196 153 116 84 58', inline=True)
            embed.add_field(name='듀얼보우건', value='196 153 116 84 58', inline=True)
            embed.add_field(name='에인션트 보우', value='196 153 116 84 58', inline=True)
            embed.add_field(name='제인', value='196 153 116 84 58', inline=True)
            embed.add_field(name='단검', value='196 153 116 84 58', inline=True)
            embed.add_field(name='부채', value='196 153 116 84 58', inline=True)

            embed.add_field(name='한손검', value='201 157 119 87 59', inline=True)
            embed.add_field(name='한손도끼', value='201 157 119 87 59', inline=True)
            embed.add_field(name='한손둔기', value='201 157 119 87 59', inline=True)
            embed.add_field(name='석궁', value='201 157 119 87 59', inline=True)
            embed.add_field(name='케인', value='201 157 119 87 59', inline=True)

            embed.add_field(name='두손검', value='210 164 124 90 62', inline=True)
            embed.add_field(name='데스페라도', value='210 164 124 90 62', inline=True)
            embed.add_field(name='튜너', value='210 164 124 90 62', inline=True)
            embed.add_field(name='두손도끼', value='210 164 124 90 62', inline=True)
            embed.add_field(name='두손둔기', value='210 164 124 90 62', inline=True)
            embed.add_field(name='창', value='210 164 124 90 62', inline=True)

            embed.add_field(name='핸드캐논', value='215 167 127 92 63', inline=True)

            embed.add_field(name='완드', value='246 192 146 106 72', inline=True)
            embed.add_field(name='샤이닝로드', value='246 192 146 106 72', inline=True)
            embed.add_field(name='ESP리미터', value='246 192 146 106 72', inline=True)
            embed.add_field(name='매직건틀렛', value='246 192 146 106 72', inline=True)
            
            embed.add_field(name='스태프', value='250 195 148 108 74', inline=True)

            await ctx.send(ctx.channel, embed = embed)

        wapon_150.callback = wapon_150_callback
        wapon_160.callback = wapon_160_callback
        wapon_200_1.callback = wapon_200_1_callback
        wapon_200_2.callback = wapon_200_2_callback
        
        view = View()

        view.add_item(wapon_150)
        view.add_item(wapon_160)
        view.add_item(wapon_200_1)
        view.add_item(wapon_200_2)

        await ctx.send(embed = nextcord.Embed(title='무기 추옵표',description="원하시는 버튼을 클릭해주세요", colour=nextcord.Colour.orange()), view=view)
    #26
    @bot.command()
    async def 레드큐브(ctx, *, msg):
        wapon = Button(label='무기', style = nextcord.ButtonStyle.green)
        emblem = Button(label='엠블렘', style = nextcord.ButtonStyle.green)
        sub_wapon = Button(label='보조무기(포스실드, 소울링 제외)', style = nextcord.ButtonStyle.green)
        force_and_soul = Button(label='포스실드, 소울링', style = nextcord.ButtonStyle.green)
        shield = Button(label='방패', style = nextcord.ButtonStyle.green)
        cap = Button(label='모자', style = nextcord.ButtonStyle.green)
        top = Button(label='상의', style = nextcord.ButtonStyle.green)
        suit = Button(label='한벌옷', style = nextcord.ButtonStyle.green)
        bottom = Button(label='하의', style = nextcord.ButtonStyle.green)
        shoes = Button(label='신발', style = nextcord.ButtonStyle.green)
        gloves = Button(label='장갑', style = nextcord.ButtonStyle.green)
        cloak = Button(label='망토', style = nextcord.ButtonStyle.green)
        belt = Button(label='벨트', style = nextcord.ButtonStyle.green)
        shoulder = Button(label='어깨장식', style = nextcord.ButtonStyle.green)
        face = Button(label='얼굴장식', style = nextcord.ButtonStyle.green)
        eyes = Button(label='눈장식', style = nextcord.ButtonStyle.green)
        earring = Button(label='귀고리', style = nextcord.ButtonStyle.green)
        ring = Button(label='반지', style = nextcord.ButtonStyle.green)
        necklace = Button(label='목걸이', style = nextcord.ButtonStyle.green)
        heart = Button(label='기계심장', style = nextcord.ButtonStyle.green)

        async def wapon_callback(Interaction):

            maple_cube.redcube.wapon(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 무기',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.wapon_result.clear()

        async def emblem_callback(Interaction):

            maple_cube.redcube.emblem(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 엠블렘',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.emblem_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.emblem_result.clear()
            
        async def sub_wapon_callback(Interaction):

            maple_cube.redcube.sub_wapon(0, int(msg))
            
            embed = nextcord.Embed(
            title = '레드큐브 보조무기',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.sub_wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.sub_wapon_result.clear()

        async def force_and_soul_callback(Interaction):

            maple_cube.redcube.force_and_soul(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 포스실드, 소울링',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.force_and_soul_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.force_and_soul_result.clear()

        async def shield_callback(Interaction):

            maple_cube.redcube.shield(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 방패',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shield_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shield_result.clear()
            
        async def cap_callback(Interaction):
            
            maple_cube.redcube.cap(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 모자',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cap_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cap_result.clear()

        async def top_callback(Interaction):

            maple_cube.redcube.top(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 상의',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.top_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.top_result.clear()

        async def suit_callback(Interaction):

            maple_cube.redcube.suit(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 한벌옷',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.suit_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.suit_result.clear()

        async def bottom_callback(Interaction):

            maple_cube.redcube.bottom(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 하의',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.bottom_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.bottom_result.clear()

        async def shoes_callback(Interaction):

            maple_cube.redcube.shoes(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 신발',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoes_result.clear()

        async def gloves_callback(Interaction):

            maple_cube.redcube.gloves(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 장갑',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.gloves_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.gloves_result.clear()

        async def cloak_callback(Interaction):

            maple_cube.redcube.cloak(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 망토',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cloak_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cloak_result.clear()

        async def belt_callback(Interaction):

            maple_cube.redcube.belt(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 벨트',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.belt_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.belt_result.clear()

        async def shoulder_callback(Interaction):

            maple_cube.redcube.shoulder(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 어깨장식',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoulder_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoulder_result.clear()

        async def face_callback(Interaction):

            maple_cube.redcube.face(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 얼굴장식',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.face_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.face_result.clear()

        async def eyes_callback(Interaction):

            maple_cube.redcube.eyes(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 눈장식',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.eyes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.eyes_result.clear()

        async def earring_callback(Interaction):

            maple_cube.redcube.earring(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 귀고리',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.earring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.earring_result.clear()

        async def ring_callback(Interaction):

            maple_cube.redcube.ring(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 반지',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.ring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.ring_result.clear()

        async def necklace_callback(Interaction):

            maple_cube.redcube.necklace(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 목걸이',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.necklace_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.necklace_result.clear()

        async def heart_callback(Interaction):

            maple_cube.redcube.heart(0, int(msg))

            embed = nextcord.Embed(
            title = '레드큐브 기계심장',
            description = '레드큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.heart_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.heart_result.clear()


        wapon.callback = wapon_callback
        emblem.callback = emblem_callback
        sub_wapon.callback = sub_wapon_callback
        force_and_soul.callback = force_and_soul_callback
        shield.callback = shield_callback
        cap.callback = cap_callback
        top.callback = top_callback
        suit.callback = suit_callback
        bottom.callback = bottom_callback
        shoes.callback = shoes_callback
        gloves.callback = gloves_callback
        cloak.callback = cloak_callback
        belt.callback = belt_callback
        shoulder.callback = shoulder_callback
        face.callback = face_callback
        eyes.callback = eyes_callback
        earring.callback = earring_callback
        ring.callback = ring_callback
        necklace.callback = necklace_callback
        heart.callback = heart_callback  

        view = View()
        view.add_item(wapon)
        view.add_item(emblem)
        view.add_item(sub_wapon)
        view.add_item(force_and_soul)
        view.add_item(shield)
        view.add_item(cap)
        view.add_item(top)
        view.add_item(suit)
        view.add_item(bottom)
        view.add_item(shoes)
        view.add_item(gloves)
        view.add_item(cloak)
        view.add_item(belt)
        view.add_item(shoulder)
        view.add_item(face)
        view.add_item(eyes)
        view.add_item(earring)
        view.add_item(ring)
        view.add_item(necklace)
        view.add_item(heart) 

        await ctx.send(embed = nextcord.Embed(title='레드큐브',description="장비 종류를 선택해주세요", colour=nextcord.Colour.orange()), view=view)
    #27
    @bot.command()
    async def 블랙큐브(ctx, *, msg):
        wapon = Button(label='무기', style = nextcord.ButtonStyle.green)
        emblem = Button(label='엠블렘', style = nextcord.ButtonStyle.green)
        sub_wapon = Button(label='보조무기(포스실드, 소울링 제외)', style = nextcord.ButtonStyle.green)
        force_and_soul = Button(label='포스실드, 소울링', style = nextcord.ButtonStyle.green)
        shield = Button(label='방패', style = nextcord.ButtonStyle.green)
        cap = Button(label='모자', style = nextcord.ButtonStyle.green)
        top = Button(label='상의', style = nextcord.ButtonStyle.green)
        suit = Button(label='한벌옷', style = nextcord.ButtonStyle.green)
        bottom = Button(label='하의', style = nextcord.ButtonStyle.green)
        shoes = Button(label='신발', style = nextcord.ButtonStyle.green)
        gloves = Button(label='장갑', style = nextcord.ButtonStyle.green)
        cloak = Button(label='망토', style = nextcord.ButtonStyle.green)
        belt = Button(label='벨트', style = nextcord.ButtonStyle.green)
        shoulder = Button(label='어깨장식', style = nextcord.ButtonStyle.green)
        face = Button(label='얼굴장식', style = nextcord.ButtonStyle.green)
        eyes = Button(label='눈장식', style = nextcord.ButtonStyle.green)
        earring = Button(label='귀고리', style = nextcord.ButtonStyle.green)
        ring = Button(label='반지', style = nextcord.ButtonStyle.green)
        necklace = Button(label='목걸이', style = nextcord.ButtonStyle.green)
        heart = Button(label='기계심장', style = nextcord.ButtonStyle.green)

        async def wapon_callback(Interaction):

            maple_cube.blackcube.wapon(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 무기',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.wapon_result.clear()

        async def emblem_callback(Interaction):

            maple_cube.blackcube.emblem(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 엠블렘',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.emblem_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.emblem_result.clear()
            
        async def sub_wapon_callback(Interaction):

            maple_cube.blackcube.sub_wapon(0, int(msg))
            
            embed = nextcord.Embed(
            title = '블랙큐브 보조무기',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.sub_wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.sub_wapon_result.clear()

        async def force_and_soul_callback(Interaction):

            maple_cube.blackcube.force_and_soul(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 포스실드, 소울링',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.force_and_soul_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.force_and_soul_result.clear()

        async def shield_callback(Interaction):

            maple_cube.blackcube.shield(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 방패',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shield_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shield_result.clear()
            
        async def cap_callback(Interaction):
            
            maple_cube.blackcube.cap(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 모자',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cap_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cap_result.clear()

        async def top_callback(Interaction):

            maple_cube.blackcube.top(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 상의',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.top_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.top_result.clear()

        async def suit_callback(Interaction):

            maple_cube.blackcube.suit(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 한벌옷',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.suit_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.suit_result.clear()

        async def bottom_callback(Interaction):

            maple_cube.blackcube.bottom(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 하의',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.bottom_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.bottom_result.clear()

        async def shoes_callback(Interaction):

            maple_cube.blackcube.shoes(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 신발',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoes_result.clear()

        async def gloves_callback(Interaction):

            maple_cube.blackcube.gloves(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 장갑',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.gloves_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.gloves_result.clear()

        async def cloak_callback(Interaction):

            maple_cube.blackcube.cloak(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 망토',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cloak_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cloak_result.clear()

        async def belt_callback(Interaction):

            maple_cube.blackcube.belt(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 벨트',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.belt_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.belt_result.clear()

        async def shoulder_callback(Interaction):

            maple_cube.blackcube.shoulder(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 어깨장식',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoulder_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoulder_result.clear()

        async def face_callback(Interaction):

            maple_cube.blackcube.face(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 얼굴장식',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.face_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.face_result.clear()

        async def eyes_callback(Interaction):

            maple_cube.blackcube.eyes(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 눈장식',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.eyes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.eyes_result.clear()

        async def earring_callback(Interaction):

            maple_cube.blackcube.earring(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 귀고리',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.earring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.earring_result.clear()

        async def ring_callback(Interaction):

            maple_cube.blackcube.ring(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 반지',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.ring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.ring_result.clear()

        async def necklace_callback(Interaction):

            maple_cube.blackcube.necklace(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 목걸이',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.necklace_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.necklace_result.clear()

        async def heart_callback(Interaction):

            maple_cube.blackcube.heart(0, int(msg))

            embed = nextcord.Embed(
            title = '블랙큐브 기계심장',
            description = '블랙큐브 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.heart_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.heart_result.clear()


        wapon.callback = wapon_callback
        emblem.callback = emblem_callback
        sub_wapon.callback = sub_wapon_callback
        force_and_soul.callback = force_and_soul_callback
        shield.callback = shield_callback
        cap.callback = cap_callback
        top.callback = top_callback
        suit.callback = suit_callback
        bottom.callback = bottom_callback
        shoes.callback = shoes_callback
        gloves.callback = gloves_callback
        cloak.callback = cloak_callback
        belt.callback = belt_callback
        shoulder.callback = shoulder_callback
        face.callback = face_callback
        eyes.callback = eyes_callback
        earring.callback = earring_callback
        ring.callback = ring_callback
        necklace.callback = necklace_callback
        heart.callback = heart_callback  

        view = View()
        view.add_item(wapon)
        view.add_item(emblem)
        view.add_item(sub_wapon)
        view.add_item(force_and_soul)
        view.add_item(shield)
        view.add_item(cap)
        view.add_item(top)
        view.add_item(suit)
        view.add_item(bottom)
        view.add_item(shoes)
        view.add_item(gloves)
        view.add_item(cloak)
        view.add_item(belt)
        view.add_item(shoulder)
        view.add_item(face)
        view.add_item(eyes)
        view.add_item(earring)
        view.add_item(ring)
        view.add_item(necklace)
        view.add_item(heart) 

        await ctx.send(embed = nextcord.Embed(title='블랙큐브',description="장비 종류를 선택해주세요", colour=nextcord.Colour.orange()), view=view)
    #28
    @bot.command()
    async def 에디셔널(ctx, *, msg):
        wapon = Button(label='무기', style = nextcord.ButtonStyle.green)
        emblem = Button(label='엠블렘', style = nextcord.ButtonStyle.green)
        sub_wapon = Button(label='보조무기(포스실드, 소울링 제외)', style = nextcord.ButtonStyle.green)
        force_and_soul = Button(label='포스실드, 소울링', style = nextcord.ButtonStyle.green)
        shield = Button(label='방패', style = nextcord.ButtonStyle.green)
        cap = Button(label='모자', style = nextcord.ButtonStyle.green)
        top = Button(label='상의', style = nextcord.ButtonStyle.green)
        suit = Button(label='한벌옷', style = nextcord.ButtonStyle.green)
        bottom = Button(label='하의', style = nextcord.ButtonStyle.green)
        shoes = Button(label='신발', style = nextcord.ButtonStyle.green)
        gloves = Button(label='장갑', style = nextcord.ButtonStyle.green)
        cloak = Button(label='망토', style = nextcord.ButtonStyle.green)
        belt = Button(label='벨트', style = nextcord.ButtonStyle.green)
        shoulder = Button(label='어깨장식', style = nextcord.ButtonStyle.green)
        face = Button(label='얼굴장식', style = nextcord.ButtonStyle.green)
        eyes = Button(label='눈장식', style = nextcord.ButtonStyle.green)
        earring = Button(label='귀고리', style = nextcord.ButtonStyle.green)
        ring = Button(label='반지', style = nextcord.ButtonStyle.green)
        necklace = Button(label='목걸이', style = nextcord.ButtonStyle.green)
        heart = Button(label='기계심장', style = nextcord.ButtonStyle.green)

        async def wapon_callback(Interaction):

            maple_cube.additional.wapon(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 무기',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.wapon_result.clear()

        async def emblem_callback(Interaction):

            maple_cube.additional.emblem(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 엠블렘',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.emblem_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.emblem_result.clear()
            
        async def sub_wapon_callback(Interaction):

            maple_cube.additional.sub_wapon(0, int(msg))
            
            embed = nextcord.Embed(
            title = '에디셔널 보조무기',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.sub_wapon_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.sub_wapon_result.clear()

        async def force_and_soul_callback(Interaction):

            maple_cube.additional.force_and_soul(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 포스실드, 소울링',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.force_and_soul_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.force_and_soul_result.clear()

        async def shield_callback(Interaction):

            maple_cube.additional.shield(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 방패',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shield_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shield_result.clear()
            
        async def cap_callback(Interaction):
            
            maple_cube.additional.cap(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 모자',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cap_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cap_result.clear()

        async def top_callback(Interaction):

            maple_cube.additional.top(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 상의',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.top_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.top_result.clear()

        async def suit_callback(Interaction):

            maple_cube.additional.suit(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 한벌옷',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.suit_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.suit_result.clear()

        async def bottom_callback(Interaction):

            maple_cube.additional.bottom(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 하의',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.bottom_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.bottom_result.clear()

        async def shoes_callback(Interaction):

            maple_cube.additional.shoes(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 신발',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoes_result.clear()

        async def gloves_callback(Interaction):

            maple_cube.additional.gloves(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 장갑',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.gloves_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.gloves_result.clear()

        async def cloak_callback(Interaction):

            maple_cube.additional.cloak(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 망토',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.cloak_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.cloak_result.clear()

        async def belt_callback(Interaction):

            maple_cube.additional.belt(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 벨트',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.belt_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.belt_result.clear()

        async def shoulder_callback(Interaction):

            maple_cube.additional.shoulder(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 어깨장식',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.shoulder_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.shoulder_result.clear()

        async def face_callback(Interaction):

            maple_cube.additional.face(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 얼굴장식',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.face_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.face_result.clear()

        async def eyes_callback(Interaction):

            maple_cube.additional.eyes(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 눈장식',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.eyes_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.eyes_result.clear()

        async def earring_callback(Interaction):

            maple_cube.additional.earring(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 귀고리',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.earring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.earring_result.clear()

        async def ring_callback(Interaction):

            maple_cube.additional.ring(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 반지',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.ring_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.ring_result.clear()

        async def necklace_callback(Interaction):

            maple_cube.additional.necklace(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 목걸이',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.necklace_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.necklace_result.clear()

        async def heart_callback(Interaction):

            maple_cube.additional.heart(0, int(msg))

            embed = nextcord.Embed(
            title = '에디셔널 기계심장',
            description = '에디셔널 ' + str(msg) + ' 회',
            colour = nextcord.Colour.orange()
            )
            embed.add_field(name=str(msg)+'회의 결과입니다', value=('\n'.join(maple_cube.heart_result)), inline=True)
            await ctx.send(ctx.channel, embed=embed)
            maple_cube.heart_result.clear()


        wapon.callback = wapon_callback
        emblem.callback = emblem_callback
        sub_wapon.callback = sub_wapon_callback
        force_and_soul.callback = force_and_soul_callback
        shield.callback = shield_callback
        cap.callback = cap_callback
        top.callback = top_callback
        suit.callback = suit_callback
        bottom.callback = bottom_callback
        shoes.callback = shoes_callback
        gloves.callback = gloves_callback
        cloak.callback = cloak_callback
        belt.callback = belt_callback
        shoulder.callback = shoulder_callback
        face.callback = face_callback
        eyes.callback = eyes_callback
        earring.callback = earring_callback
        ring.callback = ring_callback
        necklace.callback = necklace_callback
        heart.callback = heart_callback  

        view = View()
        view.add_item(wapon)
        view.add_item(emblem)
        view.add_item(sub_wapon)
        view.add_item(force_and_soul)
        view.add_item(shield)
        view.add_item(cap)
        view.add_item(top)
        view.add_item(suit)
        view.add_item(bottom)
        view.add_item(shoes)
        view.add_item(gloves)
        view.add_item(cloak)
        view.add_item(belt)
        view.add_item(shoulder)
        view.add_item(face)
        view.add_item(eyes)
        view.add_item(earring)
        view.add_item(ring)
        view.add_item(necklace)
        view.add_item(heart) 

        await ctx.send(embed = nextcord.Embed(title='에디셔널',description="장비 종류를 선택해주세요", colour=nextcord.Colour.orange()), view=view)
    
class lol:
    
    champ = []
    line = []

    @bot.command()
    async def 룬(ctx, *, msg):

        lol.champ.append(msg)
        for i in range(160):
            if lol.champ[0] == lol_info.champ_name.champ_kr[i]:
                msg = lol_info.champ_name.champ_en[i]
        
        del lol.champ[0]

        top = Button(label='탑', style = nextcord.ButtonStyle.green)
        jng = Button(label='정글', style = nextcord.ButtonStyle.green)
        mid = Button(label='미드', style = nextcord.ButtonStyle.green)
        adc = Button(label='원딜', style = nextcord.ButtonStyle.green)
        sup = Button(label='서폿', style = nextcord.ButtonStyle.green)
        
        async def top_callback(interaction):
            lol.line.append('top')
            await ctx.send('https://poro.gg/champions/'+str(msg)+'/sr/'+str(lol.line[0]))
            del lol.line[0]
        async def jng_callback(interaction):
            lol.line.append('jng')
            await ctx.send('https://poro.gg/champions/'+str(msg)+'/sr/'+str(lol.line[0]))
            del lol.line[0]
        async def mid_callback(interaction):
            lol.line.append('mid')
            await ctx.send('https://poro.gg/champions/'+str(msg)+'/sr/'+str(lol.line[0]))
            del lol.line[0]
        async def adc_callback(interaction):
            lol.line.append('adc')
            await ctx.send('https://poro.gg/champions/'+str(msg)+'/sr/'+str(lol.line[0]))
            del lol.line[0]
        async def sup_callback(interaction):
            lol.line.append('sup')
            await ctx.send('https://poro.gg/champions/'+str(msg)+'/sr/'+str(lol.line[0]))
            del lol.line[0]
            
        top.callback = top_callback
        jng.callback = jng_callback
        mid.callback = mid_callback
        adc.callback = adc_callback
        sup.callback = sup_callback

        view = View()
        view.add_item(top)
        view.add_item(jng)
        view.add_item(mid)
        view.add_item(adc)
        view.add_item(sup)

        await ctx.send(embed = nextcord.Embed(title='룬 정보',description='포지션을 선택해주세요', colour=nextcord.Colour.orange()), view=view)

    @bot.command()
    async def 추천메타(ctx):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://lolchess.gg/meta')
            driver.find_element_by_xpath('//*[@id="toggle-meta-show-name"]').click()
            element = driver.find_element_by_class_name('guide-meta__group__content')
            element_png = element.screenshot_as_png
            with open('TFT_meta.png.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'TFT_meta.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
            
@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succeseful')
    game = nextcord.Game('업데이트')
    await bot.change_presence(status=nextcord.Status.online, activity = game)
    
bot.run(TOKEN)