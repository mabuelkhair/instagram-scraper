from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys
import urllib
import os


class InstagramDownloaderTest(unittest.TestCase):
    """This class download instagram account photos."""
    account_to_download_user = ""
    username = ""
    password = ""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def login_instagram(self):
        """This function login to instagram if user and password given"""
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        inputbox = self.browser.find_element_by_name('username')
        inputbox.send_keys(self.username)
        inputbox = self.browser.find_element_by_name('password')
        time.sleep(0.5)
        inputbox.send_keys(self.password)
        time.sleep(0.5)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_downloader(self):
        """This function download instagram account photos"""

        # make sure that account name not empty
        self.assertTrue(len(self.account_to_download_user) > 0, "User is empty")
        # if username and password supported then login
        if len(self.username) > 0 and len(self.password) > 0:
            self.login_instagram()

        # open account page
        self.browser.get('https://www.instagram.com/%s' % self.account_to_download_user)
        pause_time = 2
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        images_list = []
        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(pause_time)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            # Exit if the height does not change
            if new_height == last_height:
                break
            last_height = new_height
            images = self.browser.find_elements_by_tag_name("img")
            for image in images:
                images_list.append(image.get_attribute('src'))
        # remove duplicates and keep the images orderd
        images_list = list(dict.fromkeys(images_list))
        # create directory with the account name if not exist
        if not os.path.exists(self.account_to_download_user):
            os.makedirs(self.account_to_download_user)

        index = 1
        for image in images_list:
            urllib.request.urlretrieve(image, "%s/%s.jpg" % (self.account_to_download_user, index))
            index += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        argv = sys.argv[1:]
        InstagramDownloaderTest.account_to_download_user = argv[0]
        try:
            InstagramDownloaderTest.username = argv[1]
            InstagramDownloaderTest.password = argv[2]
        except IndexError:
            pass
    unittest.main(argv=['first-arg-is-ignored'], warnings='ignore')
