'''
Created on 20 oct. 2023

@author: caril
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

class Test_001(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        
        #Ingresamos en la app de Spotify
        self.driver.get("https://www.spotify.com/ar/signup?forward_url=https%3A%2F%2Fwww.spotify.com%2Far%2Fdownload%2F")
        
        
        email=self.driver.find_element(By.ID,"email").click().send.keys("emailprueba")
        
        self.driver.find_element(By.name,"password").click()
        self.driver.find_element(By.ID,"password").send.keys("constraseñaprueba")
        
        self.driver.find_element(By.ID,"displayname").click()
        self.driver.find_element(By.ID,"displayname").send.keys("Tester")
        
        self.driver.find_element(By.ID,"day").click()
        self.driver.find_element(By.ID,"day").send_keys()
       
       
       
    def tearDown(self):
        pass 


    def test_001(self):
        email=self.driver.find_element(By.ID,"email").click().send_keys("emailprueba")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()