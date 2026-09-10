class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "#username"
        self.password = "#password"
        sself.login_button = "button[type='submit']"

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)
