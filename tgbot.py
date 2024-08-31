import json
from aiogram import Bot, Dispatcher, executor, types

# from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import os
import time
import asyncio


bot = Bot(token=('6418166216:AAGKaYlY-BxPxNpwXKgihOG7y7sNjt1zxTk'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start(message: types.Message):
  
    bundle_list = 'Текущие наборы:\n \n'
    with open(r'json\bundle_info.json') as file:
        data  = json.load(file)      
        for item in data:                   
            bundle = f'{hbold("Название: ")}{item.get("name")}\n{hbold("Краткое описание бандла: ")}{item.get("description")}\n{hbold("Содержимое бандла: ")}{item.get("content")}\n{hbold("Количество: ")}{item.get("count")}\n{hbold("Стоимость: ")}{item.get("price")}\n{hbold("Продано: ")}{item.get("sold")}\n\n'
            bundle_list = bundle_list + bundle 
        
        await message.answer(bundle_list)   

    # получить стартовое время обновления json карточки с новыми бандлами 
    startTimejson = os.path.getmtime(r"json\bundle_info.json.")


    while(True):
        lastModify = os.path.getmtime(r"json\bundle_info.json")
        if(lastModify!=startTimejson):
            startTimejson = lastModify  
            new_bundle_alert = "Вышел новый бандл! 🧨 \n \n"

            with open(r'json\bundle_info_new.json',) as file:
                data1  = json.load(file)    
                for item in data1:                   
                    bundle = f'{hbold("Название: ")}{item.get("name")}\n{hbold("Краткое описание бандла: ")}{item.get("description")}\n{hbold("Содержимое бандла: ")}{item.get("content")}\n{hbold("Количество: ")}{item.get("count")}\n{hbold("Стоимость: ")}{item.get("price")}\n{hbold("Продано: ")}{item.get("sold")}\n{hbold("Ссылка: ")}{item.get("link")}\n\n'
                    new_bundle_alert = new_bundle_alert + bundle 
                # await message.answer(new_bundle_alert)   
                await bot.send_photo(message.chat.id, photo=item.get("img"), caption=new_bundle_alert)  
        await asyncio.sleep(3)                   

def main():
        executor.start_polling(dp, skip_updates=True)



if __name__=='__main__':
    main()
