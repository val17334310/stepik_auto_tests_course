import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):return str(math.log(abs(12*math.sin(int(x))))) 
 
try:
    x_element = browser.find_element_by_id("treasure")
    x= x_element.get_attribute("valuex")
    y =str(math.log(abs(12*math.sin(int(x)))))    
    answer = browser.find_element_by_id("answer").send_keys(y)

    input = browser.find_element_by_id("robotCheckbox")
    input.click()    
    input = browser.find_element_by_id("robotsRule")
    input.click()
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
 
finally:
    
    time.sleep(10)
    
    browser.quit()
