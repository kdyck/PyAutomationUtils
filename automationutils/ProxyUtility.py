import requests
import self

from automationutils.UserAgentUtility import UserAgentUtility
from automationutils.WebDriverManager import WebDriverManager


driver = WebDriverManager()


class ProxyUtility:

    @staticmethod
    def get_proxies():
        driver.get_webdriver().get("https://free-proxy-list.net/")
        proxies = set()
        driver.get_webdriver().find_element_by_xpath('//th[7]//select').send_keys('yes')
        for element in driver.get_webdriver().find_elements_by_xpath('//tbody/tr')[:20]:
            if element.find_elements_by_xpath('.//td[7][contains(text(),"yes")]'):
                ip = element.find_element_by_xpath('.//td[1]').text
                port = element.find_element_by_xpath('.//td[2]').text
                proxy = ":".join([ip, port])
                proxies.add(proxy)
        driver.shutdown_webdriver()
        return proxies

    @staticmethod
    def get_response_with_user_agent_and_proxy(url):
        url = url
        json_response = ''

        for proxy in ProxyUtility().get_proxies():
            user_agent = UserAgentUtility().get_user_agent()
            driver.shutdown_webdriver()
            print("Requesting proxy: " + proxy)
            print(
                "Using User Agent: " + user_agent)  # TODO: Store user agent list to file and read file to avoid all the browser session
            try:
                response = requests.get(url, headers={'User-Agent':user_agent}, proxies={"http":proxy, "https":proxy})
                json_response = response.json()
                print("Using HTTP proxy %s" + json_response)
                break
            except:
                json_response = 'Skipping. Proxy Connection error!'
                print(json_response)

        if 'Skipping. Proxy Connection error!' in json_response:
            ProxyUtility().get_response_with_user_agent_and_proxy(url)
        return response


# Remove comment # from below to test base implementation
# RandomProxy().get_response_with_user_agent_and_proxy('https://httpbin.org/user-agent')
