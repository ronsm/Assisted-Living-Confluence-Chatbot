import json#needed for json manipulation (state is json data)

import requests#used for testing

import time#used for tests, specifically version 2.3, MAY BE REMOVED FOR LATER VERSIONS!!!!!!!!!!!!!!!!!

#this is for TEST PURPOSES ONLY. This program will (hopefully) allow for unit testing of the bots, simulating the Alana system as a whole.

#this SPECIFIC VERSION (2.3) is intended for extensive testing, with dditional printouts


#▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣

timeval = 0.0#this is the global variable used to measure time for testing in version 2.3

#▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣

CarryOn = True

Conversation = ""#the conversational string

name = ''

Attributes = {}

Last_bot = ''#needed so that the program will know which bot was spoken to last

Conversation = '@@@@@@@'#the user cannot naturally produce this, so it works to trigger the beginning of the survey

timeval = time.time()#JUST FOR 2.3 TEST PURPOSES

while CarryOn == True:

    try:#ensures graceful failure in the event of an exception

        r = requests.post('http://0.0.0.0:5111/', json={'current_state': {'bot_states' : {name : Attributes},'state' : {'last_bot' : Last_bot, 'input' : {'text' : Conversation}}}})

        data = json.loads(r.text)[0]#if the response is not proper json, it should crash here

        print("The bot called " + data["bot_name"] + " responded with '" + data["result"].rstrip().lstrip() + "'.")#the rstrip().lstrip() is needed to remove newlines and whitespace

        Attributes = data['user_attributes']

        name = data["bot_name"]

        Last_bot = name#this is the last bot that was selected to speak to the user.

        elapsed_time = time.time() - timeval

        print("Elapsed time for this test cycle (2) is " + str(elapsed_time))#JUST FOR 2.3 TEST PURPOSES

        Conversation = input("please enter your message here: ")
        
        timeval = time.time()#JUST FOR 2.3 TEST PURPOSES

    except:

        print("Ending Program.")

        CarryOn = False
