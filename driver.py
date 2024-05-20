from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service

chrome_driver_path = ChromeDriverManager().install()


def get_driver(is_headless=False, is_eager=False,
               user_agent=""):
    option = wd.ChromeOptions()
    arguments = [
        "no-sandbox",
        "--disable-extensions",
        '--disable-gpu',
        "window-size=1920x3000",
        "start-maximized",
        'cache-control="max-age=0"',
        "disable-blink-features=AutomationControlled"
    ]
    for argument in arguments:
        option.add_argument(argument)
    if user_agent:
        option.add_argument(f"user-agent={user_agent}")
    if is_headless:
        option.add_argument("--headless")
    if not is_eager:
        option.page_load_strategy = 'eager'
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    webdriver = wd.Chrome(service=Service(chrome_driver_path), options=option)
    with open("stealth.min.js", "r") as f:
        stealth_js = f.readlines()[-1]
    webdriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
    })
    webdriver.execute_script(stealth_js)
    return webdriver


def get_chrome_user_agent():
    driver = get_driver(is_headless=True, is_eager=True)
    driver.get('https://www.baidu.com')
    user_agent = driver.execute_script('return navigator.userAgent')
    driver.quit()
    return user_agent

if __name__ == '__main__':
    with open("stealth.min.js", "r") as f:
        js_code = f.readlines()
        print(js_code)