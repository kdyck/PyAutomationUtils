from automationutils.WebDriverManager import WebDriverManager


def get_proxies_test():
    driver = WebDriverManager()
    driver.get_webdriver().get("https://free-proxy-list.net")
    proxies = set()
    driver.get_webdriver().find_element_by_xpath('//th[7]//select').send_keys('yes')
    for element in driver.get_webdriver().find_elements_by_xpath('//tbody/tr')[:20]:
        if element.find_elements_by_xpath('.//td[7][contains(text(),"yes")]'):
            ip = element.find_element_by_xpath('.//td[1]').text
            port = element.find_element_by_xpath('.//td[2]').text
            proxy = ":".join([ip, port])
            proxies.add(proxy)
            print(proxy)
    print(proxies)
    driver.shutdown_webdriver()
    return proxies


get_proxies_test()
