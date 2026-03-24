---
id: learning_path_01
category: learning_path
type: anchor_chunk
language: pl
audience: recruiter
seniority: junior
last_updated: 2026-03-18
tags:
  - learning-path
  - python
  - backend
  - flask
  - sql
  - mysql
  - sqlite
  - git
  - linux
  - testing
  - debugging
  - ai
  - llm
  - rag
  - obsidian
---

# learning_path

## Ścieżka nauki i kierunek rozwoju

Ścieżka nauki Tomasza ma charakter **projektowy, iteracyjny i świadomie uporządkowany**. Nie polega na przypadkowym zbieraniu technologii, ale na przechodzeniu przez kolejne warstwy kompetencji: od podstaw języka, przez backend i bazy danych, aż do integracji AI i budowy portfolio z chatbotem RAG.

To profil osoby, która rozwija się według logiki:
**fundamenty języka → praca z danymi i bibliotekami → web/backend → bazy danych → testowanie i debugging → wdrożenia → AI/LLM → portfolio produktowe**.

Najważniejszy wzorzec tej ścieżki: nauka nie kończy się na teorii. Każdy etap jest możliwie szybko zamieniany w **praktyczne ćwiczenia, mini-projekty albo działające MVP**.

---

## Punkt wyjścia

Start nastąpił od decyzji o **wejściu do branży IT przez Pythona** i budowania kompetencji w sposób możliwie praktyczny. Python został wybrany jako główny język wejścia, ponieważ pozwala łączyć:

- czytelną składnię,
- szybkie budowanie aplikacji,
- backend webowy,
- pracę z danymi,
- integracje API,
- naturalne wejście w obszar AI i LLM.

Już na wczesnym etapie nauka była wspierana przez:
- systematyczne notatki w **Obsidianie**,
- pracę w **PyCharm**,
- kursowy rytm nauki,
- budowanie własnego repozytorium ćwiczeń i projektów.

To ważne, bo pokazuje nie tylko naukę składni, ale budowanie od początku **własnego workflow uczenia się**.

---

## Etap 1 — Python fundamentals

Pierwszy etap koncentrował się na opanowaniu podstaw języka:

- zmienne, typy danych, operatory,
- logika warunkowa,
- pętle,
- funkcje,
- podstawowe struktury danych,
- pierwsze klasy i wprowadzenie do OOP.

Na tym poziomie celem nie było "znać wszystko", ale zbudować stabilny fundament do dalszej pracy. Istotnym elementem było też oswajanie się z błędami składni, tracebackami i podstawowym debugowaniem.

Ten etap odpowiada przejściu od: **"uruchamiam pojedyncze instrukcje"** do **"umiem napisać mały, logicznie uporządkowany program"**.

### Pojęcia rozwijane na tym etapie

- **variables**, **conditionals**, **loops**
- **functions**
- **lists / dicts / tuples / sets**
- podstawy **OOP (Object-Oriented Programming)**
- pierwsze zrozumienie czym jest **traceback** i **exception**

---

## Etap 2 — Python standard library, pliki i codzienna praca z danymi

Po zbudowaniu podstaw nauka rozszerzyła się o realne użycie standardowej biblioteki i operacje wejścia/wyjścia:

- praca z plikami tekstowymi,
- `with open(...)` i rola **context managera**,
- CSV i JSON,
- podstawowa organizacja modułów,
- ścieżki plików i praca z katalogami,
- typowe narzędzia codziennej pracy developerskiej.

To był etap bardzo ważny praktycznie, bo właśnie tutaj Python zaczął pełnić rolę realnego narzędzia do przetwarzania danych, a nie tylko języka ćwiczeń akademickich.

### Efekt tego etapu

- swobodniejsza praca na plikach,
- większa samodzielność w małych skryptach,
- lepsze rozumienie przepływu danych: **read → transform → save**.

---

## Etap 3 — Konstrukcje bardziej zaawansowane i świadome pisanie kodu

Kolejny krok to przejście od "kod działa" do "kod jest bardziej świadomie napisany". W tym etapie pojawiły się zagadnienia takie jak:

- **list / set / dict comprehension**,
- **generators** i `yield`,
- `map()` i `lambda`,
- adnotacje typów (**type annotations**),
- dokumentowanie kodu,
- importowanie modułów,
- bardziej świadome rozumienie mutowalności, zakresów zmiennych i organizacji kodu.

Na tym poziomie rośnie nie tylko zasób składni, ale też zrozumienie, **dlaczego kod można pisać czytelniej, krócej albo bardziej przewidywalnie**.

---

## Etap 4 — Web backend i REST API

Następny logiczny etap to wejście w świat aplikacji webowych.

Tutaj ścieżka przechodzi od skryptów lokalnych do aplikacji, które:
- reagują na żądania użytkownika,
- obsługują formularze,
- renderują widoki,
- komunikują się przez HTTP,
- mogą pełnić rolę prostego API.

Główne obszary nauki:

- **Flask** jako podstawowy framework backendowy,
- routing,
- obsługa metod `GET`, `POST`, `PUT`, `DELETE`,
- **Jinja2**, HTML i CSS po stronie prezentacyjnej,
- podstawy architektury request → response,
- rozumienie **REST API**,
- `requests`, `jsonify`, `request.json`, `request.args`.

To etap, w którym Python staje się narzędziem do budowy **realnych aplikacji webowych**, a nie tylko narzędziem do ćwiczeń lokalnych.

### Znaczenie rozwojowe

Ten krok jest kluczowy, bo właśnie tutaj powstaje profil **backend-oriented junior Python developera**.

---

## Etap 5 — Relacyjne bazy danych i warstwa danych

Równolegle do backendu rozwijana była warstwa pracy z bazami danych.

Zakres obejmuje:

- podstawy relacyjnego modelu danych,
- SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`,
- relacje 1-do-wielu,
- podstawowe ograniczenia i integralność danych,
- różnice między **SQLite** a **MySQL**,
- połączenie Python ↔ baza danych,
- pierwsze użycie **SQLAlchemy** jako ORM.

Tutaj ścieżka dojrzewa z poziomu prostego przechowywania danych do rozumienia, że aplikacja to również:

- model danych,
- relacje,
- walidacja,
- stan aplikacji,
- operacje CRUD wykonywane świadomie i bezpiecznie.

### Efekt tego etapu

- większa kontrola nad logiką danych,
- rozumienie backendu nie tylko jako routingu, ale jako warstwy pośredniczącej między użytkownikiem a bazą danych,
- przygotowanie do bardziej realistycznych projektów aplikacyjnych.

---

## Etap 6 — Narzędzia developerskie, Git, Linux i debugging

Osobnym, bardzo ważnym nurtem rozwoju jest budowanie samodzielności technicznej.

Ten etap nie polega na nauce jednej biblioteki, tylko na rozwijaniu **developer workflow**:

- **Git** i GitHub,
- branch, merge, commit history,
- `.gitignore`,
- środowiska wirtualne `venv`,
- `pip`, `requirements.txt`,
- terminal, PowerShell i podstawy Linuxa,
- praca z hostingiem,
- debugowanie konfiguracji i zależności,
- różnice między środowiskiem lokalnym a serwerowym.

To bardzo istotna część tej ścieżki, bo pokazuje przejście od osoby "uczącej się pisać kod" do osoby, która zaczyna rozumieć **całe środowisko uruchomieniowe**.

### Szczególnie mocny element

Debugging i diagnozowanie problemów środowiskowych to jedna z najbardziej charakterystycznych cech tego profilu. Nauka obejmuje nie tylko kod, ale również:

- analizę tracebacków,
- testowanie hipotez,
- poprawki konfiguracji,
- aktywację właściwego środowiska,
- pracę z `.env`,
- wdrożenia i retesty.

---

## Etap 7 — Testowanie i jakość kodu

Po wejściu w bardziej złożone projekty naturalnie pojawił się obszar testów.

Zakres obejmuje:

- podstawy **unittest** i **pytest**,
- rozróżnienie testów jednostkowych, integracyjnych i funkcjonalnych,
- pierwsze zetknięcie z **TDD (Test-Driven Development)**,
- rozumienie testu jako opisu oczekiwanego zachowania systemu,
- większą dbałość o przewidywalność kodu i ograniczanie regresji.

Ten etap nie jest jeszcze obszarem maksymalnie rozwiniętym, ale jest ważny, bo pokazuje świadome przejście z poziomu "sprawdzam ręcznie" do poziomu "zaczynam automatyzować weryfikację logiki".

---

## Etap 8 — AI, LLM i integracje modelowe

Ważnym wyróżnikiem ścieżki Tomasza jest wejście w AI nie od strony teorii akademickiej, lecz od strony **praktycznej integracji produktów z modelami**.

Główne elementy tego etapu:

- praca z **OpenAI API**,
- **prompt engineering**,
- wymuszanie odpowiedzi w formacie JSON,
- rozumienie ograniczeń modeli,
- fallbacki i walidacja odpowiedzi,
- podstawowa orientacja w **structured outputs**, **tool calling**, **MCP**,
- wstęp do **local LLMs** przez **Ollama**.

To etap, który rozszerza profil z klasycznego junior backend developera w stronę:
**backend + AI integration + product experimentation**.

### Kluczowa różnica

AI nie jest tutaj dodatkiem marketingowym. Jest traktowane jako kolejna warstwa systemu, którą trzeba:

- poprawnie zasilić danymi,
- ograniczyć kontekstowo,
- obsłużyć błędnie zwróconą odpowiedź,
- włączyć w realny przepływ aplikacji.

---

## Etap 9 — Projekty jako nośnik kompetencji

Najważniejszą cechą tej ścieżki jest to, że kolejne technologie nie są ćwiczone w izolacji. Zostały przełożone na projekty, które pełnią rolę **dowodów kompetencji**.

### Story Review
Pierwsza warstwa integracji AI w formie prostszego skryptu.

### Fridge & Recipe AI
Ćwiczenie: pliki CSV + LLM + interaktywny interfejs w Streamlit.

### HeadFirst
Rozwijanie logiki backendowej, SQL i struktury aplikacji.

### HorseOwner MVP
Najmocniejszy projekt portfolio: połączenie backendu, danych, domeny, formularzy, AI i kierunku deploymentowego.

### Personal Landing Page / portfolio z chatbotem RAG
Etap łączenia wszystkich wcześniejszych kompetencji w produkt rekrutacyjny.

To właśnie projekty pokazują, że ścieżka nie jest deklaratywna. Jest **wdrażana w praktyce**.

---

## Obecny etap

Obecny etap rozwoju można opisać jako:

**junior Python developer z wyraźnym kierunkiem backend + data + AI integrations + RAG portfolio**.

Najważniejsze cechy obecnego poziomu:

- Python jako główny język pracy,
- Flask jako podstawowy framework backendowy,
- SQL i relacyjne bazy danych jako trwały filar,
- Git, terminal i debugging jako element codziennej praktyki,
- AI jako realna warstwa projektowa,
- portfolio budowane wokół własnych, działających projektów.

To nie jest jeszcze profil "wyspecjalizowanego seniora w jednym frameworku". To profil osoby, która zbudowała **szeroki i logicznie poukładany fundament techniczny** pod dalszą specjalizację.

---

## Kierunek dalszego rozwoju

Najbardziej naturalna kontynuacja tej ścieżki to pogłębianie kilku obszarów jednocześnie, ale nadal w spójnej logice.

### 1. Backend engineering
- dojrzalsza architektura aplikacji,
- lepsze rozdzielenie warstw,
- walidacja danych,
- autoryzacja, logowanie użytkowników, bezpieczeństwo.

### 2. Databases and deployment
- mocniejsze wejście w MySQL / PostgreSQL,
- migracje,
- środowiska produkcyjne,
- stabilniejsze wdrożenia i konfiguracja.

### 3. Testing and code quality
- regularniejsze użycie testów,
- większa automatyzacja jakości,
- bardziej dojrzałe podejście do refaktoryzacji.

### 4. AI application layer
- RAG w praktyce,
- embeddings,
- retrieval pipeline,
- lepsze zarządzanie promptami,
- kontrola jakości odpowiedzi modeli.

### 5. Portfolio as product
- dopracowanie Personal Landing Page,
- chatbot oparty na rzeczywistych materiałach,
- pokazanie rekruterowi nie tylko kodu, ale sposobu myślenia systemowego.

---

## Charakter tej ścieżki

Ta ścieżka nauki ma kilka charakterystycznych cech:

- **praktyczność** — teoria szybko przechodzi w implementację,
- **iteracyjność** — kolejne projekty rozwijają wcześniejsze kompetencje,
- **samodzielność** — duży nacisk na debugging, środowisko i rozwiązywanie problemów,
- **spójność** — Python, backend, dane i AI układają się w jedną linię rozwojową,
- **produktowość** — nauka prowadzi do budowy realnych MVP, a nie tylko ćwiczeń kursowych.

To ważne z perspektywy rekrutacyjnej, bo pokazuje nie tylko listę technologii, ale **sposób dojrzewania jako developera**.

---

## Skrót do retrieval

Ścieżka nauki Tomasza przebiega w kolejności:

- **Python fundamentals**
- **standard library, pliki, CSV, JSON**
- **advanced Python i OOP**
- **Flask, HTTP, REST API**
- **SQL, SQLite, MySQL, SQLAlchemy**
- **Git, terminal, Linux, virtual environments, debugging**
- **testowanie i jakość kodu**
- **OpenAI API, prompt engineering, LLM integrations**
- **RAG, embeddings, portfolio chatbot**
- **projekty MVP jako dowód kompetencji**

Końcowy kierunek: **junior Python/backend developer rozwijający się w stronę AI-enabled applications i praktycznego RAG**.

### Słowa kluczowe do retrieval

`learning path`, `career transition`, `python learning journey`, `backend roadmap`, `junior python developer`, `flask learning`, `sql learning`, `ai learning path`, `rag roadmap`, `obsidian learning system`, `project-based learning`, `debugging mindset`, `portfolio evolution`, `python to ai`, `personal landing page`
