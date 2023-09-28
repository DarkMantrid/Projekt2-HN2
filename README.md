Projekt: Temperatursensor med Raspberry Pi Pico

   Detta projekt syftar till att skapa en temperaturövervakningslösning med två komponenter: en Raspberry Pi Pico som mäter temperatur och 
   skickar data via UART.

Innehållsförteckning:

 * Krav
 * Funktionalitet
 * Installation
 * Användning
 * Konfiguration


Krav
För att köra detta projekt behöver du följande hårdvarukomponenter:

 * En Raspberry Pi Pico med MicroPython
 * En eller flera DS18B20 temperatursensorer
 * En 4.7kOhm resistor
 * Kopplingsplatta och kopplingstrådar
 * En USB-kabel för Raspberry Pi Pico

Funktionalitet
Raspberry Pi Pico:

 * Läser temperatur från DS18B20-sensor regelbundet.
 * Rapporterar temperaturdata över UART med angivet protokoll.
 * Använder energisparande åtgärder mellan mätningarna.
 * Använder en konfigurationsfil för att hantera inställningar.

Installation
Klona detta GitHub-repo till din Raspberry Pi Zero:

$ bash
$ Copy code
$ git clone https://github.com/din-användarnamn/projekt-temperatursensor.git
Gå in i projektmappen:
$ bash
$ Copy code
$ cd projekt-temperatursensor
Följ anvisningarna i sensor-mappen för att konfigurera Raspberry Pi Pico.


Användning
När projektet är korrekt konfigurerat kan du använda det enligt följande:

Raspberry Pi Pico kommer att regelbundet mäta temperatur och skicka data via UART.


Konfiguration:

Anpassa konfigurationsfiler i sensor och hub-mapparna enligt dina behov. Se respektive README-filer för detaljerad information om konfiguration.
