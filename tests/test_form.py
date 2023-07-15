from demoqa_tests.demoqa_reg_form import RegistrationPage, ResultRegistrationPage


def test_dificult_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('ivan@co.com')
    registration_page.fill_gender()
    registration_page.fill_phone_number('9999999999')
    registration_page.fill_date_of_birth('1989', 'November', '28')
    registration_page.fill_subject('Maths')
    registration_page.fill_hobbies()
    registration_page.select_picture('picture.jpeg')
    registration_page.fill_current_address('Москва, ул. Тверская, дом 1')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit_form()
    result_registration_page = ResultRegistrationPage()
    result_registration_page.validate_form(
        inform='Thanks for submitting the form',
        name='Ivan Ivanov',
        email='ivan@co.com',
        gender='Male',
        phone='9999999999',
        date_of_birth='28 November,1989',
        subject='Maths',
        hobbie='Sports',
        picture='picture.jpeg',
        address='Москва, ул. Тверская, дом 1',
        state='NCR',
        city='Delhi')
    result_registration_page.close_validation_window()
