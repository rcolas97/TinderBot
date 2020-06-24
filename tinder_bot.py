from selenium import webdriver
from time import sleep


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

        sleep(1)

        self.login()

    def login(self):
        self.driver.get('https://www.tinder.com')
        sleep(4)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        login_btn.click()

        sleep(2)

        base_window = self.driver.window_handles[0]
        current_win = self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys('r.aleph.c@gmail.com')

        sleep(1)

        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn.click()

        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys('rosthekidd')

        sleep(2)

        next_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_btn.click()

        sleep(5)

        current_win = self.driver.switch_to.window(base_window)

        loc_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_btn.click()

        noti_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        noti_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def autoswipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        ignore_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        ignore_btn.click()

    def close_match(self):
        match_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_btn.click()
