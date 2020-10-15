from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\aamir\Downloads\chromedriver_win32 (2)\chromedriver.exe")


# driver.get('http://127.0.0.1:5500/index.html')


# driver.find_element_by_xpath('//*[@id="inputEmail4"]').send_keys('check@gmail.com')
# driver.find_element_by_xpath('//*[@id="inputPassword4"]').send_keys('aamir123')
# driver.find_element_by_xpath('//*[@id="inputAddress"]').send_keys('test district test city kahuta')
# driver.find_element_by_xpath('//*[@id="inputAddress2"]').send_keys('test district test city kahuta 2')
# driver.find_element_by_xpath('//*[@id="inputCity"]').send_keys('XYZ')
# select = Select(driver.find_element_by_id('inputState'))
# select.select_by_index('1') 
# # ------------------------length of select items--------------------------
# # print(len(select.options))

# #-----------------print all text values of select options-----------------
# # for op in select.options:
# #     print(op.text)

# driver.find_element_by_xpath('//*[@id="exampleRadios1"]').click()
# driver.find_element_by_xpath('//*[@id="gridCheck"]').click()

# time.sleep(5)
# driver.close()


#----------------------working with links---------------------------------
# driver.get('https://www.expedia.com/')
# links=driver.find_elements(By.TAG_NAME,'a')
# for li in links:
#     print(li.text)

#------------find link by providing full text of that tag-----------------
# driver.find_element(By.LINK_TEXT,'Support').click()

#------------find link by providing partially text of that tag------------
# driver.find_element(By.PARTIAL_LINK_TEXT,'Sup').click()




#-----------------------Working with Alerts-------------------------------
# driver.get('http://127.0.0.1:5500/index.html')

# #for confirm alert-box
# driver.find_element_by_xpath('/html/body/div/button').click()
# time.sleep(4)

# driver.switch_to.alert.accept()
# #for cancelling alert-box
# driver.switch_to.alert.dismiss()

#------------------------Working with Frames--------------------------------

# driver.switch_to.frame('frameName')
# driver.find_element_by_name('elementName')
# driver.switch_to.default_content() #this is userd to go on for main page
# driver.switch_to.frame('frameName2') #this allow us to switch between different frames


# ---------------------Working with browswer windows-------------------

# driver.get('http://127.0.0.1:5500/index.html')
# driver.find_element_by_xpath('/html/body/div/a').click()
# handles=driver.window_handles

# for handle in handles:
#     driver.switch_to.window(handle)
#     if driver.title=='YouTube':
#         # print(driver.current_window_handle)
#         driver.close()
#         time.sleep(3)
    
# driver.quit()

# ---------------------Working with browswer TABLES-------------------

# driver.get('http://127.0.0.1:5500/')
# # data=driver.find_elements_by_xpath('/html/body/div/table/tbody/tr')

# # rows=len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr'))
# # cols=len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr[1]/th'))

# # for r in range(1,rows+1):
# #     for c in range(1,cols+1):
# #         print(driver.find_element_by_xpath('/html/body/div/table/tbody/tr['+str(r)+']/td['+str(c)+']').text)

# table=driver.find_elements_by_xpath('/html/body/div/table')
# # for i in range(len(table)):
# rowData=driver.find_elements_by_xpath('/html/body/div/table/thead/tr')
# for i in range(1,5):
#     print(driver.find_element_by_xpath('/html/body/div/table/thead/tr/th['+str(i)+']').text)


# ---------------------Working with browswer SCROLSS--------------------
# driver.get('https://www.sic-info.org/en/services/lending/national-flags/')

##WE CAN SCROLL by pixel=driver.execute_script('window.scrollBy(0,500)','')
# driver.execute_script('window.scrollBy(0,1000)','')

##WE CAN SCROLL UNTILL SPECIFIC ELEMENT IS FOUND=driver.execute_script('argument[0].scrollIntoView(),Element)
# flag=driver.find_element_by_xpath('//*[@id="mainInner"]/section/div/ul[5]/li[2]')
# driver.execute_script('arguments[0].scrollIntoView()',flag)

##WE CAN SCROLL PAGE TILL END
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')




#-------------------Working with mouse hovers---------------------------

# from selenium.webdriver import ActionChains

# driver.get('https://www.sic-info.org/en/services/lending/national-flags/')


# hov=driver.find_element_by_xpath('//*[@id="globalNav"]/div/ul/li[1]/div')

# link=driver.find_element_by_xpath('//*[@id="globalNav"]/div/ul/li[1]/ul/li[1]/a')

# actions=ActionChains(driver)

# actions.move_to_element(hov).move_to_element(link).click().perform()
# actions.move_to_element(SOURCE_ELEMENT,TARGE_ELEMENT).perform()



#-------------------Working with Uploading Files-------------------------------
# driver.get('http://127.0.0.1:5500/')
# path="E://TechyLem/Learning Meterials/selenium/project/1.jpg"
# driver.find_element_by_xpath('//*[@id="exampleFormControlFile1"]').send_keys(path)


#-------------------Working with download File-------------------------------

