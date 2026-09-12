'''
WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Be careful,this is a trojan that created for educational purposes only.
I am not responsible for any damage caused by this code. Use it at your own risk.
Creating malware is illegal and can have serious consequences.
This code is provided for educational purposes only and should not be used for any malicious or harmful activities.
Please use it responsibly and within the bounds of the law.
This code is intended to demonstrate the potential dangers of malware and the importance of cybersecurity.
It is not intended to be used for any illegal or unethical purposes.
It is a recreation of a duplication virus called "You are an idiot" that was created in 2001.
The original virus was designed to create multiple copies of itself and display a message on the screen, causing annoyance and disruption to the user.
This code is a harmless recreation of that virus and does not contain any malicious functionality.
Use it carefully if you cant stop the virus then click the Stop button on the phyton editor that you are using or close the phyton file.


HOW TO STOP / TERMINATE!!!

THERE ARE SEVERAL WAYS TO STOP THE CODE:

CHOOSING THE OPTION "CANCEL" AT THE WARNING
PRESSING B ON YOUR KEYBOARD WHILE CODE IS RUNNING WILL TERMİNATE THE CODE INSTANTLY AND IT IS FOR EMERGENCY SITUATIONS
USING THE STOP BUTTON IN YOUR PYTHON EDITING APP
OR CLOSING IT FROM TASK MANAGER

WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'''
import time
import os
import tkinter as tk
from tkinter import messagebox
import random
import pygame
import sys

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)




'''Warning message Safety First :)'''
def warning_msg():
    print("Trojan has been started so don't panic and if you think its enough execute the code with pressing B/b on your keyboard.")
    permission = messagebox.askokcancel(
        "Do you want to start simulation?", 
        "Press OK to start simulation. And press B on your keyboard or press stop on your phyton editor to stop simulation ")
    if not permission:
        sys.exit()

warning_msg()

root = tk.Tk()
root.title("You are an Idiot")
root.geometry("725x565")
root.resizable(False, False)
root.attributes("-topmost", True)

icon_path = get_resource_path("Icon.png")

if os.path.exists(icon_path):
    logo = tk.PhotoImage(file=icon_path)
    root.icon = logo 
    root.update_idletasks()
    root.iconphoto(True, logo)

screen_count=0
      

'''
Icon or other Png files should be in the same directory as this script.
If you want to change the icon, just replace the Icon.png file with your own image and make sure it is named Icon.png .
Or do the samething like mp3 or png files.
'''

'''Sound Files'''
pygame.mixer.init()
audio_path = get_resource_path("sound.mp3")
sound_effect = None

if os.path.exists(audio_path):
    pygame.mixer.set_num_channels(100)
    sound_effect = pygame.mixer.Sound(audio_path)




image_w_way = get_resource_path("whitescreen.png")
img_w = tk.PhotoImage(file=image_w_way)


label_w = tk.Label(root, image=img_w)
label_w.pack(pady=10)
label_w.image = img_w 

image_b_way = get_resource_path("blackscreen.png")
img_b = tk.PhotoImage(file=image_b_way)

label_b = tk.Label(root, image=img_b)
label_b.image = img_b
label_b.pack_forget()


current_state = True

def play_extra_sound():
    """Every time it is called it plays an extra sound."""
    if sound_effect:
        sound_effect.play(loops=-1)


def start_flashing(label, state=True):
    if label.winfo_exists(): 
        next_img = img_b if state else img_w
        label.config(image=next_img)
        label.image = next_img  


        label.after(500, lambda: start_flashing(label, not state))

'''
def nothing():
    pass
    not in use
'''
def movement(window,x,y,dx,dy):
    if window.winfo_exists():
        win_width = 725
        win_height = 565
    screen_width = window.winfo_screenwidth()     
    screen_height = window.winfo_screenheight()
    
    x +=dx
    y +=dy
    
    if x <= 0:
        x = 0
        dx = abs(dx) 
    elif x + win_width >= screen_width:
        x = screen_width - win_width
        dx = -abs(dx)  
    if y <= 0:
        y = 0
        dy = abs(dy) 
    elif y + win_height >= screen_height:
        y = screen_height - win_height
        dy = -abs(dy)
            
    window.geometry(f"{win_width}x{win_height}+{x}+{y}")
    '''Waiting 10ms '''
    window.after(10, lambda: movement(window, x, y, dx, dy))



def message():
    popup=messagebox.askyesno("You are an Idiot","Are you an Idiot?")
    if popup:
        new_screen_duplication()
    else:
        new_screen_duplication()
    root.after(10000, message)
    
def new_screen_duplication(event=None):
    global screen_count
    screen_count += 1
    
    play_extra_sound()
    
    win_width = 600
    win_height = 500
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    x = random.randint(0,max(0, screen_width - win_width))
    y = random.randint(0,max(0,screen_height - win_height))
    
    new_screen=tk.Toplevel(root)
    new_screen.title("You are an Idiot")
    new_screen.geometry(f"{win_width}x{win_height}+{x}+{y}")
    new_screen.protocol("WM_DELETE_WINDOW", new_screen_duplication)
    new_screen.attributes("-topmost", True)
    new_screen.resizable(False,False)
    
    new_label = tk.Label(new_screen, image=img_w)
    new_label.pack(pady=10)
    start_flashing(new_label,True)
    
    dx = random.choice([-10, -8, 8, 10])
    dy = random.choice([-10, -8, 8, 10])
    '''Gives movement to the other popups'''
    movement(new_screen, x, y, dx, dy)
    
    new_screen.bind("<Alt-F4>", new_screen_duplication)
    new_screen.bind("<B>", destroying)
    new_screen.bind("<b>", destroying)
    new_screen.protocol("WM_DELETE_WINDOW", new_screen_duplication)
    
def auto_duplicate_loop():
    new_screen_duplication()
    root.after(4000, auto_duplicate_loop)


def destroying(event=None):
    try:
        root.destroy()
        pygame.mixer.quit()
    except Exception:
        pass
    time.sleep(1)
    print("This is a harmless tkinter warning dont mind it :) ")
    
'''Protocols aimed at preventing the halting of the Trojan but some of them are helping to terminate the code :=() '''

root.protocol("WM_DELETE_WINDOW", new_screen_duplication)
root.bind("<Alt-F4>", new_screen_duplication)
root.bind("<B>", destroying)
root.bind("<b>", destroying)

'''Placing the first screen randomly and give it a movement'''
start_x = random.randint(0, max(0, root.winfo_screenwidth() - 725))
start_y = random.randint(0, max(0, root.winfo_screenheight() - 565))
init_dx = random.choice([-10, -8, 8, 10])
init_dy = random.choice([-10, -8, 8, 10])

movement(root, start_x, start_y, init_dx, init_dy)

start_flashing(label_w, True)
root.after(100, play_extra_sound)

root.after(5000, message)

root.after(4000,auto_duplicate_loop )

root.mainloop()

time.sleep(2)

'''
FUNCTIONS LIST

get_resource_path() = For making resource files (PNG, MP3) readable for PyInstaller, helping us convert the Python file into a working .exe file.
warning_msg() = For warning the user and getting permission before running.
os.path.exists() = For checking the resource file paths.
play_extra_sound() = Every time it is called, it plays an extra sound.
start_flashing() = For flashing between white and black. It is added because it is a feature of the original trojan.
movement() = Makes screens bounce off the screen boundaries and makes them harder to catch.
message() = It is a feature of the original trojan too, making it 1000x more annoying.
screen_duplication() = It is the most annoying part; it duplicates the screen when you try to close it.
destroying()=Terminating the code "Safety First".
nothing()=absloutly nothingggggg


'''
'''Written By Stick Man'''