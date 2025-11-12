from playwright.sync_api import Page
import allure


class BasePage:
    """
    Базовый класс для всех Page-Object классов.
    Определяет общие методы и интерфейс для работы со страницами.
    """

    def __init__(self, page: Page, path: str = "", base_url: str = None):
        self.page = page
        self.path = path
        # Получаем BASE_URL из конфигурации, если не передан явно
        if base_url is None:
            from tests.conftest import BASE_URL
            base_url = BASE_URL
        self.base_url = base_url

    def navigate(self):
        """Переход на страницу по указанному пути"""
        self.page.goto(f"{self.base_url}{self.path}")
        self.page.wait_for_load_state("domcontentloaded")

    def click(self, selector: str):
        """Клик по элементу"""
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        """Заполнение поля ввода"""
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Получение текста элемента"""
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        """Проверка видимости элемента"""
        try:
            return self.page.locator(selector).is_visible(timeout=5000)
        except:
            return False

    def screenshot(self, name: str):
        """Создание скриншота и прикрепление к Allure отчету"""
        allure.attach(
            self.page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )