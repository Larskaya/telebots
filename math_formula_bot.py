import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def get_formula_name(message):
	sent = bot.send_message(message.chat.id, '/SokrUmn - сокращенного умножения \n/SinCosTgCtg - sin cos tg ctg \n/Plosh - площади \n/Deskr - дескриминант и корни уравнения')
	bot.register_next_step_handler(sent, all_formuls)

def all_formuls(message):
	print(message.text, 'mes txt')
	if message.text == '/SokrUmn':
		print(1)
		sent = bot.send_message(message.chat.id, '/SokrUmnForm \n 2 f') # варианты
		bot.register_next_step_handler(sent, get_formula_sokr_umn)
	elif message.text == '/SinCosTgCtg':
		print(2)
		sent = bot.send_message(message.chat.id, '/SinCosTgCtg - sin,cos,tg,cts \n/TableSinCosTgCtg - таблица sin cos tg ctg')
		bot.register_next_step_handler(sent, get_formula_sin_cos)
	elif message.text == '/Plosh':
		print(3)
		sent = bot.send_message(message.chat.id, '/kvadr - квадрат \n/pryam - прямоугольник \n/treug - прямоугольный треугольник \n/krug - круг \n/romb - ромб \n/parallelep - параллелепипед \n/parallelog - параллелограмм')
		bot.register_next_step_handler(sent, get_formula_plosh)
	elif message.text == '/Deskr':
		sent = bot.send_message(message.chat.id, '/deskr - дескриминант \n/korn - корни уравнения')
		bot.register_next_step_handler(sent, get_formula_deskr)

sokr_umn_img = open('f1.png', 'rb')
sin_cos_img = open('sin-cos-tg-ctg.png', 'rb')
table_sin_img = open('table-sin-cos-tg-ctg.png', 'rb')

#площади
plKv_img = open('ploshKv.png', 'rb')
plPryam_img = open('ploshPryam.png', 'rb')
plKruga_img = open('ploshKruga.png', 'rb')
plRomba_img = open('ploshRomba.png', 'rb')
plParallelep_img = open('ploshParallelep.png', 'rb')
plParallelog_img = open('ploshParallelogramma.png', 'rb')
plPryamTreug_img = open('ploshPryamTreug.png', 'rb')

deskr_img = open('deskr.png', 'rb')
korni_img = open('korni.png', 'rb')

formuls_image_sokr = {
	'/SokrUmnForm': sokr_umn_img,
}

formuls_image_sin_cos = {
	'/SinCosTgCtg': sin_cos_img,
	'/TableSinCosTgCtg': table_sin_img,
}

formuls_image_plosh = {
	'/kvadr': plKv_img,
	'/pryam': plPryam_img,
	'/krug': plKruga_img,
	'/romb': plRomba_img,
	'/parallelep': plParallelep_img,
	'/parallelog': plParallelog_img,
	'/treug': plPryamTreug_img,
}

formuls_image_deskr = {
	'/deskr': deskr_img,
	'/korn': korni_img
}

def get_formula_sokr_umn(message):
	if message.text in formuls_image_sokr:
		sent = bot.send_photo(message.chat.id, formuls_image_sokr[message.text])
		bot.register_next_step_handler(sent, all_formuls)

def get_formula_sin_cos(message):
	if message.text in formuls_image_sin_cos:
		sent = bot.send_photo(message.chat.id, formuls_image_sin_cos[message.text])
		bot.register_next_step_handler(sent, all_formuls)

def get_formula_plosh(message):
	if message.text in formuls_image_plosh:
		sent = bot.send_photo(message.chat.id, formuls_image_plosh[message.text])
		bot.register_next_step_handler(sent, all_formuls)

def get_formula_deskr(message):
	if message.text in formuls_image_deskr:
		sent = bot.send_photo(message.chat.id, formuls_image_deskr[message.text])
		bot.register_next_step_handler(sent, all_formuls)

bot.polling()



















