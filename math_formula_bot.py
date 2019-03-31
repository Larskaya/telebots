import config
import telebot

bot = telebot.TeleBot(config.token)

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

@bot.message_handler()
def get_formula_name(message):
	if message.text == '/start':
		bot.send_message(message.chat.id, '/sokrUmn - сокращенного умножения \n/sinCosTgCtg - sin cos tg ctg \n/plosh - площади \n/deskr - дескриминант и корни уравнения')
	elif message.text == '/sokrUmn':
		bot.send_message(message.chat.id, '/SokrUmnForm \n 2 f') # варианты
	elif message.text == '/sinCosTgCtg':
		bot.send_message(message.chat.id, '/SinCosTgCtg - sin,cos,tg,cts \n/TableSinCosTgCtg - таблица sin cos tg ctg')
	elif message.text == '/plosh':
		bot.send_message(message.chat.id, '/kvadr - квадрат \n/pryam - прямоугольник \n/treug - прямоугольный треугольник \n/krug - круг \n/romb - ромб \n/parallelep - параллелепипед \n/parallelog - параллелограмм')
	elif message.text == '/deskr':
		bot.send_message(message.chat.id, '/deskr - дескриминант \n/korn - корни уравнения')

	elif message.text in formuls_image_sokr:
		bot.send_photo(message.chat.id, formuls_image_sokr[message.text])

	elif message.text in formuls_image_sin_cos:
		bot.send_photo(message.chat.id, formuls_image_sin_cos[message.text])

	elif message.text in formuls_image_plosh:
		bot.send_photo(message.chat.id, formuls_image_plosh[message.text])

	elif message.text in formuls_image_deskr:
		bot.send_photo(message.chat.id, formuls_image_deskr[message.text])

	else:
		bot.send_message(message.chat.id, 'приветствую')

bot.polling()



















