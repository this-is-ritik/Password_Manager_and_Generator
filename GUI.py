COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',\
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',\
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',\
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',\
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',\
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',\
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',\
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',\
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',\
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green','spring green',\
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',\
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',\
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',\
    'indian red', 'saddle brown', 'sandy brown',\
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',\
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',\
    'pale violet red', 'maroon', 'medium violet red', 'violet red',\
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',\
    'thistle', 'snow2', 'snow3',\
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',\
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',\
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',\
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',\
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',\
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',\
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',\
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',\
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',\
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',\
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',\
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',\
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',\
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',\
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',\
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',\
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',\
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',\
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',\
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',\
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',\
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',\
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',\
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',\
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',\
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',\
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',\
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',\
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',\
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',\
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',\
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',\
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',\
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',\
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',\
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',\
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',\
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',\
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',\
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',\
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',\
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',\
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',\
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',\
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',\
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',\
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',\
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',\
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',\
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',\
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',\
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',\
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',\
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',\
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83'\
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',\
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

import mysql.connector as sql
import random
import pyperclip
from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox as msgbox
from tkinter.ttk import *
import re

conn = sql.connect(user="user", host="localhost", password="", db="passwords")
cursor = conn.cursor()

def Password():
    entry.delete(0,'end')
    length=var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if(var.get()==1):
        for i in range(length):
            password+=random.choice(lower)
        return password
    elif(var.get()==2):
        for i in range(length):
            password+=random.choice(upper)
        return password
    elif(var.get()==3):
        for i in range(length):
            password+=random.choice(digits)
        return password
    else:
        return None

def Generate():
    password=Password()
    if(password is not None):
        entry.insert(END,password)
    else:
        msgbox.showinfo("Strength?","Select Strength first")

def Copy():
    password=entry.get()
    if(len(password)!=0):
        pyperclip.copy(password)
        msgbox._show(title="Copied",message="Password Copied to clipboard")
    else:
        msgbox.showwarning(title="Empty",message="First Generate a password")

def isEmail(Email):
    expr = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$")
    mat = re.search(expr,Email)
    if (mat):
        return True
    return False

def Store():
    if(len(entry.get())==0):
        msgbox.showwarning(title="Warning",message="Password is not generated!!")
    else:
        Email=email.get()
        if(not isEmail(Email)):
            msgbox.showwarning(title="Email?", message="Enter correct Email!!!")
            return None

        cursor.execute(f"insert into passwd values('{str(username.get())}','{str(entry.get())}','{str(email.get())}');")
        msgbox._show(title="Success",message="Password Stored successfully")


def show():
    usernames.delete("1.0", "end")
    passwords.delete("1.0", "end")
    emails.delete("1.0", "end")
    x=simpledialog.askstring(title="Password",prompt="Enter password : ")
    if(x=="StrongPass123#"):
        cursor.execute("select * from passwd;")

        usernames.insert(END,"\tUsername\n\n")
        passwords.insert(END, "\tPassword\n\n")
        emails.insert(END, "\tEmail\n\n")

        serial_no=1
        for i in cursor.fetchall():
            usernames.insert(END,str(serial_no)+". "+str(i[0])+"\n")
            passwords.insert(END,str(serial_no)+". "+str(i[1])+"\n")
            emails.insert(END,str(serial_no)+". "+str(i[2])+"\n")
            serial_no+=1
    elif(x is None):
        pass
    else:
        msgbox.showwarning(title="wrong",message="wrong password!!")


def help():
    pass
root = Tk()
root.title("Password Generator and Manager")
root.geometry("1000x1200")
_color = COLORS[random.randint(0, len(COLORS) - 1)]
root.configure(bg=_color)

menubar=Menu(root)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="help",command=help)
helpmenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)


var = IntVar()
var1 = IntVar()

usernames = Text(root)
usernames.configure(height=25, width=60)
usernames.grid(row=0, column=1)
usernames.config(bg=_color)

passwords = Text(root)
passwords.configure(height=25, width=60)
passwords.grid(row=0, column=2)
passwords.config(bg=_color)

emails = Text(root)
emails.configure(height=25, width=60)
emails.grid(row=0, column=3)
emails.config(bg=_color)

_color = COLORS[random.randint(0, len(COLORS) - 1)]

user_label = Label(root, text="Username")
user_label.place(x=500, y=406)

username = Entry(root, width=50)
username.grid(row=1, column=2)
username.configure(background=_color)

email_label = Label(root, text="Email")
email_label.place(x=500, y=425)

email = Entry(root, width=50)
email.grid(row=2, column=2)
email.configure(background=_color)

Random_Password = Label(root, text="Password")
Random_Password.place(x=500, y=444)

entry = Entry(root, width=50)
entry.grid(row=3, column=2)
entry.configure(background=_color)

c_label = Label(root, text="Length")
c_label.place(x=500, y=463)

combo = Combobox(root, textvariable=var1)

combo['values'] = (
8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(row=4, column=2)
combo.configure(background=_color)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.place(x=600, y=500)
radio_medium = Radiobutton(root, text="Medium", variable=var, value=2)
radio_medium.place(x=700, y=500)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.place(x=800, y=500)

Copy_button = Button(root, text="copy", command=Copy)
Copy_button.place(x=600, y=675)

generate_button = Button(root, text="Generate", command=Generate)
generate_button.place(x=600, y=600)

save_password = Button(root, text="Store Password", command=Store)
save_password.place(x=675, y=600)

Show_passwords = Button(root, text="show passwords", command=show)
Show_passwords.place(x=675, y=675)
root.mainloop()
conn.commit()
conn.close()