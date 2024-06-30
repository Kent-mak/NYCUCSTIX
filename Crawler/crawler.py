# -------------- Step 0: import 套件 -------------- 
from selenium import webdriver  # 引入 Selenium 的 webdriver 模組
from selenium.webdriver.common.by import By  # 引入 Selenium 的定位方式 By
from selenium.webdriver.support.wait import WebDriverWait  # 引入 Selenium 的等待模組 WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 引入 Selenium 的預期條件模組 as EC
import time  # 引入 time 模組
from SolveTask import solve_task  # 從 SolveTask 引入 solve_task 函數


url = "http://cstix.nctucsunion.me/"


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

    # 等待並確認登入按鈕出現在頁面上，若超時則拋出錯誤訊息
    loginButton = Wait.until(EC.presence_of_element_located((By.XPATH, loginButtonXPATH)), "Find Login Button Error") 
    
    # 保存當前頁面的 URL
    originalURL = driver.current_url

    # 點擊登入按鈕
    loginButton.click() 

     # 等待 URL 變化，確認頁面已跳轉到登入頁面，若無變化則拋出錯誤訊息
    Wait.until(EC.url_changes(originalURL), "Not going to login page") 
    
    # 暫停1.5秒，讓頁面有充足時間載入
    time.sleep(1.5) 


def fill_in_info():
    '''
    TODO: 找到帳號、密碼輸入框，並輸入帳號密碼 
    '''

    raise NotImplementedError("還沒找到帳號密碼輸入框位置")
    loginAccountXPath = '___(?)___'     # 找到帳號輸入框的 XPath
    loginPasswordXPath = '___(?)___'    # 找到密碼輸入框的 XPath
    loginAccount = Wait.until(EC.presence_of_element_located((By.XPATH, loginAccountXPath)), "Find Account Input Error")
    loginPassword = Wait.until(EC.presence_of_element_located((By.XPATH, loginPasswordXPath)), "Find Password Input Error")
    
    raise NotImplementedError("還沒填寫登入資訊")
    myAccount = '___(?)___'  # 第一組是 Group1，以此類推
    # Hint: send_keys()
    '_________(?)_________'
    
    myPassword = '___(?)___'
    # HINT: send_keys()
    '_________(?)_________'
    time.sleep(1.5)


def click_sign_in_button():
    '''
    TODO: 透過 XPath 找到"Sign in"按鈕
    '''
    raise NotImplementedError("還沒找到 Sign in 按鈕位置")
    signInButtonXPATH = '___(?)___'
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
    raise NotImplementedError("還沒點擊投票按鈕位置")
    targetXPATH = '//article[.//h2[text()="___(?)___"]]//button'
    targetButton = Wait.until(EC.presence_of_element_located((By.XPATH, targetXPATH)), "Error finding target ticket")
    originalURL = driver.current_url
    '_________(?)_________' # 點擊"投票"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to ticket page")
    time.sleep(1.5)


def click_next_step_button():
    '''
    TODO: 透過 XPath 找到"下一步"按鈕 
    '''
    raise NotImplementedError("還沒點擊下一步按鈕位置")
    nextStepXPATH = '___(?)___'
    nextStep = Wait.until(EC.presence_of_element_located((By.XPATH, nextStepXPATH)), "Error finding next step button")
    originalURL = driver.current_url
    nextStep.click()  # 點擊"下一步"按鈕
    Wait.until(EC.url_changes(originalURL), "Not going to next step (problem page)")
    time.sleep(1.5)


# -------------- Step 4: 驗證 --------------
def fill_in_answer():
    '''
    TODO: 透過 XPath 找到輸入值數字，並填入答案
    '''
    raise NotImplementedError("還沒找到輸入值數字")
    inputNumXPATH = '___(?)___'
    inputBox = Wait.until(EC.presence_of_element_located((By.XPATH, inputNumXPATH)), "Error finding input box")
    # Hint: 字串處理 split
    inputNum = int("___(?)___")

    raise NotImplementedError("還沒找到答案輸入框位置")
    answerBoardXPATH = '___(?)___'
    answerBoard = Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
    # HINT: send_keys()
    '_________(?)_________'
    time.sleep(1.5)


def click_submit_button():
    '''
    TODO: 透過 XPath 找到"確認答案，送出"按鈕
    '''
    raise NotImplementedError("還沒點擊送出按鈕位置")
    submitButtonXPATH = '___(?)___'
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
    raise NotImplementedError("還沒破解挑戰賽 加油")
    problemTitleXPATH = '___(?)___'
    problemTitle = Wait.until(EC.presence_of_element_located((By.XPATH, problemTitleXPATH)), "Error finding problem-title")
    # Hint: problemTitle.text + 字串處理 split
    problemID = '_______(?)_______'
    problemID = int(problemID)
    

    inputNumXPATH = '___(?)___'
    inputBox = Wait.until(EC.presence_of_element_located((By.XPATH, inputNumXPATH)), "Error finding input box")
    # Hint: 字串處理 split
    inputNum = int("___(?)___")
    

    answer = solve_task("___(?)___", inputNum)

    answerBoardXPATH = '___(?)___'
    answerBoard = Wait.until(EC.presence_of_element_located((By.XPATH, answerBoardXPATH)), "Error finding answer board")
    # HINT: send_keys()
    '_________(?)_________'
    time.sleep(1.5)



if __name__ == '__main__':

    # -------------- Step 1: 前置 --------------
    init_driver()

    # -------------- Step 2: 登入 --------------
    click_login_button()
    fill_in_info()
    click_sign_in_button()

    # -------------- Step 3: 購票 --------------
    go_to_home_page()
    click_vote_button()
    click_next_step_button()

    # -------------- Step 4: 驗證 --------------
    fill_in_answer()    # 在新手村時使用 
    # solve_problem()   # 在挑戰賽時使用
    click_submit_button()

