# dalefinen_automation_devops

## ProjectPlan

Projektplan: Delfinen
Projektmedlemmar: Kristofer, Larissa & Viji
Projektöversikt:
Projektet syftar till att bygga en webb-app som använder sig av OpenWeatherMap API där vi ska skriva en funktion för att hämta specifik plats, det vill säga att användaren skriver in en plats för att hämta ut data. Datan kommer att visas med en graf över temperaturer för angiven plats, detta kommer att ske med verktyget Streamlit.
Funktionalitet och flöde:
Användaren matar in en plats som då ska generera temperatur och visar ett resultat av temperaturen på den angivna platsen.
Arbetsflöde:
1.	API-anrop:
En förfrågan skickas till OpenWeatherMap API för att hämta temperaturen baserat på en angiven plats, detta görs av användaren.
2.	Databehandling:
En funktion bearbetar den mottagna datan och presenterar temperaturen för en angiven plats som en graf.
3.	Grundläggande UX-design:
Webb-appen kommer att ha en enkel och användarvänlig design för att säkerställa att användaren snabbt kan interagera med applikationen.
4.	Unit-tester för API och databehandling:
Unit-tester implementeras för att säkerställa att API-anropet returnerar korrekt data och att bearbetningsfunktionen fungerar som förväntat. Exempel: Testar att applikationen kan hämta korrekt plats som användaren anger.
5.	CI/CD-pipeline via GitHub Actions:
Projektet integreras med en GitHub Actions-pipeline där tester körs automatiskt. Testerna inkluderar exempelvis validering av korrekt angiven plats.
6.	Docker-containerisering:
När testerna klarar förväntade resultat, containeriseras applikationen med Docker för att skapa en enhetlig miljö inför distribution.
7.	Distribution via Azure:
Den Docker-containeriserade appen distribueras till Azure, där användarna får tillgång till applikationen med ett förväntat och pålitligt resultat.
Mål och förväntat resultat:
Målet är att utveckla en stabil webb-app som uppfyller användarnas förväntningar i form av användarvänlighet och korrekta API-anrop samt databehandling. Appen testas och distribueras i en DevOps-pipeline med GitHub Actions och Azure.

