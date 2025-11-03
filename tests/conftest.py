import pytest
from playwright.sync_api import Page
import allure
from pages.login_page import LoginPage
from pages.configurator_page import ConfiguratorPage

# Учетные данные
EMAIL = "tester@inzhenerka.tech"
PASSWORD = "LetsTest!"


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture(scope="function")
def configurator_page(page: Page) -> ConfiguratorPage:
    return ConfiguratorPage(page)


@pytest.fixture(scope="function")
def auth_configurator(page: Page) -> ConfiguratorPage:
    """Авторизованный конфигуратор"""
    login = LoginPage(page)
    login.login(EMAIL, PASSWORD)
    return ConfiguratorPage(page)