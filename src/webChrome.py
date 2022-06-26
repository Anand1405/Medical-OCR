from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
from pathlib import Path

def webList(tablet):
    
    path = '../src/chromedriver'       

    opt=Options()
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")

    opt.add_experimental_option("prefs", { "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
        })

    driver=webdriver.Chrome(options=opt, executable_path=path)

    link = 'https://www.netmeds.com/catalogsearch/result?q={}'.format(tablet)

    driver.get(link)

    med_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//ol[@id="algolia_hits"]/li/div/div//div[@class="drug_c"]/a/div')))
    med_link.click()

    alternative = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="sub_drug"]/div/div[@class="drug_c"]/a/div')))

    alternative_name = alternative.text
    #print(alternative_name)

    alternative_price = driver.find_element_by_xpath('//div[@class="sub_drug"]/div/div[@class="pricebox"]/div/span').text
    #print(alternative_price)

    alternative_link = driver.find_element_by_xpath('//div[@class="sub_drug"]/div/div[@class="drug_c"]/a').get_attribute('href')
    #print(alternative_link)

    alternative.click()

    time.sleep(5)

    os.system('cls')

    return alternative_name, alternative_price, alternative_link

