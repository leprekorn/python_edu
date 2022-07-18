import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math_function_calc_x import calc


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    inputResult = browser.find_element(By.ID, "answer")
    inputResult.send_keys(y)
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()
    robotRadioButton = browser.find_element(By.ID, "robotsRule")
    robotRadioButton.click()
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
