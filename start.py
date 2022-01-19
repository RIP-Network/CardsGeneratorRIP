import smtplib, ssl
import os
import time
import getpass

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

print(blanco+"Iniciando , espero que le guste!")

from selenium import webdriver
import time

web = webdriver.Chrome()

web.get('https://grabify.link/B1BB6Z')
time.sleep(1)
