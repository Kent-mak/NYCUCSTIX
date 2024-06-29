# -------------- Step 0: import 套件 -------------- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SolveTask import solve_task

# -------------- Step 1: 前置作業 -------------- 
url = "http://cstix.nctucsunion.me/"

if __name__ == '__main__':
    
    # 開啟 Chrome 瀏覽器
    driver = webdriver.Chrome()


    # 創造一個 WebDriverWait 物件，等待時間設定為 5 秒
    Wait = WebDriverWait(driver, 5)


    # 連結到指定網址
    driver.get(url)
    print("回到首頁: ", url)


    # -------------- Step 2: 登入 -------------- 
    # TODO: 透過 XPath 找到登入按鈕，並點擊
    loginButtonXPATH = '//button[text()="登入"]'
    loginButton = Wait.until(EC.presence_of_element_located((By.XPATH, loginButtonXPATH)), "Find Login Button Error")
    originalURL = driver.current_url
    print("點擊登入按鈕")
    loginButton.click()
    Wait.until(EC.url_changes(originalURL), "Not going to login page")


    # TODO: 透過 XPath 找到帳號、密碼輸入框
    print("現在所在網址: ", driver.current_url)
    loginAccountXPath = "___(?)___"
    loginPasswordXPath = "___(?)___"
    loginAccount = Wait.until(EC.presence_of_element_located((By.XPATH, loginAccountXPath)), "Find Account Input Error")
    loginPassword = Wait.until(EC.presence_of_element_located((By.XPATH, loginPasswordXPath)), "Find Password Input Error")
    
    # TODO: 填入帳號並送出
    myAccount = "___(?)___"  # 第一組是 Group1，以此類推
    # 這裡記得要送出帳號喔! 
    # HINT: send_keys()

    print("輸入帳號: ", myAccount)
    
    # TODO: 填入密碼並送出
    myPassword = "___(?)___"
    # 這裡記得要送出密碼喔! 
    # HINT: send_keys()

    print("輸入密碼: ", myPassword)


    # TODO: 透過 XPath 找到"Sign in"按鈕
    signInButtonXPATH = "___(?)___"
    signInButton = Wait.until(EC.presence_of_element_located((By.XPATH, signInButtonXPATH)), "Find Sign In Button Error")
    print("點擊 Sign in 按鈕")
    originalURL = driver.current_url
    # 點擊"Sign in"按鈕，並確認有重導向到我的票券頁面
    signInButton.click()
    Wait.until(EC.url_changes(originalURL), "Not going to myticket page")


    # -------------- Step 3: 購票 --------------
    print("-----------------------------------")
    # 回到首頁
    originalURL = driver.current_url
    driver.get(url)
    Wait.until(EC.url_changes(originalURL), "Not going to home page")
    print("回到首頁: ", driver.current_url)
    

    # TODO: 透過 XPath 找到"我要買"按鈕
    targetXPATH = "//article[.//h2[text()='___(?)___']]//button"
    targetButton = Wait.until(EC.presence_of_element_located((By.XPATH, targetXPATH)), "Error finding target ticket")
    originalURL = driver.current_url
    print("點擊購票按鈕: ", targetButton.text)
    # TODO: 點擊"我要買"按鈕
    
    Wait.until(EC.url_changes(originalURL), "Not going to ticket page")
    print("點擊我要買後的網址: ", driver.current_url)


    # TODO: 透過 XPath 找到"下一步"按鈕
    nextStepXPATH = "___(?)___"
    nextStep = Wait.until(EC.presence_of_element_located((By.XPATH, nextStepXPATH)), "Error finding next step button")
    print("點擊下一步: ", nextStep.text)
    originalURL = driver.current_url
    # 點擊"下一步"按鈕
    nextStep.click()
    Wait.until(EC.url_changes(originalURL), "Not going to next step (problem page)")
    print("點擊下一步後的網址: ", driver.current_url)

    # -------------- Step 4: 驗證 --------------
    # # TODO: 透過 XPath 找到題目 ID
    # problemTitleXPATH = '___(?)___'
    # problemTitle = Wait.until(EC.presence_of_element_located\
    #                         ((By.XPATH, problemTitleXPATH)), "Error finding problem-title")
    
    # # TODO: (Hint 字串處理 split)
    # problemID = problemTitle.text.'___(?)___'
    # problemID = int(problemID)
    
    # TODO: 透過 XPath 找到輸入值數字
    inputXPATH = "___(?)___"
    input = Wait.until(EC.presence_of_element_located((By.XPATH, inputXPATH)), "Error finding input box")
    # TODO: 找到輸入數字 (Hint: 字串處理split)
    inputNum = int("___(?)___")
    print("輸入數字: ", inputNum)
    

    # answer = solve_task("___(?)___", inputNum)


    # TODO: 透過 XPath 找到答案輸入框
    answerBoardXPATH = "___(?)___"
    answerBoard=Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
    # TODO: 填入答案 (HINT: send_keys())
    
    print("填入輸出答案: ", "___(?)___")


    # TODO: 透過 XPath 找到"確認答案，送出"按鈕
    submitButtonXPATH = "___(?)___"
    submitButton=Wait.until(EC.presence_of_element_located((By.XPATH, submitButtonXPATH)), "Error finding submit button")
    print("點擊確認答案，送出")
    originalURL = driver.current_url
    # 點擊"確認答案，送出"按鈕
    submitButton.click()
    Wait.until(EC.url_changes(originalURL), "Not going to confirmation page")
    print("送出答案後的網址: ", driver.current_url) 


    if(driver.current_url == url + "confirmed"):
        print("購票成功")
    else:
        print("購票失敗")