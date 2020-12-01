import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os
from urllib import parse
import requests
import urllib.request


chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

clips_links = []
twitch_channel = ""

def init_driver():
    driver = webdriver.Chrome(chromedriver)
    driver.wait = WebDriverWait(driver, 5)
    return driver


def scrape(driver, n_images):
    for i in range(1, n_images + 1):
        try:
            if i % 3 == 0:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            content_a = driver.find_element_by_xpath(
                """/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{0}]/a/div/img""".format(i)).click()
            time.sleep(0.5)
            content = driver.find_element_by_xpath(
                """/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img""").get_attribute("src")
            clips_links.append(content)
        except:
            i += 1
            n_images += 1
            print("error")


def save_images(path, name_to_save):
    counter = 0
    for i in clips_links:
        counter += 1
        try:
            urllib.request.urlretrieve(str(i), f'{path}/{name_to_save}%d.png' % int(counter))
        except:
            print(f'Error to save: {i}')


def pages_loop(waifu_type, n_images, width, height, path, name_to_save):
    driver = init_driver()
    driver.set_window_size(2160, 800)
    search = f'{waifu_type} faces {width}x{height}'
    query_str = parse.urlencode({'': search})
    driver.get(f'https://www.google.com.co/search?hl=es&tbm=isch&q{query_str}')
    time.sleep(1)

    scrape(driver, n_images)
    save_images(path, name_to_save)
    driver.close()
    print(f"Total links: {len(clips_links)}")
