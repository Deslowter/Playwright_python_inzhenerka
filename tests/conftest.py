import pytest
import os
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.configurator_page import ConfiguratorPage
from dotenv import load_dotenv

# Загрузка переменных .env файла
load_dotenv()

# Конфигурация из переменных окружения с fallbak значениями
BASE_URL = os.getenv("BASE_URL", "https://dev.topklik.online/")
EMAIL = os.getenv("EMAIL", "tester@inzhenerka.tech")
PASSWORD = os.getenv("PASSWORD", "LetsTest!")


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    """Фикстура для создания экземпляра страницы авторизации"""
    return LoginPage(page)


@pytest.fixture(scope="function")
def configurator_page(page: Page) -> ConfiguratorPage:
    """Фикстура для создания экземпляра страницы конфигуратора"""
    return ConfiguratorPage(page)


@pytest.fixture(scope="function")
def auth_configurator(page: Page) -> ConfiguratorPage:
    """Фикстура: авторизованный пользователь на странице конфигуратора"""
    login = LoginPage(page)
    login.login(EMAIL, PASSWORD)
    return ConfiguratorPage(page)