# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:00:16 2022

@author: hp
"""

#%% 环境设置

import difflib
import time,os,random
import pygame
from datetime import datetime as dt
import eyed3


path = r'C:\Users\pc\Music'
pg_path = r'C:\Users\pc\Desktop\Python\兴趣代码\音乐播放器'
song_list=[]



def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
def get_key (dict, value):
               return [k for k, v in dict.items() if v == value]


mf = ".ogg"
song_dict={}

#key_word = ' - Battle On '
key_word = ' -夜-'


#%% 加载歌曲

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
                    song_list.remove(night_music)
                    song_list.remove(day_music)
                else:
                    pass
        else: 
            pass
        
print(song_dict)

song_list =  list(song_dict.keys())
#song_list = list(map(lambda x: path + os.sep + x,song_list))
file = song_list[random.randint(0, len(song_list)-1)]

#%%
def play(file=file):
    global begin_point
    file_path = path + os.sep + file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    begin_point = dt.now()
    print('正在播放',file)
    
def change_type():
    global file
    #歌曲已经播放了多少秒
    change_point = dt.now()
    new_begin_time = change_point-begin_point
    pygame.mixer.music.stop()
    
    if file not in song_dict.keys():
        file = get_key(song_dict,file)[0]
    else:
        file = song_dict[file]
    
    file_path = path + os.sep + file
    pygame.mixer.music.load(file_path)
    
    #从歌曲已经播放了秒数位置开始播放
    pygame.mixer.music.play(start=new_begin_time.seconds)
    print('昼夜切换')
    
def random_song():
    global file
    file = song_list[random.randint(0, len(song_list)-1)]
    play(file)
    


# def auto_play():
#     for song in song_list:
#         mp3Info = eyed3.load(path+os.sep+song)
#         play(song)
#         time.sleep(mp3Info.info.time_secs)
        
# def auto_changed():
#     random_song()
#     for i in range(random.randint(4, 6)):
#         time.sleep(random.randint(10, 20))
#         change_type()
        
# def auto_playchange():
#         for a in range(len(song_list)):
#             random_song()
#             for i in range(random.randint(4, 6)):
#                 time.sleep(random.randint(10, 20))
#                 change_type()
                
def pause_music():
    pygame.mixer.music.pause()
    

def unpause_music():
    pygame.mixer.music.unpause()    

        
#运行界面
def main():
    # 初始化文字屏幕
    pygame.font.init()
    # 初始化图像屏幕
    pygame.init()
    # 初始化字体
    font_name = pygame.font.match_font('KaiTi')  # 2.获得字体文件
    font = pygame.font.Font(font_name, 20)
    
    screen = pygame.display.set_mode((880,495))
    pygame.display.set_caption("OCTOPATH MUSIC PLAYER")
    background1 = pygame.image.load(pg_path + os.sep +"octopath2.jpg")  
    background1 = pygame.transform.scale(background1, (880, 495)) #转化大小   
    background1 = background1.convert_alpha()
    background2 = pygame.image.load(pg_path + os.sep +"octopath.jpg")  
    background2 = pygame.transform.scale(background2, (880, 495)) #转化大小
    background2 = background2.convert_alpha()
    screen.blit(background1,(0,0))
 
    
    play_button = pygame.image.load(pg_path + os.sep +"play.png")
    play_button = pygame.transform.scale(play_button, (20, 20))
    
    pause_button = pygame.image.load(pg_path + os.sep +"pause.png")
    pause_button = pygame.transform.scale(pause_button, (20, 20))
    
    day_button = pygame.image.load(pg_path + os.sep +"sun.png")
    day_button = pygame.transform.scale(day_button, (20, 20))
    
    night_button = pygame.image.load(pg_path + os.sep +"moon.png")
    night_button = pygame.transform.scale(night_button, (20, 20))
    
    next_button = pygame.image.load(pg_path + os.sep +"next.png")
    next_button = pygame.transform.scale(next_button, (20, 20))
    
    
    
    button1 = pause_button
    button2 = night_button
    button3 = next_button
    
    
    button1_x = 20
    button1_y = 450
    button2_x = 50
    button2_y = 450
    button3_x = 80
    button3_y = 450
    
    pygame.mixer.init()
    
    play()
    
    screen.blit(button1, (button1_x, button1_y))
    screen.blit(button2, (button2_x, button2_y))
    screen.blit(button3, (button3_x, button3_y))
    
    font_surface = font.render('正在播放  ' + file, True, 'white')
    screen.blit(font_surface, (20, 20))
    pygame.display.flip()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            #按第一个按键    
            if event.type == pygame.MOUSEBUTTONDOWN and button1_x <= event.pos[0] <= button1_x + 20 and button1_y <= event.pos[1] <= button1_y + 22:  # 判断鼠标位置以及是否点击	
                if button1 == play_button:
                    button1 = pause_button
                    if button2 == day_button:
                        screen.blit(background2,(0,0))
                    else:
                        screen.blit(background1,(0,0))                    
                    screen.blit(button1, (button1_x, button1_y))
                    screen.blit(button2, (button2_x, button2_y))
                    screen.blit(button3, (button3_x, button3_y))
                    unpause_music()
                    print('正在播放  ' + file + file )                    
                    font_surface = font.render('正在播放  ' + file, True, 'white')
                    screen.blit(font_surface, (20, 20))
                    pygame.display.flip()
                    
                    
                elif button1 == pause_button:
                    button1 = play_button
                    if button2 == day_button:
                        screen.blit(background2,(0,0))
                    else:
                        screen.blit(background1,(0,0))                    
                    screen.blit(button1, (button1_x, button1_y))
                    screen.blit(button2, (button2_x, button2_y))
                    screen.blit(button3, (button3_x, button3_y))
                    pygame.display.flip()
                    pause_music()
                    print('暂停播放  ' + file)
                    font_surface = font.render('暂停播放  ' + file, True, 'white')
                    screen.blit(font_surface, (20, 20))
                    pygame.display.flip()
                    
            #按第二个按键
            if event.type == pygame.MOUSEBUTTONDOWN and button2_x <= event.pos[0] <= button2_x + 20 and button2_y <= event.pos[1] <= button2_y + 22:  # 判断鼠标位置以及是否点击	
                  if button2 == night_button:
                      button2 = day_button
                      
                      screen.blit(background2,(0,0))
                      screen.blit(button1, (button1_x, button1_y))
                      screen.blit(button2, (button2_x, button2_y))
                      screen.blit(button3, (button3_x, button3_y))
                      print('切换至夜晚 正在播放  ' + file)
                      font_surface = font.render('切换至夜晚 正在播放  ' + file, True, 'white')
                      screen.blit(font_surface, (20, 20))
                      pygame.display.flip()
                      
                  elif button2 == day_button:
                      button2 = night_button
                      screen.blit(background1,(0,0))
                      screen.blit(button1, (button1_x, button1_y))
                      screen.blit(button2, (button2_x, button2_y))
                      screen.blit(button3, (button3_x, button3_y))
                      print('切换至白昼 正在播放  ' + file)
                      font_surface = font.render('切换至白昼 正在播放  ' + file, True, 'white')
                      screen.blit(font_surface, (20, 20))
                      pygame.display.flip()
                  change_type()
                  
            #按第三个按键       
            if event.type == pygame.MOUSEBUTTONDOWN and button3_x <= event.pos[0] <= button3_x + 20 and button3_y <= event.pos[1] <= button3_y + 22:  # 判断鼠标位置以及是否点击	
                if button2 == day_button:
                    screen.blit(background2,(0,0))                
                    screen.blit(button1, (button1_x, button1_y))
                    screen.blit(button2, (button2_x, button2_y))
                    screen.blit(button3, (button3_x, button3_y))
                    random_song()
                    change_type()
                    print('正在播放  ' + file )                    
                    font_surface = font.render('正在播放  ' + file, True, 'white')
                    screen.blit(font_surface, (20, 20))
                    pygame.display.flip()
                    
                elif button2 == night_button:
                    screen.blit(background1,(0,0))                    
                    screen.blit(button1, (button1_x, button1_y))
                    screen.blit(button2, (button2_x, button2_y))
                    screen.blit(button3, (button3_x, button3_y))
                    random_song()
                    print('正在播放  ' + file )                    
                    font_surface = font.render('正在播放  ' + file, True, 'white')
                    screen.blit(font_surface, (20, 20))
                    pygame.display.flip()
            
            

    pygame.display.update()


#%% 运行


main()
 