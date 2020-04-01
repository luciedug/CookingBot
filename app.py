from random import *
from flask import Flask, request
from pymessenger.bot import Bot
import requests
import csv
import random
import spoonacular as sp
import os
#To connect to spoonacular API in order to get a random joke
api = sp.API("8fb217867404486192e99424e58bcb10")
#Connecion to messenger 
app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])

def receive_message():
    data = read_csv()
    welcomes = ["hello", "Hello", "Hi", "hi"]
    first_message = "Hello, what type of recipe do you want today ? Salty ? Sugary ? Surprise ?"
    salty1 = ["Enter a code (for ex s1)", "s1 random salty", "s2 Healthy salty", "s3 Comfort Salty", "s4 More options"]
    salty1final = "\n".join(salty1)
    salty2 = ["Enter a code (for ex t1)", "t1 random American", "t2 American and healthy", "t3 random Asian", "t4 Asian and healthy", "t5 Random Italian", "t6 Italian and healthy", "t7 Random French", "t8 French and healthy"]
    salty2final = "\n".join(salty2)
    sugar1 = ["Enter a code (for ex i1)", "i1 random sugar", "i2 Healthy sugary", "i3 Comfort sugary", "i4 More options"]
    sugar1final = "\n".join(sugar1)
    sugar2 = ["Enter a code (for ex v1)", "v1 random American", "v2 American and healthy", "v3 random Asian", "v4 Asian and healthy", "v5 Random Italian", "v6 Italian and healthy", "v7 Random French", "v8 French and healthy"]
    sugar2final = "\n".join(sugar2)
    list_p = create_list()
    if request.method == 'GET':
        #Check the verify token on facebook messenger
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #Then if it's not a get request, it's a post : we will answer the message
    else:
    
       output = request.get_json() #message
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text') in welcomes:
                    response_sent_text = first_message
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="Salty" or message['message'].get('text')=="salty":
                    response_sent_text = salty1final
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="s1" or message['message'].get('text')=="S1":
                    response_sent_text = get_savory_random(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="s2" or message['message'].get('text')=="S2":
                    response_sent_text = get_savory_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="s3" or message['message'].get('text')=="S3":
                    response_sent_text = get_savory_nh(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="s4" or message['message'].get('text')=="S4":
                    response_sent_text = salty2final
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t1" or message['message'].get('text')=="T1":
                    response_sent_text = get_savory_american(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t2" or message['message'].get('text')=="T2":
                    response_sent_text = get_savory_american_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t3" or message['message'].get('text')=="T3":
                    response_sent_text = get_savory_asian(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t4" or message['message'].get('text')=="T4":
                    response_sent_text = get_savory_asian_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t5" or message['message'].get('text')=="T5":
                    response_sent_text = get_savory_italian(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t6" or message['message'].get('text')=="T6":
                    response_sent_text = get_savory_italian_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t7" or message['message'].get('text')=="T7":
                    response_sent_text = get_savory_french(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="t8" or message['message'].get('text')=="T8":
                    response_sent_text = get_savory_french_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="Sugary" or message['message'].get('text')=="sugary":
                    response_sent_text = sugar1final
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="i1" or message['message'].get('text')=="I1":
                    response_sent_text = get_sugary_random(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="i2" or message['message'].get('text')=="I2":
                    response_sent_text = get_sugary_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="i3" or message['message'].get('text')=="I3":
                    response_sent_text = get_sugary_nh(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="i4" or message['message'].get('text')=="I4":
                    response_sent_text = sugar2final
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v1" or message['message'].get('text')=="V1":
                    response_sent_text = get_sugary_american(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v2" or message['message'].get('text')=="V2":
                    response_sent_text = get_sugary_american_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v3" or message['message'].get('text')=="V3":
                    response_sent_text = get_sugary_asian(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="V4" or message['message'].get('text')=="v4":
                    response_sent_text = get_sugary_asian_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v5" or message['message'].get('text')=="V5":
                    response_sent_text = get_sugary_italian(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v6" or message['message'].get('text')=="V6":
                    response_sent_text = get_sugary_italian_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="V7" or message['message'].get('text')=="v7":
                    response_sent_text = get_sugary_french(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text')=="v8" or message['message'].get('text')=="V8":
                    response_sent_text = get_sugary_french_h(data)
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('text') not in list_p:
                    resp = ["I don't understand your answer/code","Therefore, I'm goign to share a joke : ", get_joke()]
                    response_sent_text = "\n".join(resp)
                    send_message(recipient_id, response_sent_text)

                #non text item (video, photo ...)
               
                
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'



#The following functions will get a recipe for different occasion in the database
def get_savory_random(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="h":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_nh(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="nh":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="h":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_nh(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="nh":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res


def get_sugary_random(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_french_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="h" and elem[4]=="french":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_american_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="h" and elem[4]=="american":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_italian_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="h" and elem[4]=="italian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_asian_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[3]=="h" and elem[4]=="asian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_french(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[4]=="french":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_american(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[4]=="american":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_italian(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[4]=="italian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_sugary_asian(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="su" and elem[4]=="asian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_french(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[4]=="french":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_american(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[4]=="american":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_italian(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[4]=="italian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_asian(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[4]=="asian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_french_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="h" and elem[4]=="french":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_american_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="h" and elem[4]=="american":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_italian_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="h" and elem[4]=="italian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

def get_savory_asian_h(data):
    b=0
    url=""
    while b==0:
        n = randint(0, len(data)-1)
        elem = data[n]
        if elem[0]=="sa" and elem[3]=="h" and elem[4]=="asian":
            url = elem[2]
            name = elem[1]
            tab = [name, url]
            res = "\n".join(tab)
            b = 1
    return res

#if the user's answer is not handle in this list, then it will display a joke
def create_list():
    list_p = []
    
    list_p.append("Sugary")
    list_p.append("sugary")
    list_p.append("i1")
    list_p.append("I1")
    list_p.append("i2")
    list_p.append("I2")
    list_p.append("i3")
    list_p.append("I3")
    list_p.append("i4")
    list_p.append("I4")
    list_p.append("v1")
    list_p.append("V1")
    list_p.append("v2")
    list_p.append("V2")
    list_p.append("v3")
    list_p.append("V3")
    list_p.append("v4")
    list_p.append("V4")
    list_p.append("v5")
    list_p.append("V5")
    list_p.append("v6")
    list_p.append("V6")
    list_p.append("v7")
    list_p.append("V7")
    list_p.append("v8")
    list_p.append("V8")list_p.append("salty")
    list_p.append("Salty")
    list_p.append("s1")
    list_p.append("S1")
    list_p.append("s2")
    list_p.append("S2")
    list_p.append("s3")
    list_p.append("S3")
    list_p.append("s4")
    list_p.append("S4")
    list_p.append("T1")
    list_p.append("t1")
    list_p.append("T2")
    list_p.append("t2")
    list_p.append("T3")
    list_p.append("t3")
    list_p.append("T4")
    list_p.append("t4")
    list_p.append("T5")
    list_p.append("t5")
    list_p.append("T6")
    list_p.append("t6")
    list_p.append("T7")
    list_p.append("t7")
    list_p.append("T8")
    list_p.append("t8")
    list_p.append("hello")
    list_p.append("Hello")
    list_p.append("Hi")
    list_p.append("hi")
    return list_p

#function that answer to the user 
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

#display a joke from spoonacular API
def get_joke():
    response = api.get_a_random_food_joke()
    data = response.json()
    return data['text']

def read_csv():
    data = []
    with open('dataRecipe.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            line = [row[0], row[1], row[2],row[3], row[4]]
            data.append(line)
    return data
                     


if __name__ == "__main__":
    app.run()