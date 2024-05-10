import argparse
from driver import get_driver, get_chrome_user_agent
from actions import actions_list
from conditions import condition_list
import crawlipt as cpt
from variable import EvaluationVariable

for action_func in actions_list:
    cpt.Script.add_action(action_func)

for condition_func in condition_list:
    cpt.Script.add_condition(condition_func)

with open("script.crawlipt", "r") as f:
    script = f.readline()

parser = argparse.ArgumentParser(description='传入用户信息')
parser.add_argument('--username', type=str, help='输入用户名')
parser.add_argument('--password', type=str, help='输入密码')

args = parser.parse_args()

webdriver = get_driver(is_headless=True)
loader = cpt.Script(script=script)
v = EvaluationVariable(username=args.username,
                       password=args.password)
loader.process(webdriver=webdriver, variable=v)
webdriver.quit()
