import time
import utime
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C
from csv_module import * 

PINS_I2C_BME688 = {"sda": 4, "scl": 5}

i2c = PimoroniI2C(**PINS_I2C_BME688)
bme = BreakoutBME68X(i2c)

while True:
    
    #définitions des variable, elles renvoient toutes un int équivalent à leur unité de mesure
    temperature, pressure, humidity, gas, status, _, _,= bme.read()
    heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"
    life_t = "good" if temperature > 50 and temperature < -50 else "critical"
    #NB : Si la pression est trop basse alors il peut y avoir un risque de météo dangereuse
    life_p = "good" if pressure > 92000 and pressure < 160000 else "critical" 
    life_h = "good" if humidity > 40 and humidity < 70 else "critical"
    life_g = "good" if gas < 100000 else "critical"
    
    date = utime.localtime(utime.time())
 
    #J'écris toute les mesures
    ajouter_valeur(f"{date[0]}/{date[1]}/{date[2]} à {date[3]}h{date[4]}min{date[5]}sec :")
    ajouter_valeur(f"{round(temperature,2)}c")
    ajouter_valeur(f"{round(pressure,2)}Pa")
    ajouter_valeur(f"{round(humidity,2)}%")
    ajouter_valeur(f"{round(gas,2)}Ohms")
    gerer_limitation_valeurs()
    
    print(f"{date[0]}/{date[1]}/{date[2]} à {date[3]}h{date[4]}min{date[5]}sec : {round(temperature,2)}c, {round(pressure,2)}Pa, {round(humidity,2)}%, {round(gas,2)} Ohms\n")
    
    time.sleep(0.2)

    
        
    
    
    


