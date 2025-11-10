from pages.base_page import BasePage
import allure


class ConfiguratorPage(BasePage):
    """Страница конфигуратора"""

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

    def navigate(self):
        """Переход на страницу конфигуратора"""
        self.page.goto(f"{self.base_url}configurator")
        self.page.wait_for_load_state("domcontentloaded")

    # === Методы действия ===

    @allure.step("Переключить 'Скрыть столешницу'")
    def toggle_hide_countertop(self):
        """Скрыть/показать столешницу"""
        self.click(self.TOGGLE)
        # Ждем, пока изображение прямой столешницы исчезнет
        self.page.locator(self.COUNTERTOP_IMG_Q).wait_for(state="hidden")
        self.screenshot("Столешница скрыта")

    @allure.step("Выбрать П-образную столешницу")
    def select_u_shaped(self):
        """Переключение на П-образный тип столешницы"""
        self.click(self.COUNTERTOP_TYPE_U)
        # Ждем появления изображения П-образной столешницы
        self.page.locator(self.COUNTERTOP_IMG_U).wait_for(state="visible")
        self.screenshot("П-образная столешница")

    @allure.step("Установить толщину: 4 мм")
    def select_thickness_4(self):
        """Выбор толщины столешницы 4 мм"""
        self.page.locator(self.THICKNESS_BUTTON_OPEN).first.wait_for(state="visible")
        self.page.locator(self.THICKNESS_BUTTON_OPEN).first.click()
        self.page.locator(self.THICKNESS_BUTTON_SELECT).first.wait_for(state="visible")
        self.page.locator(self.THICKNESS_BUTTON_SELECT).first.click()
        self.screenshot("Толщина 4 мм")

    @allure.step("Отключить плинтус")
    def disable_plinth(self):
        """Отключение плинтуса"""
        self.page.locator(self.BASEBOARD).nth(1).click()
        self.screenshot("Плинтус отключен")

    @allure.step("Добавить остров")
    def add_island(self):
        """Добавление острова в конфигурацию"""
        self.page.locator(self.ISLAND).first.click()
        self.screenshot("Остров добавлен")

    @allure.step("Добавить проточки для стока воды")
    def add_water_grooves(self):
        """Добавление проточек для стока воды"""
        self.page.locator(self.WATER_FLOW).nth(2).click()
        self.screenshot("Проточки добавлены")

    @allure.step("Выбрать цвет: {color_name}")
    def select_color(self, color_name: str):
        """Выбор цвета материала"""
        self.page.locator(self.COLOR_BLOCK).get_by_text(color_name).click()
        self.screenshot(f"Цвет {color_name}")

    @allure.step("Рассчитать и открыть отчет")
    def calculate_and_open_report(self):
        """Выполнение расчета и открытие страницы результатов"""
        self.page.locator(self.CALC_BUTTON).scroll_into_view_if_needed()
        self.click(self.CALC_BUTTON)
        self.page.locator(self.CALCULATION_BUTTON).wait_for(state="visible")
        self.click(self.CALCULATION_BUTTON)
        self.screenshot("Страница расчета открыта")

    def get_page_text(self) -> str:
        """Получение всего текста со страницы"""
        return self.page.locator("body").inner_text()

    # === Методы проверки ===

    def is_countertop_hidden(self) -> bool:
        """Проверка: изображение прямой столешницы скрыто"""
        return not self.is_visible(self.COUNTERTOP_IMG_Q)

    def is_u_shaped_displayed(self) -> bool:
        """Проверка: изображение П-образной столешницы отображается"""
        return self.is_visible(self.COUNTERTOP_IMG_U)