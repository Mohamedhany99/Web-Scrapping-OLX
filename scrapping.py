from selenium import webdriver
from selenium.webdriver.common.by import By
DRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.olx.com.eg/en/ads/q-cats/')
titles = []
# while driver.find_element(By.CLASS_NAME, 'a5112ca8')
elements = driver.find_elements(By.CLASS_NAME, 'a5112ca8')
for element in elements:
    print(element.text)
# print(titles)
print("hiii")
# print(title.title)
