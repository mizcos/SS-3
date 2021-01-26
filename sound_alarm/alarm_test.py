# python -m pip install pygame
import pygame.mixer
import time
import os
# mixerモジュールの初期化
pygame.mixer.init()
pathTothis = os.path.dirname(os.path.abspath("__file__"))
# 音楽ファイルの読み込み
#pygame.mixer.music.load("Alarm_bugyo.mp3")
# 音量の反映(0.0~1.0)
#alVol = 0.5
#pygame.mixer.music.set_volume(alVol)
# 音楽再生、および再生回数の設定(-1はループ再生)
#pygame.mixer.music.play(0)

# alram_end = time.time()+60
# while time.time()<alram_end:
#     a = 1
#     # タッチパネル入力待機->break(インデントの都合で差し当たり適当なコードを置いています)
#     if 1<0:
#         # ----- タップ時の操作音
#         pygame.mixer.init()
#         pygame.mixer.music.load("hyoushigi2.mp3")
#         opVol = 0.5
#         pygame.mixer.music.set_volume(opVol)
#         pygame.mixer.music.play(0)
#         time.sleep(1)
#         # -----
#         break

# 再生の終了
#pygame.mixer.music.stop()

def playTapSound(vol):
    #pygame.mixer.init()
    #pygame.mixer.music.load("sound_alarm/hyoushigi2.mp3")
    opVol = vol/100
    #pygame.mixer.music.set_volume(opVol)
    #pygame.mixer.music.play(0)


def playAlarm(vol):
    #pygame.mixer.init()
    #pygame.mixer.music.set_volume(vol)
    #pygame.mixer.music.load("sound_alarm/Alarm_bugyo.mp3")
    alVol = vol/100
    #pygame.mixer.music.set_volume(alVol)
    #pygame.mixer.music.play(-1)

    
def stopAlarm():
    a = 0
    #pygame.mixer.music.stop()


