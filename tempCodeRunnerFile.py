# import random
# n = []
# s = int(input("get a number"))
# for i in (0,s):
#     ele = int(input(i))
#     n.append(ele)
# print(n)
# x=input("choose a string:")
# if x[::-1] == x[::-1]:
#     print("create a password is:", random.choice(n[::-1]) + random.choice(x[::-1]))
# with open("data.txt","w") as data_file:
#     data_file.write("hello i am alexa")
# import pandas
# data = pandas.read_csv("weather_data.csv.csv")
# print(data.temp)
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data.temp.to_list()
# print(sum(temp_list)/len(temp_list))
# print(data.temp.mean())
# print(data.temp.max())
# print(data[data.day == "monday"])
# print(data[data.temp == data.temp.max()])
# data_dict = {
#     "student": ["any" , "james" , "angela"],
#     "scores": [76 , 56 ,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# numbers = [1,2,3]
# new_list = [item*2 for item in numbers]
# print(new_list)
# numbers = "hello"
# new_list = [num for num in numbers]
# names = ["alex" , "beth" , "jack" , "harry" , "lawra"]
# short_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)
# num = [1,1,2,3,5,8,13,21,34,55]
# square_number = [num*num for num in num]
# print(square_number)
# list_of_strings = input().split(',')
# numbers = [int(x) for x in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)
# import random
# names = ["alexa" , "jack" , "mickel" , "robin" , "arian"]
# result = {student:random.randint(1,100) for student in names}
# print(result)
# student_score = {
#     "rahul": 34,
#     "jack": 65,
#     "mahato": 56,
#     "mahi": 64,
#     "akash": 60
# }
# result = {student:score for(student,score) in student_score.items() if score >= 60}
# print(result)
# sentence = input()
# result = {word:len(word) for word in sentence.split()}
# print(result)
# weather_c = eval(input())
# weather_f = {day:(temp*9/5) + 32  for(day,temp) in weather_c.items()}
# print(weather_f)
# import pandas
# student_dict = {
#     "names": ["debashis" , "rahul" , "jack" , "akash" , "angela"],
#     "score": [56 , 45 , 34 , 78 , 85]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# for (index,row) in student_data_frame.iterrows():
#     print(index)
# import pandas
# data = pandas.read_csv("Code_letter.csv")
# phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
# word = input("enter a word  ").upper()
# result = [phonetic_dict[letter] for letter in word]
# print(result)
# import tkinter
# window = tkinter.Tk()
# window.title("my first gui project")
# window.minsize(600,600)
# my_label = tkinter.Label(text="i am a label")
# my_label.pack(expand=4)
# window.mainloop()
# def add (*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(3,5,6,7))
# def calculate(n,**kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multipy"]
#     print(n) 
# calculate(2,add=3, multipy=5)
# from tkinter import *
# window = Tk()
# window.title("my gui project")
# window.minsize(500,300)
# my_label = Label(text="i am a label" , font=("arial" , 24 , "bold"))
# my_label.pack()
# def button_click():
#     my_label.config(text=input.get())
# button = Button(text="click me" , command = button_click)
# button.pack()
# input = Entry()
# input.pack()
# from tkinter import *
# window = Tk()
# window.title("Mile to Km Converter")
# label = Label(text="is equal to   0     km ")
# label.grid(column=1,row=1)
# Mile = Label(text="Miles")
# Mile.grid(column=2,row=0)
# def button_click():
#     x = float(input.get())
#     label.config(text=f"is equal to   {x*1.60934}     km ")
# button = Button(text="calculate" , command = button_click)
# button.grid(column=1,row=2)
# input = Entry()
# input.grid(column=1,row=0)
# window.mainloop()
# from tkinter import *
# import math
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 1
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
# def reset_button():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text,text="00:00")
#     title_label.config(text="Timer")
#     check_marks.config("")
#     global reps
#     reps=0

# def timer_mechanism():
#     global reps
#     reps += 1
#     work_sec = WORK_MIN*60
#     short_break_sec = SHORT_BREAK_MIN*60
#     long_break_sec = LONG_BREAK_MIN*60
#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         title_label.config(text="Break" , fg=RED)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         title_label.config(text="Break" , fg=PINK)
#     else:
#         count_down(work_sec)
#         title_label.config(text="work",fg=GREEN)
# def count_down(count):
#     count_min = math.floor(count/60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"
#     canvas.itemconfig(timer_text,text=f"0{count_min}:{count_sec}")
#     if count > 0:
#         window.after(1000,count_down,count-1)
#     else:
#         timer_mechanism()
#         marks = ""
#         work_sessions = math.floor(reps/2)
#         for _ in work_sessions:
#             marks += "✓"
#         check_marks.config(text=marks)
# window = Tk()
# window.title("Tomato Timer")
# window.config(padx=100,pady=50,bg=YELLOW)
# title_label = Label(text="Timer" , fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
# title_label.grid(column=1,row=0)
# canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100,112,image=tomato_img)
# timer_text = canvas.create_text(100,130,text="00:00" , fill="white",font=(FONT_NAME,30,"bold"))
# canvas.grid(column=1,row=1)
# start_button = Button(text="Start",highlightthickness=0,command=timer_mechanism)
# start_button.grid(column=0,row=2)
# reset_button = Button(text="Reset" , highlightthickness=0,command=reset_button) 
# reset_button.grid(column=2,row=2)
# check_marks = Label(text="✓",fg=GREEN,bg=YELLOW)
# check_marks.grid(column=1,row=3)

# window.mainloop()
# import pandas
# data = pandas.read_csv("Code_letter.csv")
# phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
# while True:
#     word = input("enter a word  ").upper()
#     try:
#         result = [phonetic_dict[letter] for letter in word]
#     except:
#         print("sorry you have number fill")
        
#     else:
#         print(result)
#         break
import smtplib
import random
import datetime as dt
my_email = "debashisgoswami000@gmail.com"
my_password = "itya nxmb zqgv mtsw"
now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt","r") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=my_password)
subject = "Motivational Code"
message = f"Subject: {subject}\n\n{quote}"
connection.sendmail(from_addr=my_email,to_addrs="debashisgoswami159@gmail.com",msg=message)
connection.close()
# import smtplib

# my_email = "debashisgoswami000@gmail.com"
# password = "vijkjvytnatilbmr"
# to_email = "debashisgoswami159@gmail.com"

# connection = smtplib.SMTP("smtp.gmail.com", 587)

# connection.starttls()

# connection.login(user=my_email, password=password)

# message = "Subject: Hello\n\nThis is a test email."

# connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)

# connection.quit()
