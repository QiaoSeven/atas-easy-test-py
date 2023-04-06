from PIL import Image

from core.CoreConfig import CoreConfig
from util.Base64Util import Base64Util


class CoreCapture:
    def __init__(self, driver, rp_logger):
        self.driver = driver.get_driver()
        self.rp_logger = rp_logger

    def capture_all(self, name):
        file_path = CoreConfig.get_screen_full_path(name)
        self.driver.save_screenshot(file_path)

    def capture_element(self, name, element):
        file_path = CoreConfig.get_screen_full_path(name)
        element.screenshot(file_path)

    def capture_element_1(self, name, element):
        file_path = CoreConfig.get_screen_full_path(name)
        self.driver.save_screenshot(file_path)
        left = element.location['x'] * 2
        top = element.location['y'] * 2
        right = (left + element.size['width'] * 2)
        bottom = (top + element.size['height'] * 2)
        im = Image.open(file_path)
        mg = im.crop((left, top, right, bottom))
        mg.save(file_path)

    def upload_capture_to_report_portal(self, name, desc):
        screenshot_file_path = CoreConfig.get_screen_full_path(name)
        with open(screenshot_file_path, "rb") as image_file:
            file_data = image_file.read()
            self.rp_logger.info(desc,
                                attachment={"name": name,
                                            "data": file_data,
                                            "mime": "image/png"})

    def get_full_path(self, name):
        return CoreConfig.get_screen_full_path(name)

    def capture_base64(self, name):
        screenshot_file_path = CoreConfig.get_screen_full_path(name)
        return Base64Util.get_base64_str(screenshot_file_path)

    def capture_base64_thumbnail(self, name):
        screenshot_file_path = CoreConfig.get_screen_full_path(name)
        return Base64Util.get_press_base64_str(screenshot_file_path, screenshot_file_path, 200, 200)
