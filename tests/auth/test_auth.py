import pytest
import allure
from pages.login_page import LoginPage
from tests.conftest import EMAIL, PASSWORD


@allure.epic("Авторизация")
@allure.feature("Вход в систему")
@pytest.mark.smoke
def test_successful_login(login_page: LoginPage):
    """Успешная авторизация"""

    with allure.step("Выполнить вход"):
        login_page.login(EMAIL, PASSWORD)

    with allure.step("Проверить успешность"):
        login_page.screenshot("После авторизации")
        assert login_page.is_logged_in(), "Пользователь не авторизован"