#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'Вставьте_свой_токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Яйца всмятку")
	item2 = types.KeyboardButton("Яйца в мешочек")
	item3 = types.KeyboardButton("Яйца Чака Норриса")


	markup.add(item1, item2, item3)

	bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text="Добро пожаловать, {0.first_name}, напомню тебе время приготовления 🥚. Чтобы все получилось, необходимо выполнить несколько условий: 1) воду довести до предкипения, но не давать ей булькать, иначе температура воды будет выше необходимой; 2) далее погружаем яйца, не очень быстро, чтобы не лопнула скорлупа; 3) по истечении времени вытаскиваем и охлаждаем под холодной водой".format(message.from_user, bot.get_me()),
        reply_markup=markup
    )

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Яйца всмятку':
			bot.send_message(message.chat.id, '7 минут с момента погружения')
			img = open('alan.jpg', 'rb')
			bot.send_photo(message.chat.id, img)
		elif message.text == 'Яйца в мешочек':
			bot.send_message(message.chat.id, '9 минут с момента погружения')
			img = open('arni.webp', 'rb')
			bot.send_photo(message.chat.id, img)
		elif message.text == 'Яйца Чака Норриса':
			bot.send_message(message.chat.id, '15 минут с момента погружения')
			img = open('petros.jpg', 'rb')
			bot.send_photo(message.chat.id, img)
		else:
			bot.send_message(message.chat.id, 'Тыкай на кнопочки😢')

bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
