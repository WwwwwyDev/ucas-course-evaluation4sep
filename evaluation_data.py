import random

why_i_like_this_course = [
    "我最喜欢这门课程的是它的实用性和与现实生活的联系紧密，让我能够学到很多能够在工作和日常生活中直接应用的知识和技能。",
    "我最喜欢这门课程的是它的教学方式和资源丰富多样，老师讲解清晰、生动有趣，而且提供了大量的案例、实例和练习题，帮助我更好地理解和掌握课程内容。",
    "我最喜欢这门课程的是它的开放性和互动性，老师鼓励学生积极参与讨论和分享自己的见解，让我有机会和同学们一起交流学习经验和观点，拓宽了我的视野和思维方式。",
    "我最喜欢这门课程的是同学们的互动和讨论。在这门课上，我有机会与同学们交流学习经验和观点，相互学习和帮助，感受到了学习的乐趣和成就感。"
    "我最喜欢这门课程的是老师的关怀和支持。老师在教学过程中关心学生的学习和生活情况，给予及时的指导和帮助，让我感受到了被重视和尊重的温暖。"]

what_to_enhance = [
    "我认为本课程可以进一步改进的地方是增加更多的实践环节，让学生能够通过实际操作来应用所学知识，提高他们的实际能力和技能。",
    "我认为本课程可以进一步改进的地方是提供更多的个性化辅导和指导，因为每个学生的学习方式和需求都不同，有针对性的辅导可以帮助他们更好地理解和掌握课程内容。",
    "我认为本课程可以进一步改进的地方是增加更多的互动和合作机会，让学生能够更多地参与到课程中来，培养他们的团队合作能力和沟通能力，提升课程的教学效果。",
    "我认为本课程可以在教学方法上进行改进，采用更多互动式教学和多媒体教学手段，激发学生的学习兴趣和主动性，提高课堂教学的效果和吸引力。"
]

the_cost_time = [
    "我平均每周在这门课程上花费大约10-12个小时，包括课堂学习、作业准备和复习。",
    "我每周在这门课程上花费大约15个小时左右，因为我会额外做一些阅读和研究来加深对课程内容的理解。",
    "我每周在这门课程上花费大约8-10个小时，主要集中在课堂学习和作业完成上，偶尔会有额外的复习时间。"
]

what_i_am_interested = [
    "参与这门课之前，我对这个学科领域其实并不太了解，但我对学习新知识和扩展自己的知识面很感兴趣，所以决定尝试学习这门课程。",
    "我在参与这门课之前对这个学科领域有一定的兴趣，但并不是很深入。我觉得这门课程可以帮助我更深入地了解这个领域，所以我决定选择这门课程。",
    "在参与这门课之前，我对这个学科领域非常感兴趣，我之前可能已经有一些相关知识或经验。我选择这门课程是因为我想深入学习这个领域，提升自己的专业能力和知识水平。"
]

participation = [
    "我在课堂上通常会积极参与，保持良好的出勤率，并尽力回答问题和参与讨论。我认为课堂是学习的重要场所，通过参与可以加深对知识的理解和掌握。",
    "我会尽量保持出勤，但有时候可能会有一些不可抗力的情况导致缺席。在课堂上，我会尽力回答问题，与同学和老师进行交流，但可能会更倾向于听课和做笔记。",
    "我会尽量维持良好的出勤率，努力参与课堂讨论和回答问题。我认为课堂是获取知识和交流思想的重要场所，所以我会尽力积极参与课堂活动。"
]

why_i_like_this_teacher = [
    "我特别喜欢这位老师的教学方法和风格。她讲课生动有趣，能够引起我的兴趣并让我更容易理解和吸收知识。她也非常耐心和细心，会耐心解答我的问题，让我感觉学习很轻松愉快。",
    "我最喜欢这位老师的教学内容和深度。她对所教授的知识非常了解，讲解清晰透彻，让我能够很好地掌握和理解课程内容。她也会提供实际例子和案例，帮助我更好地应用所学知识。",
    "我特别欣赏这位老师的互动性和关怀。她会鼓励学生积极参与课堂讨论和互动，让每个学生都能得到关注和帮助。她也会关心学生的学习情况和困难，给予个性化的建议和帮助，让我感受到她对学生的关爱和支持。"
]

what_to_enhance_teacher = [
    "我觉得老师可以在教学中更加注重学生的理解和应用能力的培养。可以多给予一些实际案例和问题，让学生能够更好地将所学知识应用到实际中去，提升学习的实用性和深度。",
    "我希望老师在课堂上能够更多地鼓励学生的参与和互动。可以设立一些小组讨论或者互动环节，让学生们积极参与课堂，更好地理解和消化所学知识。",
    "我认为老师可以在作业和考试方面给予更加详细和及时的反馈。及时了解学生的学习情况和困难，给予个性化的指导和帮助，可以帮助学生更好地提升学习效果和能力。",
    "我建议老师可以多开设一些辅导时间或者办公室小时，让学生有更多机会与老师交流和求助。这样可以提高学生学习的效率和质量，也可以增进师生之间的沟通和理解。"
]

course_evaluation = {
    "why_i_like_this_course": why_i_like_this_course,
    "what_to_enhance": what_to_enhance,
    "the_cost_time": the_cost_time,
    "what_i_am_interested": what_i_am_interested,
    "participation": participation,
}

teacher_evaluation = {
    "why_i_like_this_teacher": why_i_like_this_teacher,
    "what_to_enhance_teacher": what_to_enhance_teacher,
}

evaluation = {**course_evaluation, **teacher_evaluation}


def random_list_info(my_list):
    index = random.randint(0, len(my_list) - 1)
    return my_list[index]
