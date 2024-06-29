# -------------- Step 0: import 套件 -------------- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from SolveTask import solve_task
 
 
url = "http://127.0.0.1:3000/"
 
# -------------- Step 1: 前置 --------------
def init_driver():
    
    global driver
    global Wait
    
    # 開啟 Chrome 瀏覽器
    driver = webdriver.Chrome()
    
    # 創造一個 WebDriverWait 物件，等待時間設定為 5 秒
    Wait = WebDriverWait(driver, 5)
    
    # 連結到指定網址
    driver.get(url)
 
 
# -------------- Step 2: 登入 -------------- 
def click_login_button():
    ''' 
    TODO: 透過 XPath 找到登入按鈕，並點擊
    '''
 
    loginButtonXPATH = '//button[text()="登入"]'
    loginButton = Wait.until(EC.presence_of_element_located((By.XPATH, loginButtonXPATH)), "Find Login Button Error")
    originalURL = driver.current_url
    loginButton.click() # 點擊登入按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to login page")
    time.sleep(1.5)
 
 
def fill_in_info():
    '''
    TODO: 找到帳號、密碼輸入框，並輸入帳號密碼 
    '''
 
    # raise NotImplementedError("還沒找到帳號密碼輸入框位置")
    loginAccountXPath = '//input[@id="account"]'     # 找到帳號輸入框的 XPath
    loginPasswordXPath = '//input[@id="password"]'    # 找到密碼輸入框的 XPath
    loginAccount = Wait.until(EC.presence_of_element_located((By.XPATH, loginAccountXPath)), "Find Account Input Error")
    loginPassword = Wait.until(EC.presence_of_element_located((By.XPATH, loginPasswordXPath)), "Find Password Input Error")
    
    # raise NotImplementedError("還沒填寫登入資訊")
    myAccount = 'Test'  # 第一組是 Group1，以此類推
    # Hint: send_keys()
    loginAccount.send_keys(myAccount)
    
    myPassword = 'testuser'
    # HINT: send_keys()
    loginPassword.send_keys(myPassword)
    time.sleep(1.5)
 
 
def click_sign_in_button():
    '''
    TODO: 透過 XPath 找到"Sign in"按鈕
    '''
    # raise NotImplementedError("還沒找到 Sign in 按鈕位置")
    signInButtonXPATH = '//button[text()="Sign in"]'
    signInButton = Wait.until(EC.presence_of_element_located((By.XPATH, signInButtonXPATH)), "Find Sign In Button Error")
    originalURL = driver.current_url
    signInButton.click() # 點擊"Sign in"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to myticket page") #確認有重導向到我的票券頁面
    time.sleep(1.5)
    
 
# -------------- Step 3: 購票 -------------- 
def go_to_home_page():
    '''
    回到首頁
    '''
    originalURL = driver.current_url
    driver.get(url)
    Wait.until(EC.url_changes(originalURL), "Not going to home page")
    time.sleep(1.5)
 
 
def click_vote_button():
    '''
    TODO: 透過 XPath 找到"投票"按鈕
    '''
    # raise NotImplementedError("還沒點擊投票按鈕位置")
    targetXPATH = '//article[.//h2[text()="idol 2"]]//button'
    targetButton = Wait.until(EC.presence_of_element_located((By.XPATH, targetXPATH)), "Error finding target ticket")
    originalURL = driver.current_url
    targetButton.click() # 點擊"投票"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to ticket page")
    time.sleep(1.5)
 
 
def click_next_step_button():
    '''
    TODO: 透過 XPath 找到"下一步"按鈕 
    '''
    # raise NotImplementedError("還沒點擊下一步按鈕位置")
    nextStepXPATH = '//button[text()="下一步"]'
    nextStep = Wait.until(EC.presence_of_element_located((By.XPATH, nextStepXPATH)), "Error finding next step button")
    originalURL = driver.current_url
    nextStep.click()  # 點擊"下一步"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to next step (problem page)")
    time.sleep(1.5)
 
 
 
def fill_in_answer():
    '''
    TODO: 透過 XPath 找到輸入值數字，並填入答案
    '''
    # raise NotImplementedError("還沒找到輸入值數字")
    inputNumXPATH = '//div[contains(@class, "input")]'
    inputBox = Wait.until(EC.presence_of_element_located((By.XPATH, inputNumXPATH)), "Error finding input box")
    # Hint: 字串處理 split
    inputNum = int(inputBox.text.split('\n')[1])
 
    # raise NotImplementedError("還沒找到答案輸入框位置")
    answerBoardXPATH = '//textarea'
    answerBoard = Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
    # HINT: send_keys()
    answerBoard.send_keys(inputNum)
    time.sleep(1.5)
 
def click_submit_button():
    '''
    TODO: 透過 XPath 找到"確認答案，送出"按鈕
    '''
    # raise NotImplementedError("還沒點擊送出按鈕位置")
    submitButtonXPATH = '//button[text()="確認答案，送出"]'
    submitButton = Wait.until(EC.presence_of_element_located((By.XPATH, submitButtonXPATH)), "Error finding submit button")
    originalURL = driver.current_url
    submitButton.click() # 點擊"確認答案，送出"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to confirmation page")
    time.sleep(1.5)
 
    if(driver.current_url == url + "confirmed"):
        print("購票成功")
    else:
        print("購票失敗")
 
 
def solve_problem():
    '''
    TODO: 透過 XPath 找到題目 ID, 並解題
    ''' 
    # raise NotImplementedError("還沒破解挑戰賽 加油")
    problemTitleXPATH = "//div[contains(@class, 'problem-title')]"
    problemTitle = Wait.until(EC.presence_of_element_located((By.XPATH, problemTitleXPATH)), "Error finding problem-title")
    # Hint: problemTitle.text + 字串處理 split
    problemID = problemTitle.text.split(' ')[1]
    problemID = int(problemID)
    
 
    inputNumXPATH = "//div[contains(@class, 'input')]"
    inputBox = Wait.until(EC.presence_of_element_located((By.XPATH, inputNumXPATH)), "Error finding input box")
    # Hint: 字串處理 split
    inputNum = int(inputBox.text.split('\n')[1])
    
 
    answer = solve_task(problemID, inputNum)
 
    answerBoardXPATH = '//textarea'
    answerBoard = Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
    # HINT: send_keys()
    answerBoard.send_keys(answer)
    time.sleep(1.5)
 
    if(driver.current_url == url + "confirmed"):
        print("購票成功")
    else:
        print("購票失敗")
 
if __name__ == '__main__':
 
    # -------------- Step 1: 前置 --------------
    init_driver()
 
    # -------------- Step 2: 登入 --------------
    click_login_button()
    fill_in_info()
    click_sign_in_button()
 
    while True:
        # -------------- Step 3: 購票 --------------
        go_to_home_page()
        click_vote_button()
        click_next_step_button()
 
        # -------------- Step 4: 解題 --------------
        # fill_in_answer()    # 在新手村時使用 
        solve_problem()   # 在挑戰賽時使用
        click_submit_button()