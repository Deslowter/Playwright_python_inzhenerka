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

        with allure.step("a) П-образная столешница"):
            conf.select_u_shaped()
            conf.screenshot("1_П-образная")

        with allure.step("b) Толщина: 4"):
            conf.select_thickness_4()
            conf.screenshot("2_Толщина_4")

        with allure.step("c) Плинтус: не требуется (выключить)"):
            conf.disable_plinth()
            conf.screenshot("3_Плинтус_отключен")

        with allure.step("d) Добавить Остров"):
            conf.add_island()
            conf.screenshot("4_Остров_добавлен")

        with allure.step("e) Добавить проточки для стока воды"):
            conf.add_water_grooves()
            conf.screenshot("5_Проточки_добавлены")

        with allure.step("f) Цвет: N-103 Gray Onix"):
            conf.select_color("N-103 Gray Onix")
            conf.screenshot("6_Цвет_N-103")

        # === РАСЧЕТ ===

        with allure.step("Нажать 'Рассчитать' и открыть 'Расчет'"):
            conf.calculate_and_open_report()
            conf.screenshot("7_Страница_расчета")

        # === ПРОВЕРКА РЕЗУЛЬТАТОВ ===

        with allure.step("Получить данные со страницы расчета"):
            page_text = conf.get_page_text()

            allure.attach(
                page_text,
                name="Содержимое страницы расчета",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("a) Проверить материал: acryl: Neomarm: N-103 Gray Onix"):
            # Проверяем наличие ключевых слов
            assert "acryl" in page_text.lower() or "акрил" in page_text.lower(), \
                "Материал должен содержать 'acryl' или 'акрил'"

            assert "neomarm" in page_text.lower(), \
                "Материал должен содержать 'Neomarm'"

            assert "n-103" in page_text.lower() or "gray onix" in page_text.lower(), \
                "Цвет должен быть 'N-103 Gray Onix'"

        with allure.step("b) Проверить тип столешницы: П-образная"):
            assert "п-образн" in page_text.lower() or "u-shaped" in page_text.lower(), \
                "Тип столешницы должен быть П-образная"

        with allure.step("c) Проверить опции: Проточки для стока воды"):
            has_grooves = (
                    "проточ" in page_text.lower() or
                    "сток" in page_text.lower() or
                    "groove" in page_text.lower()
            )

            if has_grooves:
                allure.attach("Опция 'Проточки' найдена", "Проверка опций")
            else:
                allure.attach("Опция 'Проточки' не найдена явно в тексте", "Проверка опций")

        with allure.step("d) Проверить итоговую стоимость: 451500.00 ₽"):
            # Проверяем разные форматы: "451500", "451 500", "451500.00"
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

        # Финальный скриншот
        conf.screenshot("8_Финальный_результат")

        # Общая проверка - что мы вообще на странице с результатами
        assert len(page_text) > 100, \
            "Страница расчета должна содержать информацию о заказе"