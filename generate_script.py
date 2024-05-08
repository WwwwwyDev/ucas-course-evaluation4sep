from actions import actions_list
from conditions import condition_list
import crawlipt as cpt

for action_func in actions_list:
    cpt.Script.add_action(action_func)

for condition_func in condition_list:
    cpt.Script.add_condition(condition_func)

login_step = [
    {
        "method": "redirect",
        "url": "https://sep.ucas.ac.cn/",
    }, {
        "method": "input",
        "xpath": "//*[@id=\"userName1\"]",
        "text": "__v-username__",
    }, {
        "method": "input",
        "xpath": "//*[@id=\"pwd1\"]",
        "text": "__v-password__",
    }
]
if __name__ == '__main__':
    from driver import get_driver

    webdriver = get_driver()
    loader = cpt.Script(script=login_step)
    loader.process(webdriver=webdriver)
