from selenium.webdriver.common.keys import Keys

from automationutils.WebDriverManager import WebDriverManager


def main():
    driver = WebDriverManager()
    driver.get_webdriver().get("https://www.google.com")
    element = driver.get_webdriver().find_element_by_xpath("//input[@title='Search']")
    element.send_keys("qarepo")
    element.send_keys(Keys.ENTER)
    elements = driver.get_webdriver().find_elements_by_xpath("//div[@id='search']//h3")
    print(elements)
    for element in elements:
        element_text = element.text
        if "qarepo (@qarepo) | Twitter" in element_text:
            element.click()
            all_links = driver.get_webdriver().find_elements_by_tag_name("a")
            for link in all_links:
                link_text = link.get_attribute("href")
                print(link_text)
            break
    driver.shutdown_webdriver()
