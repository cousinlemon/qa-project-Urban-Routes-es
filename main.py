import helper_sms_code
from UrbanRoutesPage import UrbanRoutesPage
import data
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

''' NOTE TO SELF: optimization review checklist - Do NOT DELETE
browser setup override to be able to wrok the proyect

NOW -     place      - review config
off - browser_setup.py : should be off : inactive as comment
off - main.py - browser_call at imports : should be off : comment (2 lines)
on - main.py    cls.driver : point to webdriver should be on (and browser call off)
on - main.py - function phone and code : should be on '''

# from browser_setup import open_browser
# browser_call = open_browser()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        # cls.driver = browser_call
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        self.routes_page.wait_for_load_home_page()
        self.routes_page.set_from()
        self.routes_page.set_to()
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # prueba seleccionar tarifa comfort
    def test_choose_fare(self):
        self.routes_page.click_order_a_taxi_button()
        self.routes_page.click_fare_comfort()
        assert self.routes_page.corroborate_rate() == "Manta y pañuelos"

    # prueba agregar tarjeta de credito
    def test_add_credit_card(self):
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number_field()
        self.routes_page.set_card_code_field()
        self.routes_page.click_outside_box()
        assert self.routes_page.verify_card_number_written_before_added() == data.card_number  #  verifu de card number before adding
        self.routes_page.click_add_button()  # agrega la tarjeta y cierra el modal
        self.routes_page.click_button_close_window_payment_method()
        assert self.routes_page.verify_card_number_after_added() == "Tarjeta"  #  rev2 con este campo solo e sposible ver el tipo de pago, no el numero de tarjeta  # el campo pp-value-text contiene la palabra Tarjeta : revision en colerning con Yuliana
        assert self.routes_page.check_close_button_is_enabled()

    # prueba escribir un mensaje para el controlador
    def test_write_a_message_to_the_driver(self):
        self.routes_page.click_message_for_driver()
        self.routes_page.set_write_message()
        assert self.routes_page.verify_message() == data.message_for_driver

    # prueba pedir manta y pañuelos
    def test_order_a_blanket_and_tissues(self):
        self.routes_page.click_slider_round_button()
        assert self.routes_page.check_slider_button_is_enabled()

    # prueba Pedir 2 helados
    def test_order_2_ice_creams(self):
        self.routes_page.click_ice_cream_counter()
        assert self.routes_page.verify_quantity_icecream() == '2'

    # prueba  Rellenar el número de teléfono
    def test_fill_phone_number(self):
        self.routes_page.click_phone_number_button()
        self.routes_page.set_number_field()
        self.routes_page.click_button_next()
        # Obtención y validación del código de confirmación
        code = helper_sms_code.retrieve_phone_code(driver=self.driver)

        # Introducir el código de confirmación si es válido
        self.routes_page.set_confirmation_code(code)
        self.routes_page.click_button_confirm_code()
        assert self.routes_page.get_phone_number() == data.phone_number

    # Aparece el modal para buscar un taxi.
    def test_boton_final_pedir_un_taxi(self):
        self.routes_page.click_order_taxi_button()

        self.routes_page.modal_order_taxi()  # rev3  : verificar el modal driver
        assert self.routes_page.modal_order_taxi()  # rev3 : verificar el modal driver

        self.routes_page.check_waiting_time()
        assert self.routes_page.check_waiting_time()

    # NEW : test to verify driver assignation
    def test_view_driver_assignation(self):
        self.routes_page.asigned_driver()
        assert self.routes_page.driver_asignation_is_display()

        self.routes_page.driver_details()  # new : open order details
        assert self.routes_page.driver_details_box()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
