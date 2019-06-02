# -*- coding: utf-8 -*-
import requests
import telebot
import json
from datetime import *

bot = telebot.TeleBot(token)

file = open('AuroraFoodBot2.txt', 'r')

f = file.readlines()
file.close()
start_data = ''
if len(f) > 0:

	a = f[0]
	a = json.loads(a)

	d = a['date']
	if d.split()[0] == str(datetime.today()).split()[0]:
		file = open('AuroraFoodBot2.txt', 'r')
		start_data = file.readlines()
		file.close()
	else: 
		file = open('AuroraFoodBotConfig.txt', 'r')
		start_data = file.readlines()
		file.close()


all_data = {} 
person = { 'name': '', 'time': '', 'restaurant': ''}


bot_data = start_data[0]
bot_data = json.loads(bot_data) 

all_restaurants = bot_data['all_restaurants']
all_times = bot_data['all_times']
date = bot_data['date']


@bot.message_handler()
def main(message):
	fromUser = message.from_user
	user_name = fromUser.first_name
	person['name'] = user_name

	time_list = []
	for el in all_times:
		time_list.append(el['time'])


	if len(message.text) > 0:

		counter = 0
		while counter < len(all_restaurants):

			if message.text == all_restaurants[counter]['name']:
				person['restaurant'] = all_restaurants[counter]['name']

				all_restaurants[counter]['persons'] += user_name + ' '
			counter += 1

		counter = 0
		while counter < len(all_times):
			if message.text in time_list:
				person['time'] = message.text

				if person['time'] == all_times[counter]['time']:
					all_times[counter]['names'] += person['name']
					
			counter += 1
		
		bot.send_message(message.chat.id, generate_message(all_times))

def generate_message(all_times):
	result = ''
	time_result = ''

	for restaurant in all_restaurants:
		result += restaurant['name'] + ': ' + restaurant['persons'] + '\n'
	
	for el in all_times:
		time_result += el['time'] + ': ' + el['names'] + '\n'


	all_data['all_restaurants'] = all_restaurants
	all_data['all_times'] = all_times

	all_data['date'] = str(datetime.today()).split()[0]


	file2 = open('AuroraFoodBot2.txt', 'w')
	file2.write(json.dumps(all_data))
	file2.close()

	return result + '\n' + time_result


bot.polling()

