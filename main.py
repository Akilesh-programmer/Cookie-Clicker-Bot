from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_xpath('//*[@id="cookie"]')

game_is_on = True



def game():
    store = driver.find_elements_by_css_selector("#store div")
    new_store = store[::-1]
    for n in range(150):
        cookie.click()

    print("Hello World")
    
    for thing in new_store:
        try:
            thing.click()
        except:
            print("*")
            pass
            

time_ran = 0
while game_is_on:
    time_ran += 1
    game()
    if time_ran == 60:
        game_is_on = False
        cookies_per_second = driver.find_element_by_xpath('//*[@id="cps"]')
        print(cookies_per_second.text)
    