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
        """Тест:переключатель скрытия столешницы работает корректно"""
        conf = auth_configurator

        #Действие уже содержит шаг внутри метода
        conf.toggle_hide_countertop()

        #Проверка (методы проверки не содержат @allure.step)
        assert conf.is_countertop_hidden(), "Столешница должна быть скрыта"

    @allure.title("Переключение на П-образную столешницу")
    @allure.description("Переключение на П-образную столешницу – отображается П-образная столешница")
    @pytest.mark.smoke
    def test_u_shaped_countertop(self, auth_configurator: ConfiguratorPage):
        """Тест:переключение типа столешницы на П-образную работает"""
        conf = auth_configurator

        #Действие уже содержит шаг внутри метода
        conf.select_u_shaped()

        #Проверка (методы проверки не содержат @allure.step)
        assert conf.is_u_shaped_displayed(), "П-образная столешница не отображается"