from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Ebrowser:
    pageweb = ''
    where_save = ''
    wait = 0

    def __init__(self, pageweb, where_save, wait):

        """ Initialize the variables of the class."""
        self.pageweb = pageweb
        self.where_save = where_save
        self.wait = wait
        initialize = [self.pageweb, self.where_save, str(self.wait)]
        print(" ".join(initialize))

    def openbrowser(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": self.where_save,
            # "download.prompt_for_download": True
            # "download.directory_upgrade": True,
            # "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(os.path.join(ROOT_DIR, r"drivers\chromedriver.exe"), chrome_options=options)

        driver.maximize_window()

        driver.get(self.pageweb)
        time.sleep(self.wait)

        return driver

    def __del__(self):

        """ Kill process open by chrome driver """
        os.system("taskkill /f /im chromedriver.exe")
        print("Memoria free")



