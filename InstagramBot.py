from InstagramLoginInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
        self.followers = []
        self.followings = []

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(
            self.username)
        self.browser.find_element_by_xpath(
            "/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(
            self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
        time.sleep(2)

    def getFollewers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1.5)
        self.browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(1.5)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"{followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1.5)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"{newCount}")
                pass
            else:
                break

        temp_followers = dialog.find_elements_by_css_selector("li")

        with open("followers.txt", "w") as f:
            for user in temp_followers:
                a = user.find_element_by_css_selector("a").get_attribute("href")
                self.followers.append(a)
                f.writeline(a)

    def getFollowings(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            print(followerCount)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if 288 >= newCount:
                pass
            else:
                break

        temp_followers = dialog.find_elements_by_css_selector("li")
        with open("followings.txt", "w") as f:
            for user in temp_followers:
                a = user.find_element_by_css_selector("a").get_attribute("href")
                self.followings.append(a)
                f.writeline(a)

    def find(self):
        for following in self.followings:
            if following not in self.followers:
                print(following)

instagram = Instagram(username, password)

instagram.signIn()
instagram.getFollewers()
instagram.getFollowings()
instagram.find()

