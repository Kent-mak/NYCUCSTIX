from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SolveTask import solve_task
import time

url = "http://cstix.nctucsunion.me"

if __name__ == '__main__':
    
    # 開啟 Chrome 瀏覽器
    driver = webdriver.Chrome()


    # 創造一個 WebDriverWait 物件，等待時間設定為 5 秒
    Wait = WebDriverWait(driver, 5)


    # 連結到指定網址
    driver.get(url)
    print("回到首頁: ", url)


    # 透過 XPath 找到登入按鈕，並點擊
    loginButtonXPATH = '//button[text()="登入"]'
    loginButton = Wait.until(EC.presence_of_element_located((By.XPATH, loginButtonXPATH)), "Find Login Button Error")
    originalURL = driver.current_url
    print("點擊登入按鈕")
    loginButton.click()
    Wait.until(EC.url_changes(originalURL), "Not going to login page")


    # 找到帳號、密碼輸入框，並輸入帳號、密碼
    print("現在所在網址: ", driver.current_url)
    loginAccountXPath = '//input[@id="account"]'
    loginPasswordXPath = '//input[@id="password"]'
    loginAccount = Wait.until(EC.presence_of_element_located((By.XPATH, loginAccountXPath)), "Find Account Input Error")
    loginPassword = Wait.until(EC.presence_of_element_located((By.XPATH, loginPasswordXPath)), "Find Password Input Error")
    myAccount = "Test"
    myPassword = "testuser"
    loginAccount.send_keys(myAccount)
    print("輸入帳號: ", myAccount)
    loginPassword.send_keys(myPassword)
    print("輸入密碼: ", myPassword)


    # 透過 XPath 找到登入按鈕，並點擊，確認有重導向到我的票券頁面
    signInButtonXPATH = '//button[text()="Sign in"]'
    signInButton = Wait.until(EC.presence_of_element_located((By.XPATH, signInButtonXPATH)), "Find Sign In Button Error")
    print("點擊 Sign in 按鈕")
    originalURL = driver.current_url
    signInButton.click()
    Wait.until(EC.url_changes(originalURL), "Not going to myticket page")


    # 無限迴圈購票
    while True:
        print("-----------------------------------")
        # 回到首頁
        originalURL = driver.current_url
        driver.get(url)
        Wait.until(EC.url_changes(originalURL), "Not going to home page")
        print("回到首頁: ", driver.current_url)
        

        # 透過 XPath 找到購票按鈕，並點擊
        targetXPATH = "//article[.//h2[text()='挑戰賽']]//button"
        targetButton = Wait.until(EC.presence_of_element_located((By.XPATH, targetXPATH)), "Error finding target ticket")
        originalURL = driver.current_url
        print("點擊購票按鈕: ", targetButton.text)
        targetButton.click()
        Wait.until(EC.url_changes(originalURL), "Not going to ticket page")
        print("點擊我要買後的網址: ", driver.current_url)


        # 透過 XPath 找到下一步按鈕，並點擊
        nextStepXPATH = '//button[text()="下一步"]'
        nextStep=Wait.until(EC.presence_of_element_located((By.XPATH, nextStepXPATH)), "Error finding next step button")
        print("點擊下一步: ", nextStep.text)
        originalURL = driver.current_url
        nextStep.click()
        Wait.until(EC.url_changes(originalURL), "Not going to next step (problem page)")
        print("點擊下一步後的網址: ", driver.current_url)


        # 透過 XPath 找到題目 ID
        problemTitleXPATH = "//div[contains(@class, 'problem-title')]"
        problemTitle = Wait.until(EC.presence_of_element_located((By.XPATH, problemTitleXPATH)), "Error finding problem-title")
        print(problemTitle.text)
        problemID = problemTitle.text.split(' ')[1]
        problemID = int(problemID)
        print("問題編號: ", problemID)


        # 透過 XPath 找到輸入數字
        inputNumXPATH = "//div[contains(@class, 'input')]"
        inputNum = Wait.until(EC.presence_of_element_located((By.XPATH, inputNumXPATH)), "Error finding input number")
        inputNum = int(inputNum.text.split('\n')[1])
        print("輸入數字: ", inputNum)


        answer = solve_task(problemID, inputNum)
        

        # 透過 XPath 找到答案輸入框，並輸入答案
        answerBoardXPATH = '//textarea'
        answerBoard = Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
        answerBoard.send_keys(answer)
        print("填入輸出答案: ", answer)


        # 透過 XPath 找到確認答案，送出按鈕，並點擊 
        submitButtonXPATH = '//button[text()="確認答案，送出"]'
        submitButton=Wait.until(EC.presence_of_element_located((By.XPATH, submitButtonXPATH)), "Error finding submit button")
        print("點擊確認答案，送出")
        originalURL = driver.current_url
        submitButton.click()
        Wait.until(EC.url_changes(originalURL), "Not going to confirmation page")
        print("送出答案後的網址: ", driver.current_url) 

        if(driver.current_url == url + "/confirmed"):
            print("購票成功")
        else:
            print("購票失敗")
            break