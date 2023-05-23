from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Chain:

    def __init__(self, driver, var, page, chain):
        self.chain = ActionChains(driver)
        self.vars = var
        self.page = page
        self.actions = chain
        for action in self.actions:
            self.execute(action)
        self.chain.perform()

    def execute(self, action):
        method = action["method"]
        params = action["param"]
        param = []

        for k, v in params.items():
            if k == "element":
                param.append(getattr(self.page, v))
            elif k == "value":
                if isinstance(v, list):
                    param.extend(v)
                elif v.startswith("${"):
                    param.append(self.vars.get(v[2:-1]))
                elif v.startswith("Keys."):
                    value = getattr(Keys(), v[5:])
                    param.append(value)
                else:
                    param.append(v)

        chain_method = getattr(self.chain, method)
        chain_method(*param)
