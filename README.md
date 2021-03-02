# Workshop_IOT

## Deel 1: Installeren en configureren Raspberry PI
Alle uitleg hier plaatsen om de pi te verbinden met de wifi en eventueel de image te installeren voor thuis verder te kunnen gaan met het project.
## Deel 2: Aanmaken Discord BOT
Om met de Raspberry te comuniceren moet op het Discord profiel eerst een BOT aangemaakt worden die gebruikt kan worden op de Raspberry PI. Deze moet vervolgens gekopeld worden aan een server. 

Surf naar de [Discord Developer Console](https://discordapp.com/developers/applications/me) en log in met het Discord account waarop de BOT moet werken of maak een nieuw account aan. Kies nu voor New Application (1), geef de applicatie een naam naar keuze (2) en kies voor Create (3).

![Deel2_1](/Documentatie/Afbeeldingen/Deel2_1.jpg)

Nu de applicatie aangemaakt is kies je voor Bot (1) dan voor Add Bot (2) en ten slotte voor Yes, do it! (3).

![Deel2_2](/Documentatie/Afbeeldingen/Deel2_2.jpg)

Nu de bot aangemaakt is kan je de Token kopiëren. Bewaar deze ergens want we hebben deze straks nodig om toegang te krijgen tot de bot met de Raspberry PI.

![Deel2_3](/Documentatie/Afbeeldingen/Deel2_3.jpg)

Ga nu terug naar Genaral Information (1) en kies voor Copy bij de Client ID (2). 

![Deel2_4](/Documentatie/Afbeeldingen/Deel2_4.jpg)

Surf naar https://discordapp.com/oauth2/authorize?client_id=clientid&scope=bot&permissions=0 **en vervang clientid door jouw client id**. Kies op deze pagina aan welke server de Bot toegevoegd mag worden (1) en kies voor Autoriseren (2). Je moet wel beheersrechten heben tot deze server. (Het beste kan je voor deze test even een nieuwe server aanmaken op je Discord account.)

![Deel2_5](/Documentatie/Afbeeldingen/Deel2_5.jpg)

Je moet eventueel nog bevestigen dat je geen Robot bent. Als je dit gedaan hebt ben je helemaal klaar met Deel2. Normaal zie je op de server nu de Bot staan die je hebt toegevoegd.
