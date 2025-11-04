from pages.base_page import BasePage
import allure


class ConfiguratorPage(BasePage):

    # Переключатель "Скрыть"
    TOGGLE = "[data-testid='hide-countertop']"

    # Изображения столешницы для проверки
    COUNTERTOP_IMG_Q = "[src='/static/media/countertop-q.41258f0aa91cd0c9fa4e.png']"
    COUNTERTOP_IMG_U = "[src='/static/media/countertop-p.095c44faedc9795e1fcf.png']"

    # Тип столешницы П-образная
    COUNTERTOP_TYPE_U = "[data-testid='countertop-type-u']"

    # Толщина
    THICKNESS_BUTTON_OPEN = "[data-testid='select-thickness'] > button"
    THICKNESS_BUTTON_SELECT = "[data-testid='select-thickness'] > div > button"

    # Плинтус (Второй элемент в меню опций столешницы)
    BASEBOARD = "[data-testid='product-options-menu-countertop'] > [data-testid='top-button']"

    # Остров (Первый элемент в меню продуктов)
    ISLAND = "[data-testid='product-menu'] > [data-testid='product-item']"

    # Проточки для стока воды (третий элемент в меню опций)
    WATER_FLOW = "[data-testid='options-menu'] > [data-testid='options-item']"

    # Кнопки расчета
    CALC_BUTTON = "[data-testid='calc-button']"
    CALCULATION_BUTTON = "[data-testid='open-report-button']"

    # Цвет
    COLOR_BLOCK = "[data-testid='stone-block']"

    # === Методы действия ===

    @allure.step("Переключить 'Скрыть столешницу'")
    def toggle_hide_countertop(self):
        self.click(self.TOGGLE)
        # Ждем, пока изображение прямой столешницы исчезнет
        self.page.locator(self.COUNTERTOP_IMG_Q).wait_for(state="hidden")

    @allure.step("Выбрать П-образную столешницу")
    def select_u_shaped(self):
        self.click(self.COUNTERTOP_TYPE_U)
        # Ждем появления изображения П-образной столешницы
        self.page.locator(self.COUNTERTOP_IMG_U).wait_for(state="visible")

    @allure.step("Выбрать толщину: 4")
    def select_thickness_4(self):
        self.page.locator(self.THICKNESS_BUTTON_OPEN).first.wait_for(state="visible")
        self.page.locator(self.THICKNESS_BUTTON_OPEN).first.click()
        self.page.locator(self.THICKNESS_BUTTON_SELECT).first.wait_for(state="visible")
        self.page.locator(self.THICKNESS_BUTTON_SELECT).first.click()

    @allure.step("Отключить плинтус")
    def disable_plinth(self):
        self.page.locator(self.BASEBOARD).nth(1).click()

    @allure.step("Добавить остров")
    def add_island(self):
        self.page.locator(self.ISLAND).first.click()

    @allure.step("Добавить проточки для стока воды")
    def add_water_grooves(self):
        self.page.locator(self.WATER_FLOW).nth(2).click()

    @allure.step("Выбрать цвет: {color_name}")
    def select_color(self, color_name: str):
        self.page.locator(self.COLOR_BLOCK).get_by_text(color_name).click()

    @allure.step("Нажать 'Рассчитать' и открыть расчет")
    def calculate_and_open_report(self):
        self.page.locator(self.CALC_BUTTON).scroll_into_view_if_needed()
        self.click(self.CALC_BUTTON)
        self.page.locator(self.CALCULATION_BUTTON).wait_for(state="visible")
        self.click(self.CALCULATION_BUTTON)

    def get_page_text(self) -> str:
        return self.page.locator("body").inner_text()

    #Методы проверки (assertion helpers)

    def is_countertop_hidden(self) -> bool:
        """Проверка: изображение прямой столешницы скрыто (не видно на странице)"""
        return not self.is_visible(self.COUNTERTOP_IMG_Q)

    def is_u_shaped_displayed(self) -> bool:
        """Проверка: изображение П-образной столешницы отображается"""
        return self.is_visible(self.COUNTERTOP_IMG_U)