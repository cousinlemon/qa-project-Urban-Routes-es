from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import time
from selenium.webdriver.common.by import By


class LUrbanRoutesPage:
    # Seleccionar ruta de destino
    from_field = (By.CSS_SELECTOR, '#from')
    to_field = (By.CSS_SELECTOR, '#to')

    # Seleccionar la tarifa Comfort y accesorios
    order_a_taxi_button = (By.XPATH, "//button[@type='button'][@class='button round' and text()='Pedir un taxi']")
    fare_comfort = (By.CSS_SELECTOR, '.tcard-icon img[alt="Comfort"]')
    blankets_and_tissues_label = (By.CLASS_NAME, "r-sw-label")

    # llenar el número de teléfono.
    phone_number_button = (By.CLASS_NAME, "np-text")
    number_field = (By.CSS_SELECTOR, '#phone')
    button_next = (By.XPATH, "//button[@type='submit'][@class='button full']")
    enter_code_field = (By.XPATH, "//*[@id='code']")
    # button_confirm_code = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
    button_confirm_code = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")

    # Agregar una tarjeta de crédito
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, "//div[text()='Agregar tarjeta']")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//input[@id='code' and @name='code' and @class='card-input']")
    click_out = (By.CLASS_NAME, "card-number-label")
    add_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'full') and text()='Agregar']")
    button_close_window_payment_method = (By.XPATH,
                                          "//div[@class='section active' and .//div[text()='Método de pago']]//button[@class='close-button section-close']")
    verified_card = (By.CLASS_NAME, "pp-value-text")

    # Mensaje para el conductor
    message_for_driver = (By.XPATH, "//label[@for='comment' and contains(text(), 'Mensaje para el conductor...')]")
    write_message = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")
    confirm_message = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")

    # Pedir una manta y pañuelos
    slider_round_button = (By.XPATH, "//span[@class='slider round'][1]")

    # Pedir 2 helados
    ice_cream_counter = (By.CLASS_NAME, "counter-plus")
    counter_value = (By.CLASS_NAME, "counter-value")

    # clic al boton para buscar un taxi.
    order_taxi_button = (By.CLASS_NAME, "smart-button-main")
    modal_taxi = (By.CLASS_NAME, "order-header-title")
    waiting_time = (By.CLASS_NAME, "order-header-time")
    driver_asigned = (By.CLASS_NAME, "order-number")
    details_button_with_burger_icon = (By.CSS_SELECTOR, "button.order-button img[src*='burger.7f0605c2.svg']")
    driver_details_box = (By.CSS_SELECTOR, ".order-details.shown")


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LUrbanRoutesPage.from_field))

    def set_from(self):
        self.driver.find_element(*LUrbanRoutesPage.from_field).send_keys(data.address_from)

    def set_to(self):
        self.driver.find_element(*LUrbanRoutesPage.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*LUrbanRoutesPage.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*LUrbanRoutesPage.to_field).get_property('value')

    # clic pedir un taxi
    def click_order_a_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LUrbanRoutesPage.order_a_taxi_button))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LUrbanRoutesPage.order_a_taxi_button))
        self.driver.find_element(*LUrbanRoutesPage.order_a_taxi_button).click()

    # clic en la tarifa confort
    def click_fare_comfort(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LUrbanRoutesPage.fare_comfort))
        self.driver.find_element(*LUrbanRoutesPage.fare_comfort).click()

    def corroborate_rate(self):
        return self.driver.find_element(*LUrbanRoutesPage.blankets_and_tissues_label).text

    # campo numero de telefono
    def click_phone_number_button(self):
        self.driver.find_element(*LUrbanRoutesPage.phone_number_button).click()

    # llenar campo numero de telefono
    def set_number_field(self):
        self.driver.find_element(*LUrbanRoutesPage.number_field).send_keys(data.phone_number)
        # time.sleep(3) # rev 1 pausas para ver el proceso, los elementos que esperan trabajan con webdriverwait

    # clic en el boton siguiente
    def click_button_next(self):
        self.driver.find_element(*LUrbanRoutesPage.button_next).click()

    # llenar el campo introducir codigo
    def set_confirmation_code(self, code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LUrbanRoutesPage.enter_code_field))
        self.driver.find_element(*LUrbanRoutesPage.enter_code_field).send_keys(code)
        # time.sleep(3) # pausa forzada para visualizar el proceso, no para cargar elementos

    # clic en el boton confirm
    def click_button_confirm_code(self):
        self.driver.find_element(*LUrbanRoutesPage.button_confirm_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*LUrbanRoutesPage.phone_number_button).text

    #  Agregar una tarjeta de crédito
    # clic boton metodo de pago
    def click_payment_method_button(self):
        self.driver.find_element(*LUrbanRoutesPage.payment_method_button).click()

    # clic en agregar tarjeta
    def click_add_card(self):
        self.driver.find_element(*LUrbanRoutesPage.add_card).click()

    # llenar numero de tarjeta
    def set_card_number_field(self):
        self.driver.find_element(*LUrbanRoutesPage.card_number_field).send_keys(data.card_number)

    # llenar codigo de tarjeta
    def set_card_code_field(self):
        self.driver.find_element(*LUrbanRoutesPage.card_code_field).send_keys(data.card_code)
        # time.sleep(3) # pausa forzada para visualizar el proceso, no para cargar elementos

    # presiona clic afuera
    def click_outside_box(self):
        self.driver.find_element(*LUrbanRoutesPage.click_out).click()

    # clic al boton agregar
    def click_add_button(self):
        self.driver.find_element(*LUrbanRoutesPage.add_button).click()

    # clic en el boton cerrar de la ventana metodo de pago
    def click_button_close_window_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LUrbanRoutesPage.button_close_window_payment_method))
        self.driver.find_element(*LUrbanRoutesPage.button_close_window_payment_method).click()

    def check_close_button_is_enabled(self):
        return self.driver.find_element(*LUrbanRoutesPage.button_close_window_payment_method).is_enabled()

    # verify card number display after added()
    def verify_card_number_after_added(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "pp-value-text")))
        return element.text

    # verify_card_number_written
    def verify_card_number_written_before_added(self):
        # campo card input
        return self.driver.find_element(*LUrbanRoutesPage.card_number_field).get_attribute("value")

    # Escribir un mensaje para el conductor
    # clic en mensaje para el conductor
    def click_message_for_driver(self):
        self.driver.find_element(*LUrbanRoutesPage.message_for_driver).click()

    def set_write_message(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LUrbanRoutesPage.message_for_driver))
        # escribir mensaje para el coductor
        self.driver.find_element(*LUrbanRoutesPage.write_message).send_keys(data.message_for_driver)
        # time.sleep(2) # pausa forzada para visualizar el proceso, no para cargar elementos

    def verify_message(self):
        return self.driver.find_element(*LUrbanRoutesPage.write_message).get_property('value')

    # pedir manta y pañuelos
    def click_slider_round_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LUrbanRoutesPage.slider_round_button))
        self.driver.find_element(*LUrbanRoutesPage.slider_round_button).click()
        # time.sleep(2) # pausa forzada para visualizar el proceso, no para cargar elementos

    def check_slider_button_is_enabled(self):
        return self.driver.find_element(*LUrbanRoutesPage.slider_round_button).is_enabled()

        # Pedir 2 helados
    def click_ice_cream_counter(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LUrbanRoutesPage.ice_cream_counter))
        self.driver.find_element(*LUrbanRoutesPage.ice_cream_counter).click()
        self.driver.find_element(*LUrbanRoutesPage.ice_cream_counter).click()

    def verify_quantity_icecream(self):
        return self.driver.find_element(*LUrbanRoutesPage.counter_value).text

    # clic en el boton pedir un taxi
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LUrbanRoutesPage.order_taxi_button))
        self.driver.find_element(*LUrbanRoutesPage.order_taxi_button).click()

    def check_waiting_time(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LUrbanRoutesPage.waiting_time))
        return self.driver.find_element(*LUrbanRoutesPage.slider_round_button).is_displayed()

    def asigned_driver(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.invisibility_of_element_located(LUrbanRoutesPage.waiting_time))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LUrbanRoutesPage.driver_asigned))

    def driver_asignation_is_display(self):
        return self.driver.find_element(*LUrbanRoutesPage.driver_asigned).is_displayed()

    def driver_details(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LUrbanRoutesPage.details_button_with_burger_icon))
        self.driver.find_element(*LUrbanRoutesPage.details_button_with_burger_icon).click()

    def driver_details_box(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LUrbanRoutesPage.driver_details_box))

        return self.driver.find_element(*LUrbanRoutesPage.driver_details_box).is_displayed()

