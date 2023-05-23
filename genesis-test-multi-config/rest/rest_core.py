import importlib


class Rest:

    def __init__(self, var, resource, action, index, config_name):
        self.vars = var
        self.resource = resource
        self.actions = action
        self.config_name = config_name
        for action in self.actions:
            self.call(action, index)

    def call(self, action, index):
        method = action["method"]
        params = action["param"]

        class_name = "Service"
        module_name = "rest." + self.resource

        module = importlib.import_module(module_name)
        obj_c = getattr(module, class_name)
        service = obj_c(self.vars, params, index, self.config_name)

        getattr(service, method)()
