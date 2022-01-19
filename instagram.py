from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()

        # time.sleep(2)
        #
        # followers = self.browser.find_element_by_css_selector("div[role=tablist] ul").find_elements_by_css_selector("li")
        #
        # for user in followers:
        #     link = user.find_element_by_css_selector("a").get_attribute("href")
        #     print(link)


    def followUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Takiptesin":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin")

    # def unfollowUser(self, username):
    #     self.browser.get("https://www.instagram.com/" + username)
    #     time.sleep(2)
    #
    #     followButton = self.browser.find_element_by_tag_name("button")
    #
    #     if followButton.text == "Takiptesin":
    #         followButton.click()
    #         time.sleep(2)
    #         self.browser.find_element_by_xpath('//button[text()="Takibi Bırak"]').click()
    #     else:
    #         print("zaten takip etmiyorsunuz")

 # Scroll
 # "window.scrollTo(0,document.documentElement.scrollHeigh

instgram = Instagram(username, password)
instgram.signIn()
# instgram.getFollowers()
# instgram.followUser("kod_evreni")
# instgram.unfollowUser('kod_evreni')