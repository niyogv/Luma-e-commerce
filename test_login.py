import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

# url
URL='https://magento.softwaretestingboard.com/'

@pytest.mark.parametrize('user,password,expected',
                         [('niyog1994@gmail.com','Test@123','Welcome, Niyog V!'), ## valid cred
                          ('niyog1994@gmail.com','test@123','Support This Project'), ## invalid cred
                          ('niyog1994@gmail.com','','Support This Project'), ## without password
                          ('','Test@123','Support This Project'), ## without mail
                          ('','','Support This Project') ## without mail and password
                         ])
def test_login(user,password,expected):
    driver=webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a').click()
    wait=WebDriverWait(driver,60)
    wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(user)
    wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))).send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="send2"]').click()
    time.sleep(2)
    check=wait.until(Ec.presence_of_element_located((By.XPATH, '//ul[@class="header links"]/li/span')))
    assert check.text==expected

