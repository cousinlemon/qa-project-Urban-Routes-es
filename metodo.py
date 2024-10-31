from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import localizadores
import time
from selenium.webdriver.common.by import By


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.from_field))
        # pass

    def set_from(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.from_field).send_keys(data.address_from)

    def set_to(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.to_field).get_property('value')

    # clic pedir un taxi
    def click_order_a_taxi_button(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.order_a_taxi_button).click()

    # clic en la tarifa confort
    def click_fare_comfort(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.fare_comfort))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.fare_comfort).click()

    def corroborate_rate(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.label).text

    # Rellenar el número de teléfono
    # clic en el campo numero de telefono
    def click_phone_number_button(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.phone_number_button).click()

    # llenar campo numero de telefono
    def set_number_field(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.number_field).send_keys(data.phone_number)
        time.sleep(3)

    # clic en el boton siguiente
    def click_button_next(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.button_next).click()

    # llenar el campo introducir codigo
    def set_confirmation_code(self, code):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.enter_code_field))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.enter_code_field).send_keys(code)
        time.sleep(3)

    # clic en el boton confirm
    def click_button_confirm_code(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.button_confirm_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.phone_number_button).text

    #  Agregar una tarjeta de crédito
    # clic boton metodo de pago
    def click_payment_method_button(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.payment_method_button).click()

    # clic en agregar tarjeta
    def click_add_card(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.add_card).click()
        # llenar numero de tarjeta

    def set_card_number_field(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.card_number_field).send_keys(data.card_number)

    # llenar codigo de tarjeta
    def set_card_code_field(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.card_code_field).send_keys(data.card_code)
        time.sleep(3)

    # presiona clic afuera
    def click_outside_box(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.click_out).click()

    # clic al boton agregar
    def click_add_button(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.add_button).click()

    # clic en el boton cerrar de la ventana metodo de pago
    def click_button_close_window_payment_method(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(localizadores.LUrbanRoutesPage.button_close_window_payment_method))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.button_close_window_payment_method).click()

    def check_close_button_is_enabled(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.button_close_window_payment_method).is_enabled()

    # Escribir un mensaje para el conductor
    # clic en mensaje para el conductor
    def click_message_for_driver(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.message_for_driver).click()

    def set_write_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.message_for_driver))
        # escribir mensaje para el coductor
        self.driver.find_element(*localizadores.LUrbanRoutesPage.write_message).send_keys(data.message_for_driver)
        time.sleep(2)

    def verify_message(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.write_message).get_property('value')

    # pedir manta y pañuelos
    def click_slider_round_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.slider_round_button))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.slider_round_button).click()
        time.sleep(2)

    def check_slider_button_is_enabled(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.slider_round_button).is_enabled()

        # Pedir 2 helados
    def click_ice_cream_counter(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.ice_cream_counter))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.ice_cream_counter).click()
        self.driver.find_element(*localizadores.LUrbanRoutesPage.ice_cream_counter).click()

    def verify_quantity_icecream(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.counter_value).text

    # clic en el boton pedir un taxi
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.order_taxi_button))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.order_taxi_button).click()

    def check_waiting_time_is_enabled(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.waiting_time).is_enabled()
