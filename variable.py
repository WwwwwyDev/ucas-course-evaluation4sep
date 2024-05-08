import crawlipt as cpt
from evaluation_data import evaluation, random_list_info


class EvaluationVariable(cpt.VariableBase):

    @cpt.check
    def __init__(self, username: str, password:str):
        self.username = username
        self.password = password

    @cpt.check
    def get(self, key: str) -> str:
        if key == "username":
            return self.username
        if key == "password":
            return self.password
        return random_list_info(evaluation[key])

    @cpt.check
    def __contains__(self, key: str) -> bool:
        if key == "username" or key == "password":
            return True
        return key in evaluation

