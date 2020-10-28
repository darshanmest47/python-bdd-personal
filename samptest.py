import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mynewportofolio.herokuapp.com/')
driver.maximize_window()

driver.execute_script("window.scrollTo(0,1500)")

driver.switch_to.frame(1)
print(driver.title)
print("printed")

val1 = 2
val2 = 2

for ele in range(1, 10):
    val1 = val1 * 2
    time.sleep(0.5)
    driver.execute_script(f"window.scrollBy(0,{val1})")

for ele1 in range(1, 10):
    val2 = val2 * 2
    time.sleep(0.5)
    driver.execute_script(f"window.scrollBy(0,{-val2})")
