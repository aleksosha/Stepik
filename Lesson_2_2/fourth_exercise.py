import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import re  # Для работы с регулярными выражениями

# Инициализация браузера
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

# Заполнение формы
browser.find_element(By.NAME, 'firstname').send_keys('Имя')
browser.find_element(By.NAME, 'lastname').send_keys('Фамилия')
browser.find_element(By.NAME, 'email').send_keys('email@example.com')

# Указываем путь к файлу
file_path = r'C:\Users\Sosha\file.txt'  # Убедитесь, что файл существует по этому пути

# Проверка наличия файла
if not os.path.exists(file_path):
    print(f"Файл {file_path} не существует. Создайте файл перед запуском.")
else:
    # Загрузка файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Ожидание, пока кнопка не станет доступной
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Нажатие на кнопку submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Обработка alert
    WebDriverWait(browser, 10).until(EC.alert_is_present())  # Ожидание появления alert
    alert = Alert(browser)
    alert_text = alert.text  # Извлекаем текст из alert

    # Используем регулярное выражение для извлечения числа
    match = re.search(r"[-+]?\d*\.\d+|\d+", alert_text)
    if match:
        number = match.group(0)  # Извлекаем найденное число
        print(f"Извлеченное число: {number}")
    else:
        print("Число не найдено в тексте алерта.")

    # Принятие alert
    alert.accept()

# Закрытие браузера
browser.quit()
