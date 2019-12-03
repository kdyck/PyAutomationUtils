import unittest
import urllib.request

from automationutils.UserAgentUtility import UserAgentUtility
from automationutils.WebDriverManager import WebDriverManager

url = 'https://httpbin.org/'


class UserAgentUtilityTest(unittest.TestCase):
    def test_get_user_agent(self):
        user_agent = UserAgentUtility().get_user_agent()
        WebDriverManager().shutdown_webdriver()
        self.assertTrue(self, user_agent)

    def test_user_agent_request(self):
        user_agent = UserAgentUtility().get_user_agent()
        WebDriverManager().shutdown_webdriver()
        request = urllib.request.Request(url, headers={'User-Agent': user_agent})
        response = urllib.request.urlopen(request)
        html = response.read()
        self.assertTrue(self, html)


if __name__ == '__main__':
    unittest.main()
