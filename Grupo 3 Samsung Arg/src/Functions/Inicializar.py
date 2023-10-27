'''
Created on 24 oct. 2023

@author: caril
'''
import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))

    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + "/pages"
    Environment = 'Dev'
    
    # BROWSER DE PRUEBAS
    NAVEGADOR = 'CHROME'
    
    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'
    
    # HOJA DE DATOS EXCEL
    Excel = basedir + '/data/DataTest.xlsx'
    if Environment == 'Dev':
        """Aquí ponemos la configuración y precondiciones a utilizar en los tests. Por ejemplo usuarios ya
        resgistrados,ambiente donde se testea, APPservers etc """
    URL = 'https://shop.samsung.com/ar/'
    User = ''
    Password = ''
    """Lo completamos si lo necesitamos luego"""