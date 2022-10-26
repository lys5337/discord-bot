from gc import callbacks
from http.client import NON_AUTHORITATIVE_INFORMATION
from logging import StrFormatStyle
from pydoc import describe
from sqlite3 import enable_shared_cache
from tkinter import Button
from unittest import result
from xml.dom.minidom import Element
import nextcord
from nextcord.ui import Button, View
from nextcord import Color, Intents, User, user_command
from nextcord.ext import commands
from nextcord.utils import get
from pkg_resources import empty_provider
from selenium.webdriver.chrome.options import Options
from numpy import number
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

def close_new_tabs(driver):
    time.sleep(1)
    tabs = driver.window_handles
    print(tabs)
    while len(tabs) !=1:
        driver.switch_to_window(tabs[1])
        driver.close()

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
        #class weather
        embed.add_field(name = '!날씨[지역]', value = '해당하는 지역의 오늘의 날씨정보와 내일의 날씨정보를 알려줍니다', inline = True) #19
        embed.add_field(name = '!해외날씨[지역]', value = '해당하는 지역의 오늘의 날씨정보와 내일의 날씨정보를 알려줍니다', inline = True) #20
        #class lotto
        embed.add_field(name = '!복권', value = '복권번호를 랜덤추첨 합니다', inline = True) #21

        await ctx.send(channel, embed = embed)

    async def command_game_callback(interaction):
        embed = nextcord.Embed(title = '명령어목록',
        description = '모든 명령어 앞에는 !를 붙입니다',
        colour = nextcord.Colour.blue())

        #class maplestory
        embed.add_field(name = '!메소시세', value = '전날의 메소시세를 알려줍니다', inline = True) #maple-1
        embed.add_field(name = '!유저정보[닉네임]', value = '해당하는 닉네임의 유저정보를 제공합니다', inline = True) #maple-2
        embed.add_field(name = '!강화공식', value = '주문의 흔적, 스타포스의 강화수치를 제공합니다', inline = True) #maple-3
        embed.add_field(name = '!무기추옵', value = '파프니르, 앱솔랩스, 아케인셰이드, 제네시스 무기의 추가옵션을 제공합니다', inline = True) #maple-4
        embed.add_field(name = '!레드큐브[횟수]', value = '레드큐브를 [횟수] 만큼 시뮬레이션 해줍니다', inline = True) #maple-5
        embed.add_field(name = '!블랙큐브[횟수]', value = '블랙큐브를 [횟수] 만큼 시뮬레이션 해줍니다', inline = True) #maple-6
        embed.add_field(name = '!에디셔널[횟수]', value = '에디셔널큐브를 [횟수] 만큼 시뮬레이션 해줍니다', inline = True) #maple-7
        embed.add_field(name = '!레벨[닉네임]', value = '해당하는 닉네임의 레벨 그래프를 보여줍니다', inline = True) #maple-8
        embed.add_field(name = '!심볼', value = '아케인, 어센틱 심볼의 정보를 알려줍니다', inline = True) #maple-9

        embed.add_field(name = '----------------------------------↑메이플----------------------------------', 
                        value = '----------------------------------↓롤----------------------------------', inline = False)
        #class lol
        embed.add_field(name = '!협곡[챔피언 이름]', value = '해당 챔피언의 소환사의 협곡 룬을 알려줍니다', inline = True) #lol-1
        embed.add_field(name = '!칼바람[챔피언 이름]', value = '해당 챔피언의 칼바람나락 룬을 알려줍니다', inline = True) #lol-2
        embed.add_field(name = '!카운터[챔피언 이름]', value = '해당하는 챔피언의 상성을 알려줍니다', inline = True) #lol-3
        embed.add_field(name = '!추천메타', value = '현재 롤토체스 추천메타를 알려줍니다', inline = True) #lol-4

        embed.add_field(name = '----------------------------------↑롤----------------------------------', 
                        value = '----------------------------------↓배그----------------------------------', inline = False)
        #class battle_ground
        embed.add_field(name = '!전적', value = '해당하는 유저의 랭크, 노말게임의 전적을 알려줍니다', inline = True) #bag-1
        embed.add_field(name = '!맵정보', value = '배틀그라운드 전장의 정보를 제공합니다', inline = True) #bag-2
        
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
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

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
            options.add_argument("disable-gpu") 
            options.add_argument("disable-infobars") 
            options.add_argument("--disable-extensions")
            prefs = {'profile.default_content_setting_values': 
            {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
            'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
            'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
            'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
            options.add_experimental_option('prefs', prefs)

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
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

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
            options.add_argument("disable-gpu") 
            options.add_argument("disable-infobars") 
            options.add_argument("--disable-extensions")
            prefs = {'profile.default_content_setting_values': 
            {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
            'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
            'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
            'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
            options.add_experimental_option('prefs', prefs)

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
                options.add_argument("disable-gpu") 
                options.add_argument("disable-infobars") 
                options.add_argument("--disable-extensions")
                prefs = {'profile.default_content_setting_values': 
                {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
                'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
                'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
                'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
                options.add_experimental_option('prefs', prefs)

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
    async def on_reaction_add(reaction, users):

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

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
                
                elif str(reaction.emoji) == '\U0001F4DD':
                    await reaction.message.channel.send("플레이리스트가 나오면 생길 기능이랍니다. 추후에 올릴 영상을 기다려주세요!")
 
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
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

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

    #maple-1
    @bot.command()
    async def 메소시세(ctx):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)
        
        try:
            driver.get('https://talk.gamemarket.kr/maple/graph/')
            element = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[2]/div/div[11]/div[2]/div')
            element_png = element.screenshot_as_png
            with open('pic_maple_meso.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_maple_meso.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #maple-2
    @bot.command()
    async def 유저정보(ctx, *, msg):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://maple.gg/u/' + str(msg))
            element = driver.find_element_by_xpath('//*[@id="user-profile"]/section/div[2]/div[2]/div[4]/button[3]/span').click()
            element = driver.find_element_by_xpath('//*[@id="character-card"]/img[2]')
            element_png = element.screenshot_as_png
            with open('pic_maple_user_info.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_maple_user_info.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #maple-3
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
                title = '140제 강화수치',
                description = '펜살리르, 여제 등',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='1 ~ 5성', value='주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='6 ~ 15성', value='주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='16성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 8', inline=False)
            embed.add_field(name='17성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 9', inline=False)
            embed.add_field(name='18성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 10', inline=False)
            embed.add_field(name='19성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 11', inline=False)
            embed.add_field(name='20성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 12', inline=False)
            embed.add_field(name='21성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 13', inline=False)
            embed.add_field(name='22성', value='주스텟 + 9, 방어구 : 공/마 + 0, 무기 : 공/마 + 15', inline=False)
            
            await ctx.send(ctx.channel, embed = embed)

        async def star_force_150_callback(interaction):
            embed = nextcord.Embed(
                title = '150제 강화수치',
                description = '카루타 세트',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='1 ~ 5성', value='주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='6 ~ 15성', value='주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='16성', value='주스텟 + 11, 방어구 : 공/마 + 9, 무기 : 공/마 + 8', inline=False)
            embed.add_field(name='17성', value='주스텟 + 11, 방어구 : 공/마 + 10, 무기 : 공/마 + 9', inline=False)
            embed.add_field(name='18성', value='주스텟 + 11, 방어구 : 공/마 + 11, 무기 : 공/마 + 9', inline=False)
            embed.add_field(name='19성', value='주스텟 + 11, 방어구 : 공/마 + 12, 무기 : 공/마 + 10', inline=False)
            embed.add_field(name='20성', value='주스텟 + 11, 방어구 : 공/마 + 13, 무기 : 공/마 + 11', inline=False)
            embed.add_field(name='21성', value='주스텟 + 11, 방어구 : 공/마 + 14, 무기 : 공/마 + 12', inline=False)
            embed.add_field(name='22성', value='주스텟 + 11, 방어구 : 공/마 + 15, 무기 : 공/마 + 13', inline=False)
            
            await ctx.send(ctx.channel, embed = embed)
        
        async def star_force_160_callback(interaction):
            embed = nextcord.Embed(
                title = '160제 강화수치',
                description = '앱솔랩스',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='1 ~ 5성', value='주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='6 ~ 15성', value='주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='16성', value='주스텟 + 13, 방어구 : 공/마 + 10, 무기 : 공/마 + 9', inline=False)
            embed.add_field(name='17성', value='주스텟 + 13, 방어구 : 공/마 + 11, 무기 : 공/마 + 9', inline=False)
            embed.add_field(name='18성', value='주스텟 + 13, 방어구 : 공/마 + 12, 무기 : 공/마 + 10', inline=False)
            embed.add_field(name='19성', value='주스텟 + 13, 방어구 : 공/마 + 13, 무기 : 공/마 + 11', inline=False)
            embed.add_field(name='20성', value='주스텟 + 13, 방어구 : 공/마 + 14, 무기 : 공/마 + 12', inline=False)
            embed.add_field(name='21성', value='주스텟 + 13, 방어구 : 공/마 + 15, 무기 : 공/마 + 13', inline=False)
            embed.add_field(name='22성', value='주스텟 + 13, 방어구 : 공/마 + 17, 무기 : 공/마 + 14', inline=False)
            
            await ctx.send(ctx.channel, embed = embed)

        async def star_force_200_callback(interaction):
            embed = nextcord.Embed(
                title = '200제 강화수치',
                description = '아케인셰이드',
                colour = nextcord.Colour.orange()
            )
            embed.add_field(name='1 ~ 5성', value='주스텟 + 2, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='6 ~ 15성', value='주스텟 + 3, 방어구 : 공/마 + 0, 무기 : 공/마 + 변동', inline=False)
            embed.add_field(name='16성', value='주스텟 + 15, 방어구 : 공/마 + 12, 무기 : 공/마 + 13', inline=False)
            embed.add_field(name='17성', value='주스텟 + 15, 방어구 : 공/마 + 13, 무기 : 공/마 + 13', inline=False)
            embed.add_field(name='18성', value='주스텟 + 15, 방어구 : 공/마 + 14, 무기 : 공/마 + 14', inline=False)
            embed.add_field(name='19성', value='주스텟 + 15, 방어구 : 공/마 + 15, 무기 : 공/마 + 14', inline=False)
            embed.add_field(name='20성', value='주스텟 + 15, 방어구 : 공/마 + 16, 무기 : 공/마 + 15', inline=False)
            embed.add_field(name='21성', value='주스텟 + 15, 방어구 : 공/마 + 17, 무기 : 공/마 + 16', inline=False)
            embed.add_field(name='22성', value='주스텟 + 15, 방어구 : 공/마 + 19, 무기 : 공/마 + 17', inline=False)

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
    #maple-4
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
    #maple-5
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
    #maple-6
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
    #maple-7
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
    #maple-8
    @bot.command()
    async def 레벨(ctx, *, msg):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://maple.gg/u/' + str(msg))
            element = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/section/div[2]')
            element_png = element.screenshot_as_png
            with open('pic_maple_user_level.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_maple_user_level.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #maple-9
    @bot.command()
    async def 심볼(ctx):
        embed = nextcord.Embed(
            title='아케인, 어센틱 심볼 정보',
            description='각 심볼 렐벨별 개수, 가격',
            colour = nextcord.Colour.orange())
        
        embed.add_field(name='레벨별 필요 개수',
        value=
        '1 > 2 : 12개\n'+ 
        '2 > 3 : 15개\n'+
        '3 > 4 : 20개\n'+
        '4 > 5 : 27개\n'+
        '5 > 6 : 36개\n'+
        '6 > 7 : 47개\n'+
        '7 > 8 : 60개\n'+
        '8 > 9 : 75개\n'+
        '9 > 10 : 92개\n'+
        '10 > 11 : 111개\n'+
        '11 > 12 : 132개\n'+
        '12 > 13 : 155개\n'+
        '13 > 14 : 180개\n'+
        '14 > 15 : 207개\n'+
        '15 > 16 : 236개\n'+
        '16 > 17 : 267개\n'+
        '17 > 18 : 300개\n'+
        '18 > 19 : 335개\n'+
        '19 > 20 : 372개\n',
        inline=True)
        
        embed.add_field(name='소멸의 여로 (가격)',
        value=
        '7,070,000\n'+
        '11,030,000\n'+
        '14,990,000\n'+
        '18,950,000\n'+
        '22,910,000\n'+
        '26,870,000\n'+
        '30,830,000\n'+
        '34,790,000\n'+
        '38,750,000\n'+
        '42,710,000\n'+
        '46,670,000\n'+
        '50,630,000\n'+
        '54,590,000\n'+
        '58,550,000\n'+
        '62,510,000\n'+
        '66,470,000\n'+
        '70,430,000\n'+
        '74,390,000\n'+
        '78,350,000\n'+
        '총가격:811,490,000'
        ,inline=True)

        embed.add_field(name='츄츄 아일랜드 (가격)',
        value=
        '10,840,000\n'+
        '15,460,000\n'+
        '20,080,000\n'+
        '24,700,000\n'+
        '29,320,000\n'+
        '33,940,000\n'+
        '38,560,000\n'+
        '43,180,000\n'+
        '47,800,000\n'+
        '52,420,000\n'+
        '57,040,000\n'+
        '61,660,000\n'+
        '66,280,000\n'+
        '70,900,000\n'+
        '75,520,000\n'+
        '80,140,000\n'+
        '84,760,000\n'+
        '89,380,000\n'+
        '94,000,000\n'+
        '총가격: 995,980,000'
        ,inline=True)

        embed.add_field(name='레벨별 필요 개수',
        value=
        '1 > 2 : 12개\n'+ 
        '2 > 3 : 15개\n'+
        '3 > 4 : 20개\n'+
        '4 > 5 : 27개\n'+
        '5 > 6 : 36개\n'+
        '6 > 7 : 47개\n'+
        '7 > 8 : 60개\n'+
        '8 > 9 : 75개\n'+
        '9 > 10 : 92개\n'+
        '10 > 11 : 111개\n'+
        '11 > 12 : 132개\n'+
        '12 > 13 : 155개\n'+
        '13 > 14 : 180개\n'+
        '14 > 15 : 207개\n'+
        '15 > 16 : 236개\n'+
        '16 > 17 : 267개\n'+
        '17 > 18 : 300개\n'+
        '18 > 19 : 335개\n'+
        '19 > 20 : 372개\n',
        inline=True)

        embed.add_field(name='레헬른 (가격)',
        value=
        '14,610,000\n'+
        '19,890,000\n'+
        '25,170,000\n'+
        '30,450,000\n'+
        '35,730,000\n'+
        '41,010,000\n'+
        '46,290,000\n'+
        '51,570,000\n'+
        '56,850,000\n'+
        '62,130,000\n'+
        '67,410,000\n'+
        '72,690,000\n'+
        '77,970,000\n'+
        '83,250,000\n'+
        '88,530,000\n'+
        '93,810,000\n'+
        '99,090,000\n'+
        '104,370,000\n'+
        '109,650,000\n'+
        '총가격: 1,180,470,000'
        ,inline=True)

        embed.add_field(name='아르카나 ~ 에스페라 (가격)',
        value=
        '17,136,000\n'+
        '23,076,000\n'+
        '29,016,000\n'+
        '34,956,000\n'+
        '40,896,000\n'+
        '46,836,000\n'+
        '52,776,000\n'+
        '58,716,000\n'+
        '64,656,000\n'+
        '70,596,000\n'+
        '76,536,000\n'+
        '82,476,000\n'+
        '88,416,000\n'+
        '94,356,000\n'+
        '100,296,000\n'+
        '106,236,000\n'+
        '112,176,000\n'+
        '118,116,000\n'+
        '124,056,000\n'+
        '총가격: 1,341,324,000'
        ,inline=True)

        await ctx.send(ctx.channel, embed = embed)


class lol:
    
    champ = []
    link = []
    #lol-1
    @bot.command()
    async def 협곡(ctx, *, msg):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://lol.ps/ko/statistics/')
            element = driver.find_element_by_name('q')
            element.clear
            element.send_keys(str(msg))
            element.send_keys(Keys.RETURN)

            element = driver.find_element_by_xpath('/html/body/main/div[3]/section')
            element_png = element.screenshot_as_png
            with open('pic_lol_lune.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_lol_lune.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #lol-2
    @bot.command()
    async def 칼바람(ctx, *, msg):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        for i in range(len(lol_info.champ_name.champ_kr)):
            if msg == lol_info.champ_name.champ_kr[i]:
                msg = lol_info.champ_name.champ_en[i]
        
        for i in range(len(lol_info.champ_name.champ_slang_kr)):
            if msg == lol_info.champ_name.champ_slang_kr[i]:
                msg = lol_info.champ_name.champ_slang_en[i]
        
        try:
            driver.get('https://poro.gg/champions/'+str(msg)+'/aram')
            element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/section[2]')
            element_png = element.screenshot_as_png
            with open('pic_lol_aram.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_lol_aram.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #lol-3
    @bot.command()
    async def 카운터(ctx, *, msg):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://lol.ps/ko/statistics/')
            element = driver.find_element_by_name('q')
            element.clear
            element.send_keys(str(msg))
            element.send_keys(Keys.RETURN)

            element = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/section[2]/div')
            element_png = element.screenshot_as_png
            with open('pic_lol_counter.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_lol_counter.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))
    #lol-4
    @bot.command()
    async def 추천메타(ctx):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)
        
        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        try:
            driver.get('https://lolchess.gg/meta')
            driver.find_element_by_xpath('//*[@id="toggle-meta-show-name"]').click()
            element = driver.find_element_by_class_name('guide-meta__group__content')
            element_png = element.screenshot_as_png
            with open('pic_lol_TFT_meta.png', 'wb') as file:
                file.write(element_png)
            driver.quit()
            print("### capture complete")
        except Exception as e:
            print('### error msg :: ', e)
            driver.quit()

        pic_name = 'pic_lol_TFT_meta.png'
        pic = pic_name.split(' ')[0]
        await ctx.send(file = nextcord.File(pic))

class battleground:
    #bag-1
    @bot.command()
    async def 전적(ctx, *, msg):
        steam = Button(label='STEAM', style = nextcord.ButtonStyle.green)
        kakao = Button(label='kakao', style = nextcord.ButtonStyle.green)
        psn = Button(label='PSN', style = nextcord.ButtonStyle.green)
        Stadia = Button(label='Stadia', style = nextcord.ButtonStyle.green)
        Xbox = Button(label='Xbox', style = nextcord.ButtonStyle.green)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x3400')
        options.add_argument("disable-gpu") 
        options.add_argument("disable-infobars") 
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': 
        {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 
        'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 
        'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 
        'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(r"C:\Users\c\Desktop\chromedriver.exe", options=options)

        async def steam_callback(interaction):
            try:
                driver.get('https://dak.gg/pubg/profile/steam/'+ str(msg))
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[1]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_rank.png', 'wb') as file:
                    file.write(element_png)
                    
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[2]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_normal.png', 'wb') as file:
                    file.write(element_png)
                driver.quit()
                print("### capture complete")
            except Exception as e:
                print('### error msg :: ', e)
                driver.quit()
                embed = nextcord.Embed(
                    title = '해당하는 유저가 없습니다',
                    description = '닉네임을 다시 입력하여 주세요\n' + '혹은 서버를 다시 확인하여 주세요',
                    colour = nextcord.Colour.dark_green())
                await ctx.send(ctx.channel, embed = embed)
                return 0

            pic_name = 'pic_battleground_rank.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('랭크')
            await ctx.send(file = nextcord.File(pic))

            pic_name = 'pic_battleground_normal.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('일반')
            await ctx.send(file = nextcord.File(pic))

        async def kakao_callback(interaction):
            try:
                driver.get('https://dak.gg/pubg/profile/kakao/'+ str(msg))
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[1]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_rank.png', 'wb') as file:
                    file.write(element_png)
                    
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[2]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_normal.png', 'wb') as file:
                    file.write(element_png)
                driver.quit()
                print("### capture complete")
            except Exception as e:
                print('### error msg :: ', e)
                driver.quit()
                embed = nextcord.Embed(
                    title = '해당하는 유저가 없습니다',
                    description = '닉네임을 다시 입력하여 주세요\n' + '혹은 서버를 다시 확인하여 주세요',
                    colour = nextcord.Colour.dark_green())
                await ctx.send(ctx.channel, embed = embed)
                return 0

            pic_name = 'pic_battleground_rank.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('랭크')
            await ctx.send(file = nextcord.File(pic))

            pic_name = 'pic_battleground_normal.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('일반')
            await ctx.send(file = nextcord.File(pic))

        async def psn_callback(interaction):
            try:
                driver.get('https://dak.gg/pubg/profile/psn/'+ str(msg))
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[1]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_rank.png', 'wb') as file:
                    file.write(element_png)
                    
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[2]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_normal.png', 'wb') as file:
                    file.write(element_png)
                driver.quit()
                print("### capture complete")
            except Exception as e:
                print('### error msg :: ', e)
                driver.quit()
                embed = nextcord.Embed(
                    title = '해당하는 유저가 없습니다',
                    description = '닉네임을 다시 입력하여 주세요\n' + '혹은 서버를 다시 확인하여 주세요',
                    colour = nextcord.Colour.dark_green())
                await ctx.send(ctx.channel, embed = embed)
                return 0

            pic_name = 'pic_battleground_rank.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('랭크')
            await ctx.send(file = nextcord.File(pic))

            pic_name = 'pic_battleground_normal.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('일반')
            await ctx.send(file = nextcord.File(pic))

        async def Stadia_callback(interaction):
            try:
                driver.get('https://dak.gg/pubg/profile/stadia/'+ str(msg))
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[1]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_rank.png', 'wb') as file:
                    file.write(element_png)
                    
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[2]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_normal.png', 'wb') as file:
                    file.write(element_png)
                driver.quit()
                print("### capture complete")
            except Exception as e:
                print('### error msg :: ', e)
                driver.quit()
                embed = nextcord.Embed(
                    title = '해당하는 유저가 없습니다',
                    description = '닉네임을 다시 입력하여 주세요\n' + '혹은 서버를 다시 확인하여 주세요',
                    colour = nextcord.Colour.dark_green())
                await ctx.send(ctx.channel, embed = embed)
                return 0

            pic_name = 'pic_battleground_rank.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('랭크')
            await ctx.send(file = nextcord.File(pic))

            pic_name = 'pic_battleground_normal.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('일반')
            await ctx.send(file = nextcord.File(pic))

        async def Xbox_callback(interaction):
            try:
                driver.get('https://dak.gg/pubg/profile/xbox/'+ str(msg))
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[1]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_rank.png', 'wb') as file:
                    file.write(element_png)
                    
                element = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/section[1]/section[2]')
                element_png = element.screenshot_as_png
                with open('pic_battleground_normal.png', 'wb') as file:
                    file.write(element_png)
                driver.quit()
                print("### capture complete")
            except Exception as e:
                print('### error msg :: ', e)
                driver.quit()
                embed = nextcord.Embed(
                    title = '해당하는 유저가 없습니다',
                    description = '닉네임을 다시 입력하여 주세요\n' + '혹은 서버를 다시 확인하여 주세요',
                    colour = nextcord.Colour.dark_green())
                await ctx.send(ctx.channel, embed = embed)
                return 0

            pic_name = 'pic_battleground_rank.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('랭크')
            await ctx.send(file = nextcord.File(pic))

            pic_name = 'pic_battleground_normal.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('일반')
            await ctx.send(file = nextcord.File(pic))

        steam.callback = steam_callback
        kakao.callback = kakao_callback
        psn.callback = psn_callback
        Stadia.callback = Stadia_callback
        Xbox.callback = Xbox_callback

        view = View()
        view.add_item(steam)
        view.add_item(kakao)
        view.add_item(psn)
        view.add_item(Stadia)
        view.add_item(Xbox)

        await ctx.send(embed = nextcord.Embed(title='배그 전적검색',description='서버를 선택해주세요', colour=nextcord.Colour.dark_green()), view=view)
    #vag-2
    @bot.command()
    async def 맵정보(ctx):
        Erangel = Button(label='에란겔', style = nextcord.ButtonStyle.green)
        Miramar = Button(label='미라마', style = nextcord.ButtonStyle.green)
        Taego = Button(label='태이고', style = nextcord.ButtonStyle.green)
        DESTON = Button(label='데스턴', style = nextcord.ButtonStyle.green)
        Vikendi = Button(label='비켄디', style = nextcord.ButtonStyle.green)
        Sanhok = Button(label='사녹', style = nextcord.ButtonStyle.green)
        Paramo = Button(label='파라모', style = nextcord.ButtonStyle.green)
        Karakin = Button(label='카라킨', style = nextcord.ButtonStyle.green)
        HAVEN = Button(label='헤이븐', style = nextcord.ButtonStyle.green)
        Camp = Button(label='캠프자칼(훈련장)', style = nextcord.ButtonStyle.green)

        async def Erangel_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '에란겔',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/erangel/', value='링크를 클릭해주세요', inline=False)
            await ctx.send(ctx.channel, embed = embed)

        async def Miramar_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '미라마',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/miramar/', value='링크를 클릭해주세요', inline=False)
            await ctx.send(ctx.channel, embed = embed)

        async def Taego_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '태이고',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/taego/', value='링크를 클릭해주세요', inline=False)
            await ctx.send(ctx.channel, embed = embed)

        async def DESTON_callback(interaction):
            pic_name = 'pic_battleground_DESTON.png'
            pic = pic_name.split(' ')[0]
            await ctx.send('데스턴 (빨간색 = 등강기)\n' + '아직 인벤에 업로드되지 않은 맵이므로 정확한이미지가 없습니다')
            await ctx.send(file = nextcord.File(pic))

        async def Vikendi_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '비켄디',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/vikendi/', value='링크를 클릭해주세요', inline=False)                
            await ctx.send(ctx.channel, embed = embed)

        async def Sanhok_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '사녹',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/sanhok/', value='링크를 클릭해주세요', inline=False)   
            await ctx.send(ctx.channel, embed = embed)

        async def Paramo_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '파라모',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/paramo/', value='링크를 클릭해주세요', inline=False)  
            await ctx.send(ctx.channel, embed = embed)
              
        async def Karakin_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '카라킨',
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/karakin/', value='링크를 클릭해주세요', inline=False)
            await ctx.send(ctx.channel, embed = embed)

        async def HAVEN_callback(interaction):
            embed = nextcord.Embed(title = '배그 맵정보',
                    description = '헤이븐', 
                    colour = nextcord.Colour.blue())
            embed.add_field(name='https://pubg.inven.co.kr/dataninfo/map/haven/', value='링크를 클릭해주세요', inline=False)
            await ctx.send(ctx.channel, embed = embed)

        async def Camp_callback(interaction):
            await ctx.send('test success')

        Erangel.callback = Erangel_callback
        Miramar.callback = Miramar_callback
        Taego.callback = Taego_callback
        DESTON.callback = DESTON_callback
        Vikendi.callback = Vikendi_callback
        Sanhok.callback = Sanhok_callback
        Paramo.callback = Paramo_callback
        Karakin.callback = Karakin_callback
        HAVEN.callback = HAVEN_callback
        Camp.callback = Camp_callback

        view = View()
        view.add_item(Erangel)
        view.add_item(Miramar)
        view.add_item(Taego)
        view.add_item(DESTON)
        view.add_item(Vikendi)
        view.add_item(Sanhok)
        view.add_item(Paramo)
        view.add_item(Karakin)
        view.add_item(HAVEN)
        view.add_item(Camp)

        await ctx.send(embed = nextcord.Embed(title='배그 맵정보',description='원하는 맵의 버튼을 놀러주세요', colour=nextcord.Colour.dark_green()), view=view)

        
@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succeseful')
    game = nextcord.Game('업데이트')
    await bot.change_presence(status=nextcord.Status.online, activity = game)
    
bot.run(TOKEN)