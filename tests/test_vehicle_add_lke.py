import time
import allure
import pytest
from pages.producers_list_page import ProducersList
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания ТС Экс: номер - ТС-timestamp, модель - Монорамник, выпуск - 2023г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - Рандом, '
                    'добавить/убрать - 2 и 1 водителя, эксплуотация - останавливаем/востанавливаем/завершаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_transport_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Монорамное ТС")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТС-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2022")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 30.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.exploitation_finish_button)
    add_ts.click_button(add_ts.yes_button, do_assert=True)
    add_ts.click_button(add_ts.ok_button)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания ПП Экс: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 2023г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - Рандом, '
                    'добавить/заменить - Тягач, эксплуотация - останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_trailer_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2022")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 100.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление тягача
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания тягача Экс: номер - ТЯГ-timestamp, модель - Тягач, выпуск - 2023г, собственник'
                    ' - Подрядчик, добавить/убрать - 2 и 1 водителя, эксплуотация - останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractor1_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания тягача Экс: номер - ТЯГ-timestamp, модель - Тягач, выпуск - 2023г, собственник'
                    ' - Подрядчик, добавить/заменить - ПП, эксплуотация - останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractor2_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление полуприцепа
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form", wait_type="visible")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form", wait_type="visible")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания ТС Внутр. ПВ: номер - ВТС-timestamp, модель - Монорамник, выпуск - 2023г, '
                    'собственник - Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - '
                    'Рандом, добавить/убрать - 2 и 1 водителя, эксплуотация - останавливаем/востанавливаем/завершаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_transport_inner_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Монорамное ТС")
    # Выбор владельца ТС
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВТС-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2022")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 30.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.exploitation_finish_button)
    add_ts.click_button(add_ts.yes_button, do_assert=True)
    add_ts.click_button(add_ts.ok_button)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания ПП Внутр. ПВ: номер - ВПП-timestamp, модель - Полуприцеп, выпуск - 2023г, '
                    'собственник - Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - '
                    'Рандом, добавить/заменить - Тягач, эксплуотация - останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_trailer_inner_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Выбор владельца ТС
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2022")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 100.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление тягача
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания Тягача Внутр. ПВ: номер - ВТЯГ-timestamp, модель - Тягач, выпуск - 2023г, '
                    'собственник - Подрядчик, добавить/убрать - 2 и 1 водителя, эксплуотация - '
                    'останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractor1_inner_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Выбор владельца ТС
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКЭ. Тест создания Тягача Внутр. ПВ: номер - ВТЯГ-timestamp, модель - Тягач, выпуск - 2023г, '
                    'собственник - Подрядчик, добавить/заменить - ПП, эксплуотация - останавливаем/востанавливаем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractor2_inner_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Выбор владельца ТС
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление полуприцепа
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    # Конец теста
