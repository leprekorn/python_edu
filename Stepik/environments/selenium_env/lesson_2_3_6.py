import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math_function_calc_x import calc

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    startButton = browser.find_element(By.CLASS_NAME, 'btn')
    startButton.click()

    windows = browser.window_handles
    print(windows)

    newWindow = browser.window_handles[1]
    browser.switch_to.window(newWindow)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
