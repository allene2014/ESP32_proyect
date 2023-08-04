#proyecto micropython esp32
#autor Pacific logging
#version testing
#desarrollado by: departamento tecnologia (Ae)t

from machine import Pin, I2C, ADC
import time
import ssd1306
from ADS1115 import *
from utils import UtilsMpy

# Configurar conexión I2C y crear objeto de pantalla SSD1306
i2c = I2C(-1, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = 36
Adc = ADC(Pin(btn))
Adc.atten(ADC.ATTN_11DB)

# Definir lista de opciones del menú
menu_options = ["Analogicos", "Digitales", "Opcion 3"]
selected_option = 0
time_run = 0
ntr = 0

# Configurar ADS1115
addr = 72 # Dirección I2C del ADS1115
adc = ADS1115(addr, i2c)
adc.setVoltageRange_mV(ADS1115_RANGE_6144)
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_SINGLE)

# Define el valor de la resistencia que se utilizará para convertir la señal de corriente en una señal de voltaje
R = 250
def readCurrent(channel):
    # Configura el canal a medir
    adc.setCompareChannels(channel)
    # Inicia una medición única
    adc.startSingleMeasurement()
    # Espera a que la medición se complete
    while adc.isBusy():
        pass
    # Obtiene el resultado en voltios
    voltage = adc.getResult_V()
    # Calcula la corriente correspondiente utilizando la ley de Ohm (I = V / R)
    current = voltage / R
    return current

def handle_menu_selection(selected_option):
    if selected_option == 0:
        # Mostrar submenú para la opción 1
        current = readCurrent(ADS1115_COMP_0_GND)
        current1 = readCurrent(ADS1115_COMP_1_GND)
        current2 = readCurrent(ADS1115_COMP_2_GND)
        current3 = readCurrent(ADS1115_COMP_3_GND)
        oled.fill(0)
        #oled.text("I: {:.2f} mA".format(current * 1000), 0, 0)
        A0=current*1000
        A1=current1*1000
        A2=current2*1000
        A3=current3*1000
        oled.show()
        #submenu_options = [str(A0),str(A1),str(A2),str(A3),"Salir"]
        submenu_options = ["Salir"]
        selected_submenu_option = 0
        print(UtilsMpy.rtm(0,0))
        while True:
            # Leer el valor del botón utilizando el ADC
            raw_value = Adc.read()

            # Limpiar pantalla y mostrar título del submenú
            oled.fill(0)
            current = readCurrent(ADS1115_COMP_0_GND)
            current1 = readCurrent(ADS1115_COMP_1_GND)
            current2 = readCurrent(ADS1115_COMP_2_GND)
            current3 = readCurrent(ADS1115_COMP_3_GND)
            #oled.text("Analogicos", 0, 0)
            print (current * 1000)
            oled.text(str(current*1000), 0, 20)
            oled.text(str(current1*1000), 0, 30)
            oled.text(str(current2*1000), 0, 40)
            oled.text(str(current3*1000), 0, 50)

            # Mostrar las opciones del submenú resaltando la opción seleccionada actualmente
            if (raw_value >=3000 and raw_value <=3500):
                if selected_submenu_option == len(submenu_options) - 1:
                    # Si se seleccionó la opción de volver al menú principal, salir del bucle
                    break
                else:
                    # Aquí puedes agregar código para manejar la selección de las otras opciones del submenú
                    pass
            elif (raw_value >=1200 and raw_value <=1600):
                selected_submenu_option -=1
                if selected_submenu_option < 0:
                    selected_submenu_option=len(submenu_options)-1
            elif (raw_value >=2000 and raw_value <=25000):
                selected_submenu_option +=1
                if selected_submenu_option > len(submenu_options)-1:
                    selected_submenu_option = 0

            for index, option in enumerate(submenu_options):
                if index == selected_submenu_option:
                    oled.text("> " + option, 5, (index+1)*10)
                    time.sleep_ms(180)
                else:
                    oled.text(option ,5,(index+1)*10)
            oled.show()
    elif selected_option == 1:
        # Mostrar submenú para la opción 1
        submenu_options = ["I0", "I1","I2","I3","I4","I5","I6","I7","Salir"]
        selected_submenu_option = 0
        while True:
            # Leer el valor del botón utilizando el ADC
            raw_value = Adc.read()

            # Limpiar pantalla y mostrar título del submenú
            oled.fill(0)
            #oled.text("Digitales", 0, 0)

            # Mostrar las opciones del submenú resaltando la opción seleccionada actualmente
            if (raw_value >=3000 and raw_value <=3500):
                if selected_submenu_option == len(submenu_options) - 1:
                    # Si se seleccionó la opción de volver al menú principal, salir del bucle
                    break
                else:
                    # Aquí puedes agregar código para manejar la selección de las otras opciones del submenú
                    pass
            elif (raw_value >=1200 and raw_value <=1600):
                selected_submenu_option -=1
                if selected_submenu_option < 0:
                    selected_submenu_option=len(submenu_options)-1
            elif (raw_value >=2000 and raw_value <=25000):
                selected_submenu_option +=1
                if selected_submenu_option > len(submenu_options)-1:
                    selected_submenu_option = 0

            for index, option in enumerate(submenu_options):
                if index == selected_submenu_option:
                    oled.text("* " + option, 5, (index+1)*10)
                    time.sleep_ms(180)
                else:
                    oled.text(option ,5,(index+1)*10)
            oled.show()
        # Mostrar submenú para la opción 2
        #pass
    elif selected_option == 2:
        # Mostrar submenú para la opción 1
        submenu_options = ["ASD", "QWE", "Salir"]
        selected_submenu_option = 0
        while True:
            # Leer el valor del botón utilizando el ADC
            raw_value = Adc.read()

            # Limpiar pantalla y mostrar título del submenú
            oled.fill(0)
            oled.text("Conexiones", 0, 0)

            # Mostrar las opciones del submenú resaltando la opción seleccionada actualmente
            if (raw_value >=3000 and raw_value <=3500):
                if selected_submenu_option == len(submenu_options) - 1:
                    # Si se seleccionó la opción de volver al menú principal, salir del bucle
                    break
                else:
                    # Aqui puedes agregar codigo para manejar la seleccion de las otras opciones del submenu
                    pass
            elif (raw_value >=1200 and raw_value <=1600):
                selected_submenu_option -=1
                if selected_submenu_option < 0:
                    selected_submenu_option=len(submenu_options)-1
            elif (raw_value >=2000 and raw_value <=25000):
                selected_submenu_option +=1
                if selected_submenu_option > len(submenu_options)-1:
                    selected_submenu_option = 0

            for index, option in enumerate(submenu_options):
                if index == selected_submenu_option:
                    oled.text("> " + option, 5, (index+1)*10)
                    time.sleep_ms(180)
                else:
                    oled.text(option ,5,(index+1)*10)
            oled.show()
        # Mostrar submenú para la opción 3
        #pass

while True:
    # Leer el valor del botón utilizando el ADC
    raw_value = Adc.read()

    # Limpiar pantalla y mostrar título del menú
    oled.fill(0)
    oled.text("Main Menu", 0, 0)
    oled.text("Run:"+str(ntr), 0, 50)
    if ntr == 30:

        oled.contrast(0)

    # Mostrar las opciones del menú resaltando la opción seleccionada actualmente
    if (raw_value >=3000 and raw_value <=3500):
        handle_menu_selection(selected_option)
        #ntr = 0
        #oled.contrast(255)
        UtilsMpy.slp(oled,255)
        ntr = 0
    elif (raw_value >=1200 and raw_value <=1600):
        #ntr = 0
        #oled.contrast(255)
        UtilsMpy.slp(oled,255)
        ntr = 0
        selected_option -=1
        if selected_option < 0:
            selected_option=len(menu_options)-1

    elif (raw_value >=2000 and raw_value <=25000):
        #ntr = 0
        #oled.contrast(255)
        UtilsMpy.slp(oled,255)
        ntr = 0
        selected_option +=1

        if selected_option > len(menu_options)-1:
            selected_option = 0

    for index, option in enumerate(menu_options):
        if index == selected_option:
            oled.text("* " + option, 5, (index+1)*10)
            time.sleep_ms(180)
        else:
            oled.text(option ,5,(index+1)*10)
    oled.show()
    #time.sleep(1)
    #contador para controlar los segundo de actividad del dispositivo
    time_run += float(1.5)
    #print (time_run, 'antes while')
    while time_run == 6:
        time_run = 0
        ntr += 1
        print (ntr, 'incremento')
