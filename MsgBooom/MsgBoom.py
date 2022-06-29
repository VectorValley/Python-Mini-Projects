from os import times
from tabnanny import check
from tkinter import W
import pyautogui
import time
import random




#Timer - to inform user.
def countdown(time_sec):  
    while time_sec > 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"  =>=>=>  {timeformat}", end='\r')
        time.sleep(1)
        time_sec -= 1
        
        
#loop For start sending massages.
def send_msg(num_of_msg, list):
    num_of_msg = int(num_of_msg)
    while 0 < num_of_msg:
        msg = random.choice(list)
        pyautogui.typewrite(msg)
        time.sleep(.2)
        pyautogui.press('enter')
        print(msg, end='\r')
        time.sleep(.5)
           
        num_of_msg -= 1
        

#Checking that, the input is int or not
def check_int(user_input):
    try:
        int(user_input)
        it_is = True
    except ValueError:
        it_is = False
    return it_is


# _list_romantic = [
#     "I miss you", "I love you",
#     "I adore you", "I'm thinking about you",
#     "You take my breath away", "You are my everything",
#     "You are my soulmate","You complete me",
#     "I can't wait to hold you","We're perfect for each other",
#     "We will get through this","The long the wait, the sweeter the kiss",
#     "I feel so lucky to be with you","I believe in this love",
#     "We are a perfect match","You're my other half",
#     "You make me a better person","I'm proud to be yours",
#     "I found love when I found you","ogether, forever and ever",
#     "You bring me so much joy","I think about you 24/7",
#     "I can't wait to be with you again","You are my sunshine",
#     "When I have you, I have everything I need","You are the one for me",
#     "You make my heart melt","If I could hold you close again, I'd never let you go",
#     "You have my heart, keep it safe","Be mine",
#     "You are my rock, I love you so much","Be true to me & I'll do the same",
#     "You mean the world to me","You are my best friend",
# ]

comments = [
    "wow", "wonderfull", "ki valo dekhte", "cander tukra", "Ore pagol hoye jabo ami pagol hoye jabo",
    "osadharon", "darun valo", "pore na cokher polok ki tomar ruper jholok", "social media er sera photo", "emon pose jati aro dekhte cay",
    "wah wah wah", "corom", "oh ki dekhale guru", "leg dust dao guru", "apni thakchen sir",
    "bekayda", "kono kotha hobe na", "Ami sihorit", "tumi guru valo", "tomartlona nei",
    "Otuoniyo", "Ovabonio", "Besomvob valo", "Ami vasa hin", "amon drrishyo jati aro dekhte cay",
    "Ooo ki lagce", "ata sudhu photo noy internet basir onuprerona", "ki valo lagche....","Ami nirbak", "caridik sudhu wow"
]
if __name__ == '__main__':
    
    try_again = 1
    while try_again == 1:
        num_msg = input("Enter the number of Massages => ")
        check = check_int(num_msg)
        
        if check == True:
            print("\nMassages sending will start within 10 Sec.")
            time.sleep(1)
            print("Be sure that, the Cursor is in right msg box...\n")
            time.sleep(1)
            countdown(10)
            send_msg(num_msg, comments)
            try_again = 0
        else:
            print("Wrong Input. Your input must be a number.")
            time.sleep(2)
            try_again = 1
        
        
        
        
        
     
   

