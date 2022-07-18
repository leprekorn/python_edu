from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Babuin@rambler.ru")

    file_input = browser.find_element(By.ID, "file")
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currentDir, 'upload_file.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(currentDir)
    print(filePath)
    file_input.send_keys(filePath)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
