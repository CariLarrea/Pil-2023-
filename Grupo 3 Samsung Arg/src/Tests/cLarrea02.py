'''
Created on 26 oct. 2023

@author: caril
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_002_emailInvalido(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Abrir Navegador")
        
        self.driver.get("https://shop.samsung.com/ar/")
        print("Ir a Samsung Home Page")

    def test_login_with_invalid_credentials(self):

        self.driver.find_element(By.ID, "user-bold").click()
        print("Ir a Login Page")
        # Validar titulo de la pagina Login
        wait = WebDriverWait(self.driver, 40)
        try:
            # Buscar el titulo de la pagina Login
            h3_element = self.driver.find_element(By.XPATH, "//h3[normalize-space()='Entrar con e-mail y contraseña']")  
        
            # Comparar el titulo obtenido con el esperado
            title_text = h3_element.text

            # texto del tirulo esperado
            expected_titel = "Entrar con e-mail y contraseña"


            if title_text == expected_titel:
                print("Validation pass: El titulo de la pagina Login es correcto.")
            else:
                print(f"Validation failed: El titulo de la pagina es '{title_text}', pero el titulo esperado es '{expected_titel}'.")

        except Exception as e:
            print(f"Ocurrio un error inesperado: {str(e)}")

        # Ingresar email y password
        self.driver.find_element(By.XPATH, "//input[@placeholder='E-mail']").send_keys("emailprueba")
        print("Ingreso email invalido")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys("password")
        print("Ingreso contraseña")
        
        # Scroll to the "Entrar" button and click it       
        btnEntrar = self.driver.find_element(By.XPATH, "//div[@class='vtex-button__label flex items-center justify-center h-100 ph5 '][contains(.,'Entrar')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", btnEntrar)
        print("Buscar el botón, Entrar")
        
        btnEntrar.click()
        print("Hacer clic en Entrar")
            
        self.driver.execute_script("window.scrollTo(0, 0);")
        
        # Comparar el mensaje de error obtenido con el mensaje de error esperado. 
        self.compareMensajes()

    def compareMensajes(self):
        mensajeEsperado = "Entre con un e-mail válido"  # Corrected the text

        # Usa WebDriverWait para esperar, en caso de ser necesario, hasta que el mensaje de error se visualice.
        wait = WebDriverWait(self.driver, 20)
        smsUsrValidacion = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Entre con un e-mail válido']")))
        mensajeActual = smsUsrValidacion.text
        
        if mensajeEsperado == mensajeActual:
            print("Validation pass: Informa que el email ingresado no es válido")
        else:
            print(f"Validation failed: El mensaje actual es '{mensajeActual}', pero el mensaje esperado es '{mensajeEsperado}'.")

            
        # Take a screenshot and save it to a file

        self.driver.save_screenshot("TC002-e-mailInvalido.png")
        print("Guardar captura de pantalla en el path:..\Grupo 3 Samsung Arg\src\Tests")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
        