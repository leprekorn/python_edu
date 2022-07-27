from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math_function_calc_x import calc
import time

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    bookButton = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "book"))
        )
    bookButton.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
