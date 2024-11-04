- Hugo Martinez : grupo 14, sprint 8
- ---

# Urban Routes app

selenium automatization

 ---
### Indice:
- Descripción
- Test o Lista de comprobación
- Archivos de proyecto
- Paquetes
- Instrucciones para las pruebas
---

# •••••••

---
### DESCRIPCIÓN
Este proyecto de pruebas automatizadas tiene como objetivo validar el flujo completo de solicitar un taxi en la aplicación Urban Routes. Abarca cada paso necesario en el proceso de pedido, asegurando que se cumplan las interacciones y validaciones necesarias para una experiencia fluida en la aplicación.

Este conjunto de pruebas garantiza la interacción correcta de todos los elementos del flujo de solicitud de taxi en la aplicación

---
### LISTA DE COMPROBACIÓN
- test_set_route.
- test_choose_fare.
- test_add_credit_card.
- test_write_a_message_to_the_driver.
- test_order_a_blanket_and_tissues.
- test_order_2_ice_creams.
- test_fill_phone_number. - incluye Obtención y validación del código de confirmación
- test_boton_final_pedir_un_taxi.

---
### ARCHIVOS DE PROYECTO
- .gitignore
- README.md
- data.py
- helper_sms_code.py
- UrbanRoutesPage.py
- main.py

.
- browser_setup (archivo usado para resolver una situación con el driver en el ambiente probado)

el codigo esta optimizado para que los revisores lo puedan correr sin usar el archivo browser_setup.

---
### PAQUETES DE PYTHON
- pytest
- requests
- selenium

---
### Otros paquetes
- Chrome webdriver (https://googlechromelabs.github.io/chrome-for-testing/)
  - usa la version estable
  - tarta que el driver y el navegador chrome tengan la misma version)
---
### INSTRUCCIONES
Para correr estas pruebas usamos Chrome:
- asegurate de tener los paquetes y el webdriver para chrome
- actualiza la url en el archivo data.py : aqui lo puedes hacer( https://tripleten.com/trainer/qa-engineer/lesson/0f23a649-8168-41d4-be6a-19fab7206f66/ )
- ve al archivo main: puedes correr las pruebas