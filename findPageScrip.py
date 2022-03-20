
from sqlite3 import DataError
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd


def find_lincks(driver):
    
    for i in range(10):
        elem = driver.find_elements(
            By.XPATH, '//*["@id=div"]//div[2]/div[1]/div[1]/div/span/span/a'
        )
        elem[i].click()
        sleep(4)
        if elem:
            find_lincks_scrip(driver)
            sleep(4)
            driver.back()
            sleep(4)
            driver.back()
            sleep(3)

templist = []

def find_lincks_scrip(driver):

    try: 
        sleep(4)
        elem = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.LINK_TEXT,
                        "About",
                    )
                )
        )
        elem.click()
        title = driver.find_element(
            By.XPATH,
            '//*["@id=main"]/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/h1/span'
        ).text
    except NoSuchElementException:
        title = "N/A"
        sleep(2)
    try:
        addresse = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[2]/div[1]/h3/div/p'
        ).text 
    except NoSuchElementException:
        addresse = "N/A"
        sleep(2)
    try:
        phone = driver.find_element(
            By.XPATH,
            '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/dl/dd[2]/a/span[1]'
        ).text 
    except NoSuchElementException:
        phone = "N/A"
        sleep(2)
    try:
        web_site = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/dl/dd[1]/a/span'
        ).text 
    except NoSuchElementException:
        web_site = "N/A"
        sleep(2)
    try:
        overview = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/p'
        ).text  
    except NoSuchElementException:
        overview = "N/A"
        sleep(2)
    try:
        specialties = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/dl/dd[7]'
        ).text   
    except NoSuchElementException:
        specialties = "N/A"
        sleep(2)
    try:
        industry = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/dl/dd[2]'
        ).text  
    except NoSuchElementException:
        industry = "N/A"
        sleep(2)
    try:
        headquarters = driver.find_element(
            By.XPATH, '//*["@id=main"]/div[2]/div/div[2]/div[1]/section/dl/dd[5]'
        ).text
    except NoSuchElementException:
        headquarters = "N/A"
        sleep(2)
    
    # Table_dict={ 
    #             'Title': [title],
    #             'Addresse' : [addresse], 
    #             'Phone ' : [phone ], 
    #             'Website' : [web_site], 
    #             'Overview' : [overview], 
    #             'Specialties': [specialties],
    #             'Industry': [industry], 
    #             'Headquarters' : [headquarters],
                     
    #   }
     
    # df = pd.DataFrame(Table_dict)

    # # df = pd.DataFrame(header=['Title', 'Addresse', 'Phone ', 'Website', 'Overview', 'Specialties', 'Industry', 'Headquarters' ], 
    # # column=[[title],[addresse],[phone ],[web_site],[overview],[specialties],[industry],[headquarters],] )
    # with  open("test1.csv","a"):
    #     df.to_csv('test1.csv', 'a', index = False ) 
    #         # driver.close()

    
    with open("test.csv", "a", encoding="utf-8" ,newline='') as file:
        
        # writer = csv.writer(file)
        # writer.writerow([title,  addresse,  phone,  web_site, overview,  specialties, industry,  headquarters])
        file.write(title + " ; " + addresse + " ; " + phone + " ; " + web_site + ";" + overview + " ; " + specialties + " ;" + industry + " ; " + headquarters + " ; \n") 



