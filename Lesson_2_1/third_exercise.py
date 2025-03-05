from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_icon = browser.find_element(By.ID, 'treasure')
    treasure_icon_attribute = treasure_icon.get_attribute('valuex')

    y = calc(treasure_icon_attribute)
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    i_am_robot = browser.find_element(By.ID,'robotCheckbox')
    i_am_robot.click()

    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    submit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

# Даем время на просмотр результата
    time.sleep(5)

finally:
# Закрываем браузер
    browser.quit()