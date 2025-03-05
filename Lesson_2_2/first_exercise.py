import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def solve_sum_select(url):
    # Открываем браузер
    driver = webdriver.Chrome()
    driver.get(url)
try:


    num1 = int(driver.find_element(By.ID, 'num1').text)
    num2 = int(driver.find_element(By.ID, 'num2').text)
    result = str(num1 + num2)
    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(result)

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)  # Даем время посмотреть результат и закрываем браузер
    driver.quit()

# Запускаем для первой и второй страницы
solve_sum_select("https://suninjuly.github.io/selects1.html")
solve_sum_select("https://suninjuly.github.io/selects2.html")