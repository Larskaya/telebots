import telebot
from telebot import types

bot = telebot.TeleBot('729994535:AAH2BkvmcKzI6bsFoA3uPIPvGlK3kqiICNA')

@bot.message_handler(commands=['start'])
def start(message):

	keyboard_HTML_button = types.InlineKeyboardMarkup() #resize_keyboard = True
	keyboard_HTML_button.add(*[types.InlineKeyboardButton(text = a, callback_data = a) for a in ['HTML', 'Buttons', 'keyboard']])
	
	sent = bot.send_message(message.chat.id, 'HTML or buttons or keyboard ?', reply_markup = keyboard_HTML_button)

@bot.callback_query_handler(func = lambda m:True)
def inline(m):

	if m.data == 'Buttons':
		keyboard_button = types.InlineKeyboardMarkup()
		keyboard_button.add(*[types.InlineKeyboardButton(text = letter, callback_data = letter) for letter in ['a', 'b', 'c']])
		
		sent = bot.send_message(m.message.chat.id, 'a b c', reply_markup = keyboard_button)

	elif m.data == 'HTML':
		sent = bot.send_message(chat_id = m.message.chat.id, text = '<b>bold</b>\n<strong>bold</strong>\n<i>italic</i>\n<em>italic</em>\n<a href="http://www.example.com/">inline URL</a>\n<a href="tg://user?id=123456789">inline mention of a user</a>\n<code>inline fixed-width code</code>\n<pre>pre-formatted fixed-width code block</pre>', parse_mode='HTML')


	elif m.data == 'keyboard':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
		keyboard.add(*[types.KeyboardButton(letter) for letter in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o']])

		sent = bot.send_message(chat_id = m.message.chat.id, text = 'А вот и клавиатура!', reply_markup = keyboard)

	#bot.send_message(chat_id = m.message.chat.id, text = 'you entered ' + m.data)
	#(parse_mode='Markdown', reply_markup = keyboard)

bot.polling()





