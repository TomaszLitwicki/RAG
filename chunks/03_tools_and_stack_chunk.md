---
id: tools_and_stack_01
category: tools_and_stack
type: anchor_chunk
language: pl
audience: recruiter
seniority: junior
last_updated: 2026-03-18
tags:
  - python
  - flask
  - streamlit
  - django
  - sqlite
  - mysql
  - sqlalchemy
  - git
  - github
  - pycharm
  - powershell
  - linux
  - pandas
  - beautifulsoup
  - requests
  - pythonanywhere
  - openai-api
  - ollama
  - rag
  - tooling
---

# tools_and_stack

## Narzędzia i stack technologiczny

Profil technologiczny Tomasza opiera się na praktycznym stacku **Python + web backend + relacyjne bazy danych + narzędzia developerskie + integracje AI**. Używane technologie nie są przypadkowym zbiorem haseł, tylko zestawem realnie wykorzystywanym podczas budowy projektów, nauki frameworków, pracy z bazą danych, debugowania i wdrażania własnych aplikacji.

Najmocniej widoczny jest kierunek: **junior Python Developer rozwijający się w stronę backendu, aplikacji webowych i AI-enabled products**, z dużym naciskiem na samodzielność techniczną, środowisko pracy i praktyczne rozumienie narzędzi.

---

## Core stack — technologie używane najaktywniej

### Python
Główny język programowania i centrum całego stacku.

Zakres praktycznego użycia:
- logika aplikacji
- przetwarzanie danych
- praca z plikami CSV i JSON
- komunikacja z API
- backend webowy
- skrypty pomocnicze i automatyzacja prostych zadań

Python jest tutaj nie tylko językiem nauki, ale realnym narzędziem do budowania działających MVP i rozwijania portfolio projektowego.

### Flask
Podstawowy framework backendowy.

Zastosowanie:
- routing HTTP
- obsługa metod `GET`, `POST`, `PUT`, `DELETE`
- renderowanie szablonów Jinja2
- formularze i logika serwera
- proste endpointy CRUD
- podstawy obsługi błędów i hooków request lifecycle

Flask pełni rolę głównego frameworka aplikacyjnego w projektach webowych, szczególnie w **HorseOwner MVP**.

### SQLite
Domyślna baza danych w projektach MVP i aplikacjach edukacyjno-praktycznych.

Zastosowanie:
- lokalna persystencja danych
- szybkie prototypowanie
- relacyjne modelowanie danych
- integracja z aplikacją Flask

To podstawowa baza wykorzystywana w aplikacjach takich jak HorseOwner.

### Git + GitHub
Podstawowy system kontroli wersji i repozytoryjnej organizacji pracy.

Zakres użycia:
- `git add`, `git commit`, `git branch`, `merge`
- `push`, `fetch`, praca ze zdalnym repozytorium
- historia zmian i dokumentowanie progresu
- `.gitignore`, workflow commitów, podstawy rozwiązywania konfliktów

GitHub pełni jednocześnie rolę miejsca publikacji projektów i dowodu praktyki programistycznej.

---

## Backend, web i API stack

### Jinja2 + HTML + CSS
Warstwa prezentacyjna dla aplikacji Flask.

Zastosowanie:
- szablony HTML renderowane po stronie serwera
- formularze użytkownika
- podstawowa struktura interfejsu
- stylowanie i układ stron

To nie jest profil frontend-first, ale warstwa UI jest wystarczająco rozwinięta do budowy działających aplikacji webowych.

### REST API i HTTP
Istotna część stacku backendowego.

Zakres:
- `request / response`
- metody HTTP: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- `request.json`, `jsonify(...)`
- `request.args.get(...)`
- rozumienie `path parameters` i `query parameters`
- podstawy projektowania REST API

### requests
Biblioteka używana do komunikacji HTTP i integracji z zewnętrznymi usługami.

Zastosowanie:
- pobieranie danych z internetu
- wywołania API
- odbiór danych JSON
- wsparcie prostych integracji i web scrapingu

### Streamlit
Dodatkowy framework użyty do szybkiego budowania prostych aplikacji interaktywnych.

Najważniejszy przykład:
- **Fridge & Recipe AI** — MVP oparte na Python + Streamlit + LLM

### Django (podstawy)
Framework znany na poziomie podstaw architektury i pierwszych ćwiczeń.

Znaczenie w stacku:
- świadomość większego frameworka webowego
- rozumienie struktury projektu, modeli i migracji
- kierunek do dalszego rozwoju, ale nie główny framework projektowy na dziś

---

## Data i database stack

### SQL
Relacyjny fundament pracy z danymi.

Zakres:
- `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- `JOIN`
- relacje 1-do-wielu
- podstawy integralności danych
- `CHECK`, `DEFAULT`, `NULL`
- podstawy `REGEXP`

### MySQL
Druga baza danych w stacku — używana na poziomie podstaw i integracji z Pythonem.

Zakres:
- lokalne połączenia do bazy
- podstawy pracy z serwerem bazodanowym
- świadomość różnic względem SQLite
- użycie z poziomu `mysql.connector`

### mysql.connector
Najważniejsze praktyczne ogniwo Python ↔ MySQL.

Zakres:
- `connect()`
- `cursor()`
- `execute()`
- `fetchone()`, `fetchmany()`, `fetchall()`
- `commit()`

### SQLAlchemy
Podstawy ORM jako kolejny krok po ręcznym SQL.

Znaczenie:
- rozumienie idei ORM
- modelowanie danych przez klasy
- podstawy CRUD na modelach
- pierwsze relacje i nawigacja po encjach

### pandas
Biblioteka do analizy i obróbki danych.

Zakres:
- `read_csv()`
- `head()`, `tail()`, `info()`, `describe()`
- filtrowanie danych
- `value_counts()`, `groupby()`
- czyszczenie i konwersje typów
- podstawowe agregacje

To element stacku wspierający analizę danych, ćwiczenia i pracę na plikach tabelarycznych.

---

## Web scraping i data acquisition

### BeautifulSoup
Biblioteka do parsowania HTML.

### requests + BeautifulSoup
Najczęściej używany duet do prostego web scrapingu.

Zastosowanie:
- pobieranie HTML
- parsowanie drzewa dokumentu
- wyszukiwanie elementów po tagach, klasach i atrybutach
- ekstrakcja tekstu i linków
- świadomość ograniczeń i zasad `robots.txt`

To nie jest główny filar portfolio, ale ważny komponent narzędziowy w nauce Pythona i pracy z danymi.

---

## Developer tools i środowisko pracy

### PyCharm
Główne IDE do codziennej pracy.

W praktyce wykorzystywane do:
- pisania i organizacji kodu
- debugowania krok po kroku
- pracy z terminalem
- integracji z Gitem
- refaktoryzacji i inspekcji błędów

### PowerShell / terminal / CLI
Bardzo ważna część workflow.

Zakres:
- uruchamianie skryptów
- aktywacja środowisk wirtualnych
- instalacja pakietów
- praca z Gitem
- podstawowa nawigacja po systemie plików
- rozumienie pagera `less`

### Linux basics
Podstawowa znajomość środowiska Linux, istotna przy pracy z hostingiem i terminalem.

Zakres:
- katalog roboczy
- komendy nawigacyjne
- odczyt wyników poleceń
- podstawowe rozumienie systemu plików

### Virtual environments (`.venv`)
Stały element workflow projektowego.

Znaczenie:
- izolacja zależności
- porządek między projektami
- przewidywalność środowiska uruchomieniowego

### pip / PyPI / requirements
Podstawowy mechanizm zarządzania zależnościami.

Zakres:
- `pip install`
- `pip list`
- praca z pakietami z PyPI
- odtwarzanie środowiska projektu

### `.env` + `python-dotenv`
Podstawowa praktyka zarządzania konfiguracją.

Zastosowanie:
- przechowywanie kluczy API
- separacja sekretów od kodu źródłowego
- bezpieczniejsze uruchamianie aplikacji lokalnie i na hostingu

### Obsidian
Narzędzie wspierające organizację wiedzy technicznej.

Rola w stacku:
- prywatna baza wiedzy
- notatki z nauki
- porządkowanie pojęć, technologii i roadmapy
- zaplecze merytoryczne pod przyszłe portfolio RAG

### Jupyter / VS Code
Narzędzia uzupełniające, używane pomocniczo do testowania fragmentów kodu i eksploracji danych.

---

## Hosting, deployment i środowiska uruchomieniowe

### PythonAnywhere
Najważniejszy kierunek deploymentu w obecnych projektach webowych.

Znaczenie:
- hosting aplikacji Flask
- praktyczna nauka różnic między środowiskiem lokalnym i serwerowym
- konfiguracja zależności i zmiennych środowiskowych
- pierwsze doświadczenia z publikacją aplikacji online

### Windows + Linux
Stack pracy jest hybrydowy:
- lokalna nauka i development na Windows
- podstawy wdrożenia i pracy serwerowej w środowisku Linux

To ważny element profilu, bo pokazuje gotowość do przechodzenia między kodem, środowiskiem lokalnym i hostingiem.

---

## AI stack i tooling wokół LLM

### OpenAI API
Najważniejsze aktywnie używane API AI.

Zastosowanie:
- analiza tekstu
- generowanie odpowiedzi i rekomendacji
- integracje AI w projektach takich jak Story Review, FridgeAI i HorseOwner
- wymuszanie struktury odpowiedzi, w tym JSON

### Prompt engineering
Istotna część praktycznego stacku AI.

Zakres:
- budowanie kontekstu dla modelu
- sterowanie formatem odpowiedzi
- ograniczanie zakresu odpowiedzi modelu
- przygotowanie danych wejściowych do analizy przez LLM

### RAG
Koncepcja rozwijana jako element portfolio i przyszłego chatbota rekrutacyjnego.

Zakres:
- retrieval z własnych materiałów
- budowa bazy wiedzy o projektach i kompetencjach
- łączenie wyszukiwania z generowaniem odpowiedzi

### Embeddings / structured outputs / tool calling
Znajomość pojęciowa i rozwijana praktycznie w obszarze AI workflow.

### Ollama
Podstawowa orientacja w lokalnym uruchamianiu modeli językowych.

Znaczenie:
- wstęp do pracy z local LLMs
- kierunek dalszego rozwoju w stronę bardziej niezależnego stacku AI

---

## Charakter stacku

Ten stack nie jest „szeroki dla samej szerokości”. Jego logika jest spójna:

- **Python** jako główny język
- **Flask / Streamlit** jako narzędzia do szybkiego budowania działających aplikacji
- **SQLite / MySQL / SQLAlchemy** jako warstwa danych
- **Git / PyCharm / terminal / .venv** jako codzienny workflow developerski
- **OpenAI API / prompt engineering / RAG** jako warstwa AI
- **PythonAnywhere** jako pierwszy realny kanał wdrożeniowy

To profil osoby, która buduje kompetencje przez realne użycie narzędzi, a nie przez same deklaracje technologiczne.

---

## Skrót do retrieval

Najważniejsze elementy stacku Tomasza:
- **Language:** Python
- **Backend:** Flask
- **UI / templating:** Jinja2, HTML, CSS
- **Interactive app framework:** Streamlit
- **Databases:** SQLite, MySQL
- **ORM:** SQLAlchemy
- **HTTP / API:** requests, REST API, JSON
- **Data:** pandas
- **Scraping:** BeautifulSoup
- **Version control:** Git, GitHub
- **IDE / tooling:** PyCharm, PowerShell, terminal, `.venv`, pip, `.env`
- **Knowledge workflow:** Obsidian
- **Deployment:** PythonAnywhere
- **AI:** OpenAI API, prompt engineering, RAG, embeddings, structured outputs, Ollama

### Słowa kluczowe do retrieval

`tools and stack`, `technology stack`, `Python`, `Flask`, `Streamlit`, `SQLite`, `MySQL`, `SQLAlchemy`, `Git`, `GitHub`, `PyCharm`, `PowerShell`, `Linux`, `pandas`, `BeautifulSoup`, `requests`, `PythonAnywhere`, `OpenAI API`, `prompt engineering`, `RAG`, `Ollama`, `developer tooling`, `junior Python developer`.
