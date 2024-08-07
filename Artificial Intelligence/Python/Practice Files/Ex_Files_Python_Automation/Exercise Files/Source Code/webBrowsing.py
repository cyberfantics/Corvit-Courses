from selenium import webdriver
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver = webdriver.Chrome()
driver.get(url)
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hello World")
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('12')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()