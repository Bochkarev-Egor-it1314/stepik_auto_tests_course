from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# По условию задачи тест должен падать на этой странице из-за бага
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля по уникальным селекторам
    input1 = browser.find_element(By.CSS_SELECTOR, ".first:required")
    input1.send_keys("Ivan")

    # На странице registration2.html этот элемент отсутствует (баг),
    # поэтому здесь ожидаемо возникает NoSuchElementException
    input2 = browser.find_element(By.CSS_SELECTOR, ".second:required")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, ".third:required")
    input3.send_keys("Smolensk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()