from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.login_page import LoginPage

def test_user_can_login(browser):
    link = 'https://develop-app.workeat.co.il/#/login'
    page = LoginPage(browser,link)
    page.open()
    page.go_to_forgot_password()
