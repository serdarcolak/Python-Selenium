from selenium import webdriver
import time

driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url) # ilgili web sitesine vs. gitme

time.sleep(2) # İki saniye bekleme
driver.maximize_window() # Büyük ekran yapma
driver.save_screenshot("github.com-homepage.png") # ss alma

url = "http://github.com/serdarcolak"
driver.get(url)

print(driver.title)

if "serdarcolak" in driver.title:
    driver.save_screenshot("github-serdarcolak.png")

time.sleep(2)

driver.back() # Geri gitme
#driver.forward() ileriye alma

time.sleep(2)

driver.close() # kapatma