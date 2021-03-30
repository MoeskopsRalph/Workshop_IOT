# Workshop_IOT

## Deel 1: Installeren en configureren Raspberry PI
Om de Raspberry PI zero te kunnen gebruiken voor het IOT project moet eerst het Raspberry Pi operating system geïnstaleerd worden (1.1). Daarna moet de wifi op de PI geconfigureerd worden en het IP genoteerd worden zodat vanaf een andere pc ingelogd kan worden op de PI via SSH (1.2). **Als je de workshop volgt tijdens de demo kan je stap 1 overslaan (dit is reeds geïnstaleerd). Wil je het project bij je thuis nabouwen, dan moet je eerst stap 1 doornemen om het project te kunnen opbouwen.**

### 1.1: Installeren Raspberry Pi OS

Om het project te kunnen bouwen moet het Raspberry PI operating system geïnstalleerd worden (op een SD-kaart van minstens 16GB die volledig geformateerd mag worden) samen met enkele instalatie pakketten. **Bij de PI die tijdens de workshop gebruikt wordt is dit reeds uitgevoerd. Om dit thuis ook te kunnen moet dit eerst nog op de SD-kaart geïnstalleerd worden.** Er zijn 2 opties voorzien om dit te doen. De eerste optie is om hier een geconfigureerde image te downloaden, deze te unzippen en te installeren via de [Raspberry Pi Imager](https://www.raspberrypi.org/software/). De tweede optie is om via de [Raspberry Pi Imager](https://www.raspberrypi.org/software/) het Raspberry PI OS te installeren op de SD-kaart en vervolgens via een script de juiste pakketten te installeren. Als je voor de 2de optie kiest moet je na stap 1.2 ook stap 1.3 volgen.

Wanneer je de melding krijgt dat het schrijven van de image succesvol afgerond is mag je de kaart verwijderen uit je PC en in de Raspberry PI Zero plaatsen. Sluit vervolgens het toetsenbord, muis, camera en HDMI scherm aan. Stap 1.1 is nu succesvol afgerond. Je kan verder gaan met stap 1.2.

### 1.2: Raspberry PI Zero verbinden met wifi en noteren IP-adres


## Deel 2: Aanmaken Discord BOT
Om met de Raspberry te comuniceren moet op het Discord profiel eerst een BOT aangemaakt worden die gebruikt kan worden op de Raspberry PI. Deze moet vervolgens gekopeld worden aan een server. 

Surf naar de [Discord Developer Console](https://discordapp.com/developers/applications/me) en log in met het Discord account waarop de BOT moet werken of maak een nieuw account aan. Kies nu voor New Application (1), geef de applicatie een naam naar keuze (2) en kies voor Create (3).

![Deel2_1](/Documentatie/Afbeeldingen/Deel2_1.jpg)

Nu de applicatie aangemaakt is kies je voor Bot (1), dan voor Add Bot (2) en ten slotte voor Yes, do it! (3).

![Deel2_2](/Documentatie/Afbeeldingen/Deel2_2.jpg)

Nu de bot aangemaakt is kan je de Token kopiëren. Bewaar deze ergens want we hebben deze straks nodig om toegang te krijgen tot de bot met de Raspberry PI.

![Deel2_3](/Documentatie/Afbeeldingen/Deel2_3.jpg)

Ga nu terug naar Genaral Information (1) en kies voor Copy bij de Client ID (2). 

![Deel2_4](/Documentatie/Afbeeldingen/Deel2_4.jpg)

Surf naar https://discordapp.com/oauth2/authorize?client_id=clientid&scope=bot&permissions=0 **en vervang clientid door jouw client id**. Kies op deze pagina aan welke server de Bot toegevoegd mag worden (1) en kies voor Autoriseren (2). Je moet wel beheersrechten heben tot deze server. (Het beste kan je voor deze test even een nieuwe server aanmaken op je Discord account.)

![Deel2_5](/Documentatie/Afbeeldingen/Deel2_5.jpg)

Je moet eventueel nog bevestigen dat je geen Robot bent. Als je dit gedaan hebt ben je helemaal klaar met Deel2. Normaal zie je op de server nu de Bot staan die je hebt toegevoegd.
 
## Referenties
1. „Python: Create a Discord Bot on Your Raspberry Pi Using Discord.py,” The Ginger Ninja, 3 Mei 2017. [Online]. Available: https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi. [Geopend 28 Februari 2021].
