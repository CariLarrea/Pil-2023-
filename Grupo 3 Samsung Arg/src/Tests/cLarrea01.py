'''
Created on 24 oct. 2023

@author: caril
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_001_ingresoExitoso(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Abrir Navegador")
        
        self.driver.get("https://shop.samsung.com/ar/")
        print("Ir a Samsung Home Page")

    def test_login_with_valid_credentials(self):
        # Si es necesario esperar hasta 30 seg hasta que los elementos esten visibles.
        wait = WebDriverWait(self.driver, 60)
        
        try:
            # Use a tuple for the locator strategy and value
            account = wait.until(EC.presence_of_element_located((By.ID, "user-bold")))
            account.click()
            print("Ir a Login Page")
        except Exception as e:
            print("An error occurred:", str(e))

        # Validar acceso a la pagina Login
        try:
            # Buscar el titulo de la pagina Login
            
            h3_element = wait.until(EC.presence_of_element_located(By.XPATH, "//h3[normalize-space()='Entrar con e-mail y contraseña']"))
        
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
        try:
            self.driver.implicitly_wait(40)  # Wait for up to 40 seconds for elements to be found
            email = self.driver.find_element(By.XPATH, "//input[@placeholder='E-mail']")
            email.send_keys("piltets2023@gmail.com")
            print("Email field found")
        except Exception as e:
            print("An error occurred:", str(e))
            
        try:
            self.driver.implicitly_wait(40)  # Wait for up to 40 seconds for elements to be found
            password = self.driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']")
            password.send_keys("Juangrillo1")
            print("Password field found")
        except Exception as e:
            print("An error occurred:", str(e))
        
                # Scroll to the "Entrar" button and click it       
        btnEntrar = self.driver.find_element(By.XPATH, "//div[@class='vtex-button__label flex items-center justify-center h-100 ph5 '][contains(.,'Entrar')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", btnEntrar)
        print("Buscar el boton Entrar")
        
        btnEntrar.click()
        print("Hacer clic en Entrar")
            
        self.driver.execute_script("window.scrollTo(0, 0);")
        
      
        # DATOS DE LA CUENTA DEL USAURIO REGISTRADO 
        
        Titulo = "Perfil"
        nombre = "Pil"  
        apellido = "Test"
        email= "piltets2023@gmail.com"
        dni= "12457836"
        género= "Femenino"

 
        # OBTENER DATOS DEL PERFIL 
        # validacion Logica
        is_valid_title =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='db-m dn']//div[@class='vtex-pageHeader__container pa5 pa7-ns']//div[1]//div[1]"))).text
        is_valid_nombre =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Pil']"))).text
        is_valid_apellido =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Test']"))).text
        is_valid_email =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='piltets2023@gmail.com']"))).text 
        is_valid_dni =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='12457836']"))).text 
        is_valid_genero =  wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Femenino']"))).text 
        is_valid_birthDate =  wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(.,'01/01/1978')])[16]"))).text 
        # VALIDAR ACCESSO A CUENTA VALIDA          
        print("****VALIDAR DATOS DEL PERFIL****")     
        
        # VALIDAR NOMBRE
        assert is_valid_title, "The page name is not valid."
        print("Titulo:" + is_valid_title)    
        
         # VALIDAR NOMBRE
        assert is_valid_nombre, "The first name is not valid."
        print("Nombre:" + is_valid_nombre)
        
        # VALIDAR APELLIDO
        assert is_valid_apellido, "The last name is not valid."
        print("Apellido:" + is_valid_apellido)      
        
         # VALIDAR EMAIL
        assert is_valid_email, "The page name is not valid."
        print("email:" + is_valid_email)  
        
        # VALIDAR DNI
        assert is_valid_dni, "The document is not valid."
        print("dni:" + is_valid_dni)  
        
         # GENERO
        assert is_valid_genero, "The gender is not valid."
        print("género:" + is_valid_genero)         
        
        # FECHA NACIMIENTO
        assert is_valid_birthDate, "The document is not valid."
        print("email:" + is_valid_birthDate)       
        
        self.driver.save_screenshot("TC001-loginExitoso.png")
        print("Guardar captura de pantalla en el path:..\Grupo 3 Samsung Arg\src\Tests")
            
               
    def tearDown(self):
        self.driver.quit()
        

     
if __name__ == "__main__":
        unittest.main()           