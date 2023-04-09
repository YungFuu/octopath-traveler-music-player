# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:00:16 2022
@author: B站 搜索 加加大勇者
"""

#%% 环境设置

import difflib
import time,os,random
import pygame
from datetime import datetime as dt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # 隐藏根窗口

# 打开文件夹选择对话框
path = filedialog.askdirectory()
song_list=[]
song_dict={}


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
def get_key (dict, value):
               return [k for k, v in dict.items() if v == value]


#key_word = ' - Battle On '
key_word = ' -夜-'



#%% 加载歌曲


for i in os.listdir(path):
    if '.mp3' in i:
        mf = ".mp3"
    elif '.ogg' in i:
        mf = ".ogg"
 
#配对主题曲       
for i in os.listdir(path):    
    if 'OCTOPATH TRAVELER II メインテーマ' in i:
        old_name = path + os.sep + i
        new_name = path + os.sep + "西木康智 - メインテーマ"  +mf
        os.rename(old_name, new_name)


for i in os.listdir(path):    
    if mf in i:
        song_list.append(i)

for z in range(0,6):
    for night_music in song_list:
        if key_word in night_music:
            day_name = night_music.split(key_word + mf )[0] + mf


            for day_music in song_list:
                if day_name == day_music :
                    song_dict[day_name]=night_music
                else:
                    pass
        else: 
            pass


song_list =  list(song_dict.keys())
song_list2 = list(song_dict.values())
file = song_list[0]

print('歌单列表')
print('====================')
for i in song_list:
    print(i)



#%%

def play(file=file):
    global begin_point
    file_path = path + os.sep + file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    begin_point = dt.now()
    
    
def random_song():
    global file
    file = song_list[random.randint(0, len(song_list)-1)]
    play(file)
    


def auto_play(daytype):
    global file
    
    if daytype == True: #白天，继续播放白天歌曲
        if len(song_list) > song_list.index(file)+1:
            file = song_list[song_list.index(file) + 1]
        elif len(song_list) == song_list.index(file)+1:
            file = song_list[0]
    elif daytype == False: #晚上，继续播放晚上的歌曲
        if len(song_list2) > song_list2.index(file)+1:
            file = song_list2[song_list2.index(file) + 1]
        elif len(song_list2) == song_list2.index(file)+1:
            file = song_list2[0]
    play(file)
        
        
        
    
    
                
def pause_music():
    pygame.mixer.music.pause()
    

def unpause_music():
    pygame.mixer.music.unpause()    

def fadeout(sleeptime):
    pygame.mixer.music.fadeout(int(sleeptime/2*10000))
    
    
    
    
        
#运行界面
def main():
    # 初始化文字屏幕
    pygame.font.init()
    # 初始化图像屏幕
    pygame.init()

    #初始化窗口
    pygame.display.set_caption("OCTOPATH MUSIC PLAYER")
    logo = pygame.image.load("pic\icon"+ os.sep+ "logo.png")
    pygame.display.set_icon(logo)
    
    # 初始化字体
    font_name = pygame.font.match_font('KaiTi')  # 2.获得字体文件 KaiTi
    font = pygame.font.Font(font_name, 20)
    
    #初始化背景
    screen = pygame.display.set_mode((880,495))
    bg_path = "pic" + os.sep + "bg"
    
    #加载角色轮播图
    font_surface = font.render('载入中，请稍后......', True, 'white')
    screen.blit(font_surface, (20, 20))
    pygame.display.flip()
    
    # #百兽村/纳那西村岛   ケモノ達の古里
    shouren_day = pygame.image.load(bg_path+ os.sep+ "shouren_day.png")
    shouren_night = pygame.image.load(bg_path+ os.sep+ "shouren_night.png")
    shouren_dusk = pygame.image.load(bg_path+ os.sep+ "shouren_dusk.png")
    
    #库国 朱き晩陽のク国
    kuguo_day = pygame.image.load(bg_path+ os.sep+ "kuguo_day.png")
    kuguo_night = pygame.image.load(bg_path+ os.sep+ "kuguo_night.png")    
    kuguo_dusk = pygame.image.load(bg_path+ os.sep+ "kuguo_dusk.png")
    
    
    #托洛普赫岛  秘密の楽園トロップホップ
    leyuan_day = pygame.image.load(bg_path+ os.sep+ "leyuan_day.png")
    leyuan_night = pygame.image.load(bg_path+ os.sep+ "leyuan_night.png")
    leyuan_dusk = pygame.image.load(bg_path+ os.sep+ "leyuan_dusk.png")
    
    
    # 刺客，都会 華やかなる都会
    duhui_day = pygame.image.load(bg_path+ os.sep+ "duhui_day.png")
    duhui_night = pygame.image.load(bg_path+ os.sep+ "duhui_night.png")
    duhui_dusk = pygame.image.load(bg_path+ os.sep+ "duhui_dusk.png")
    
    # 瓦兹乐修  開拓の町オアーズラッシュ
    kaituo_day  = pygame.image.load(bg_path+ os.sep+ "kaituo_day.png")
    kaituo_night  = pygame.image.load(bg_path+ os.sep+ "kaituo_night.png")
    kaituo_dusk  = pygame.image.load(bg_path+ os.sep+ "kaituo_dusk.png")

    # 瓦兹乐修 枯れた町オアーズラッシュ 商人的城镇
    xiaotiao_day = pygame.image.load(bg_path+ os.sep+ "xiaotiao_day.png")
    xiaotiao_night = pygame.image.load(bg_path+ os.sep+ "xiaotiao_night.png")
    xiaotiao_dusk = pygame.image.load(bg_path+ os.sep+ "xiaotiao_dusk.png")

    # 神官，圣火之乡 聖火の郷フレイムチャーチ
    shenghuo_day = pygame.image.load(bg_path+ os.sep+ "shenghuo_day.png")
    shenghuo_night = pygame.image.load(bg_path+ os.sep+ "shenghuo_night.png")
    shenghuo_dusk = pygame.image.load(bg_path+ os.sep+ "shenghuo_dusk.png")
    
    
    # 库罗普德尔（舞者出生地） のどかなクロップデール
    wuzhe_day = pygame.image.load(bg_path+ os.sep+ "wuzhe_day.png")
    wuzhe_night = pygame.image.load(bg_path+ os.sep+ "wuzhe_night.png")
    wuzhe_dusk = pygame.image.load(bg_path+ os.sep+ "wuzhe_dusk.png")
    
    # 柯林奎克/卡纳布莱茵  潮騒の鳴く街 黄昏-学者
    seacity_day = pygame.image.load(bg_path+ os.sep+ "seacity_day.png")
    seacity_night = pygame.image.load(bg_path+ os.sep+ "seacity_night.png")
    seacity_dusk = pygame.image.load(bg_path+ os.sep+ "seacity_dusk.png")
    
    
    # 赛伊/沙砾之村的旅馆 その集落は砂の行く先
    saiyi_day = pygame.image.load(bg_path+ os.sep+ "saiyi_day.png")
    saiyi_night = pygame.image.load(bg_path+ os.sep+ "saiyi_night.png")
    saiyi_dusk = pygame.image.load(bg_path+ os.sep+ "saiyi_dusk.png")
    
    # 洛克城 蒸気の鼓動ロック島
    luokecity_day = pygame.image.load(bg_path+ os.sep+ "luokecity_day.png")
    luokecity_night = pygame.image.load(bg_path+ os.sep+ "luokecity_night.png")
    luokecity_dusk = pygame.image.load(bg_path+ os.sep+ "luokecity_dusk.png")
    
    # 废弃之城 棄てられた都
    feiqicity_day = pygame.image.load(bg_path+ os.sep+ "feiqicity_day.png")
    feiqicity_night = pygame.image.load(bg_path+ os.sep+ "feiqicity_night.png")
    feiqicity_dusk = pygame.image.load(bg_path+ os.sep+ "feiqicity_dusk.png")
    
    
    # 戈德克普 / 温特布鲁    降る白雪の町村
    northtown_day = pygame.image.load(bg_path+ os.sep+ "northtown_day.png")
    northtown_night = pygame.image.load(bg_path+ os.sep+ "northtown_night.png")
    northtown_dusk = pygame.image.load(bg_path+ os.sep+ "northtown_dusk.png")
    
    # 库拉雷吉 / 古拉贝尔  峡谷が閉ざす村
    gobitown_day = pygame.image.load(bg_path+ os.sep+ "gobitown_day.png")
    gobitown_night = pygame.image.load(bg_path+ os.sep+ "gobitown_night.png")
    gobitown_dusk = pygame.image.load(bg_path+ os.sep+ "gobitown_dusk.png")
    
    
    # 延贝伦/威古罗布  都に吹く、緑の風
    greencity_day = pygame.image.load(bg_path+ os.sep+ "greencity_day.png")
    greencity_night = pygame.image.load(bg_path+ os.sep+ "greencity_night.png")
    greencity_dusk = pygame.image.load(bg_path+ os.sep+ "greencity_dusk.png")
    
    # 史东海尔  希望なき極寒の地
    northcity_day = pygame.image.load(bg_path+ os.sep+ "northcity_day.png")
    northcity_night = pygame.image.load(bg_path+ os.sep+ "northcity_night.png")
    northcity_dusk = pygame.image.load(bg_path+ os.sep+ "northcity_dusk.png")
    
    
    # 蒙特怀兹 智慧与艺术之都  智慧と芸術の都
    artcity_day = pygame.image.load(bg_path+ os.sep+ "artcity_day.png")
    artcity_night = pygame.image.load(bg_path+ os.sep+ "artcity_night.png")
    artcity_dusk = pygame.image.load(bg_path+ os.sep+ "artcity_dusk.png")
    
    # maintheme
    maintheme_day = pygame.image.load(bg_path+ os.sep+ "maintheme_day.png")
    maintheme_night = pygame.image.load(bg_path+ os.sep+ "maintheme_night.png")
    maintheme_dusk = pygame.image.load(bg_path+ os.sep+ "maintheme_dusk.png")

    

    #加载图片切换模块
    def backgroundchange(file,daytype):
        if random.random() > 0.05:
            if daytype == True:
                if '朱き晩陽のク国' in file:
                    background = kuguo_day
                elif 'ケモノ達の古里' in file:
                    background = shouren_day            
                elif '秘密の楽園トロップホップ' in file:
                    background = leyuan_day
                elif '華やかなる都会' in file:
                    background = duhui_day
                elif '開拓の町オアーズラッシュ' in file:
                    background = kaituo_day
                elif '枯れた町オアーズラッシュ' in file:
                    background = xiaotiao_day
                elif '聖火の郷フレイムチャーチ' in file:
                    background = shenghuo_day
                elif 'のどかなクロップデール' in file:
                    background = wuzhe_day
                elif '潮騒の鳴く街' in file:
                    background = seacity_day
                elif 'その集落は砂の行く先' in file:
                    background = saiyi_day
                elif '蒸気の鼓動ロック島' in file:
                    background = luokecity_day
                elif '棄てられた都' in file:
                    background = feiqicity_day
                elif '降る白雪の町村' in file:
                    background = northtown_day
                elif '峡谷が閉ざす村' in file:
                    background = gobitown_day
                elif '都に吹く、緑の風' in file:
                    background = greencity_day
                elif '希望なき極寒の地' in file:
                    background = northcity_day
                elif '智慧と芸術の都' in file:
                    background = artcity_day
                else:
                    background = maintheme_day
                    
            elif daytype == False:
                if  '朱き晩陽のク国' in file:
                    background = kuguo_night
                elif 'ケモノ達の古里' in file:
                    background = shouren_night
                elif '秘密の楽園トロップホップ' in file:
                    background = leyuan_night
                elif '華やかなる都会' in file:
                    background = duhui_night
                elif '開拓の町オアーズラッシュ' in file:
                    background = kaituo_night
                elif '枯れた町オアーズラッシュ' in file:
                    background = xiaotiao_night
                elif '聖火の郷フレイムチャーチ' in file:
                    background = shenghuo_night
                elif 'のどかなクロップデール' in file:
                    background = wuzhe_night
                elif '潮騒の鳴く街' in file:
                    background = seacity_night
                elif 'その集落は砂の行く先' in file:
                    background = saiyi_night
                elif '蒸気の鼓動ロック島' in file:
                    background = luokecity_night
                elif '棄てられた都' in file:
                    background = feiqicity_night
                elif '降る白雪の町村' in file:
                    background = northtown_night
                elif '峡谷が閉ざす村' in file:
                    background = gobitown_night
                elif '都に吹く、緑の風' in file:
                    background = greencity_night
                elif '希望なき極寒の地' in file:
                    background = northcity_night
                elif '智慧と芸術の都' in file:
                    background = artcity_night
                else:
                    background = maintheme_night
        else:
            if  '朱き晩陽のク国' in file:
                background = kuguo_dusk
            elif 'ケモノ達の古里' in file:
                background = shouren_dusk
            elif '秘密の楽園トロップホップ' in file:
                background = leyuan_dusk
            elif '華やかなる都会' in file:
                background = duhui_dusk
            elif '開拓の町オアーズラッシュ' in file:
                background = kaituo_dusk
            elif '枯れた町オアーズラッシュ' in file:
                background = xiaotiao_dusk
            elif '聖火の郷フレイムチャーチ' in file:
                background = shenghuo_dusk
            elif 'のどかなクロップデール' in file:
                background = wuzhe_dusk
            elif '潮騒の鳴く街' in file:
                background = seacity_dusk
            elif 'その集落は砂の行く先' in file:
                background = saiyi_dusk
            elif '蒸気の鼓動ロック島' in file:
                background = luokecity_dusk
            elif '棄てられた都' in file:
                background = feiqicity_dusk
            elif '降る白雪の町村' in file:
                background = northtown_dusk
            elif '峡谷が閉ざす村' in file:
                background = gobitown_dusk
            elif '都に吹く、緑の風' in file:
                background = greencity_dusk
            elif '希望なき極寒の地' in file:
                background = northcity_dusk
            elif '智慧と芸術の都' in file:
                background = artcity_dusk
            elif 'メインテーマ' in file:
                background = maintheme_dusk
            else:
                if daytype == False:
                    background = maintheme_night
                elif daytype == True:
                    background = maintheme_day
                    
        background = pygame.transform.smoothscale(background, (880, 495))
        background = background.convert_alpha()
        return background
    
    #加载渐入渐出模块
    def change_type(sleeptime):
        global file
        #歌曲已经播放了多少秒
        change_point = dt.now()
        new_begin_time = change_point-begin_point
        #pygame.mixer.music.stop()
        fadeout(sleeptime)
        if sound_effect_type ==1:
            sound_effect.play()
        if file not in song_dict.keys():
            file = get_key(song_dict,file)[0]
        else:
            file = song_dict[file]
        
        file_path = path + os.sep + file
        pygame.mixer.music.load(file_path)
        
        #从歌曲已经播放了秒数位置开始播放
        pygame.mixer.music.play(start=new_begin_time.seconds)
    
    def fadein(sleeptime):
        increment = 0.1
        transparency = 0 #图片透明度
        font_surface = font.render('正在播放  ' + file, True, 'white')
        
        #先设置音量为0
        pygame.mixer.music.set_volume(0) #设置音量0-1,浮点数
        volume = pygame.mixer.music.get_volume()
        
        #当音量小于1时，每隔0.1秒增加一点音量,背景图片也同步变化
        while volume + increment < 1: #理论上，从0到1中有20次间隔，每次停留0.1s，需要2s时间
            volume = pygame.mixer.music.get_volume() #获得音量0-1,浮点数
            pygame.mixer.music.set_volume(volume + increment)
            
            transparency += int(round(250*sleeptime))
            background.set_alpha(transparency)
            font_surface.set_alpha(transparency)
            
            screen.blit(background,(0,0))
            screen.blit(button1, (button1_x, button1_y))
            screen.blit(button2, (button2_x, button2_y))
            screen.blit(button3, (button3_x, button3_y))
            screen.blit(button4, (button4_x, button4_y))
            screen.blit(button5, (button5_x, button5_y))
            screen.blit(font_surface, (20, 20))
            
            pygame.display.flip()
            time.sleep(sleeptime)
    
    #加载画帧刷新模块
    def screenflip():
        screen.blit(background,(0,0))
        screen.blit(button1, (button1_x, button1_y))
        screen.blit(button2, (button2_x, button2_y))
        screen.blit(button3, (button3_x, button3_y))
        screen.blit(button4, (button4_x, button4_y))
        screen.blit(button5, (button5_x, button5_y))
        font_surface = font.render('正在播放  ' + file, True, 'white')
        screen.blit(font_surface, (20, 20))
        pygame.display.flip()
    
    #加载按钮图标
    play_button = pygame.image.load("pic\icon"+ os.sep+ "play.png")
    play_button = pygame.transform.smoothscale(play_button, (25, 25))
    
    pause_button = pygame.image.load("pic\icon"+ os.sep+ "pause.png")
    pause_button = pygame.transform.smoothscale(pause_button, (25, 25))
    
    day_button = pygame.image.load("pic\icon"+ os.sep+ "sun.png")
    day_button = pygame.transform.smoothscale(day_button, (25, 25))
    
    night_button = pygame.image.load("pic\icon"+ os.sep+ "moon.png")
    night_button = pygame.transform.smoothscale(night_button, (25, 25))
    
    next_button = pygame.image.load("pic\icon"+ os.sep+ "next.png")
    next_button = pygame.transform.smoothscale(next_button, (25, 25))

    timeropen_button = pygame.image.load("pic\icon"+ os.sep+ "timer_opened.png")
    timeropen_button = pygame.transform.smoothscale(timeropen_button,(25, 25))
    
    timerclosed_button = pygame.image.load("pic\icon"+ os.sep+ "timer_closed.png")
    timerclosed_button = pygame.transform.smoothscale(timerclosed_button, (25, 25))    
    
    setting_button = pygame.image.load("pic\icon"+ os.sep+ "setting.png")
    setting_button = pygame.transform.smoothscale(setting_button, (25, 25))
    
    #加载转变音效
    sound_effect = pygame.mixer.Sound("pic\icon"+ os.sep+ 'transform.wav')
    sound_effect.set_volume(0.2)
    
    #初始化状态
    daytype = True
    pause_flag = False
    auto_daynight_change_flag = False
    sound_effect_type = 1
    timer = 0
    timer_set_time = 300
    sleeptime = 0.05
    fadetime = 1
    prevent_clock = round(time.time())
    
    button1 = pause_button
    button2 = night_button
    button3 = next_button
    button4 = timerclosed_button
    button5 = setting_button
    
    button1_x = 20
    button1_y = 450
    button2_x = 60
    button2_y = 450
    button3_x = 100
    button3_y = 450
    button4_x = 140
    button4_y = 450
    button5_x = 180
    button5_y = 450
    
        
    #启动音乐模块
    pygame.mixer.init()
    
    #初始播放
    auto_play(daytype)
    background = backgroundchange(file,daytype)
    
    #加载初始界面
    screenflip()
    
    main_running = True
    #程序运行
    while main_running:
        
        try:
            #判断歌曲是否正在播放
            if pygame.mixer.music.get_busy():
                if auto_daynight_change_flag == True:
                    time_now = round(time.time())
                    if (time_now - timer) % timer_set_time == 0 and time_now - timer != 0 and time_now != prevent_clock:
                        if daytype == True:
                            daytype = False
                            button2 = day_button
                            background = backgroundchange(file,daytype)
                            
                            change_type(sleeptime)
                            fadein(sleeptime)
                            pygame.display.flip()
                            print('自动切换至夜晚 正在播放  ' + file)
                            
                        elif daytype == False:
                            daytype = True
                            button2 = night_button
                            background = backgroundchange(file,daytype)
                            
                            change_type(sleeptime)
                            fadein(sleeptime)
                            pygame.display.flip()
                            
                            print('自动切换至白昼 正在播放  ' + file)
                        prevent_clock = round(time.time())
                else:
                    pass
            elif pause_flag == False: # 不在播放，且没按暂停
                auto_play(daytype)
                background = backgroundchange(file,daytype)
                screenflip()
            elif pause_flag == True: #不在播放，且按下暂停
                pass
        except:
            break
        
        #获取事件
        for event in pygame.event.get():
            #退出
            if event.type == pygame.QUIT:
                main_running = False
                
            #按第一个按键，暂停或播放 
            if event.type == pygame.MOUSEBUTTONDOWN and button1_x <= event.pos[0] <= button1_x + 20 and button1_y <= event.pos[1] <= button1_y + 22:  # 判断鼠标位置以及是否点击	
                #暂停播放，按键显示播放键
                if pause_flag == True:
                    pause_flag = False
                    button1 = pause_button
                    unpause_music()
                    screenflip()
                    
                    print('正在播放  ' + file)                    
                    
                #正在播放，按键显示暂停键，按下暂停    
                elif pause_flag == False:
                    pause_flag = True
                    button1 = play_button
                    pause_music()
                    screenflip()
                    
                    print('暂停播放  ' + file)
                    
            #按第二个按键,切换昼夜
            if event.type == pygame.MOUSEBUTTONDOWN and button2_x <= event.pos[0] <= button2_x + 20 and button2_y <= event.pos[1] <= button2_y + 22:  # 判断鼠标位置以及是否点击	
                if daytype == True:
                    daytype = False
                    button2 = day_button
                    background = backgroundchange(file,daytype)
                    
                    change_type(sleeptime)
                    fadein(sleeptime)
                    pygame.display.flip()
                    
                    print('切换至夜晚 正在播放  ' + file)
                    
                elif daytype == False:
                    daytype = True
                    button2 = night_button
                    background = backgroundchange(file,daytype)
                    
                    change_type(sleeptime)
                    fadein(sleeptime)
                    pygame.display.flip()
                    
                    print('切换至白昼 正在播放  ' + file)
                  
            #按第三个按键       
            if event.type == pygame.MOUSEBUTTONDOWN and button3_x <= event.pos[0] <= button3_x + 20 and button3_y <= event.pos[1] <= button3_y + 22:  # 判断鼠标位置以及是否点击	
                if pause_flag == True: #若此时暂停状态
                    button1 = play_button
                    auto_play(daytype)
                    background = backgroundchange(file,daytype)
                    screenflip()
                    
                    print('正在播放  ' + file ) 
                    
                    
                elif pause_flag == False: #若此时正在播放
                    auto_play(daytype)
                    background = backgroundchange(file,daytype)
                    screenflip()
                    
                    print('正在播放  ' + file )
        
            #按第四个按键
            if event.type == pygame.MOUSEBUTTONDOWN and button4_x <= event.pos[0] <= button4_x + 20 and button4_y <= event.pos[1] <= button4_y + 22:  # 判断鼠标位置以及是否点击	
                if auto_daynight_change_flag == True:
                    auto_daynight_change_flag = False
                    button4 = timerclosed_button
                    screenflip()
                    
                    print('关闭自动昼夜切换模式')
                    
                elif auto_daynight_change_flag == False:
                    auto_daynight_change_flag = True
                    button4 = timeropen_button
                    timer = round(time.time())
                    screenflip()
                    
                    print('开启自动昼夜切换模式')
                    
            #按第五个按键
            if event.type == pygame.MOUSEBUTTONDOWN and button5_x <= event.pos[0] <= button5_x + 20 and button5_y <= event.pos[1] <= button5_y + 22:  # 判断鼠标位置以及是否点击	
                    print('开启设置')

                    # 设置窗口大小和标题
                    setting_screen_width, setting_screen_height = 300, 400
                    setting_screen = pygame.display.set_mode((setting_screen_width, setting_screen_height))
                    pygame.display.set_caption("设置")

                    # 设置字体
                    setting_font = pygame.font.SysFont("KaiTi", 18)

                    # 创建表单元素
                    fadetime_input_rect = pygame.Rect(20, 40, 100, 30)
                    timer_set_time_input_rect = pygame.Rect(20, 100, 100, 30)
                    sound_effect_set_rect = pygame.Rect(20, 160, 100, 30)
                    save_button_rect = pygame.Rect(130, 360, 50, 30)
                    
                    
                    fadetime_input_active = False
                    timer_set_time_input_active = False
                    soung_effect_set_input_active = False
                    fadetime = ""
                    timer_set_time_temp = ""
                    sound_effect_type_temp = ""
                    
                    # 主循环
                    running = True
                    while running:
                        # 处理事件
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:                                
                                running = False
                                
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if fadetime_input_rect.collidepoint(event.pos):
                                    fadetime_input_active = True
                                else:
                                    fadetime_input_active = False
                                    
                                    
                                if timer_set_time_input_rect.collidepoint(event.pos):
                                    timer_set_time_input_active = True
                                else:
                                    timer_set_time_input_active = False
                                    
                                if sound_effect_set_rect.collidepoint(event.pos):
                                    soung_effect_set_input_active = True
                                else:
                                    soung_effect_set_input_active = False
                                    
                                    
                                if save_button_rect.collidepoint(event.pos):
                                    
                                    if fadetime != "":
                                        try:
                                            if int(fadetime) in [1,2,3,4]: 
                                                sleeptime = int(fadetime) / 20
                                            else:
                                                pass
                                        except:
                                            pass
                                    else:
                                        pass
                                        
                                    if timer_set_time_temp != "":
                                        try:
                                            if int(timer_set_time_temp) >0: 
                                                timer_set_time = int(timer_set_time_temp)
                                            else:
                                                pass
                                        except:
                                            pass
                                    else:
                                        pass
                                        
                                    if sound_effect_type_temp != "":
                                        try:
                                            if int(sound_effect_type_temp) in [0,1]: 
                                                sound_effect_type = sound_effect_type_temp
                                            else:
                                                pass
                                        except:
                                            pass
                                    else:
                                        pass
                                        
                                    running = False
                                    
                                    
                            elif event.type == pygame.KEYDOWN:
                                if fadetime_input_active:
                                    if event.key == pygame.K_RETURN:
                                        fadetime_input_active = False
                                    elif event.key == pygame.K_BACKSPACE:
                                        fadetime = fadetime[:-1]
                                    else:
                                        fadetime += event.unicode
                                elif timer_set_time_input_active:
                                    if event.key == pygame.K_RETURN:
                                        timer_set_time_input_active = False
                                    elif event.key == pygame.K_BACKSPACE:
                                        timer_set_time_temp = timer_set_time[:-1]
                                    else:
                                        timer_set_time_temp += event.unicode
                                elif soung_effect_set_input_active:
                                    if event.key == pygame.K_RETURN:
                                        timer_set_time_input_active = False
                                    elif event.key == pygame.K_BACKSPACE:
                                        sound_effect_type_temp = sound_effect_type_temp[:-1]
                                    else:
                                        sound_effect_type_temp += event.unicode
                                
                                        

                        # 填充背景
                        setting_screen.fill((255, 255, 255))

                        # 绘制表单元素
                        fadetime_text = setting_font.render("昼夜渐变时间（秒,仅限1-4整数）:", True, (0, 0, 0))
                        setting_screen.blit(fadetime_text, (20, 20))
                        pygame.draw.rect(setting_screen, (175,171, 171), fadetime_input_rect, 0)
                        pygame.draw.rect(setting_screen, (217,217, 217), fadetime_input_rect, 2)
                        fadetime_input_text = setting_font.render(fadetime, True, (0, 0, 0))
                        setting_screen.blit(fadetime_input_text, (fadetime_input_rect.x + 5, fadetime_input_rect.y + 5))

                        timer_set_time_text = setting_font.render("昼夜自动切换间隔（秒）:", True, (0, 0, 0))
                        setting_screen.blit(timer_set_time_text, (20, 80))
                        pygame.draw.rect(setting_screen, (175,171, 171), timer_set_time_input_rect, 0)
                        pygame.draw.rect(setting_screen, (217, 217, 217), timer_set_time_input_rect, 2)
                        timer_set_time_input_text = setting_font.render(timer_set_time_temp, True, (0, 0, 0))
                        setting_screen.blit(timer_set_time_input_text, (timer_set_time_input_rect.x + 5, timer_set_time_input_rect.y + 5))
                        
                        sound_effect_set_text = setting_font.render("昼夜切换音效（1：开，0：关）:", True, (0, 0, 0))
                        setting_screen.blit(sound_effect_set_text, (20, 140))
                        pygame.draw.rect(setting_screen, (175,171, 171), sound_effect_set_rect, 0)
                        pygame.draw.rect(setting_screen, (217, 217, 217), sound_effect_set_rect, 2)
                        sound_effect_set_input_text = setting_font.render(sound_effect_type_temp, True, (0, 0, 0))
                        setting_screen.blit(sound_effect_set_input_text, (sound_effect_set_rect.x + 5, sound_effect_set_rect.y + 5))
                        
                        save_text = setting_font.render("保存", True, (0, 0, 0))
                        pygame.draw.rect(setting_screen,(175,171, 171), save_button_rect, 0)
                        pygame.draw.rect(setting_screen, (217, 217, 217), save_button_rect, 2)
                        setting_screen.blit(save_text, (136 , 365))

                        setting_text = setting_font.render('当前设置:', True, (0, 0, 0))
                        setting_text1 = setting_font.render('昼夜渐变时间: '+ str(sleeptime*20), True, (0, 0, 0))
                        setting_text2 = setting_font.render('昼夜自动切换间隔: '+ str(timer_set_time), True, (0, 0, 0))
                        setting_text3 = setting_font.render('昼夜切换音效: ' + str(sound_effect_type), True, (0, 0, 0))
                        setting_screen.blit(setting_text, (20, 200))
                        setting_screen.blit(setting_text1, (20, 220))
                        setting_screen.blit(setting_text2, (20, 240))
                        setting_screen.blit(setting_text3, (20, 260))
                        
                        setting_text4 = setting_font.render('B站 @加加大勇者 出品 ', True, (0, 0, 0))
                        setting_screen.blit(setting_text4, (100, 330))

                        # 更新屏幕
                        pygame.display.flip()
                        

                    settings = {
                        "昼夜渐变时间（秒）": fadetime,
                        "昼夜自动切换间隔（秒）": timer_set_time,
                        "昼夜切换音效（1：开，0：关）": sound_effect_type
                        
                    }
                    
                    print(settings)
                    screen = pygame.display.set_mode((880,495))
                    pygame.display.set_caption("OCTOPATH MUSIC PLAYER")
                    
                    
            #鼠标反馈
            if button1_x <= pygame.mouse.get_pos()[0] <= button1_x + 25 and button1_y <= pygame.mouse.get_pos()[1] <= button1_y + 25:
                button1.set_alpha(200)
                screenflip()
            else:
                button1.set_alpha(255)
                screenflip()
            
            if button2_x <= pygame.mouse.get_pos()[0] <= button2_x + 25 and button2_y <= pygame.mouse.get_pos()[1] <= button2_y + 25: 
                button2.set_alpha(200)
                screenflip()        
            else:
                button2.set_alpha(255)
                screenflip()          
                
            if button3_x <= pygame.mouse.get_pos()[0] <= button3_x + 25 and button3_y <= pygame.mouse.get_pos()[1] <= button3_y + 25: 
                button3.set_alpha(200)
                screenflip() 
            else:
                button3.set_alpha(255)
                screenflip()
            if button4_x <= pygame.mouse.get_pos()[0] <= button4_x + 25 and button4_y <= pygame.mouse.get_pos()[1] <= button4_y + 25: 
                button4.set_alpha(200)
                screenflip()                
            else:
                button4.set_alpha(255)
                screenflip()
            if button5_x <= pygame.mouse.get_pos()[0] <= button5_x + 25 and button5_y <= pygame.mouse.get_pos()[1] <= button5_y + 25: 
                button5.set_alpha(200)
                screenflip()                
            else:
                button5.set_alpha(255)
                screenflip()
            
    pygame.quit()
#%% 运行


main()