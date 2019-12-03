import random

from automationutils.WebDriverManager import WebDriverManager


class UserAgentUtility(object):

    @staticmethod
    def get_user_agent():
        driver = WebDriverManager()
        driver.get_webdriver().get("https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/")
        assert "WhatIsMyBrowser.com" in driver.get_webdriver().title
        user_agent_links = driver.get_webdriver().find_elements_by_xpath("//td/a")
        random_index = random.randrange(len(user_agent_links))
        return user_agent_links[random_index].text
