from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

game_is_on = True

while game_is_on:
    for n in range(200):
        cookie.click()
    