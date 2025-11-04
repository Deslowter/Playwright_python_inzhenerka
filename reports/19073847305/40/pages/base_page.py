from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://dev.topklik.online/"

    def navigate(self):
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("domcontentloaded")

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible(timeout=5000)
        except:
            return False

    def screenshot(self, name: str):
        allure.attach(
            self.page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )