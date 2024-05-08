from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import crawlipt as cpt
import ddddocr


@cpt.check(exclude="driver")
@cpt.alias("captcha")
def crackCaptcha(driver: WebDriver, xpath: str) -> str:
    """
    Handling keyboard input events
    :param driver: selenium webdriver
    :param xpath: The xpath path of the captcha
    """
    element = driver.find_element(By.XPATH, xpath)
    pic = element.screenshot_as_png
    ocr = ddddocr.DdddOcr(show_ad=False)
    res = ocr.classification(pic)
    return res


actions_list = [crackCaptcha]
