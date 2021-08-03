from _typeshed import Self
from pygame.locals import *
import pygame
import sys

class View:
    def __init__(self,screen):
        self.screen = screen
    
    def draw(self):
        return

class Controller:
    def __init__(self):
        None

class Main:
    def __init__(self):
        self.WIN_WEIGHT = 500
        self.WIN_HEIGHT = 250



def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((500, 250))    # 画面を作成.return Surface
    pygame.display.set_caption("Timetimer")    # タイトルを作成
    
    time_bar_weight = 300
    passed_min = 0 #１分を何回繰り返したか記録
    min_1_button = pygame.Rect(30, 180, 50, 50)  # creates a rect object Return Rect
    min_5_button = pygame.Rect(170,180,50,50)
    min_60_button = pygame.Rect(100, 180, 50, 50)  # creates a rect object
    start_button = pygame.Rect(350,180,50,50)#スタートボタン
    reset_button = pygame.Rect(420,180,50,50)#リセットボタン
    
    time_bar_back = pygame.Rect(100,100,time_bar_weight,30)#時間を示すバーの後ろ
    #STEP1.フォントの用意  
    font = pygame.font.SysFont(None, 25)#文字の描画時にfontモジュールを使うらしい。#Fontオブジェクトを返す。
    
    #STEP2.テキストの設定
    '''
    Pygameでは作成済みのSurfaceに直接文字を描写することができません。
    ：描写するためにはFont.render命令を使用して文字の画像 (Surface)をその都度作成し、
    作成済みSurfaceにコピー描写しなければならないのです。
    '''
    working_time = 0
    one_min_fps = 0 #なんfps経過したかを記録
    decrease_num = 0 #１分経過ごとのいくつバーの長さを変更するか

    text1 = font.render("1min", True, (0,0,0))#surfaceに文字を描画、return Surface
    text5 = font.render("5min",True,(0,0,0))
    text60 = font.render("60min", True, (0,0,0))
    text_start = font.render("start", True, (0,0,0))
    text_reset = font.render("reset", True, (0,0,0))
    text_working_time = font.render(str(working_time),True,(255,255,255))
    
    
    running = True
    timer_runnning = False #タイマーが作動しているかどうか
    #メインループ
    while running:
        screen.fill((0,0,0))  #画面を黒で塗りつぶす
        time_bar = pygame.Rect(100,100,time_bar_weight,30)#時間を示すバー
        pygame.draw.rect(screen, (255, 0, 0), min_1_button) #四角形を描画するreturn Rect
        pygame.draw.rect(screen, (0, 255, 0), min_60_button)
        pygame.draw.rect(screen,(0,0,255),min_5_button)
        pygame.draw.rect(screen,(112,112,112),reset_button)
        pygame.draw.rect(screen,(112,112,112),start_button)
        pygame.draw.rect(screen,(255,112,112),time_bar_back)
        pygame.draw.rect(screen,(0,128,0),time_bar)
        screen.blit(text1, (40, 190))#画像を他の画像の上に描画する
        screen.blit(text60, (100,190))
        screen.blit(text5,(170,190))
        screen.blit(text_start,(350,190))
        screen.blit(text_reset,(420,190))
        text_working_time = font.render(str(working_time)+"min",True,(255,255,255)) #値を更新するため
        screen.blit(text_working_time,(420,230))

        clock = pygame.time.Clock()
        pygame.display.update() #描画処理を実行.スクリーンの一部を更新、引数変えれば全体display.flipと一緒らしい.
        for event in pygame.event.get(): #イベントキューからイベントを取り出す
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  #pygameのウィンドウを閉じる
                sys.exit() #システム終了
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if min_1_button.collidepoint(event.pos) and timer_runnning==False: #点座標がrectオブジェクトの範囲内か？
                    print("red button was pressed")
                    pygame.draw.rect(screen, (100, 0, 0), min_1_button) #色を変える
                    pygame.display.update(min_1_button)
                    working_time += 1
                    pygame.time.wait(30) #一瞬止める
                if min_60_button.collidepoint(event.pos) and timer_runnning==False:
                    print("green button was pressed")
                    pygame.draw.rect(screen, (0, 100, 0), min_60_button) #色を変える
                    pygame.display.update(min_60_button)
                    pygame.time.wait(30) #一瞬止める
                    working_time += 60
                if min_5_button.collidepoint(event.pos) and timer_runnning==False:
                    print("blue button was pressed")
                    pygame.draw.rect(screen, (0, 0, 100), min_5_button) #色を変える
                    pygame.display.update(min_5_button)
                    pygame.time.wait(30) #一瞬止める
                    working_time += 5
                if start_button.collidepoint(event.pos) and timer_runnning==False and working_time!=0:
                    print("start button was pressed")
                    pygame.draw.rect(screen, (20, 20, 20), start_button) #色を変える
                    pygame.display.update(start_button)
                    timer_runnning = True
                    decrease_num = 1 / working_time
                    pygame.time.wait(30) #一瞬止める
                if reset_button.collidepoint(event.pos):
                    print("reset button was pressed")
                    pygame.draw.rect(screen, (20, 20, 20), reset_button) #色を変える
                    pygame.display.update(reset_button)
                    timer_runnning = False
                    passed_min = 0
                    one_min_fps = 0
                    working_time = 0
                    time_bar_weight = 300
                    pygame.time.wait(30) #一瞬止める
        if timer_runnning:
            one_min_fps += 1
            if one_min_fps >= 2:
                one_min_fps = 0
                time_bar_weight -= decrease_num
            
        if time_bar_weight-decrease_num*passed_min <= 0:
            timer_runnning = False
            passed_min = 0
            one_min_fps = 0
            working_time = 0
            time_bar_weight = 300

        clock.tick(10)
                    
if __name__=="__main__":
    main()