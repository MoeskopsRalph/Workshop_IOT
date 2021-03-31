# Workshop_IOT

Steeds meer dingen – auto’s, deurbellen, rookmelders, koelkasten, noem maar op – zijn via een ‘embedded systeem’ verbonden met het internet. Internet of Things (IoT) noemen we dat. Hoe werken die systemen en wat zijn de elementaire bouwstenen om een volwaardig IoT-device te maken? In deze workshop bouwen we een eerste IoT-device. We bouwen een koppeling tussen sociale media (Discord) en een “thing” met behulp van een Raspberry Pi-computertje verbonden met een temepratuur en luchtvochtigheid sensor, een bewegingssensor en een camera. Dit alles doen we op een laagdrempelige manier. Alles is beschikbaar zodat je thuis - met je eigen Raspberry Pi – het werk kan voortzetten, als je dat wil.

## Deel 1: Installeren en configureren Raspberry PI
Om de Raspberry PI zero te kunnen gebruiken voor het IOT project moet eerst het Raspberry Pi operating system geïnstaleerd worden (1.1). Daarna moet de wifi op de PI geconfigureerd worden en het IP genoteerd worden zodat vanaf een andere pc ingelogd kan worden op de PI via SSH (1.2). **Als je de workshop volgt tijdens de demo kan je stap 1.1 en 1.3 overslaan (dit is reeds geïnstaleerd). Wil je het project bij je thuis nabouwen, dan moet je eerst stap 1.1 doornemen om het project te kunnen opbouwen.**

### 1.1: Installeren Raspberry Pi OS

Om het project te kunnen bouwen moet het Raspberry PI operating system geïnstalleerd worden (op een SD-kaart van minstens 16GB die volledig geformateerd mag worden) samen met enkele instalatie pakketten. **Bij de PI die tijdens de workshop gebruikt wordt is dit reeds uitgevoerd. Om dit thuis ook te kunnen doen moet dit eerst nog op de SD-kaart geïnstalleerd worden.** Er zijn 2 opties voorzien om dit te doen. De eerste optie is om hier een geconfigureerde image te downloaden: http://pxl-ea-ict.be/iot/WorkshopIOT.zip, deze te unzippen en te installeren via de [Raspberry Pi Imager](https://www.raspberrypi.org/software/). De tweede optie is om via de [Raspberry Pi Imager](https://www.raspberrypi.org/software/) het Raspberry PI OS te installeren op de SD-kaart en vervolgens via een script de juiste pakketten te installeren. Als je voor de 2de optie kiest moet je na stap 1.2 ook stap 1.3 volgen.

Raadpleeg voor meer informatie over hoe de image te installeren de [website van Raspberry](https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility/). 

Wanneer je de melding krijgt dat het schrijven van de image succesvol afgerond is mag je de kaart verwijderen uit je PC en in de Raspberry PI Zero plaatsen. Sluit vervolgens het toetsenbord, muis, camera, HDMI scherm en de sensoren aan (bouw je de workshop van thuis lees dan hier de hardware vereisten). Stap 1.1 is nu succesvol afgerond. Je kan nu verder gaan met stap 1.2.

### 1.2: Raspberry PI Zero verbinden met wifi en noteren IP-adres

Start de Raspberry PI Zero op en klik recht boven op het wifi icoontje (1), controleer vervolgens of de wifi ingeschakeld is (2) en selecteer daarna het gewenste netwerk (3). Er zal nu een melding komen om een wachtwoord in te geven (4). Kies na het ingeven van het wachtwoord ten slotte voor OK (5).
![Deel1_1](/Documentatie/Afbeeldingen/Deel1_1.jpg)

De Raspberry is nu verbonden met het wifi netwerkt en er werd door de router een IP-adres toegewezen aan de Raspberry. Beweeg met de cursor over het wifi icoontje (1), er zal nu een text vlak verschijnen met daarin het IP-adres (2). Noteer dit IP_adres ergens wat je zal het later nodig hebben om via de PC te verbinden met de Raspberry.
![Deel1_2](/Documentatie/Afbeeldingen/Deel1_2.jpg)

Als je de workshop volgt tijdens de demo of als je in Stap1.1 voor een image gekozen hebt mag je nu naar Deel2 gaan. Heb je in Stap1.1 gekozen om met het script te werken, ga dan verder met Stap1.3.

### 1.3: Raspberry PI Zero instellen via script

**Als je in stap 1.1 koos om de instalatie uit te voeren met het script moet je deze stap nog volgen. Volg je de workshop tijdens de demo of heb je de voorgeconfigureerde image gebruikt? Dan kan je deze stap overslaan.**

Open de terminal op de Raspberry PI door op het terminal icoontje te klikken of door gebruik te maken van de sneltots ctrl+alt+t

![Deel1_3](/Documentatie/Afbeeldingen/Deel1_3.jpg)

Via de terminal gaan we nu het script van GitHub downloaden zodat de Raspberry weet welke files geïnstalleerd moeten worden en hoe alles geconfigureerd moet worden.

Geef onderstaand commando in om het script te downloaden: 
```bash
wget https://raw.github.com/MoeskopsRalph/Workshop_IOT/main/Code/install.sh
```

Maak het script uitvoerbaar voor een snelle configuratie van AutoInstall:
```bash
chmod +x install.sh
```

Start nu het script met onderstaand commando. Kijk hier bij wel na dat je het commando zeker start met sudo. Als je dit niet doet zal het script om een wachtwoord vragen. Als dit gebeurt geeft je ctrl+c in en start je het script opnieuw met sudo.
```bash
sudo ./install.sh
```

Als het script uitgevoerd is zal de Raspberry opnieuw opstarten. Stap 1.3 is nu succescvol uitgevoerd. Je kan nu verder gaan met Deel2.

## Deel 2: Aanmaken Discord BOT
Om met de Raspberry te comuniceren moet op het Discord profiel eerst een BOT aangemaakt worden die gebruikt kan worden op de Raspberry PI. Deze moet vervolgens gekopeld worden aan een server. 

Surf naar de [Discord Developer Console](https://discordapp.com/developers/applications/me) en log in met het Discord account waarop de BOT moet werken of maak een nieuw account aan. Kies nu voor New Application (1), geef de applicatie een naam naar keuze (2) en kies voor Create (3).

![Deel2_1](/Documentatie/Afbeeldingen/Deel2_1.jpg)

Nu de applicatie aangemaakt is kies je voor Bot (1), dan voor Add Bot (2) en ten slotte voor Yes, do it! (3).

![Deel2_2](/Documentatie/Afbeeldingen/Deel2_2.jpg)

Nu de bot aangemaakt is kan je de Token kopiëren (1). Bewaar deze ergens want we hebben deze straks nodig om toegang te krijgen tot de bot met de Raspberry PI.

![Deel2_3](/Documentatie/Afbeeldingen/Deel2_3.jpg)

Ga nu terug naar Genaral Information (1) en kies voor Copy bij de Client ID (2). 

![Deel2_4](/Documentatie/Afbeeldingen/Deel2_4.jpg)

Surf naar https://discordapp.com/oauth2/authorize?client_id=clientid&scope=bot&permissions=0 **en vervang clientid door jouw client id**. Kies op deze pagina aan welke server de Bot toegevoegd mag worden (1) en kies voor Autoriseren (2). Je moet wel beheersrechten heben tot deze server. (Het beste kan je voor deze test even een [nieuwe server aanmaken](https://support.discord.com/hc/nl/articles/204849977-Hoe-kan-ik-een-server-cre%C3%ABren-) op je [Discord account](https://discord.com/app).)

![Deel2_5](/Documentatie/Afbeeldingen/Deel2_5.jpg)

Je moet eventueel nog bevestigen dat je geen Robot bent. Als je dit gedaan hebt zie je normaal op de server nu de Bot staan die je hebt toegevoegd. Het enige wat we nu nog nodig hebben is de server-ID. Ga hiervoor eerst naar de gebruikersinstellingen (1).

![Deel2_6](/Documentatie/Afbeeldingen/Deel2_6.jpg)
 
 
Scrol nu in de linkerbalk naar beneden en kies voor weergave (1). Activeer nu de ontwikkelaarsmodus (2).

![Deel2_7](/Documentatie/Afbeeldingen/Deel2_7.jpg)

Klik ten slotte rechts op de servernaam (1) en Kopieer ID (2).

![Deel2_8](/Documentatie/Afbeeldingen/Deel2_8.jpg)

Bewaar deze ID ergens want we hebben deze straks nodig om te comuniceren met de server vanaf de Raspberry PI. Deel2 is nu volledig afgerond en je kan verder gaan met Deel3.

## Referenties
1. „Introducing Raspberry Pi Imager, our new imaging utility” RaspberryPi, 5 Maart 2020. [Online]. Available: https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility. [Geopend 30 Maart 2021].
2. „Python: Create a Discord Bot on Your Raspberry Pi Using Discord.py” The Ginger Ninja, 3 Mei 2017. [Online]. Available: https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi. [Geopend 28 Februari 2021].
3. „DHT11 Temperature and Humidity Sensor and the Raspberry Pi” The Ginger Ninja, 21 September 2017. [Online]. Available: https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi. [Geopend 28 Februari 2021].
4. „Getting started with the Camera Module” Projects RaspberryPi. [Online]. Available: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera. [Geopend 10 Maart 2021].
5. „The parent detector” Projects RaspberryPi. [Online]. Available: https://projects.raspberrypi.org/en/projects/parent-detector/3. [Geopend 15 Maart 2021].
