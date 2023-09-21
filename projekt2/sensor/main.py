import machine
import onewire
import ds18x20
import utime
import ujson

with open("config.json", "r") as config_file:
    config = ujson.load(config_file)

uart = machine.UART(0, baudrate=115200)
uart.init(tx=0, rx=1)

ow = onewire.OneWire(machine.Pin(config["pin"]))
temp_sensor = ds18x20.DS18X20(ow)

measurement_interval = config.get("interval", 900)

while True:
    temp_sensor.convert_temp()
    utime.sleep_ms(750)  

    roms = temp_sensor.scan()
    temperature_data = {}

    for rom in roms:
        temperature = temp_sensor.read_temp(rom)
        uart.write(f"{config['unit_id']} {rom.hex()} {temperature:.2f}\n")

    utime.sleep(measurement_interval)
