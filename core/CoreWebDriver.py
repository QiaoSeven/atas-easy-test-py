import json
import time

from appium import webdriver as appdriver
from selenium import webdriver
from selenium.common import TimeoutException

from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.CoreConfig import CoreConfig


class CoreWebDriver:
    def __init__(self, browser_type, if_head, logger):
        self.browser_type = browser_type
        self.if_head = if_head
        self.driver = self.get_web_driver()
        self.logger = logger
        self.action = ActionChains(self.driver)

    def get_web_driver(self):
        driver = webdriver.Chrome
        if self.browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            if CoreConfig.get_proxy('if_proxy') == 'True':
                options.add_argument(
                    '--proxy-server=http://' + CoreConfig.get_proxy('ip') + ':' + CoreConfig.get_proxy('port'))
            if not self.if_head:
                options.add_argument('headless')
                options.add_argument('disable-gpu')
                options.add_argument('no-sandbox')
                options.add_argument('--window-size=1920,1080')
                options.add_argument('disable-dev-shm-usage')
            driver = webdriver.Chrome(
                chrome_options=options
            )
            driver.maximize_window()
        elif self.browser_type.lower() == 'remote-chrome':
            options = webdriver.ChromeOptions()
            if CoreConfig.get_proxy('if_proxy') == 'True':
                options.add_argument(
                    '--proxy-server=http://' + CoreConfig.get_proxy('ip') + ':' + CoreConfig.get_proxy('port'))
            if not self.if_head:
                options.add_argument('headless')
                options.add_argument('disable-gpu')
                options.add_argument('no-sandbox')
                options.add_argument('--window-size=1920,1080')
                options.add_argument('disable-dev-shm-usage')
                options.browser_version = '105.0'
            driver = webdriver.Remote(
                # 'http://' + CoreConfig.get_grid('ip') + ':' + CoreConfig.get_grid('port') + '/wd/hub',
                'http://' + CoreConfig.get_grid('url') + '/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME,
                options=options)
            driver.maximize_window()
        elif self.browser_type.lower() == 'cloud-chrome':
            options = webdriver.ChromeOptions()
            if CoreConfig.get_proxy('if_proxy') == 'True':
                options.add_argument(
                    '--proxy-server=http://' + CoreConfig.get_proxy('ip') + ':' + CoreConfig.get_proxy('port'))
            if not self.if_head:
                options.add_argument('headless')
                options.add_argument('disable-gpu')
                options.add_argument('no-sandbox')
                options.add_argument('disable-dev-shm-usage')
            driver = webdriver.Remote(
                'http://' + CoreConfig.get_grid('url') + '/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME,
                options=options)
            driver.maximize_window()
        elif self.browser_type.lower() == 'firefox':
            driver = webdriver.Firefox()
            driver.maximize_window()
        elif self.browser_type.lower() == 'android':
            cap_result = CoreConfig.get_caps_by_type("android")
            caps = {"platformName": cap_result.get("platformName"), "deviceName": cap_result.get("deviceName"),
                    "appPackage": cap_result.get("appPackage"),
                    "appActivity": cap_result.get("appActivity"), "noReset": cap_result.get("noReset"),
                    "chromeOptions": json.loads(cap_result.get("chromeOptions"))}
            driver = appdriver.Remote(
                "http://" + cap_result.get("app_server") + ":" + cap_result.get("app_port") + "/wd/hub", caps)
        elif self.browser_type.lower() == 'ios':
            cap_result = CoreConfig.get_caps_by_type("ios")
            caps = {"platformName": cap_result.get("platformName"), "deviceName": cap_result.get("deviceName"),
                    "udid": cap_result.get("udid"),
                    "automationName": cap_result.get("automationName"), "bundleId": cap_result.get("bundleId"),
                    "xcodeOrgId": cap_result.get("xcodeOrgId"), "xcodeSigningId": cap_result.get("xcodeSigningId"),
                    "noReset": cap_result.get("noReset"),
                    "shouldTerminateApp": cap_result.get("shouldTerminateApp")}
            driver = appdriver.Remote(
                "http://" + cap_result.get("app_server") + ":" + cap_result.get("app_port") + "/wd/hub", caps)
        elif self.browser_type.lower() == 'android_kobiton':
            cap_result = CoreConfig.get_caps_by_type("android_kobiton")
            caps = {"sessionName": cap_result.get("sessionName"),
                    "deviceOrientation": cap_result.get("deviceOrientation"),
                    "fullReset": bool(cap_result.get("fullReset")),
                    "captureScreenshots": bool(cap_result.get("captureScreenshots")),
                    "noReset": bool(cap_result.get("noReset")),
                    "app": cap_result.get("app"), "groupId": cap_result.get("groupId"),
                    "deviceGroup": cap_result.get("deviceGroup"), "deviceName": cap_result.get("deviceName"),
                    "platformName": cap_result.get("platformName"),
                    "platformVersion": cap_result.get("platformVersion")}
            driver = appdriver.Remote(cap_result.get("kobitonServerUrl"), caps)
        elif self.browser_type.lower() == 'ios_kobiton':
            cap_result = CoreConfig.get_caps_by_type("ios_kobiton")
            caps = {"sessionName": cap_result.get("sessionName"),
                    "deviceOrientation": cap_result.get("deviceOrientation"),
                    "fullReset": bool(cap_result.get("fullReset")),
                    "captureScreenshots": bool(cap_result.get("captureScreenshots")),
                    "noReset": bool(cap_result.get("noReset")),
                    "bundleId": cap_result.get("bundleId"), "groupId": cap_result.get("groupId"),
                    "deviceGroup": cap_result.get("deviceGroup"), "deviceName": cap_result.get("deviceName"),
                    "platformName": cap_result.get("platformName"),
                    "platformVersion": cap_result.get("platformVersion")}
            driver = appdriver.Remote(cap_result.get("kobitonServerUrl"), caps)
        elif self.browser_type.lower() == 'android_debug':
            cap_result = CoreConfig.get_caps_by_type("android_debug")
            caps = {"platformName": cap_result.get("platformName"), "deviceName": cap_result.get("deviceName"),
                    "appPackage": cap_result.get("appPackage"),
                    "appActivity": cap_result.get("appActivity"), "noReset": cap_result.get("noReset")}
            driver = appdriver.Remote(
                "http://" + cap_result.get("app_server") + ":" + cap_result.get("app_port") + "/wd/hub", caps)
        return driver

    def get_driver(self):
        return self.driver

    def get_browser_type(self):
        return self.browser_type

    def get_action(self):
        return self.action

    def wait_and_find_element(self, by, pros, times):
        try:
            element = WebDriverWait(self.driver, times).until(
                EC.element_to_be_clickable((by, pros))
            )
            return element
        except TimeoutException:
            self.logger.error('Can not find element')
            self.driver.quit()

    def ensure_element_exist(self, by, pros, times):
        try:
            element = WebDriverWait(self.driver, times).until(
                EC.element_to_be_clickable((by, pros))
            )
            return True
        except TimeoutException:
            return False

    def find_element(self, by, props):
        return self.driver.find_element(by, props)

    def find_elements(self, by, props):
        return self.driver.find_elements(by, props)

    def scroll_to_element(self, element):
        js4 = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js4, element)
        time.sleep(3)

    def click_element(self, element):
        js4 = "arguments[0].click();"
        self.driver.execute_script(js4, element)

    def action_hover(self, element):
        self.action.move_to_element(element).perform()
        time.sleep(5)

    def action_move_click(self, element):
        self.action.move_to_element(element)
        time.sleep(1)
        self.action.click(element).perform()

    def navigate_to_app(self):
        self.driver.switch_to.context("NATIVE_APP")

    def navigate_to_webview(self):
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[1])

    def page_refresh(self):
        self.driver.refresh()


