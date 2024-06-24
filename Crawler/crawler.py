from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://localhost:5173/"

if __name__ == '__main__':

    # 開啟 Chrome 瀏覽器
    driver = webdriver.Chrome()


    # 創造一個 WebDriverWait 物件，等待時間設定為 5 秒
    Wait = WebDriverWait(driver, 5)


    # 連結到指定網址
    driver.get(url)                
    print("現在所在網址: ", url)


    # 透過 XPath 找到登入按鈕，並點擊
    loginButton = Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="登入"]')), "Find Login Button Error")
    print("點擊登入按鈕")
    loginButton.click()


    # 找到帳號、密碼輸入框，並輸入帳號、密碼
    print("現在所在網址: ", driver.current_url)
    loginAccount = Wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="account"]')), "Find Account Input Error")
    loginPassword = Wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')), "Find Password Input Error")
    myAccount = "Group1"
    myPassword = "cscamp1"
    print("輸入帳號: ", myAccount)
    loginAccount.send_keys("Group1")
    print("輸入密碼: ", myPassword)
    loginPassword.send_keys("cscamp1")

    signInButton = Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Sign in"]')), "Find Sign In Button Error")
    print("點擊 Sign in 按鈕")
    signInButton.click()


    # 等待 0.5 秒，確認是否登入成功
    time.sleep(0.5)
    print("現在所在網址: ", driver.current_url)
    print("預期網址: ", url + "my_ticket")
    if driver.current_url == url + "myticket": 
        print("登入成功")
    else:
        print("登入失敗")
        driver.close()
        exit()


    # 無限迴圈購票
    while True:
        # 回到首頁
        driver.get(url)
        print("現在所在網址: ", driver.current_url)
        

        # 透過 XPath 找到購票按鈕，並點擊
        targetXPATH = "//article[.//h2[text()='新手村']]//button"
        targetButton = Wait.until(EC.presence_of_element_located((By.XPATH, targetXPATH)), "Error finding target ticket")
        buyButton=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="我要買"]')), "我要買")
        print(buyButton.text)
        buyButton.click()


        nextStep=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="下一步"]')), "Error")
        print(nextStep.text)
        # nextStep=driver.find_elements(By.XPATH, '//button')
        nextStep.click()

        # driver.implicitly_wait(5)
        time.sleep(0.15) 
        input=Wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="輸入: "]')), "Error")
        print(input.text)
        input=input.text.split(' ')
        print(input[1])
        answerBoard=Wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')), "Error")
        answerBoard.send_keys(input[1])
        
        submitButton=Wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="確認答案，送出"]')), "Error")
        submitButton.click()


    time.sleep(1)
    driver.close()
