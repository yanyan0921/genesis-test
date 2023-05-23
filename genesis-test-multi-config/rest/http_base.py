import logging
import core.config_parser as config_parser
import core.property_parser as properties
import base64


class HttpClient:
    logger = logging.getLogger("main.http")
    headers = {'Content-Type': 'application/json'}

    def __init__(self, var, param, index, config_name):
        self.vars = var
        self.params = param
        self.index = index
        self.parser = config_parser.ConfigLoader(config_name)
        self.properties = properties.parse(self.parser.get_setting("config", "path"))
        self.default_url = self.parser.get_setting("endpoint", "default.url")

    def get_service_token(self):
        service_client_key = "serviceClient"
        service_secret_key = "serviceSecret"

        client = self.properties.get(service_client_key)
        secret = self.properties.get(service_secret_key)

        service_token = 'Basic ' + str(base64.b64encode((client + ":" + secret).encode('utf-8')),
                                                       'utf-8')
        self.headers["Authorization"] = service_token
        return service_token

    def get_vetting_token(self):
        vetting_client_key = "vettingClient"
        vetting_secret_key = "vettingSecret"

        client = self.properties.get(vetting_client_key)
        secret = self.properties.get(vetting_secret_key)

        vetting_token = 'Basic ' + str(base64.b64encode((client + ":" + secret).encode('utf-8')),
                                       'utf-8')
        self.headers["Authorization"] = vetting_token
        return vetting_token


if __name__ == '__main__':
    http = HttpClient()
    http.get_service_token()
    print(http.headers)
