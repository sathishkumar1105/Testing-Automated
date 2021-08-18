from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://thesparksfoundationsingapore.org")
driver.maximize_window()
print(driver.title)

#about us page
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Corporate Partners").click()
    time.sleep(2)
    print("about us page is present")
except NoSuchElementException:
    print("about us page is not there")

#policies and code page
try:
    driver.find_element_by_link_text("Policies and Code").click()
    time.sleep(2)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(2)
    print("Policies and Code page is present")
except NoSuchElementException:
    print("Policies and Code is not there")

#contact us page
try:
    driver.find_element_by_id('link-effect-3').click()  
    time.sleep(2)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(2)
    print("contact us page is present")
except NoSuchElementException:
    print("contact us page is not present")

#logo of webpage
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img').click()
    print("The logo of this web page is present")
    time.sleep(2)
except NoSuchElementException:
    print("no logo is present")

#Join us page
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Why Join Us").click()
    time.sleep(2)
    user = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
    user.send_keys("Selenium Testing")
    time.sleep(2)
    email = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
    email.send_keys("123@gmail.com")
    time.sleep(5)
    print("Join us page is present")
    driver.quit()
except NoSuchElementException:
    print("join us page is not there")
    
