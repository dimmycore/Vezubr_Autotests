import time
import allure
import pytest
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.story("Smoke test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест редактирования пользователя: '
                    '1) создание пользователя и фильтрация по его фамилии, '
                    '2) редактируем: ФИО - ФИО-timestamp, тип - API, роль - Логист, тлф - Рандом, '
                    'email - Etimestamp@mail.ru, часовой пояс - Абиджан')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_first_user_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке добавления пользователя
    profile.click_button(profile.add_user_button)
    
    user = User(base.driver)
    surname = f"Ф-{base.get_timestamp()}"
    # Выбор типа пользователя
    user.dropdown_without_input(user.user_type_select, "Пользователь")
    # Выбор роли пользователя
    user.dropdown_without_input(user.user_role_select, "Администратор")
    # Выбор часового пояса пользователя
    time.sleep(2)
    user.dropdown_without_input(user.user_timezone_select, "Asia/Yekaterinburg")
    time.sleep(2)
    # Ввод фамилии пользователя
    user.input_in_field(user.surname_input, surname)
    # Ввод имени пользователя
    user.input_in_field(user.name_input, f"И-{base.get_timestamp()}")
    # Ввод отчества пользователя
    user.input_in_field(user.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод номера телефона пользователя
    user.click_button(user.phone_input)
    user.input_in_field(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    # Ввод email пользователя
    user.input_in_field(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    # Клик по кнопке создания пользователя
    user.click_button(user.create_user_button, do_assert=True)
    # Подтверждение создания пользователя
    user.click_button(user.confirm_add_button)
    
    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter, surname)
    time.sleep(1)
    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    
    # Редактирование данных пользователя
    user.click_button(user.user_edit_button, wait="form")
    # Изменение типа пользователя на "API"
    user.dropdown_without_input(user.user_type_select, "API")
    # Сброс роли пользователя
    user.click_button(user.user_role_reset)
    # Изменение роли пользователя на "Логист"
    user.dropdown_without_input(user.user_role_select, "Логист")
    # Изменение часового пояса на "Africa/Abidjan"
    time.sleep(3)
    user.dropdown_without_input(user.user_timezone_select, "Africa/Abidjan")
    time.sleep(3)
    # Изменение фамилии пользователя
    user.backspace_and_input(user.surname_input, f"Ф-{base.get_timestamp()}")
    # Изменение имени пользователя
    user.backspace_and_input(user.name_input, f"И-{base.get_timestamp()}")
    # Изменение отчества пользователя
    user.backspace_and_input(user.patronymic_input, f"О-{base.get_timestamp()}")
    # Изменение номера телефона пользователя
    user.click_button(user.phone_input)
    user.backspace_and_input(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    # Изменение email пользователя
    user.backspace_and_input(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    # Сохранение изменений
    user.click_button(user.save_edit_user_button, do_assert=True)
    # Подтверждение изменений
    user.click_button(user.confirm_add_button)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест управления ответственностью за КА: '
                    '1) создание пользователя и фильтрация по его фамилии, '
                    '2) назначение на ГВ - Все, делегировать - Шестому, отвязать - Всех.')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_responsible_fo_client_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке добавления пользователя
    profile.click_button(profile.add_user_button)
    
    user = User(base.driver)
    surname = f"Ф-{base.get_timestamp()}"
    # Выбор типа пользователя
    user.dropdown_without_input(user.user_type_select, "Пользователь")
    # Выбор роли пользователя
    user.dropdown_without_input(user.user_role_select, "Администратор")
    # Выбор часового пояса пользователя
    time.sleep(2)
    user.dropdown_without_input(user.user_timezone_select, "Asia/Yekaterinburg")
    time.sleep(2)
    # Ввод фамилии пользователя
    user.input_in_field(user.surname_input, surname)
    # Ввод имени пользователя
    user.input_in_field(user.name_input, f"И-{base.get_timestamp()}")
    # Ввод отчества пользователя
    user.input_in_field(user.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод номера телефона пользователя
    user.click_button(user.phone_input)
    user.input_in_field(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    # Ввод email пользователя
    user.input_in_field(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    # Клик по кнопке создания пользователя
    user.click_button(user.create_user_button, do_assert=True)
    # Подтверждение создания пользователя
    user.click_button(user.confirm_add_button)
    
    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter, surname)
    time.sleep(1)
    # Переход к профилю пользователя
    profile.click_button(profile.user_link, wait="form")
    
    # Клик по кнопке добавления ответственности
    user.click_button(user.add_responsible_button, wait="lst")
    # Назначение ответственности за всех клиентов
    user.click_button(user.all_client_on_checkbox)
    # Подтверждение назначения ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")
    
    # Отмена назначения ответственности за всех контрагентов
    user.click_button(user.all_contractor_off_checkbox)
    # Делегирование ответственности шестому пользователю
    user.click_button(user.delegate_responsibility_button, wait="lst")
    user.click_button(user.user_checkbox, 6)
    # Подтверждение делегирования ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")
    
    # Отмена назначения ответственности за всех контрагентов
    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.off_responsibility_button)
    # Подтверждение отмены ответственности
    user.click_button(user.confirm_off_responsible_button, wait="lst", do_assert=True)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест управления ответственностью за КА: '
                    '1) создание пользователя и фильтрация по его фамилии, '
                    '2) назначение на ПВ - Все, делегировать - Шестому, отвязать - Всех.')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_responsible_fo_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке добавления пользователя
    profile.click_button(profile.add_user_button)
    
    user = User(base.driver)
    surname = f"Ф-{base.get_timestamp()}"
    # Выбор типа пользователя
    user.dropdown_without_input(user.user_type_select, "Пользователь")
    # Выбор роли пользователя
    user.dropdown_without_input(user.user_role_select, "Администратор")
    # Выбор часового пояса пользователя
    time.sleep(2)
    user.dropdown_without_input(user.user_timezone_select, "Asia/Yekaterinburg")
    time.sleep(2)
    # Ввод фамилии пользователя
    user.input_in_field(user.surname_input, surname)
    # Ввод имени пользователя
    user.input_in_field(user.name_input, f"И-{base.get_timestamp()}")
    # Ввод отчества пользователя
    user.input_in_field(user.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод номера телефона пользователя
    user.click_button(user.phone_input)
    user.input_in_field(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    # Ввод email пользователя
    user.input_in_field(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    # Клик по кнопке создания пользователя
    user.click_button(user.create_user_button, do_assert=True)
    # Подтверждение создания пользователя
    user.click_button(user.confirm_add_button)
    
    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter, surname)
    time.sleep(1)
    # Переход к профилю пользователя
    profile.click_button(profile.user_link, wait="form")
    
    # Клик по кнопке добавления ответственности
    user.click_button(user.add_responsible_button, wait="lst")
    # Переход на вкладку "Перевозчики"
    user.click_button(user.producer_tab, wait="lst")
    time.sleep(2)
    # Назначение ответственности за всех перевозчиков
    user.click_button(user.all_producer_on_checkbox)
    # Подтверждение назначения ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")
    
    # Клик по выпадающему списку выбора роли КА
    user.click_button(user.contractor_role_select)
    # Выбор перевозчика
    user.click_button(user.select_producer)
    
    # Отмена назначения ответственности за всех перевозчиков
    user.click_button(user.all_contractor_off_checkbox)
    # Делегирование ответственности шестому пользователю
    user.click_button(user.delegate_responsibility_button, wait="lst")
    user.click_button(user.user_checkbox, 6)
    # Подтверждение делегирования ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")
    
    # Отмена назначения ответственности за всех перевозчиков
    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.off_responsibility_button)
    # Подтверждение отмены ответственности
    user.click_button(user.confirm_off_responsible_button, wait="lst", do_assert=True)
    # Конец теста
