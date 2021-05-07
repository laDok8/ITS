
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException


def before_all(context):
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        context.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        context.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    context.driver.implicitly_wait(15)
    context.base_url = "http://localhost:8080/VALU3S"
    context.driver.get("http://localhost:8080/VALU3S")

def after_all(context):
    context.driver.close()