#Braedon Kukan
#Web-Scraper
#March 24th, 2021
#---------------------

from bs4 import BeautifulSoup
import requests
import re
import tkinter as tk
import json
import statistics

#initiating the gui popup
window = tk.Tk()
window.title("Baseball Card Lookup")


#function calculates the value of the baseball card
def getValue():
    player_name = inp1.get()
    card_number = inp2.get()
    url = 'https://mavin.io/search?q='
    checkPlayer = list(player_name)
    for i in range(0,10):
        if str(i) in checkPlayer:
            result.config(text = "Invalid")

    finalPlayer = player_name.split(' ')
    for i in range(len(finalPlayer)):
        url += finalPlayer[i] + '+'
    url += card_number
    source = requests.get(url, headers=headers).content
    soup = BeautifulSoup(source,'lxml')
    script = soup.find_all('script', {'type':'application/ld+json'})[1]
    jsonData = json.loads(script.string)[0]
    highPrice = float(jsonData['offers']['highPrice'])
    lowPrice = float(jsonData['offers']['lowPrice'])
    average = round(statistics.mean([highPrice, lowPrice]),2)
    result.config(text = "Your card coud potentially be worth $" + str(average))
    


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}


#setting up the GUI with tkinter
#------------------------------


#setting up the label/welcome message  greetings1,greetings2,etc....
g1 = tk.Label(window,text="Want to know the value of your baseball card?")
g2 = tk.Label(window,text="You found the place, enter the name of the player and the card number below.")
g3 = tk.Label(window,text='')
g1.pack()
g2.pack()
g3.pack()

#adding entry widgets
l1 = tk.Label(window,text="Enter the player's name:")
inp1 = tk.Entry()
l1.pack()
inp1.pack()
l2 = tk.Label(window,text = "Enter the card number (if available):")
inp2 = tk.Entry()
l2.pack()
inp2.pack()

#the result label
result = tk.Label(window,text = '')
result.pack()

#adding button
b1 = tk.Button(window,text = "Value", width=10, command = getValue)
b1.pack()


window.mainloop()