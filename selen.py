from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def parser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://live.skillbox.ru/')


    daniil = '//*[@id="#app"]/main/div/div/div[2]/div[1]/div[2]/ul/li[1]/label/span'

    checkbox = browser.find_element(by=By.XPATH, value=daniil)
    checkbox.click()
    time.sleep(3)
    webinars = browser.find_elements(by=By.CSS_SELECTOR, value='.webinar-card__title')
    webinars_list = [webinar.text for webinar in webinars]
    return webinars_list


from telegram import Update # кусок новой входящей информации
from telegram.ext import Updater, Filters # инструмент, который получает апдейты и дает нам возможность их обработать
from telegram.ext import MessageHandler # обработчик апдейта
import datetime

BOT_KEY = ''

# Функция будет вызвана при получении апдейта
def bot_reply(upd: Update, ctx):
    msg = upd.message.text
    print(msg)
    if msg == 'Вебинары':
        current_time = datetime.datetime.now().strftime("%c")
        webinars = parser()
        print(f"Найдено вебинаров: {len(webinars)}")
        webinars_list = "\n".join(webinars)
        reply = f'В ответ на ваш запрос от {current_time}, я нашел для вас следующие вебинары:\n {webinars_list}'
        upd.message.reply_text(reply)
    else:
        upd.message.reply_text('ОК') #бот отвечает ОК

bot = Updater(BOT_KEY) # подключение к боту
handler = MessageHandler(Filters.text, bot_reply)
bot.dispatcher.add_handler(handler)
bot.start_polling()
bot.idle()