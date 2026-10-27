import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    select_taxi_locator = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    select_comfort_tariff_locator = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']/..")
    select_phone_number_locator = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    phone_number_field = (By.ID, 'phone')
    select_next_locator = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    select_confirm_locator = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    confirm_phone_number_locator = (By.XPATH, "//div[@class='np-text']")
    select_payment_method_locator = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    select_add_card_locator = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_field = (By.ID, 'number')
    code_field = (By.ID, 'code')
    select_add_locator = (By.XPATH, "//button[ text()='Agregar']")
    confirm_added_card_locator = (By.XPATH, "//input[@class='checkbox']")
    comment_field = (By.ID, 'comment')
    confirm_comment_locator = (By.ID, 'comment')
    select_add_requirement_switch_locator = (By.XPATH, "//div[text()='Manta y pañuelos']/following::input[1]")
    confirm_add_requirement_checkbox_locator = (By.XPATH, "//div[contains(@class, 'r-sw-container') and .//div[text()='Manta y pañuelos']]//input")
    select_add_ice_cream_locator = (By.XPATH, "//div[text()='Helado']/following::div[@class='counter-plus'][1]")
    confirm_added_ice_cream_locator = (By.XPATH, "//div[@class='counter-value']")
    select_reserve_locator = (By.CLASS_NAME, 'smart-button')
    confirm_reserve_locator = (By.XPATH, "//div[@class='order-header-title']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def select_taxi_button(self):
        self.driver.find_element(*self.select_taxi_locator).click()

    def select_comfort_tariff_button(self):
        self.driver.find_element(*self.select_comfort_tariff_locator).click()

    def get_comfort_tariff_class(self):
        return self.driver.find_element(*self.select_comfort_tariff_locator).get_attribute('class')

    def select_phone_number_modal(self):
        self.driver.find_element(*self.select_phone_number_locator).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def select_next_button(self):
        self.driver.find_element(*self.select_next_locator).click()

    def set_phone_code(self, phone_code):
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def select_confirm_button(self):
        self.driver.find_element(*self.select_confirm_locator).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.confirm_phone_number_locator).text

    def select_payment_method(self):
        self.driver.find_element(*self.select_payment_method_locator).click()

    def select_add_card(self):
        self.driver.find_element(*self.select_add_card_locator).click()

    def set_card(self, number):
            self.driver.find_element(*self.card_field).send_keys(number)

    def set_code(self, code):
        field = self.driver.find_element(*self.code_field)
        field.send_keys(code)
        field.send_keys(Keys.TAB)

    def select_add(self):
        self.driver.find_element(*self.select_add_locator).click()

    def get_added_card(self):
        return self.driver.find_element(*self.confirm_added_card_locator).is_selected()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def get_comment(self):
        return self.driver.find_element(*self.confirm_comment_locator).get_property('value')

    def select_add_requirement_switch(self):
        self.driver.find_element(*self.select_add_requirement_switch_locator).click()

    def get_add_requirement(self):
        return self.driver.find_element(*self.confirm_add_requirement_checkbox_locator).is_selected()

    def select_add_ice_cream(self):
        for i in range(2):
            self.driver.find_element(*self.select_add_ice_cream_locator).click()

    def get_add_ice_cream(self):
        return self.driver.find_element(*self.confirm_added_ice_cream_locator).text

    def select_reserve(self):
        self.driver.find_element(*self.select_reserve_locator).click()

    def get_reserve(self):
        return self.driver.find_element(*self.confirm_reserve_locator).text

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    @pytest.fixture
    def setup_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        return routes_page

    def test_initial_address(self, setup_route):
        routes_page = setup_route
        address_from = data.address_from
        address_to = data.address_to
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_tariff (self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_comfort_tariff_button()
        assert routes_page.get_comfort_tariff_class() == 'tcard active'

    def test_phone_number(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_phone_number_modal()
        routes_page.set_phone_number(data.phone_number)
        routes_page.select_next_button()
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.select_confirm_button()
        assert routes_page.get_phone_number() == data.phone_number

    def test_payment_method(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_payment_method()
        routes_page.select_add_card()
        routes_page.set_card(data.card_number)
        routes_page.set_code(data.card_code)
        routes_page.select_add()
        assert routes_page.get_added_card()

    def test_add_comment(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_comfort_tariff_button()
        routes_page.set_comment(data.message_for_driver)
        assert routes_page.get_comment() == data.message_for_driver

    def test_add_requirement(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_comfort_tariff_button()
        routes_page.select_add_requirement_switch()
        assert routes_page.get_add_requirement()

    def test_add_ice_cream(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_comfort_tariff_button()
        routes_page.select_add_ice_cream()
        assert routes_page.get_add_ice_cream() == '2'

    def test_add_reserve(self, setup_route):
        routes_page = setup_route
        routes_page.select_taxi_button()
        routes_page.select_comfort_tariff_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.select_next_button()
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.select_confirm_button()
        routes_page.select_reserve()
        assert 'El conductor llegará en' in routes_page.get_reserve()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
