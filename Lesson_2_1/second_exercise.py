from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots redio: ', robots_checked)
    assert robots_checked is None

    robot_check_box = browser.find_element(By.ID, 'robotCheckbox')
    robots_check_box_checked =  robot_check_box.get_attribute('checked')
    print('value of robots checkbox: ', robots_check_box_checked)
    assert robots_check_box_checked is None

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button_disabled = submit_button.get_attribute('disabled')
    print('submit button is', submit_button_disabled)
    assert submit_button_disabled is None

    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    submit_button_disabled = submit_button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", submit_button_disabled)
    assert submit_button_disabled is not None

finally:
# Закрываем браузер
    browser.quit()