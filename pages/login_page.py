from playwright.sync_api import expect
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """Страница авторизации"""

    EMAIL_INPUT = "[name=login]"
    PASSWORD_INPUT = "[name=pass]"
    LOGIN_BUTTON = "[type=button]"
    LOGOUT_BUTTON = "//button[text()='Выйти']"

    def navigate(self):
        """Переход на страницу авторизации"""
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("domcontentloaded")

    @allure.step("Авторизация: {email}")
    def login(self, email: str, password: str):
        """Выполнение входа в систему"""
        self.navigate()
        # Ждем что поле email доступно для ввода (страница загружена)
        expect(self.page.locator(self.EMAIL_INPUT)).to_be_visible(timeout=60000)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        # Ждем появления кнопки "Выйти"
        self.page.locator(self.LOGOUT_BUTTON).wait_for(state="visible", timeout=60000)
        self.screenshot("После авторизации")

    @allure.step("Проверка статуса авторизации")
    def is_logged_in(self) -> bool:
        """Проверка, что пользователь авторизован"""
        return self.is_visible(self.LOGOUT_BUTTON)