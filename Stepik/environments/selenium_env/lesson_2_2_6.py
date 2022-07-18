import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math_function_calc_x import calc

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(y)
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()
    robotRadioButton = browser.find_element(By.ID, "robotsRule")
    robotRadioButton.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
