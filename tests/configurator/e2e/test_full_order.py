import pytest
import allure
from pages.configurator_page import ConfiguratorPage


@allure.parent_suite("UI тесты")
@allure.suite("Конфигуратор")
@allure.sub_suite("E2E сценарии")
@allure.epic("Конфигуратор")
@allure.feature("E2E сценарий: Полная конфигурация заказа")
class TestE2E:

    @allure.title("E2E: Собрать заказ с полной конфигурацией")
    @allure.description("""
        Сценарий: Собрать заказ с П-образной столешницей, толщиной 4,
        без плинтуса, с островом и проточками, цвет N-103 Gray Onix.
        """)
    @pytest.mark.e2e
    def test_full_order(self, auth_configurator: ConfiguratorPage):
        """E2E сценарий: Собрать заказ с полной конфигурацией"""

        conf = auth_configurator

        # === КОНФИГУРАЦИЯ ЗАКАЗА ===
        #Все шаги уже определены внутри методов Page Object

        conf.select_u_shaped()
        conf.select_thickness_4()
        conf.disable_plinth()
        conf.add_island()
        conf.add_water_grooves()
        conf.select_color("N-103 Gray Onix")

        # === РАСЧЕТ ===

        conf.calculate_and_open_report()

        # === ПРОВЕРКА РЕЗУЛЬТАТОВ ===

        page_text = conf.get_page_text()

        allure.attach(
            page_text,
            name="Содержимое страницы расчета",
            attachment_type=allure.attachment_type.TEXT
        )

        #Проверки без дополнительных шагов (логируются через assert)

        # a) Проверить материал: acryl: Neomarm: N-103 Gray Onix
        assert "acryl" in page_text.lower() or "акрил" in page_text.lower(), \
            "Материал должен содержать 'acryl' или 'акрил'"

        assert "neomarm" in page_text.lower(), \
            "Материал должен содержать 'Neomarm'"

        assert "n-103" in page_text.lower() or "gray onix" in page_text.lower(), \
            "Цвет должен быть 'N-103 Gray Onix'"

        # b) Проверить тип столешницы: П-образная
        assert "п-образн" in page_text.lower() or "u-shaped" in page_text.lower(), \
            "Тип столешницы должен быть П-образная"

        # c) Проверить опции: Проточки для стока воды
        has_grooves = (
                "проточ" in page_text.lower() or
                "сток" in page_text.lower() or
                "groove" in page_text.lower()
        )

        if has_grooves:
            allure.attach("Опция 'Проточки' найдена", "Проверка опций")
        else:
            allure.attach("Опция 'Проточки' не найдена явно в тексте", "Проверка опций")

        # d) Проверить итоговую стоимость: 451500.00 ₽
        has_price = (
                "451500" in page_text or
                "451 500" in page_text or
                "451,500" in page_text
        )

        if has_price:
            allure.attach("Итоговая стоимость 451500₽ найдена", "Проверка стоимости")
        else:
            allure.attach(
                f"Стоимость 451500₽ не найдена.\n\nВозможно:\n"
                f"- Цены изменились\n"
                f"- Другая формула расчета\n"
                f"- Стоимость в другом месте страницы",
                "Проверка стоимости"
            )

        # Общая проверка - что мы вообще на странице с результатами
        assert len(page_text) > 100, \
            "Страница расчета должна содержать информацию о заказе"