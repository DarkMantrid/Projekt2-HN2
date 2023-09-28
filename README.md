Temperaturmätning med Raspberry Pi Pico (G-delen)
Detta är ett projekt där en Raspberry Pi Pico används för att mäta temperatur med en DS18B20-sensor och skicka den avlästa temperaturen via UART-kommunikation. Följ dessa instruktioner för att konfigurera och använda systemet.


Innehållsförteckning
 * Krav
 * Installation
 * Användning
 * Konfiguration
 * Bidrag


Krav

För att använda projektet behöver du följande komponenter och programvara:

 * Raspberry Pi Pico
 * DS18B20 temperatursensor
 * En dator med MicroPython och Thonny IDE installerat
 * UART-kommunikation mellan Raspberry Pi Pico och en annan enhet (t.ex. en dator)


Installation

Följ dessa steg för att installera och konfigurera projektet:


Anslut DS18B20-sensorn: Anslut DS18B20-sensorn till Raspberry Pi Pico enligt tillverkarens anvisningar.

Ladda upp MicroPython: Använd Thonny IDE för att ladda upp MicroPython-firmware till Raspberry Pi Pico. Du kan hitta detaljerade instruktioner om hur du gör detta på Raspberry Pi Pico webbplats.

Kopiera koden: Kopiera innehållet från sensor/main.py-filen i detta projekt till din Raspberry Pi Pico. Du kan använda Thonny IDE för att skapa en ny Python-fil och klistra in koden där.

Anslut till UART: Anslut Raspberry Pi Pico till din dator via UART (Universal Asynchronous Receiver-Transmitter) för att övervaka seriell kommunikation och visa temperaturen som läses från sensorn. Använd ett terminalprogram som PuTTY (Windows) eller minicom (Linux) och ställ in rätt serieport och baudrate.

Användning

När du har installerat och konfigurerat projektet kan du använda det på följande sätt:

 * Raspberry Pi Pico kommer att regelbundet mäta temperaturen från DS18B20-sensorn.
 * Temperaturen kommer att skickas över UART och visas i ditt terminalprogram.
 * Om du vill anpassa mätintervallen eller andra inställningar, redigera koden i main.py-filen enligt dina behov.

Konfiguration

Du kan anpassa projektet genom att redigera koden i main.py-filen på Raspberry Pi Pico. Ändra mätintervall, lägg till fler sensorer eller ändra UART-inställningar enligt dina specifika krav.
