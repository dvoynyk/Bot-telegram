import telebot
from telebot import types
import json
bot = telebot.TeleBot('')

from datetime import timedelta, datetime, timezone

day_week = [26,4,5,8,11,12,18,19,25,26]
day_work1 = ['1. Разговор о важном',
             '2. Немецкий язык (подготовка химия)',
             '3. История',
             '4. География',
             '5. Химия',
             '6. Родная литература',
             '7. Алгебра',
             '8. Английский язык']
day_work2 = ['1. Подготовка история, биология',
             '2. Геометрия',
             '3. География',
             '4. Русский язык',
             '5. История',
             '6. Физика',
             '7. Английский язык',
             '8. Подготовка обществознание']
day_work3 = ['1. Алгебра',
             '2. Русский язык',
             '3. Литература',
             '4. Химия',
             '5. Биология',
             '6. Информатика',
             '7. Физика',
             '8. Подготовка информатика']
day_work4 = ['1. Русский язык (подготовка)',
             '2. Литература',
             '3. Физ-ра',
             '4. Обществознание',
             '5. Алгебра',
             '6. Физика',
             '7-8. Подготовка математика']
day_work5 = ['1. Физ-ра (подготовка биология)',
             '2. Английский язык',
             '3. ОБЖ',
             '4. Геометрия',
             '5. Биология',
             '6. Литература']
day_monday = [27,6,13,20,27]
day_tuesday = [28,7,14,21,28]
day_wednesday = [1,8,15,22,29]
day_thursday = [2,9,16,23,30]
day_friday = [3,10,17,24,31]
oge = ['24 мая — история, физика, биология', 
       '30 мая — обществознание, информатика и ИКТ, география, химия',
       '2 июня — иностранные языки',
       '3 июня — иностранные языки',
       '6 июня — русский язык',
       '9 июня — математика',
       '14 июня — литература, физика, информатика и ИКТ, география',
       '17 июня — обществознание, биология, химия']
def day():
    offset = timezone(timedelta(hours=3))  # Московское время
    now = datetime.now(offset)  # Текущая дата
    min_week = now
    day_ = str(min_week.day)  # Получение значения дня
    day__ = int(day_)
    return day__
    # if min_week.day < 10:
    #     day = f'0{min_week.day}'  #Чтобы день выводился было "09" а не "9"
    # if min_week.month < 10:
    #     month = f'0{min_week.month}'
    # result = f'{month}-{day}'
    #return result   # Возвращает время в виде "06-26"
def month():
    offset = timezone(timedelta(hours=3))  # Московское время
    now = datetime.now(offset)  # Текущая дата
    min_week1 = now + timedelta(7)
    month_ = str(min_week1.month)
    return month_
def day_month():
    offset = timezone(timedelta(hours=3))  # Московское время
    now = datetime.now(offset)  # Текущая дата
    min_week = now
    min_week1 = now + timedelta(7)
    month_ = str(min_week1.month)
    day_ = str(min_week.day)  # Получение значения дня
    a = day_ + '.' + month_ + '.' + '23'
    return a
def print_list(my_list):
    print('\n'.join(my_list))

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Полезные СсЫлОчКи')
    btn2 = types.KeyboardButton('Расписание на сегодня')
    btn3 = types.KeyboardButton('Сколько мне осталось страдать(огэшки, каникулы)')
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник! (P.S. Я не помогу тебе с твоими личными проблемами, но облегчу твою участь в школе)", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Полезные СсЫлОчКи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('#Ссылка в школьную группу#')
        btn2 = types.KeyboardButton('#Ссылка в Сибирь:)#')
        btn3 = types.KeyboardButton('BAAAAAAAAACK!')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Получай', reply_markup=markup) #ответ бота
    elif message.text == 'BAAAAAAAAACK!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Полезные СсЫлОчКи')
        btn2 = types.KeyboardButton('Расписание на сегодня')
        btn3 = types.KeyboardButton('Сколько мне осталось страдать(огэшки, каникулы)')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник! (P.S. Я не помогу тебе с твоими личными проблемами, но облегчу твою участь в школе)", reply_markup=markup)
    elif message.text == 'Расписание на сегодня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('BAAAAAAAAACK!')
        markup.add(btn1)
        if day() not in day_week:
            if day() in day_monday:
                bot.send_message(message.from_user.id, '\n'.join(day_work1), reply_markup=markup) #parse_mode='Markdown'
            elif day() in day_tuesday:
                bot.send_message(message.from_user.id,'\n'.join(day_work2) , reply_markup=markup) 
            elif day() in day_wednesday:
                bot.send_message(message.from_user.id, '\n'.join(day_work3), reply_markup=markup)
            elif day() in day_thursday:
                bot.send_message(message.from_user.id,'\n'.join(day_work4), reply_markup=markup)
            elif day() in day_friday:
                bot.send_message(message.from_user.id,'\n'.join(day_work5), reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, f'Сегодня {day_month()}. Поздравляю, лох, у тебя выходной', reply_markup=markup)
    elif message.text == 'Сколько мне осталось страдать(огэшки, каникулы)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ОГЭ')
        btn2 = types.KeyboardButton('Каникулы')
        btn3 = types.KeyboardButton('BAAAAAAAAACK!')
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.from_user.id, 'Ну кароч, не очень расклад:',reply_markup=markup)
    elif message.text == 'ОГЭ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('BAAAAAAAAACK!')
        markup.add(btn1)
        bot.send_message(message.from_user.id,'\n'.join(oge) , reply_markup=markup)
    elif message.text == 'Каникулы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('BAAAAAAAAACK!')
        markup.add(btn1)
        bot.send_message(message.from_user.id,'20.02 - 26.02; \n 03.04 - 09.04' , reply_markup=markup)
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
