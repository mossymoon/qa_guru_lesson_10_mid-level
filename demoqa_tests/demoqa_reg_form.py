import os

from selene import browser, be, have
from selene.core import command

class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('automation-practice-form')
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        #     have.size_less_than_or_equal(3)
        # )
        # browser.all('id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('[id=firstName]').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('[id=lastName]').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('[id=userEmail]').should(be.blank).type(value)

    def fill_gender(self):
        browser.element('.custom-control-label').click()

    def fill_phone_number(self, value):
        browser.element('[id=userNumber]').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year).click()
        browser.element('.react-datepicker__month-select').send_keys(month).click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, value):
        browser.element('[id="subjectsInput"]').click().send_keys(value).press_enter()

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view)
        browser.element('[for="hobbies-checkbox-1"]').click()

    def select_picture(self, file):
        browser.element('#uploadPicture').set_value(os.path.abspath('../tests/resources/picture.jpeg'))

    def fill_current_address(self, address):
        browser.element('[id=currentAddress]').type(address)

    def select_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def select_city(self, city):
        browser.element('#city').perform(command.js.scroll_into_view)
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

class ResultRegistrationPage:

    def validate_form(self, inform, name, email, gender, phone, date_of_birth, subject, hobbie, picture, address, state, city):
        # Проверка формы
        browser.element('.modal-header').should(have.exact_text(inform))
        browser.all('.modal-body tr td')[1].should(have.exact_text(name))
        browser.all('.modal-body tr td')[3].should(have.exact_text(email))
        browser.all('.modal-body tr td')[5].should(have.exact_text(gender))
        browser.all('.modal-body tr td')[7].should(have.exact_text(phone))
        browser.all('.modal-body tr td')[9].should(have.exact_text(date_of_birth))
        browser.all('.modal-body tr td')[11].should(have.exact_text(subject))
        browser.all('.modal-body tr td')[13].should(have.exact_text(hobbie))
        browser.all('.modal-body tr td')[15].should(have.exact_text(picture))
        browser.all('.modal-body tr td')[17].should(have.exact_text(address))
        browser.all('.modal-body tr td')[19].should(have.text(f'{state} {city}'))

    def close_validation_window(self):
        browser.element('[id="closeLargeModal"]').click()
        # browser.element('.modal-dialog').should(be.absent)