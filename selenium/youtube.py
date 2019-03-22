from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('E:/Downloads - data drive/chromedriver_win32/chromedriver.exe')
#driver.fullscreen_window()
driver.maximize_window()
#driver.get('https://www.amazon.ca')
#driver.find_element_by_id('nav-your-amazon').click()
#driver.find_element_by_id('ap_email').send_keys('jyx940709@gmail.com')
driver.get('https://www.timeanddate.com/')
#driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()
#driver.find_element_by_css_selector('body.hp.vasq:nth-child(2) div.ctr-p:nth-child(4) div.jhp.big:nth-child(4) form.tsf.nj:nth-child(5) div:nth-child(2) div.A8SBwf div.FPdoLc.VlcLAe:nth-child(4) center:nth-child(1) > input:nth-child(2)').click()
selectedElement = driver.find_element_by_id('month')
month = Select(selectedElement)
month.select_by_visible_text('July')
viewCalendar = driver.find_element_by_xpath("//input[@value='View Calendar']")
viewCalendar.click()