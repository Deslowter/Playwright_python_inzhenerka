import pytest
import allure
from pages.login_page import LoginPage
from tests.conftest import EMAIL, PASSWORD


@allure.parent_suite("UI тесты")
@allure.suite("Авторизация")
@allure.sub_suite("Позитивные сценарии")
@allure.epic("Авторизация")
@allure.feature("Вход в систему")
@pytest.mark.smoke
def test_successful_login(login_page: LoginPage):
    """Успешная авторизация пользователя"""

    #Выполняем авторизацию - определен в метод login
    login_page.login(EMAIL, PASSWORD)

    #Проверяем успешность - в методе is_logged_in
    assert login_page.is_logged_in(), "Пользователь не авторизован"