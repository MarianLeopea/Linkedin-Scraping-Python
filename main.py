from matplotlib.pyplot import close
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from csv import DictReader
import pickle
from selenium.common.exceptions import NoSuchElementException
import csv
from selenium.webdriver.support import expected_conditions as EC
from torch import layout
from findPageScrip import find_lincks_scrip, find_lincks
from pySimple import pySimple
 
# with  open("test1.csv","w",newline='', encoding="utf-8")
# writer = csv.writer(outfile)
# df = pd.DataFrame(columns=['title', 'addresse', 'phone', 'website', 'overview', 'specialties', 'industry', 'headquarters'])

with open("test.csv", "w", encoding="utf-8" ,newline='') as file:
    file.write("title, addresse, phone, web site, overview, specialties, industry, headquarters \n")


window = sg.Window("Linkedin scraping", pySimple(layout))
event, values = window.read()


def clear_input():
    for key in values:
        window[key]("")
    return None


address = values["address"]
password = values["password"]
search_keyword = values["Keyword"]
location = values["Location"]
nr_of_page = values["NrPages"]
# search_categories = values["Search_Categories"]

People = values["People"]
Companies = values["Companies"]
Jobs = values["Jobs"]
Groups = values["Groups"]
Posts = values["Posts"]
Schools = values["Schools"]
Events_key = values["Events"]
Courses = values["Courses"]
Services = values["Services"]


def login_cat(driver):
    elem = driver.find_element(By.XPATH, "/html/body/div[2]/main/p[1]/a")
    sleep(2)
    elem.send_keys(Keys.ENTER)
    sleep(3)

    elem = driver.find_element(By.XPATH, '//*[@id="username"]')
    elem.send_keys(address)
    sleep(3)
    elem = driver.find_element(By.XPATH, '//*[@id="password"]')
    elem.send_keys(password)
    sleep(3)
    elem = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    elem.send_keys(Keys.ENTER)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    sleep(3)
    elem = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    sleep(2)
    elem.clear()
    elem.send_keys(search_keyword)
    sleep(2)
    elem.send_keys(Keys.ENTER)
    sleep(3)


def search_cat(driver):
    if People:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Companies:
        elem =WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[2]/button')
            )
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Posts:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Jobs:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[4]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Groups:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[5]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Schools:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[6]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Events_key:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[7]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Courses:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[8]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    if Services:
        elem = driver.find_element(
            By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[9]/button'
        )
        elem.send_keys(Keys.ENTER)
        sleep(3)
    else:
        pass


def location_cat(driver):
    elem = driver.find_element(
        By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]'
    )

    elem.click()
    sleep(2)
    elem = driver.find_element(By.XPATH, '//input[@placeholder="Add a location"]')
    elem.click()
    sleep(2)
    elem.send_keys(location)
    sleep(3)
    elem.send_keys(Keys.DOWN)
    sleep(3)
    elem.send_keys(Keys.ENTER)
    #elem.click()
    sleep(4)
    elem = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/section/div/nav/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')
    elem.click()
    sleep(5)


def location_check_cat(driver):
    elem = driver.find_element(
        By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]'
    )
    sleep(2)
    elem.send_keys(Keys.ENTER)

    elem = driver.find_element(
        By.XPATH,
        '//*[@id="artdeco-hoverable-artdeco-gen-65"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p/span[1]',
    )
    sleep(2)
    elem.send_keys(Keys.ENTER)
    elem = driver.find_element(By.XPATH, '//*[@id="ember508"]')
    sleep(2)
    elem.send_keys(Keys.ENTER)

def next_page(driver):
    try:
        page_nr = []
        total_page = nr_of_page
        for x in range(1, total_page):
            page_nr = x + 1
            driver.get(f"https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101174742%22%5D&keywords={search_keyword}&origin=FACETED_SEARCH&page={page_nr}")
            sleep(3)
            find_lincks(driver)
    except:
        driver.close()


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    url = "https://www.linkedin.com/"
    driver.get(url)

    # loading the stored cookies
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        # adding the cookies to the session through webdriver instance
        driver.add_cookie(cookie)
    driver.get(url)
    login_cat(driver)
    sleep(3)
    search_cat(driver)
    sleep(3)
    location_cat(driver)
    find_lincks(driver)
    driver.refresh
    sleep(3)
    next_page(driver)
    sleep(5)
    driver.close()


while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Clear":
        clear_input()
    if event == "Submit":
        main()
        sleep(2)


window.close()
