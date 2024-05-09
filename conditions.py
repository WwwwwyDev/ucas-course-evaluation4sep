from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import crawlipt as cpt


@cpt.check(exclude="driver")
def is_over_evaluation(driver: WebDriver, xpath: str) -> bool:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                             "#main-content > div > div.m-cbox.m-lgray > div.mc-body > table > tbody > tr > td:nth-child(8) > a")))
    elements = driver.find_elements(By.CSS_SELECTOR,
                                    "#main-content > div > div.m-cbox.m-lgray > div.mc-body > table > tbody > tr > td:nth-child(8) > a")
    for element in elements:
        inner_text = element.get_attribute('innerText')
        if inner_text and inner_text == "评估":
            return True
    return False


condition_list = [is_over_evaluation]
