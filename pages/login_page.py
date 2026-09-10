
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "#username"
        self.password = "#password"
        self.login_button = "#login"

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)
