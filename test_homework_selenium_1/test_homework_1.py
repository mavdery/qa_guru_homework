import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

def test_01():

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        #web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Олег Гело")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("oleg@example.com")

        # CurrentAddress
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("тут. Адрес, 17")

        # PermanentAddress
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("там. Тоже Адрес, 19")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Находим каждый элемент внутри блока output
        name_result = result_box.find_element(By.ID, "name")
        email_result = result_box.find_element(By.ID, "email")
        current_address_result = result_box.find_element(By.ID, "currentAddress")
        permanent_address_result = result_box.find_element(By.ID, "permanentAddress")

        # Проверяем, что в каждом элементе появился введенный текст
        assert "Олег Гело" in name_result.text
        assert "oleg@example.com" in email_result.text
        assert "тут. Адрес, 17" in current_address_result.text
        assert "там. Тоже Адрес, 19" in permanent_address_result.text

        print("Тест успешно пройден!")


    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_02():

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        #web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("@nrt")

        # CurrentAddress
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("")

        # PermanentAddress
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert result_box.text == ""
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_03():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("dot@")

        # CurrentAddress
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("")

        # PermanentAddress
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert result_box.text == ""
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()
