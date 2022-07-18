import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text
    print(num1)
    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text
    print(num2)
    sum = int(num1) + int(num2)
    css_sum = f"[value='{sum}']"
    sum = "'" + str(sum) + "'"
    print(sum)
    list = browser.find_element(By.ID, "dropdown")
    list.click()
    browser.find_element(By.CSS_SELECTOR, css_sum).click()


    # select = Select(browser.find_element(By.ID, "dropdown"))
    # select.select_by_value(sum)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
