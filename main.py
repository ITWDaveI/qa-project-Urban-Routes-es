import data
import pytest
from selenium import webdriver
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage

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
        routes_page.select_phone_number_modal()
        routes_page.set_phone_number(data.phone_number)
        routes_page.select_next_button()
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.select_confirm_button()
        routes_page.set_comment(data.message_for_driver)
        routes_page.select_reserve()
        assert 'El conductor llegará en' in routes_page.get_reserve()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
