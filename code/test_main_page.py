from selenium.webdriver.common.by import By

from code.pages.login_page import LoginPage
from code.pages.main_page import MainPage
import pytest


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_url()


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_form()


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_register_form()