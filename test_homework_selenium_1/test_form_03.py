import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        # 3. Поиск элементов и заполнение полей
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Гоша Ашог")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("gosha@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "Гоша Ашог" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера
        driver.quit()