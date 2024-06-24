import requests
# from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
url="http://localhost:5173/"

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    Wait=WebDriverWait(driver, 5)
    login=driver.find_elements(By.XPATH, '//button')
    loginButton=login[1]
    login[1].click()

    inputs=driver.find_elements(By.XPATH, '//input')
    inputs[0].send_keys('Kent')
    inputs[1].send_keys('kent')

    signInButton=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Sign in"]')), "Error")
    signInButton.click()
    time.sleep(3)
    # driver.implicitly_wait(5) 
    # tiky=driver.find_element(By.XPATH, '//div[text()="活動一覽"]')
    # tiky.click()
    while True:
        
        driver.get(url)
        # tiky=Wait.until(EC.presence_of_element_located((By.XPATH, '//nav/div/div[2]')), "Error")
        # tiky=driver.find_element(By.XPATH, '//div[text()="活動一覽"]')
        # tiky.click()
        
        print(driver.current_url)
        # driver.implicitly_wait(5) 
        buyButton=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="我要買"]')), "我要買")
        print(buyButton.text)
        buyButton.click()

        # driver.implicitly_wait(5) 
        nextStep=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="下一步"]')), "Error")
        print(nextStep.text)
        # nextStep=driver.find_elements(By.XPATH, '//button')
        nextStep.click()

        # driver.implicitly_wait(5)
        # TODO: Get problem ID
        time.sleep(0.15) 
        input=Wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="輸入: "]')), "Error")
        print(input.text)
        input=input.text.split(' ')
        print(input[1])
        answerBoard=Wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')), "Error")

        # TODO: ans
        answerBoard.send_keys(input[1])
        
        submitButton=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="確認答案，送出"]')), "Error")
        submitButton.click()


    time.sleep(1)
    driver.close()