from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_xpath('//*[@id="cookie"]')

game_is_on = True

store = driver.find_elements_by_css_selector("#store div")
new_store = store[::-1]

def game():


while game_is_on:
    for n in range(150):
        cookie.click()

    print("Hello World")
    
    for thing in new_store:
        print(thing.get_attribute("id"))
        try:
            thing.click()
        except:
            pass
        else:
            game()
    