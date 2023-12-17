import gameFly
import tkinter
import puzzle
import mainWinOnly
import pong
import main
import customtkinter as tk
from PIL import Image
import mysql.connector
import random
from time import time
from pygame import mixer
tk.set_appearance_mode("dark")
win=tk.CTk()
win.configure(bg="#0e142a")
win.geometry("850x600")
firstTime=0
def story():
    mixer.music.fadeout(3)
    start_time=time() 
    vict=mainWinOnly.runner()
    if vict:
        vict2=puzzle.runner(True)
        if vict2:
            vict3=gameFly.runner(70,True)
            if vict3:
                pong.runner(True)
                end_time=time()
                score=end_time-start_time
                sqlc = mysql.connector.connect(host='localhost',user='root',passwd='password',database="icarus")
                cur=sqlc.cursor()
                cur.execute(f"select highscore from data where username = '{username1}'")
                k=cur.fetchall()
                new_value = f'{score}'
                if k[0][0]=='None' or new_value<k[0][0]:
                    query = f"UPDATE data SET highscore = {str(new_value)} where username = '{username1}'"
                    cur.execute(query)
                    sqlc.commit()

    quit()
def running():
    mixer.music.fadeout(3)
    gameFly.runner(70,False)
    quit()
def platforming():
    mixer.music.fadeout(3)
    main.runner()
    quit()
def ponging():
    mixer.music.fadeout(3)
    pong.runner(False)
    quit()
def typing():
    mixer.music.fadeout(3)
    puzzle.runner(False)
    quit()
def first():
    login.pack_forget()
    signin.pack_forget()
    p1.pack()
    p2.pack_forget()
    begin.pack_forget()
def second():
    p2.pack()
    p1.pack_forget()
    begin.pack_forget()
def starting():
    begin.pack()
    user.pack_forget()
    p2.pack_forget()
    p1.pack_forget()
def loginShow():
    signin.pack_forget()
    begin.pack_forget()
    user.pack_forget()
    login.pack()
def signinShow():
    begin.pack_forget()
    user.pack_forget()
    signin.pack()
def userShow():
    begin.pack_forget()
    login.pack_forget()
    signin.pack_forget()
    user.pack()
def leaderboardShow():
    sqlc = mysql.connector.connect(host='localhost',user='root',passwd='password',database="icarus")
    cur=sqlc.cursor()
    cur.execute("select username,highscore from data")
    li=cur.fetchall()
    li.sort(key=lambda x:(x[1]))
    cur.execute(f"select highscore from data where username = '{username1}'")
    y=cur.fetchall()
    x=y[0][0]
    title=tk.CTkLabel(leaderboardbox,text=f"LEADERBOARD",font=("courier",40))
    number0=tk.CTkLabel(leaderboardbox,text=f"{li[0][0]} is first with time of {round(float((li[0][1])))  if li[0][1][0].isdigit() else li[0][1]} seconds",font=("courier",23))
    number1=tk.CTkLabel(leaderboardbox,text=f"{li[1][0]} is second with time of {round(float((li[1][1]))) if li[1][1][0].isdigit() else li[1][1]} seconds",font=("courier",23))
    number2=tk.CTkLabel(leaderboardbox,text=f"{li[2][0]} is third with time of {round(float((li[2][1])))  if li[2][1][0].isdigit() else li[2][1]} seconds",font=("courier",23))
    yours=tk.CTkLabel(leaderboardbox,text=f"Your fastest time is {x} seconds",font=("courier",23))
    start2=tk.CTkButton(leaderboardbox,text="START GAME",command=story, bg_color="transparent", fg_color="white",hover_color="#aab6d7",text_color="#0e142a",font=("courier",20))
    p1.pack_forget()
    p2.pack_forget()
    leaderboard.pack()
    leaderboardbox.pack(padx=(150,150))
    title.grid(row=0,column=0,pady=(100,50))
    number0.grid(row=1,column=0,sticky="w",pady=5)
    number1.grid(row=2,column=0,sticky="w",pady=5)
    number2.grid(row=3,column=0,sticky="w",pady=5)  
    yours.grid(row=4,column=0,sticky="w",pady=50)
    start2.grid(row=5,column=0,pady=(10,150))
leaderboard=tk.CTkFrame(win,fg_color="#0e142a",bg_color='#0e142a')
leaderboardbox=tk.CTkFrame(leaderboard,fg_color="#0e142a",bg_color='#0e142a')
mixer.init()
mixer.music.load('sounds/title screen.mp3')
mixer.music.play(-1)
p1=tk.CTkFrame(win,fg_color="#0e142a",bg_color="#0e142a")
p2=tk.CTkFrame(win,fg_color="#0e142a",bg_color='#0e142a')
begin=tk.CTkFrame(win,fg_color="transparent",bg_color="transparent")
login=tk.CTkFrame(win,fg_color="#0e142a",bg_color="#0e142a")
signin=tk.CTkFrame(win,fg_color="#0e142a",bg_color="#0e142a")
user=tk.CTkFrame(win,fg_color="#0e142a",bg_color="#0e142a")
box1=tk.CTkFrame(user,fg_color="transparent")
box2=tk.CTkFrame(login,fg_color="transparent",width=500)
box3=tk.CTkFrame(signin,fg_color="transparent",width=500)
box4=tk.CTkFrame(p1,fg_color="#0e142a")
topleft=tk.CTkFrame(p2,fg_color="#0e142a")
topright=tk.CTkFrame(p2,fg_color="#0e142a")
bottomleft=tk.CTkFrame(p2,fg_color="#0e142a")
bottomright=tk.CTkFrame(p2,fg_color="#0e142a")
beginside1=tk.CTkFrame(begin,fg_color="transparent",bg_color="transparent")
beginside2=tk.CTkFrame(begin,fg_color="transparent",bg_color="transparent")
left=tk.CTkFrame(p1,fg_color="transparent")
right=tk.CTkFrame(p1,fg_color="transparent")
img=Image.open("./assets/icarus.png")
bg_img=Image.open("./assets/beginning.png")
story_img=Image.open("./images/story.png")
mini_img=Image.open("./images/minigame.png")
start_img=Image.open("./assets/start.png")
fly_img=Image.open("./images/fly.png")
pong_img=Image.open("./images/pong.png")
plat_img=Image.open("./images/platform.png")
puzzle_img=Image.open("./images/puzzle.png")
back1=tk.CTkButton(login, text="<",command=userShow, bg_color="transparent", fg_color="transparent",font=("courier",25),width=20,hover=False)
back2=tk.CTkButton(signin, text="<",command=userShow, bg_color="transparent", fg_color="transparent",font=("courier",25),width=20,hover=False)
#img=img.resize((50,50))
img=tk.CTkImage(light_image=img, dark_image=img, size=(50,50))
mini_img=tk.CTkImage(light_image=mini_img, dark_image=mini_img, size=(100,100))
story_img=tk.CTkImage(light_image=story_img, dark_image=story_img, size=(100,100))
start=tk.CTkImage(light_image=start_img, dark_image=start_img)
background=tk.CTkImage(light_image=bg_img, dark_image=bg_img, size=(850,600))
fly_img=tk.CTkImage(light_image=fly_img, dark_image=fly_img, size=(200,200))
puzzle_img=tk.CTkImage(light_image=puzzle_img, dark_image=puzzle_img, size=(200,200))
plat_img=tk.CTkImage(light_image=plat_img, dark_image=plat_img, size=(200,200))
pong_img=tk.CTkImage(light_image=pong_img, dark_image=pong_img, size=(200,200))
topleft.grid(column=0,row=0,pady=(40,50),padx=(175,30))
topright.grid(column=1,row=0,pady=(40,50),padx=(30,175))
bottomleft.grid(column=0,row=1,pady=(0,50),padx=(175,30))
bottomright.grid(column=1,row=1,pady=(0,50),padx=(30,175))
Name1=tk.CTkLabel(topleft,text="Runner Game:",font=("courier",23))
b1=tk.CTkButton(topleft, text="",command=running, image=fly_img, bg_color="transparent", fg_color="transparent",hover_color="#5c678b")
Name1.pack(anchor="center")
b1.pack(anchor="center")
Name2=tk.CTkLabel(topright,text="Pong Game:",font=("courier",23))
b2=tk.CTkButton(topright, text="",command=ponging, image=pong_img, bg_color="transparent", fg_color="transparent",hover_color="#5c678b")
Name2.pack(anchor="center")
b2.pack(anchor="center")
Name3=tk.CTkLabel(bottomleft,text="Platformer Game:",font=("courier",23))
b3=tk.CTkButton(bottomleft, text="",command=platforming, image=plat_img, bg_color="transparent", fg_color="transparent",hover_color="#5c678b")
Name3.pack(anchor="center")
b3.pack(anchor="center")
Name4=tk.CTkLabel(bottomright,text="Typing Game:",font=("courier",23))
b4=tk.CTkButton(bottomright, text="",command=typing, image=puzzle_img, bg_color="transparent", fg_color="transparent",hover_color="#5c678b")
Name4.pack(anchor="center")
b4.pack(anchor="center")
miniLabel=tk.CTkLabel(right,text="Mini Game Mode",font=("courier",23))
miniLabel.pack(pady=(0,20))
bHome1=tk.CTkButton(right, text="",command=second, image=mini_img, bg_color="transparent", fg_color="#0e142a",hover_color="#5c678b")
bHome1.pack()
storyLabel=tk.CTkLabel(left,text="Story Mode",font=("courier",23))
storyLabel.pack(pady=(0,20))
bHome2=tk.CTkButton(left, text="",command=leaderboardShow, image=story_img, bg_color="transparent", fg_color="transparent",hover_color="#5c678b",corner_radius=100)
bHome2.pack()
start=tk.CTkButton(beginside2,text="START",command=userShow, bg_color="transparent", fg_color="white",hover_color="#aab6d7",text_color="#0e142a",font=("courier",20))
loginB=tk.CTkButton(box1,text="LOGIN",command=loginShow, bg_color="#0e142a", fg_color="white",hover_color="#aab6d7",text_color="#0e142a",font=("courier",20))
signinB=tk.CTkButton(box1,text="SIGN UP",command=signinShow, bg_color="#0e142a", fg_color="white",hover_color="#aab6d7",text_color="#0e142a",font=("courier",20))
loginB.grid(row=0,column=0, padx=30,pady=300)
signinB.grid(row=0,column=1, padx=30,pady=300)
bg=tk.CTkLabel(beginside1,text="",image=background)
bg.pack()
start.pack()
back1.place(x=20,y=20)
back2.place(x=20,y=20)
box1.pack(padx=230)
#box4.pack()
left.grid(column=0,row=0,padx=(200,85),pady=(225,300))
right.grid(column=1,row=0,padx=(85,200),pady=(225,300))
beginside1.grid(row=0,column=0)
beginside2.grid(row=0,column=0,sticky="s",pady=100)
loginLabel=tk.CTkLabel(login,text="LOGIN",font=("courier",30))
loginLabel.pack(pady=(100,0))
signinLabel=tk.CTkLabel(signin,text="SIGN UP",font=("courier",30))
signinLabel.pack(pady=(100,0))
name1=tk.CTkLabel(box2,text="Username:",text_color="white",font=("courier",15))
pass1=tk.CTkLabel(box2,text="Password:",text_color="white",font=("courier",15))
#entries
username2=tk.CTkEntry(box2,fg_color="white",text_color="#0e142a",width=140)
password2=tk.CTkEntry(box2,fg_color="white",text_color="#0e142a",width=140)
def login1():
    sqlc = mysql.connector.connect(host='localhost',user='root',passwd='password',database="icarus")
    cur=sqlc.cursor()
    cur.execute("select username,password from data;")
    x=cur.fetchall()
    print(x)
    global username1
    global password1
    username1 = username2.get() 
    password1 = password2.get()
    print(username1,password1)
    data=(username1,password1)
    if data in x:
        print("login successful")
        
        #for the game played 
        list_games=['pong game','runner game','platformer game','typing game']

        game=random.choice(list_games)

        query = f"UPDATE data SET game = '{game}' where username = '{username1}'"
        cur.execute(query)

        sqlc.commit()
        cur.execute('select * from data')
        k=cur.fetchall()
        first()
    else:
        print("login unsuccesful")
loginBu=tk.CTkButton(box2,text="SUBMIT" , bg_color="#0e142a", fg_color="white",text_color="#0e142a",font=("courier",20), command=login1,hover_color="#aab6d7")
name2=tk.CTkLabel(box3,text="Username:",text_color="white",font=("courier",15))
pass2=tk.CTkLabel(box3,text="Password:",text_color="white",font=("courier",15))
global nameE2
global passE2
nameE1=tk.CTkEntry(box3,fg_color="white",text_color="#0e142a")
passE1=tk.CTkEntry(box3,fg_color="white",text_color="#0e142a")

def signup():
    sqlc = mysql.connector.connect(host='localhost',user='root',passwd='password',database="icarus")
    cur=sqlc.cursor()
    global nameE2
    global passE2
    nameE2 = nameE1.get()
    passE2 = passE1.get()
    cur.execute("select username from data;")
    x=cur.fetchall()
    if (nameE2,) not in x:
        sql = "INSERT INTO data (username, password , highscore) VALUES(%s, %s ,%s)"
        val =(f'{nameE2}', f'{passE2}',f'{"None"}')
        cur.execute(sql,val)
        sqlc.commit()
        loginShow()
    else:
        print("user exists please login ")
        loginShow()

signinBu=tk.CTkButton(box3,text="SUBMIT" , bg_color="#0e142a", fg_color="white",text_color="#0e142a",font=("courier",20), command=signup,hover_color="#aab6d7")
box3.pack(padx=375,pady=(100,0))
box2.pack(padx=375,pady=(100,0))
name1.pack()
username2.pack()
pass1.pack()
password2.pack()
loginBu.pack(pady=(30,200))
name2.pack()
nameE1.pack()
pass2.pack()
passE1.pack()
signinBu.pack(pady=(30,200))
starting()
win.mainloop()
