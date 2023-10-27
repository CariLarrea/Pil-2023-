'''
Created on 24 oct. 2023

@author: caril
'''
from Functions.Inicializar import Inicializar
# Importamos del archivo Inicializar, a la clase Inicializar
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import string
import pytest
import unittest
import json
from test.test_tomllib.test_data import json_path

"""Importamos las librerías para poder usarlas, incluida json"""
#Importamos del archivo Inicializar, a la clase Inicializar


class Functions(Inicializar): #Le pasamos como parámetro la clase Inicializar
    def abrir_navegador(self, URL= Inicializar.URL, navegador=Inicializar.NAVEGADOR): #traemos los datos de Inicilizar
        self.ventanas ={} #Porsi tenemos que pasar de ventana en ventana en nuestros TCs

        if navegador == {"CHROME"}:
            self.driver = webdriver.Chrome() #Abrir Chrome
            self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
            self.driver.maximize_window() #Maximizamos la ventana
            return self.driver

    def tearDown(self): #Pasamos a este archivo, el tearDown de los TCs
        self.driver.quit()