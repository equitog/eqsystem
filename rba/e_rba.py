from selenium import webdriver
import os
import time
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Ebrowser:

    def openbrowser(self, pageweb, wait):

        driver = webdriver.Chrome(os.path.join(ROOT_DIR, r"drivers\chromedriver.exe"))
        driver.get(pageweb)
        time.sleep(wait)
        driver.close()
        return 1

    def __del__(self):
        print("Memoria free")

a = Ebrowser().openbrowser("http://172.57.154.18/sistema/backend/web/user/login", 10)
