from playwright.sync_api import expect
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    EMAIL_INPUT = "[name=login]"
    PASSWORD_INPUT = "[name=pass]"
    LOGIN_BUTTON = "[type=button]"
    LOGOUT_BUTTON = "//button[text()='Выйти']"

    @allure.step("Авторизация: {email}")
    def login(self, email: str, password: str):
        self.navigate()
        # Ждём, что поле email доступно для ввода (страница загружена)
        expect(self.page.locator(self.EMAIL_INPUT)).to_be_visible(timeout=60000)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        # Вместо wait_for_timeout — ждём появления кнопки "Выйти"
        self.page.locator(self.LOGOUT_BUTTON).wait_for(state="visible", timeout=60000)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGOUT_BUTTON)