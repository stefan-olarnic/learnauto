class Context:
    def __init__(self, driver, base_url, env, valid_user):
        self.driver = driver
        self.base_url = base_url
        self.env = env
        self.validuser = valid_user