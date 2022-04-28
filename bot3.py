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
from urllib.request import urlopen, Request
import urllib
import urllib.request

TOKENVALUE = open(r'C:\Users\c\Desktop\bot_TOKEN\discord_TOKEN.txt','r')
TOKEN = TOKENVALUE.read()
TOKENVALUE.close()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)
client = nextcord.Client()

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
#00
    @bot.command()
    async def 명령어(ctx):
        detail_command = Button(label="자세히", style = nextcord.ButtonStyle.green)
        simple_command = Button(label="간단히", style = nextcord.ButtonStyle.green)
        channel = ctx.channel
        
        async def detail_command_callback(interaction):
            embed = nextcord.Embed(title = '명령어목록',
            description = '모든 명령어 앞에는 !를 붙입니다',
            colour = nextcord.Colour.blue())
            embed.add_field(name = '!들어와', value = '봇이 음성채널에 참가합니다(사용자가 있을경우에만)',inline = False) #01
            embed.add_field(name = '!나가', value = '봇이 음성채널에서 나갑니다', inline = False) #02
            embed.add_field(name = '!재생[제목/링크]', value = '제목/링크를 입력하면 재생합니다, 이미 재생중이라면 목록에 추가합니다', inline = False) #03
            embed.add_field(name = '!반복재생[제목/링크]', value = '제목/링크를 입력하면 그 노래를 반복재생합니다.', inline = False) #04
            embed.add_field(name = '!멜론차트', value = '최신 주의 멜론차트를 재생합니다', inline = False) #05
            embed.add_field(name = '!지금노래', value = '현재 재생중인 곡의 제목을 알려줍니다', inline = False) #06
            embed.add_field(name = '!목록', value = '앞으로 재생할 곡의 리스트를 보여줍니다.', inline = False) #07
            embed.add_field(name = '!추가/삭제[제목,링크]', value = '목록에있는 리스트에 추가/삭제 합니다', inline = False) #08
            embed.add_field(name = '!목록재생', value = '목록에 등록되어있는 리스트를 재생합니다', inline = False) #09
            embed.add_field(name = '!목록초기화', value = '현재 목록에 등록된 모든 노래를 초기화시킵니다', inline = False) #10
            embed.add_field(name = '!목록섞기', value = '현재 목록에 등록된 모든 노래의 순서를 랜덤하게 섞습니다', inline = False) #11
            embed.add_field(name = '!일시정지', value = '현재 재생중인 곡을 일시정지 시킵니다.', inline = False) #12
            embed.add_field(name = '!다시재생', value = '일시정지중인 곡을 다시 재생시킵니다', inline = False) #13
            embed.add_field(name = '!노래끄기', value = '현재 재생중인 곡을 즉시종료시킵니다', inline = False) #14
            embed.add_field(name = '!스킵', value = '현재 재생중인 곡을 스킵하고 다음곡을 재생합니다', inline = False) #15
            embed.add_field(name = '!즐겨찾기', value = '유저별로 플레이리스트를 저장하여 보여줍니다', inline = False) #16
            embed.add_field(name = '!즐겨찾기추가 / 즐겨찾기삭제', value = '유저별 즐겨찾기 목록에 곡을 추가/삭제 합니다', inline = False) #17
            embed.add_field(name = '!정밀검색', value = '검색한 내용의 유튜브영상을 최대 5개까지 보여줍니다') #18

            await ctx.send(channel, embed = embed)

        async def simple_command_callback(interaction):
            embed = nextcord.Embed(
            title = '명령어목록',
            description = '모든 명령어 앞에는 !를 붙입니다',
            colour = nextcord.Colour.blue())
            embed.add_field(name = '.', value = 
            '목록섞기, 목록, 추가/삭제[제목,링크], 목록재생, 목록초기화, 일시정지\n'+
            '들어와, 나가, 재생[제목/링크], 반복재생[제목/링크], 멜론차트, 지금노래\n' +
            '다시재생, 노래끄기, 스킵, 즐겨찾기, 즐겨찾기추가 / 즐겨찾기삭제, 정밀검색\n', inline = False)
            
            await ctx.send(channel, embed = embed)

        detail_command.callback = detail_command_callback
        simple_command.callback = simple_command_callback

        view = View()
        view.add_item(detail_command)
        view.add_item(simple_command)
    
        await ctx.send(embed = nextcord.Embed(title='명령어 설명',description="원하시는 버튼을 클릭해주세요", colour=nextcord.Colour.blue()), view=view)

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
            await ctx.send(embed = nextcord.Embed(title = "노래 재생", description = "현재 " + musicbot.musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
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

    @bot.command()
    async def 날씨(ctx, *,msg):
        weather.location.append(msg)
        enc_location = urllib.parse.quote(str(weather.location[0]) + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'weather_info'})
        tommorrowBase = bsObj.find('ul', {'class': 'weather_info_list'})

        todayTemp1 = todayBase.find('div', {'class': 'temperature_text'})
        todayTemp2 = todayTemp1.find('strong')
        todayTemp = todayTemp2.text.strip()  # 온도

        thanYesturday1 = todayBase.find('div', {'class':'temperature_info'})
        thanYesturday = thanYesturday1.text.strip() #현재상태

        todayDust1 = todayBase.find('ul', {'class': 'today_chart_list'})
        todayDust = todayDust1.text.strip() #대기상

        tommorrowMornig = [] #내일 오전 정보
        tommorrowAfternoon = [] #내일 오후 정보
        tommorrowMornig = tommorrowBase.text.strip()
        tommorrowAfternoon = tommorrowBase.text.strip()

        embed = nextcord.Embed(
            title = str(weather.location) + ' 날씨 정보',
            description = str(weather.location) + '날씨 정보입니다.',
            colour = nextcord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=str(todayTemp), inline=False)  # 현재온도
        embed.add_field(name='현재상태', value=str(thanYesturday), inline=False)  # 현재상태
        embed.add_field(name='대기상태', value=str(todayDust), inline=False)  # 대기상태
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일오전', value=str(tommorrowMornig[0:70]), inline=False) #내일오전
        embed.add_field(name='내일오후', value=str(tommorrowAfternoon[76:140]), inline=False) #내일오후

        await ctx.send(ctx.channel,embed=embed)

        del weather.location[0]


 

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succeseful')
    game = nextcord.Game('음악 연구')
    await bot.change_presence(status=nextcord.Status.online, activity = game)
    
bot.run(TOKEN)