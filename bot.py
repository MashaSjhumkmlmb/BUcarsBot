from telebot import *
import time
import requests
from bs4 import BeautifulSoup

bot: TeleBot = telebot.TeleBot('5887321915:AAHexjMTqp_VknoLKs4qYwY0Q9wuZr1_z5g')


@bot.message_handler(commands=['start'])
def start(messege):
    kb = types.InlineKeyboardMarkup()
    kia = types.InlineKeyboardButton(text='Kia', callback_data='kia')
    skoda = types.InlineKeyboardButton(text='Skoda', callback_data='skoda')
    nissan = types.InlineKeyboardButton(text='Nissan', callback_data='nissan')
    alfa_romeo = types.InlineKeyboardButton(text='Alfa Romeo', callback_data='alfa')
    audio = types.InlineKeyboardButton(text='Audi', callback_data='audio')
    bmw = types.InlineKeyboardButton(text='BMW', callback_data='bmw')
    chevrolet = types.InlineKeyboardButton(text='Chevrolet', callback_data='chevrolet')
    chrysler = types.InlineKeyboardButton(text='Chrysler', callback_data='chrysler')
    citroen = types.InlineKeyboardButton(text='Citroen', callback_data='citroen')
    dodge = types.InlineKeyboardButton(text='Dodge', callback_data='dodge')
    fiat = types.InlineKeyboardButton(text='Fiat', callback_data='fiat')
    ford = types.InlineKeyboardButton(text='Ford', callback_data='ford')
    geely = types.InlineKeyboardButton(text='Geely', callback_data='geely')
    honda = types.InlineKeyboardButton(text='Honda', callback_data='honda')
    hyndai = types.InlineKeyboardButton(text='Hyndai', callback_data='hyndai')
    lada = types.InlineKeyboardButton(text='Lada', callback_data='lada')
    lexus = types.InlineKeyboardButton(text='Lexus', callback_data='lexus')
    mazda = types.InlineKeyboardButton(text='Mazda', callback_data='mazda')
    mersedes = types.InlineKeyboardButton(text='Mersedes-Benz', callback_data='mersedes')
    mitsubishi = types.InlineKeyboardButton(text='Mitsubishi', callback_data='mitsubishi')
    opel = types.InlineKeyboardButton(text='Opel', callback_data='opel')
    peugeot = types.InlineKeyboardButton(text='Peugeot', callback_data='peugeot')
    renaut = types.InlineKeyboardButton(text='Renaut', callback_data='renaut')
    rover = types.InlineKeyboardButton(text='Rover', callback_data='rover')
    seat = types.InlineKeyboardButton(text='Seat', callback_data='seat')
    subaru = types.InlineKeyboardButton(text='Subaru', callback_data='subaru')
    suzuki = types.InlineKeyboardButton(text='Suzuki', callback_data='suzuki')
    toyota = types.InlineKeyboardButton(text='Toyota', callback_data='toyota')
    volkswagen = types.InlineKeyboardButton(text='Volkswagen', callback_data='volkswagen')
    volvo = types.InlineKeyboardButton(text='Volvo', callback_data='volvo')
    kb.add(kia, skoda, nissan, alfa_romeo, audio, bmw, chevrolet, chrysler, citroen, dodge, fiat, ford, geely, honda,
           hyndai, lada,
           lexus, mazda, mersedes, mitsubishi, opel, peugeot, renaut, rover, seat, subaru, suzuki, toyota, volvo,
           volkswagen)
    bot.send_message(messege.chat.id, ' Привет! Какая б/у машина тебя интересует?', reply_markup=kb)

    time.sleep(2)

    bot.send_message(messege.chat.id, 'Выбрал марку?) Напиши модель машины на английском языке!')



@bot.callback_query_handler(func=lambda call: True)
def call_back_inline(call):
    if call.data == 'kia':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/kia/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                        break


    if call.data == 'skoda':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/skoda/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'nissan':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/nissan/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'audio':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/audi/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'bmw':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/bmw/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'alfa':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/alfa-romeo/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'chevrolet':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/chevrolet/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'chrysler':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/chrysler/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'citroen':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/citroen/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'dodge':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/dodge/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'fiat':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/fiat/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'ford':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/ford/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'geely':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/geely/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'honda':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/honda/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'hyundai':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/hyundai/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'lada':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/lada-vaz/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                    try:
                        soup = BeautifulSoup(r.text, 'html.parser')
                        cost = soup.find_all('div', class_='listing-item__params')
                        clear = []
                        for i in cost:
                            clear.append(i.getText())

                            model = soup.find_all('div', class_='listing-item__priceusd')
                            clear1 = []
                            for k in model:
                                clear1.append(k.getText())

                            img = soup.select('div.listing-item__photo img ')

                            bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                            bot.send_message(messsege.chat.id, f'{img[count]}')
                            count += 1
                    except:
                        if count == 0:
                            bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                        else:
                            bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                               'Более подробную информацию смотри на сайте av.by')
                        break

    if call.data == 'lexus':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/lexus/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'mazda':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/mazda/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'mersedes':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/mersedes-benz/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'mitsubishi':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/mitsubishi/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'opel':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/opel/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'peugeot':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/peugeot/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'renaut':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/renault/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'rover':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/rover/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    commands=['start']

    if call.data == 'subaru':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/subaru/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'toyota':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/toyota/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'volkswagen':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/volkswagen/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break

    if call.data == 'volvo':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/volvo/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break


    if call.data == 'suzuki':
        @bot.message_handler()
        def answer(messsege):
            text = messsege.text
            text = str(text).lower()
            url = f'https://cars.av.by/suzuki/{text}'
            r = requests.get(url)
            r.encoding = 'UTF-8'
            count = 0
            while count >= 0:
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    cost = soup.find_all('div', class_='listing-item__params')
                    clear = []
                    for i in cost:
                        clear.append(i.getText())

                    model = soup.find_all('div', class_='listing-item__priceusd')
                    clear1 = []
                    for k in model:
                        clear1.append(k.getText())

                    img = soup.find_all('div', class_='listing-item__photo')

                    bot.send_message(messsege.chat.id, f'{count + 1} - {clear1[count]} {clear[count]}')

                    bot.send_message(messsege.chat.id, f'{img[count]}')
                    count += 1
                except:
                    if count == 0:
                        bot.send_message(messsege.chat.id, 'Хммм...я не знаю такой модели...')
                    else:
                        bot.send_message(messsege.chat.id, 'Это самые актуальные предложения.'
                                                           'Более подробную информацию смотри на сайте av.by')
                    break



bot.polling(none_stop=True)
