class scrapper:
    def scrapping(name):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        DRIVER_PATH = "chromedriver.exe"
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get('https://www.olx.com.eg/en/ads/q-cats/')
        titles = []
        # while driver.find_element(By.CLASS_NAME, 'a5112ca8')
        titles = driver.find_elements(By.CLASS_NAME, 'a5112ca8')
        prices = driver.find_elements(By.CLASS_NAME, '_52497c97') 
        count = 0
        # for element in prices:
        #     print(element.text)
        #     count+=1
        return titles,prices
        # print(titles)
        print("counter  = ",count)
        # print(title.title)
