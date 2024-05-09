from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import crawlipt as cpt
import ddddocr


@cpt.check(exclude="driver")
@cpt.alias("captcha")
def crackCaptcha(driver: WebDriver, xpath: str) -> str:
    element = driver.find_element(By.XPATH, xpath)
    pic = element.screenshot_as_png
    ocr = ddddocr.DdddOcr(show_ad=False)
    res = ocr.classification(pic)
    return res

@cpt.check(exclude="driver")
@cpt.alias("captcha")
def clickFirstEvaluation(driver: WebDriver) -> str:
    elements = driver.find_elements(By.CSS_SELECTOR,
                                    "#main-content > div > div.m-cbox.m-lgray > div.mc-body > table > tbody > tr > td:nth-child(8) > a")
    cnt = 0
    for element in elements:
        cnt += 1
        inner_text = element.get_attribute('innerText')
        if inner_text and inner_text == "评估":
            driver.execute_script("arguments[0].click();", element)
            return f"[info] 正在评估未评估列表的第{str(cnt)}个"


actions_list = [crackCaptcha, clickFirstEvaluation]
