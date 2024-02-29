from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by   import By
import random
import time

options = Options()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def one_option_click(list):
    random = random.choice(list)
    q = driver.find_element(By.CSS_SELECTOR, f"#i{random} .AB7Lab")
    q.click()

n = 0
while (n < 10):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://docs.google.com/forms/d/1t3malcQ4eZctC4J65qOeY4Jw4ccCvv1Y_riOmK5-8Wg/viewform?fbclid=IwAR0k7YHK4Lq7BjxffMIQG-Y1zNnr3U4UsXrEhMzkbQHaTcX_luZs4aSWhrI&edit_requested=true")
    # print(driver.title)
    time.sleep(1)
    button1 = driver.find_element(By.CSS_SELECTOR, ".zo8FOc .NPEfkd")
    button1.click()

    one_option_click([5,8,11])
    one_option_click([18, 21])
    one_option_click([31, 34, 37, 40])
    one_option_click([47, 50])

    button2 = driver.find_element(By.XPATH, "//form[@id='mG61Hd']/div[2]/div/div[3]/div/div/div[2]/span/span")
    button2.click()

    one_option_click([5, 8])
    time.sleep(2)

    random_q6= random.sample([16, 19, 22, 25, 28], 3)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, f"#i{random_q6[0]} > .uHMk6b").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, f"#i{random_q6[1]} > .uHMk6b").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, f"#i{random_q6[2]} > .uHMk6b").click()

    random_q7= random.choice([1, 2, 3, 4, 5])
    if random_q7 != 1:
        q7 = driver.find_element(By.XPATH, f"//label[{ random_q7 }]/div[2]/div/div/div[3]/div")
        q7.click()
    else:
        q7 = driver.find_element(By.XPATH, f"//label/div[2]/div/div/div[3]/div")
        q7.click()

    button3 = driver.find_element(By.XPATH, f"//form[@id='mG61Hd']/div[2]/div/div[3]/div/div/div[2]/span/span")
    button3.click()

    one_option_click([5, 8, 11, 14, 17])

    random_q9= random.choice([28, 31, 34, 37])
    q9 = driver.find_element(By.CSS_SELECTOR, f"#i{random_q9} > .uHMk6b")
    q9.click()

    one_option_click([47,50 ])
    one_option_click([57, 60, 63, 66, 69, 72])

    q12 = driver.find_element(By.XPATH,"//form[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div" )
    q12.click()

    input = driver.find_element(By.XPATH, "//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div[2]/textarea")
    input.send_keys("Nothing more")

    submit = driver.find_element(By.XPATH, "//form[@id='mG61Hd']/div[2]/div/div[3]/div/div/div[2]/span")
    submit.click()

    driver.close()
    time.sleep(2)
    n+=1
