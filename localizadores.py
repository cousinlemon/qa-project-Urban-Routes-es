from selenium.webdriver.common.by import By

class LUrbanRoutesPage:
    # Seleccionar ruta de destino
    from_field = (By.CSS_SELECTOR, '#from')
    to_field = (By.CSS_SELECTOR, '#to')

    # Seleccionar la tarifa Comfort y accesorios
    order_a_taxi_button = (By.XPATH, "//button[@type='button'][@class='button round' and text()='Pedir un taxi']")
    fare_comfort = (By.CSS_SELECTOR, '.tcard-icon img[alt="Comfort"]')
        # revision1 : before : fare_comfort = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img")
    blankets_and_tissues_label = (By.CLASS_NAME, "r-sw-label")
        # revision 1 : before : label = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]")


    # llenar el número de teléfono.
    phone_number_button = (By.CLASS_NAME,"np-text")
    number_field = (By.CSS_SELECTOR,'#phone')
    button_next = (By.XPATH, "//button[@type='submit'][@class='button full']")
    enter_code_field = (By.XPATH,"//*[@id='code']")
    # button_confirm_code = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
    button_confirm_code = (By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")

    # Agregar una tarjeta de crédito
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, "//div[text()='Agregar tarjeta']")
        # revision 1 add_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//input[@id='code' and @name='code' and @class='card-input']")
    click_out = (By.CLASS_NAME, "card-number-label")
    add_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'full') and text()='Agregar']")
        # revision 1 add_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
    button_close_window_payment_method = (By.XPATH, "//div[@class='section active' and .//div[text()='Método de pago']]//button[@class='close-button section-close']")
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
    # waiting_time = (By.CLASS_NAME, "order-header-title")
    waiting_time = (By.CLASS_NAME, "order-header-time")
    driver_asigned =(By.CLASS_NAME, "order-number")