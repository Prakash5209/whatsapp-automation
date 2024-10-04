from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd 
import time 
import os

options = webdriver.FirefoxOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

driver = webdriver.Firefox(options=options)

df = pd.read_excel('data.xlsx')
filter_df = df.iloc[0:,:]

driver.get("https://web.whatsapp.com/")

input('Press Enter after logging in')

for index,row in filter_df.iterrows():
    new_chat_button = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@data-icon="new-chat-outline"]'))
    )
    time.sleep(1)
    new_chat_button.click()
    print('new_chat_button_clicked')
    time.sleep(1)
    new_chat_search = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.x1hx0egp.x6ikm8r.x1odjw0f.x6prxxf.x1k6rcq7.x1whj5v'))
    )

    new_chat_search.clear()

    for num in str(row.Number):
        new_chat_search.send_keys(num)

    print('new_chat_search_send_keys')
    time.sleep(1)

    try:
        search_profile = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'_ak8q'))
        )
        time.sleep(2)
        search_profile.click()
        if row.Location and os.path.exists(os.path.abspath(row.Location)):
            file_input_div = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//input[@type="file"]'))
            )
            print('finding input field with type = file')

            print('loading image')
            file_input_div.send_keys(os.path.abspath(row.Location))

            send_btn = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'.x78zum5.x6s0dn4.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1f6kntn.xk50ysn.x7o08j2.xtvhhri.x1rluvsa.x14yjl9h.xudhj91.x18nykt9.xww2gxu.xu306ak.x12s1jxh.xkdsq27.xwwtwea.x1gfkgh9.x1247r65.xng8ra'))
            )
            send_btn.click()
            print('image sent')
            print()
            print('data updated')
            filter_df.at[index,'status'] = 1
            print('status 1 which means sent')
            print()
            print(f'index {index} success'.center(25,'-'))
            time.sleep(1)
        else:
            filter_df.at[index,'status'] = None
            print(f'image location not found: index {index}')
            print('failed')
            print('skipping and going home')
    except:
        print('searched profile not found')
        print('failed')
        print('skipping and going home')
        reset_to_home = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.x1okw0bk.x16dsc37.x1ypdohk.xeq5yr9.xfect85'))
        )
        reset_to_home.click()

filter_df.to_excel('data.xlsx',index=False)

input('enter to terminate the program')
print('browser closing now')
time.sleep(3)
driver.quit()
