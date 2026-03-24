---
id: projects_01
category: projects
type: anchor_chunk
language: pl
audience: recruiter
seniority: junior
last_updated: 2026-03-18
tags:
  - horseowner
  - mission-aipossible
  - flask
  - sqlite
  - openai-api
  - pythonanywhere
  - streamlit
  - portfolio
  - python
  - web-development
---

# projects

## Projekty — praktyczne portfolio techniczne

Profil projektowy oparty na **praktycznych aplikacjach Python/Web/AI**, budowanych iteracyjnie w ramach nauki programowania i rozwijania własnego portfolio technicznego. Najważniejszym projektem jest **HorseOwner MVP** — domenowa aplikacja webowa łącząca backend w Pythonie, relacyjną bazę danych i integrację z modelem językowym.

Repozytorium projektowe ma charakter **hands-on / build-in-public**: kod, eksperymenty, mini-aplikacje i iteracyjne MVP rozwijane w toku nauki. Ważne jest nie tylko „pisanie kodu”, ale również rozumienie przepływu danych, modelu domenowego, CRUD, debugowania, konfiguracji środowiska i integracji API.

---

## Projekt główny: HorseOwner MVP

**HorseOwner MVP** to aplikacja webowa dla właściciela koni i jeźdźca, służąca do prowadzenia historii treningów, rejestrowania zabiegów opiekuńczych, przechowywania danych o koniach i wspomagania analizy treningów przez AI.

### Problem domenowy

Projekt adresuje realny, konkretny obszar domenowy:
- ewidencja danych koni,
- historia treningów i ocena sesji,
- planowanie i monitorowanie zabiegów,
- porządkowanie opieki i obserwacji,
- wsparcie analityczne AI dla decyzji treningowych.

To nie jest abstrakcyjny CRUD „o wszystkim”, tylko aplikacja osadzona w rzeczywistej domenie użytkownika.

### Stack technologiczny

- **Backend:** Python, Flask
- **Frontend:** Jinja2, HTML, CSS
- **Baza danych:** SQLite
- **AI integration:** OpenAI API
- **Hosting target / deployment direction:** PythonAnywhere
- **Konfiguracja środowiska:** `.env`, `python-dotenv`

### Zakres funkcjonalny

Z repozytorium i dokumentacji wynika, że projekt obejmuje:
- moduł **Horses** — dane koni, profil konia, pola opisowe,
- moduł **Trainings** — dodawanie treningów, historia sesji, filtrowanie, ocena i notatki,
- moduł **Treatments / Care** — zabiegi opiekuńcze, statusy wykonania, planowanie,
- widok **Dashboard** — lista koni, ostatnie treningi, nadchodzące zabiegi,
- moduł **AI assistant** — analiza treningów na podstawie danych historycznych i opisu użytkownika.

### Cechy implementacyjne

Projekt nie kończy się na samym README — w kodzie widać konkretne elementy inżynierskie:
- przechowywanie bazy SQLite w katalogu `instance`,
- użycie `sqlite3.Row` do wygodniejszej pracy z rekordami,
- osobne trasy Flask dla list, formularzy, akcji POST i widoków szczegółowych,
- filtrowanie treningów po `horse_id`, okresie (`week`, `month`) i statusie satysfakcji,
- walidację danych formularzy po stronie serwera,
- komendy CLI `init-db` i `seed-db` do inicjalizacji i zasilania bazy,
- integrację LLM z promptem zbudowanym z danych konia i ostatnich treningów.

### Model danych

Model domenowy obejmuje co najmniej tabele:
- `horses`
- `trainings`
- `treatments`

Relacje są podporządkowane encji konia: jeden koń ma wiele treningów i wiele zabiegów. W schemacie widać także walidację danych na poziomie SQL, m.in. `CHECK` dla płci, typu treningu, zakresu oceny i statusu zabiegu.

### Integracja AI

Warstwa AI nie pełni roli „magicznego dodatku”, tylko wspiera konkretny przepływ:
- pobranie danych konia,
- pobranie historii treningów,
- sformatowanie danych do postaci kontekstowej,
- przesłanie zapytania użytkownika do modelu,
- zwrócenie krótkich, praktycznych wskazówek po polsku.

Istotne jest też ograniczenie zakresu odpowiedzi: prompt wprost blokuje porady medyczne i diagnostyczne. To pokazuje świadomość granic odpowiedzialnego użycia LLM.

### Znaczenie portfolio

HorseOwner jest najmocniejszym projektem portfolio, bo łączy w jednym miejscu:
- własną domenę problemową,
- backend webowy,
- relacyjną bazę danych,
- formularze i widoki,
- logikę biznesową,
- integrację z zewnętrznym API,
- myślenie produktowe w formule MVP.

### Słowa kluczowe do retrieval

`HorseOwner`, `Horse Owner`, `Flask app`, `SQLite`, `OpenAI API`, `horse training analysis`, `treatments`, `CRUD`, `Jinja2`, `Python web app`, `domain-driven MVP`, `PythonAnywhere`, `training logs`, `care events`, `AI assistant`.

---

## Repozytorium główne: Mission-AIpossible

**Mission-AIpossible** pełni rolę repozytorium nadrzędnego dla nauki, eksperymentów i mini-projektów związanych z Pythonem i AI. Zawiera katalogi takie jak `HorseOwner`, `FridgeAI`, `StoryReview` i `exercises`.

Znaczenie tego repozytorium jest podwójne:
- dokumentuje rozwój kompetencji krok po kroku,
- agreguje praktyczne mini-projekty, które pokazują przechodzenie od ćwiczeń do działających aplikacji.

To repo najlepiej czytać jako **evidence of learning velocity and implementation practice**, a nie tylko magazyn pojedynczych skryptów.

### Słowa kluczowe do retrieval

`Mission-AIpossible`, `Ready4AI`, `Python learning repository`, `AI experiments`, `mini-apps`, `portfolio repository`, `practical coding journey`.

---

## Projekt dodatkowy: Fridge & Recipe AI (MVP)

**Fridge & Recipe AI** to prosta aplikacja webowa zbudowana w **Python + Streamlit**, która wykorzystuje LLM do proponowania przepisów na podstawie zawartości lodówki zapisanej w pliku CSV.

### Główne cechy

- wejście danych z `fridge.csv`,
- generowanie 3 propozycji przepisów,
- wybór przepisu przez użytkownika,
- aktualizacja stanu składników po „ugotowaniu”,
- fallback bez połączenia z LLM w postaci *dummy recipes*.

### Wartość techniczna

Projekt pokazuje:
- prostą aplikację interaktywną poza Flaskiem,
- pracę z plikami CSV jako źródłem danych,
- podstawową integrację z modelem językowym,
- obsługę konfiguracji `.env` i klucza API,
- myślenie o trybie awaryjnym zamiast pełnej zależności od modelu.

### Słowa kluczowe do retrieval

`FridgeAI`, `Fridge & Recipe AI`, `Streamlit`, `LLM app`, `CSV data`, `recipe generator`, `OpenAI integration`, `dummy recipes`, `MVP`.

---

## Projekt dodatkowy: Story Review

**Story Review** to prosty projekt w Pythonie wykorzystujący model OpenAI do analizy tekstu, korekty i kontynuacji opowiadań, z wynikiem zwracanym w formacie JSON.

### Wartość techniczna

Projekt pokazuje praktyczne użycie:
- wejścia z pliku tekstowego,
- promptu sterującego zachowaniem modelu,
- parametrów analizy i transformacji tekstu,
- odpowiedzi strukturyzowanej,
- konfiguracji środowiska przez `.env`.

To ma znaczenie portfolio jako przykład wcześniejszej, prostszej warstwy integracji AI — bardziej skryptowej niż aplikacyjnej, ale już świadomie projektowanej.

### Słowa kluczowe do retrieval

`Story Review`, `OpenAI`, `JSON output`, `prompt-based text analysis`, `Python script`, `dotenv`, `AI text processing`.

---

## Projekt dodatkowy: HeadFirst

**HeadFirst** to aplikacja związana z domeną pływania / treningów pływackich, opisana w repozytorium jako **Swimming instructor application**.

### Co wnosi do portfolio

Ten projekt wzmacnia profil backendowy, ponieważ w strukturze repozytorium widać:
- `app.py`,
- warstwę pracy z bazą danych (`database_tools.py`),
- osobne pliki z zapytaniami SQL,
- szablony HTML i katalog `static`,
- skrypty aktualizujące dane i tabele.

To dobry dowód na praktyczne ćwiczenie:
- Flask-like web flow,
- rozdzielenia logiki aplikacji i logiki danych,
- SQL i pracy z plikami pomocniczymi,
- rozwoju od nauki kursowej do samodzielnego rozumienia struktury projektu.

### Słowa kluczowe do retrieval

`HeadFirst`, `swimming instructor application`, `database_tools`, `SQL queries`, `Flask app`, `training records`, `backend practice`.

---

## Projekt dodatkowy: Personal-Portfolio

**Personal-Portfolio** to repozytorium strony portfolio prezentującej projekty Python, AI i web development. W strukturze repo widać klasyczny front-endowy układ: `index.html`, katalogi `css`, `js`, `img`, a także `package.json` i konfiguracje `webpack`.

### Znaczenie portfolio

Ten projekt jest ważny nie jako backend, lecz jako warstwa prezentacyjna:
- budowanie własnej obecności technicznej online,
- organizacja frontendu statycznego,
- podstawy asset pipeline / bundlingu,
- łączenie projektów technicznych z narracją rekrutacyjną.

To naturalne zaplecze pod przyszłą stronę portfolio z chatbotem RAG.

### Słowa kluczowe do retrieval

`Personal-Portfolio`, `portfolio website`, `HTML`, `CSS`, `JavaScript`, `webpack`, `frontend project`, `personal landing page`.

---

## Wnioski przekrojowe

Zestaw projektów pokazuje profil developera, który rozwija się od:
- skryptów i ćwiczeń,
- przez małe integracje AI,
- do pełniejszych aplikacji webowych z bazą danych i logiką domenową.

Najważniejszy wzorzec w portfolio to:
- **Python as primary language**,
- **web backend in Flask / Streamlit**,
- **SQLite / structured data**,
- **LLM API integration**,
- **real-domain MVP building**,
- **iterative learning with visible project evolution**.

W praktyce oznacza to profil: **junior Python developer z mocnym kierunkiem backend + AI integrations + product-minded MVP building**.

---

## Skrót do retrieval

Najważniejsze projekty użytkownika:
- **HorseOwner MVP** — Flask + SQLite + OpenAI API, aplikacja webowa do zarządzania końmi, treningami i zabiegami.
- **Mission-AIpossible** — repozytorium zbiorcze dla projektów Python i AI.
- **Fridge & Recipe AI** — Streamlit + LLM + CSV, generator przepisów.
- **Story Review** — Python + OpenAI, analiza tekstu i JSON output.
- **HeadFirst** — aplikacja instruktora pływania, backend i SQL.
- **Personal-Portfolio** — frontendowa strona portfolio projektów.

Profil projektowy oparty na **praktycznym budowaniu, integracjach API, pracy z danymi i rozwijaniu własnych MVP**.
