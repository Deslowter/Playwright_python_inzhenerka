import pytest
import allure
from pages.configurator_page import ConfiguratorPage


@allure.parent_suite("UI тесты")
@allure.suite("Конфигуратор")
@allure.sub_suite("Тесты переключателей")
@allure.epic("Конфигуратор")
@allure.feature("Переключатели отображения")
class TestToggles:

    @allure.title("Проверка 'Скрыть столешницу'")
    @allure.description("Проверить, что работает переключатель 'Скрыть столешницу' – столешница не отображается")
    @pytest.mark.smoke
    def test_hide_countertop(self, auth_configurator: ConfiguratorPage):
        conf = auth_configurator

        with allure.step("Переключить 'Скрыть столешницу'"):
            conf.toggle_hide_countertop()

        with allure.step("Проверить, что столешница не отображается"):
            conf.screenshot("Столешница скрыта")
            assert conf.is_countertop_hidden(), "Столешница должна быть скрыта"

    @allure.title("Переключение на П-образную столешницу")
    @allure.description("Переключение на П-образную столешницу – отображается П-образная столешница")
    @pytest.mark.smoke
    def test_u_shaped_countertop(self, auth_configurator: ConfiguratorPage):
        conf = auth_configurator

        with allure.step("Выбрать П-образную столешницу"):
            conf.select_u_shaped()

        with allure.step("Проверить отображение П-образной столешницы"):
            conf.screenshot("П-образная столешница")
            assert conf.is_u_shaped_displayed(), "П-образная столешница не отображается"