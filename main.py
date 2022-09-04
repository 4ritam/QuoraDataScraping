from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class QuoraDataScrap:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.quora.com")
        time.sleep(1)
        self.login()

    def login(self):
        login_button = self.driver.find_element(by="xpath", value="/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div")
        login_button.click()
        time.sleep(2)

        fb_email = self.driver.find_element(by="name", value="email")
        fb_email.send_keys("")
        fb_password = self.driver.find_element(by="name", value="pass")
        fb_password.send_keys("")
        fb_submit = self.driver.find_element(by="id", value="loginbutton")
        fb_submit.click()
        time.sleep(10)

    def get_follower_list(self):
        self.driver.get("https://www.quora.com/profile/Prasoon-Goyal/followers")
        main = self.driver.find_element(By.TAG_NAME, value="body")
        number_of_followers = int(self.driver.find_element(by="xpath", value="/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span/span[2]/div/div").text.split(" ")[0].replace(",", ""))
        print(number_of_followers)

data_scrap = QuoraDataScrap()
data_scrap.get_follower_list()