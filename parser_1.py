from asyncio import wait
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import json
# from fake_useragent import UserAgent
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

# аргументы для webdriver
ua_arr = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/571.37 (KHTML, like Gecko) Chrome/104.0.2153 Safari/537.36',
          'Mozilla/5.0 (Linux; Android 10; AKA-L29; HMSCore 6.12.2.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.311 Mobile Safari/537.36',
          'Mozilla/5.0 (Linux; arm; Android 13; 22101316UG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.83 YaBrowser/23.9.5.83.00 SA/3 Mobile Safari/537.36',
          'Mozilla/5.0 (Linux; Android 14; M2012K11C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
          'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition Yx GX 03)',
          'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.98',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 SberBrowser/9.2.63.1',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
          'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
          'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0',
          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3',
          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3',
          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
          'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0']

options =webdriver.ChromeOptions()


options.add_argument('--headless')  
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f"useragent={ua_arr[random.randint(0, len(ua_arr) - 1)]}")

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    'source':'''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
'''
})

result = []
bundles = []
json_res = []
old_item_list = []
new_item_list = []
new_bundle_item_list = []
try:
    while True:

        # парсинг
        driver.maximize_window()
        driver.get("https://www.humblebundle.com/")
        driver.implicitly_wait(5)

        # получить секцию с бандлами
        m = driver.find_element(By.CSS_SELECTOR,'#mm-0 > div.page-wrap > div.base-main-wrapper > div.inner-main-wrapper > section > div.humble-home.js-humble-home > div > div:nth-child(4)')

        bundles = m.find_elements(By.CLASS_NAME, 'js-tile-holder')
        for item in bundles:

            # вытянуть название бандла
            bundle_name = item.find_element(By.CLASS_NAME,'name')
            bundle_name_html = driver.execute_script("return arguments[0].outerHTML;", bundle_name)
            bundle_name_res = re.sub(r"<[^>]+>", "", bundle_name_html, flags=re.S)

            # вытянуть краткое описание бандла
            bundle_description = item.find_element(By.CLASS_NAME,'short-marketing-blurb')
            bundle_description_html = driver.execute_script("return arguments[0].outerHTML;", bundle_description)
            bundle_description_res = re.sub(r"<[^>]+>", "", bundle_description_html, flags=re.S)

            # вытянуть содержимое бандла 
            bundle_content = item.find_element(By.CLASS_NAME,'marketing-blurb')
            bundle_content_html = driver.execute_script("return arguments[0].outerHTML;", bundle_content)
            bundle_content_res = re.sub(r"<[^>]+>", "", bundle_content_html, flags=re.S)

            # вытянуть доп информацию 
            bundle_highlights = item.find_element(By.CLASS_NAME,'highlights')
            bundle_highlights_html = driver.execute_script("return arguments[0].outerHTML;", bundle_highlights)
            bundle_highlights_res = re.sub(r"<[^>]+>", "", bundle_highlights_html, flags=re.S)

            bundle_highlights_arr = bundle_highlights_res.split('\n  \n      ')

            bundle_price = re.sub(r"\b Value\b", "", bundle_highlights_arr[2], flags=re.S)
            bundle_sold = re.sub(r"\n  \n    ", "", bundle_highlights_arr[3], flags=re.S)

            # вытянуть тип бандла 
            bundle_type = item.find_element(By.CLASS_NAME,'full-tile-view')
            attribute_value = bundle_type.get_attribute("href")
            bundle_type_name = re.findall(r"(?i)(games|software|books)", attribute_value)

            # вытянуть ссылку на картинку бандла 
            bundle_img = item.find_element(By.TAG_NAME,"img")
            bundle_img_value = bundle_img.get_attribute("data-lazy")

            # вытянуть ссылку на страницу бандла 
            bundle_link = item.find_element(By.CLASS_NAME,"full-tile-view")
            bundle_link_value = bundle_link.get_attribute("href")

            result.append(
                {
                    'name': bundle_name_res,
                    'description': bundle_description_res,
                    'content': bundle_content_res,
                    'count': bundle_highlights_arr[1],
                    'price': bundle_price,
                    'sold': bundle_sold,
                    'type': bundle_type_name[0],
                    'img': bundle_img_value,
                    'link': bundle_link_value
                }
            )

        # сравнение новой информации с имеющиеся 

            # записать названия бандлов в словари, новую информацию берет из результатов парсинга, старую с json

        with open(r'json\bundle_info.json') as file:
            data  = json.load(file)      
            for item in data:          
                old_item_list.append(item)
        number_of_old_item = len(old_item_list)
        for item in result:   
            if item['type'] == 'software':       
                new_item_list.append(item)                
        number_of_new_item = len(new_item_list)

        # если появились новые бандлы, обновить информацию в json + записать информацию в json для новых бандлов
        if (number_of_old_item == number_of_new_item):
            print('новых бандлов нет')  
        else:
            print('вышли новые бандлы!')  

            
            # запись новых бандлов в отдельный json
            for new_item in new_item_list:
                for old_item in old_item_list:
                    if new_item['name'] == old_item['name']:
                        print('ключ есть')
                    else:
                        print('ключа нет')
                        new_bundle_item_list.append(new_item)
                        with open(r"json\bundle_info_new.json", 'w', encoding='utf-8') as file:
                            json.dump(new_bundle_item_list, file, ensure_ascii=False, indent=2)

            # обновить данные в главном json 
            for item in result:
                if item['type'] == 'software':
                    json_res.append(item) 
            with open(r"json\bundle_info.json", 'w', encoding='utf-8') as file:
                json.dump(json_res, file, ensure_ascii=False, indent=2)
        
        # очистить словари
        json_res = []
        result = []
        old_item_list = []
        new_item_list = []
        new_bundle_item_list = []
        print('['+str(datetime.now())+'] информация обновлена')
        time.sleep(60)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    