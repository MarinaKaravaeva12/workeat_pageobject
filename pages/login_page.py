from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def go_to_forgot_password(self):
        forgot_password_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//p[text()="Forgot Password"]'))
        )
        forgot_password_link.click()