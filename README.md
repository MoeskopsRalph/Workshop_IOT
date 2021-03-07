# Workshop_IOT

## Deel 1: Installeren en configureren Raspberry PI
Om de Raspberry PI zero te kunnen gebruiken voor het IOT project moet eerst het Raspberry Pi operating system geïnstaleerd worden (1.1). Daarna moet de wifi op de PI geconfigureerd worden en het IP genoteerd worden zodat vanaf een andere pc ingelogd kan worden op de PI via SSH (1.2). **Als je de workshop volgt tijdens de demo kan je stap 1 overslaan (dit is reeds geïnstaleerd). Wil je het project bij je thuis nabouwen, dan moet je eerst stap 1 doornemen om het project te kunnen opbouwen.**

### 1.1: Installeren Raspberry Pi OS

Om het project te kunnen bouwen moet het Raspberry PI operating system geïnstalleerd worden samen met enkele instalatie pakketten en er moeten ook enkele configuraties aangepast worden. Bij de PI die tijdens de workshop gebruikt wordt is dit reeds uitgevoerd. Om dit thuis ook te kunnen doen is er een image gemaakt die je gewoon op een SD-kaart kan plaatsen. Hier zijn alle nodige configuraties al op uitgevoerd. 

Download de image via deze link: **NOG VOORZIEN VAN LINK NAAR IMAGE** en installeer op je PC een image flasher zoals [Etcher](https://www.balena.io/etcher/). Gebruik voor het installeren van de image een SD-kaart van minstens 16GB die volledig geformateerd mag worden. 

Open nu het image flash programma dat je geïnstaleerd hebt en kies voor flash from file en selecteer de image die je zojuist gedownload hebt (Workshop_IOT.img) (1), kies bij select target de SD-kaart waar het programma op geplaatst mag worden (2) en kies ten slotte voor Flash (3).

![Deel1_1](/Documentatie/Afbeeldingen/Deel1_1.jpg)

Wanneer je de melding krijgt dat het flashen van de image succesvol afgerond is mag je de kaart verwijderen uit je PC en in de Raspberry PI Zero plaatsen. Stap 1.1 is nu succesvol afgerond. Je kan verder gaan met stap 1.2.

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
