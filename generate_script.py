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
    }, {
        "method": "click",
        "xpath": "//*[@id=\"sb1\"]"
    }
]

into_evaluation_step = [
    {
        "method": "click",
        "xpath": "//*[@id=\"main-metro\"]/ul/li[3]/a[3]"
    }, {
        "method": "log",
        "msg": "1.登录成功"
    }, {
        "method": "alert",
        "operation": "accept",
        "if": {
            "condition": "alert_is_present",
            "wait": 3
        }
    }, {
        "method": "click",
        "xpath": "//*[@id=\"sidebar\"]/ul/li[4]"
    }, {
        "method": "click",
        "xpath": "//*[@id=\"sidebar\"]/ul/li[4]/ul/li"
    }, {
        "method": "url",
        "return_flag": "eval_course_uri"
    }, {
        "method": "log",
        "msg": "2.进入课程评估页面成功"
    },
]

course_evaluation = {
    "loop": {
        "while": {
            "condition": "is_over_evaluation",
            "xpath": "__rf-eval_course_uri__"
        },
        "script": [
            {
                "method": "clickFirstEvaluation",
            }, {
                "method": "log",
                "msg": "__PRE_RETURN__"
            }, {
                "method": "clickAllByJs",
                "xpath": "//*[@id=\"regfrm\"]/table/tbody/tr/td[1]/input"
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1119\"]",
                "text": "__v-why_i_like_this_course__",
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1120\"]",
                "text": "__v-what_to_enhance__",
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1121\"]",
                "text": "__v-the_cost_time__",
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1122\"]",
                "text": "__v-what_i_am_interested__",
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1123\"]",
                "text": "__v-participation__",
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"1125\"]"
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"1132\"]",
            }, {
                "method": "scrollToBottom",
            }, {
                "method": "crackCaptcha",
                "xpath": "//*[@id=\"adminValidateImg\"]"
            }, {
                "method": "input",
                "xpath": "//*[@id=\"adminValidateCode\"]",
                "text": "__PRE_RETURN__",
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"sb1\"]"
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"jbox-state-state0\"]/div[2]/button[1]"
            }, {
                "method": "interval",
                "num": 1
            }, {
                "method": "redirect",
                "url": "__rf-eval_course_uri__"
            }
        ]
    }
}

switch_to_teacher = [
    {
        "method": "log",
        "msg": "3.课程评估已完成"
    },
    {
        "method": "click",
        "xpath": "//*[@id=\"main-content\"]/div/div[2]/ul/li[2]/a",
    }, {
        "method": "url",
        "return_flag": "eval_teacher_uri"
    }, {
        "method": "log",
        "msg": "4.进入教师评估页面成功"
    },
]

teacher_evaluation = {
    "loop": {
        "while": {
            "condition": "is_over_evaluation",
            "xpath": "__rf-eval_course_uri__"
        },
        "script": [
            {
                "method": "clickFirstEvaluation",
            }, {
                "method": "log",
                "msg": "__PRE_RETURN__"
            }, {
                "method": "clickAllByJs",
                "xpath": "//*[@id=\"regfrm\"]/table/tbody/tr/td[1]/input"
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1167\"]",
                "text": "__v-why_i_like_this_teacher__",
            }, {
                "method": "input",
                "xpath": "//*[@id=\"item_1168\"]",
                "text": "__v-what_to_enhance_teacher__",
            }, {
                "method": "scrollToBottom",
            }, {
                "method": "crackCaptcha",
                "xpath": "//*[@id=\"adminValidateImg\"]"
            }, {
                "method": "input",
                "xpath": "//*[@id=\"adminValidateCode\"]",
                "text": "__PRE_RETURN__",
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"sb1\"]"
            }, {
                "method": "clickByJs",
                "xpath": "//*[@id=\"jbox-state-state0\"]/div[2]/button[1]"
            }, {
                "method": "interval",
                "num": 1
            }, {
                "method": "redirect",
                "url": "__rf-eval_teacher_uri__"
            }
        ]
    }
}
step = [*login_step, *into_evaluation_step, course_evaluation, *switch_to_teacher, teacher_evaluation, {
    "method": "log",
    "msg": "5.教师评估已完成"
}, ]

if __name__ == '__main__':
    cpt.Script.syntax_check(cpt.Script.generate(step))
    with open("script.crawlipt", "w") as f:
        f.write(cpt.Script.generate_json(step))
