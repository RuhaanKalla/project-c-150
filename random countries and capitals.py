# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:03:11 2022

@author: Dell
"""

from tkinter import*
import random
root = Tk()
root.title("Random countries and capitals")
root.geometry("800x800")
root.configure(background = "yellow")

input_country = Entry(root,bg = "blue" , fg = "white" , font = 25)
input_country.place(relx = 0.5 , rely = 0.2 , anchor = CENTER)
input_capital = Entry(root,bg = "blue" , fg = "white" , font = 25)
input_capital.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
label_country_list = Label(root ,bg = "yellow", fg = "red", font = 25)
label_country_list.place(relx = 0.5 ,rely = 0.5 , anchor = CENTER)
label_capital_list = Label(root ,bg = "yellow", fg = "red", font = 25)
label_capital_list.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
label_random_country = Label(root,bg = "yellow",fg = "red", font = 25)
label_random_country.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)
label_random_capital = Label(root,bg = "yellow",fg = "red", font = 25)
label_random_capital.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

list_country = []
list_capital = []

def add_to_list():
    country_name = input_country.get()
    capital_name = input_capital.get()
    list_country.append(country_name)
    label_country_list["text"] = "Country Name : " + str(list_country)
    list_capital.append(capital_name)
    label_capital_list["text"] = "Capital Name : " + str(list_capital)
    
def random_country_and_capital():
    length_country_list = len(list_country)
    length_capital_list = len(list_capital)
    random_number_1 = random.randint(0,length_country_list - 1)
    random_number_2 = random.randint(0,length_capital_list - 1)
    random_country = list_country[random_number_1]
    random_capital = list_capital[random_number_2]
    label_random_country["text"] = "Random country : " + str(random_country)
    label_random_capital["text"] = "Random capital : " + str(random_capital)


btn_add_country_to_list = Button(root,text = "Display country and city name" , bg = "purple" , fg = "yellow" ,font = 25 , command = add_to_list )
btn_add_country_to_list.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
btn_add_country_to_list = Button(root,text = "Display country and city name randomly" , bg = "purple" , fg = "yellow" ,font = 25,command = random_country_and_capital )
btn_add_country_to_list.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

root.mainloop()