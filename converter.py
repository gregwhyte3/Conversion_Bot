import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class YTDownloader:
    def __init__(self):
        """Initializes Chromedriver and sets common url"""

        self.driver = webdriver.Chrome()

        self.base_url = "https://ytmp3.cc/en13/"

    def new_link(self):
        """Asks user for youtube link(s)"""

        self.link = input("Please paste Youtube video link :)\n")

        # ask user for multiple video links
        # store links in list and loop downloading

        # print("How many videos would you like me to download?\n")
        # self.downloads = int(input())
        # print("Please paste link for video(s) :)")

        # self.multiple = []

        # if self.downloads == 1:
        #     print("Thanks!")

        # elif self.downloads > 1:
        #     self.link = input(""),
        #     self.multiple.append(self.link)
        #     print(self.multiple)

    def nav(self):
        """Bot goes to landing page"""

        self.driver.get(self.base_url)
        # self.driver.maximize_window()
        time.sleep(1)

    def convert(self):
        """Paste link and click on convert button click()"""

        self.driver.find_element_by_id("input").send_keys(self.link)
        time.sleep(1)
        self.driver.find_element_by_id("submit").click()

    def download(self):
        """Click on download button"""

        time.sleep(2)
        self.driver.find_element_by_link_text("Download").click()

    def _multiple(self):
        # loop through links
        pass

    def close(self):
        """Window closes"""
        time.sleep(15)
        self.driver.close()


yt = YTDownloader()

yt.new_link()
yt.nav()
yt.convert()
yt.download()
yt.close()
