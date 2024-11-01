# NOTE TO MY SELF : dont forget to comment all before sending review

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def open_browser():
    # Configura las opciones de Chrome
    chrome_options = Options()
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Ajusta la ruta

    # Si necesitas opciones adicionales, añádelas al mismo objeto 'chrome_options'
    #chrome_options.add_argument('--headless') # Ejecuta el navegador desde la terminal sin una interfaz gráfica
    #chrome_options.add_argument('--window-size=640,480') # Ajusta el tamaño de la ventana a 640 x 480 pixeles


    # Define la ruta de chromedriver
    chromedriver_path = "/Users/mac/Documents/Selenium/WebDriver/chromedriver"
    service = Service(executable_path=chromedriver_path)


    # Inicia el driver de Chrome con las opciones configuradas
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window() # Modo de pantalla completa


    # Navega a tu destino
    return driver
