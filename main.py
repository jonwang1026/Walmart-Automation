from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Personal_Info
import time

def order(web, info):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(web['url'])
    time.sleep(3) #remove if you can bypass the captcha
    driver.find_element_by_xpath(
        '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span').click()  # adds to cart
    time.sleep(3) #remove if you can bypass the captcha
    driver.get(web['cart'])  # go to cart website
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]'
        '/div/div[1]/div/section/section/div/button').click() # continue without account
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/'
                                 'div/div/div/div[3]/div/div/div[2]/button').click()  # clicks the continue button
    # form fill out
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName")))
    while not element:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))

    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(info["firstname"])
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(info["lastName"])
    driver.find_element_by_xpath('//*[@id="addressLineOne"]').send_keys(info["address"])
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys(info["phone"])
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(info["email"])
    driver.find_element_by_xpath('//*[@id="city"]').clear()
    driver.find_element_by_xpath('//*[@id="city"]').send_keys(info["city"])
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="postalCode"]').clear()
    driver.find_element_by_xpath('//*[@id="postalCode"]').send_keys(info["zip"])
    time.sleep(10) #remove if you can bypass captcha
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/'
        'div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button').click()  # continue after filling the form
    #####delete this if you want to manually enter your credit card#####
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(info["firstname"])
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(info["lastName"])
    driver.find_element_by_xpath('//*[@id="creditCard"]').send_keys(info["creditCard"])
    driver.find_element_by_xpath('//*[@id="cvv"]').send_keys([info["cvv"]])
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys(info["phone"])
    driver.find_element_by_xpath('//*[@id="month-chooser"]/option[5]').click()  # chooses month expiration date
    driver.find_element_by_xpath('//*[@id="year-chooser"]/option[6]').click()  # chooses year expiration date
    driver.find_element_by_xpath('//html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/'
                                 'div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/'
                                 'div/div/form/div[3]/div/button').click()
    time.sleep(10)

order(Personal_Info.web, Personal_Info.info)



#driver.execute_script('document.getElementById("firstName").setAttribute("value", "enter_name")')