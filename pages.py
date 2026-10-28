from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

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
    code_field = (By.CSS_SELECTOR, '.card-code-input input')
    select_add_locator = (By.XPATH, "//button[ text()='Agregar']")
    confirm_added_card_locator = (By.ID, 'card-1')
    close_modal_locator = (By.XPATH, "//div[@class='head' and text()='Método de pago']/parent::div/button")
    comment_field = (By.ID, 'comment')
    confirm_comment_locator = (By.ID, 'comment')
    select_add_requirement_switch_locator = (By.XPATH, "//div[text()='Manta y pañuelos']/following::span[1][@class='slider round']")
    confirm_add_requirement_checkbox_locator = (By.XPATH, "//div[contains(@class, 'r-sw-container') and .//div[text()='Manta y pañuelos']]//input")
    select_add_ice_cream_locator = (By.XPATH, "//div[text()='Helado']/following::div[@class='counter-plus'][1]")
    confirm_added_ice_cream_locator = (By.XPATH, "//div[@class='counter-value']")
    select_reserve_locator = (By.CLASS_NAME, 'smart-button')
    confirm_reserve_locator = (By.XPATH, "//div[@class='order-header-title']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_field))
        element.send_keys(from_address)

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
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.select_taxi_locator))
        element.click()

    def select_comfort_tariff_button(self):
        self.driver.find_element(*self.select_comfort_tariff_locator).click()

    def get_comfort_tariff_class(self):
        return self.driver.find_element(*self.select_comfort_tariff_locator).get_attribute('class')

    def select_phone_number_modal(self):
        self.driver.find_element(*self.select_phone_number_locator).click()

    def set_phone_number(self, phone_number):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_number_field))
        field.send_keys(phone_number)

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
        field = self.driver.find_element(*self.card_field)
        field.send_keys(number)
        field.send_keys(Keys.TAB)

    def set_code(self, code):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_field))
        field.send_keys(code)
        field.send_keys(Keys.TAB)
        self.driver.save_screenshot('debug.png')

    def select_add(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_add_locator))
        element.click()

    def get_added_card(self):
        return self.driver.find_element(*self.confirm_added_card_locator).is_selected()

    def close_modal(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_modal_locator))
            element.click()
        except TimeoutException:
            self.driver.save_screenshot('debug.png')
            raise

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def get_comment(self):
        return self.driver.find_element(*self.confirm_comment_locator).get_property('value')

    def select_add_requirement_switch(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_add_requirement_switch_locator))
        element.click()

    def get_add_requirement(self):
        return self.driver.find_element(*self.confirm_add_requirement_checkbox_locator).is_selected()

    def select_add_ice_cream(self):
        for i in range(2):
            self.driver.find_element(*self.select_add_ice_cream_locator).click()

    def get_add_ice_cream(self):
        return self.driver.find_element(*self.confirm_added_ice_cream_locator).text

    def select_reserve(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_reserve_locator))
        element.click()

    def get_reserve(self):
        element = WebDriverWait(self.driver, 40).until(EC.text_to_be_present_in_element(self.confirm_reserve_locator, 'El conductor llegará en'))
        return self.driver.find_element(*self.confirm_reserve_locator).text