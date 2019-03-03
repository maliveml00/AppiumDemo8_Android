from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Appium(object):


    driver=None
    "@type driver: WebDriver"

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)