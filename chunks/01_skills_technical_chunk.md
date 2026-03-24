---
id: skills_technical_current
category: skills_technical
type: unified_chunk
language: pl
audience: recruiter
seniority: junior
last_updated: 2026-03-18
tags:
  - python
  - flask
  - rest-api
  - sql
  - mysql
  - sqlalchemy
  - git
  - debugging
  - testing
  - pandas
  - web-scraping
  - linux
  - tooling
  - ai
  - llm
---

# skills_technical

## Profil techniczny — kompetencje aktualne

Profil: **Python Developer (junior / junior+)**  
Kompetencje budowane praktycznie, przez naukę projektową, rozwiązywanie realnych problemów technicznych, debugging, konfigurację środowisk i integrację narzędzi.

Profil pokazuje nie tylko znajomość składni, ale też rosnącą świadomość inżynierską: **jak działa kod, jak przepływają dane, jak działa środowisko, jak diagnozować błędy i jak łączyć aplikację z bazą danych, API oraz narzędziami AI**.

---

## Python — kompetencje główne

- Bardzo dobra znajomość składni Pythona oraz standardowych struktur danych:
  - `list`, `dict`, `tuple`, `set`
  - operacje mutowalne vs niemutowalne (*mutability*)
  - świadomość semantyki referencji: `a = b` vs `a = b.copy()`
- Funkcje i paradygmat funkcyjny:
  - `map()` (*higher-order function*)
  - `lambda` (*anonymous functions*)
  - rozumienie różnic czytelności i zastosowań vs pętle
- Pythonic constructs:
  - `list comprehension`, `set comprehension`, `dict comprehension`
  - generatory i `yield`
  - `generator expression`
  - `itertools.islice()` oraz `next()` przy pracy z iteratorami
- Programowanie obiektowe (OOP):
  - klasy, metody, konstruktor `__init__`
  - `self`, enkapsulacja logiki
  - modelowanie prostych encji w kodzie
- Obsługa błędów i wyjątków:
  - `try / except`
  - analiza `traceback`
  - użycie `repr()` do diagnostyki i logowania

**Poziom:** junior+  
**Charakterystyka:** świadome pisanie kodu z naciskiem na czytelność, przewidywalność działania i kontrolę błędów.

---

## Python — standard library, I/O i organizacja kodu

- Praca z plikami:
  - `with open(...)` i rozumienie roli *context managera*
  - tryby otwierania plików: `r`, `w`, `a`, `x`, `r+`, `w+`, `a+`
  - odczyt i zapis danych: `.read()`, `.readline()`, `.readlines()`, `.write()`
  - operacje na pozycji kursora pliku: `.seek()`
- Praca ze ścieżkami i systemem plików:
  - `pathlib.Path`
  - podstawowe operacje na plikach i katalogach
  - świadomość różnic między `os` a `pathlib`
- Formatowanie i wymiana danych:
  - `csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`
  - `json.load()`, `json.loads()`, `json.dump()`, `json.dumps()`
- Typowanie i czytelność:
  - *type annotations* dla parametrów i wartości zwracanych
  - podstawowa znajomość `mypy`
  - `docstring`, PEP 257, `help()`, `__doc__`, `__annotations__`
- Organizacja modułów:
  - `import`, `from ... import ...`, aliasy
  - świadomość roli `if __name__ == "__main__":`

**Poziom:** junior / junior+  
**Mocna strona:** dobra praktyczna znajomość codziennej pracy z danymi, plikami i strukturą modułów.

---

## Backend & Web (Python)

- Flask:
  - routing `GET / POST`
  - praca z szablonami Jinja2
  - obsługa formularzy
  - logika aplikacji po stronie serwera
- Rozwinięcie Flask w kierunku API:
  - `@app.route()`
  - `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()`
  - implementacja prostych endpointów CRUD
  - `request.json`, `jsonify(...)`
  - wydzielanie funkcji pomocniczych i centralizacja prostych błędów aplikacyjnych
  - podstawowa znajomość `@app.before_request`, `@app.after_request`, `@app.errorhandler(...)`
- Django (podstawy):
  - struktura projektu
  - uruchamianie projektu i aplikacji
  - świadomość różnic wersji frameworka
- Podstawy architektury webowej:
  - rozróżnienie frontend / backend
  - cykl request → response
  - podstawowe pojęcia REST

**Poziom:** junior  
**Mocna strona:** backendowa logika aplikacji i poprawne rozumienie przepływu HTTP.  
**Do rozwoju:** bardziej zaawansowane Django, walidacja danych, testy webowe.

---

## REST API i komunikacja HTTP

- Rozumienie podstaw REST:
  - request / response
  - bezstanowość (*statelessness*)
  - metody HTTP: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- Zapytania HTTP w Pythonie:
  - biblioteka `requests`
  - praktyczne wysyłanie zapytań `GET` i `POST`
  - odbiór odpowiedzi JSON i praca na danych zwróconych przez API
- Parametry w API:
  - *path parameters*
  - *query parameters*
  - użycie `request.args.get(...)`
- Dobre praktyki projektowania REST API:
  - endpointy oparte na rzeczownikach, nie czasownikach
  - rozdzielenie znaczenia metod HTTP od adresów URL
  - poprawne użycie kodów odpowiedzi: `400`, `401`, `403`, `404`, `201`, `204`
  - filtrowanie i paginacja przez query parameters

**Poziom:** junior  
**Charakterystyka:** poprawne rozumienie konwencji REST i praktyki integracji aplikacji z zewnętrznymi usługami.

---

## Bazy danych i SQL

- Relacyjne bazy danych:
  - SQLite (praktyczne użycie w aplikacjach)
  - MySQL (podstawy i integracja z Pythonem)
- Projektowanie prostych schematów danych:
  - relacje 1-do-wielu
  - podstawowa świadomość integralności danych
- SQL:
  - `SELECT`, `INSERT`, `UPDATE`, `DELETE`
  - `JOIN` (INNER / LEFT)
  - funkcje tekstowe: `SUBSTRING`, `SUBSTR`, `SUBSTRING_INDEX`
  - podstawowa znajomość `REGEXP`
- Integralność i ograniczenia:
  - `CHECK CONSTRAINT`
  - `DEFAULT`, `NULL`
- Uprawnienia:
  - `GRANT`, `REVOKE`
  - `WITH GRANT OPTION`
- Świadomość różnic między systemami bazodanowymi:
  - SQLite vs MySQL / PostgreSQL
  - skalowalność, użytkownicy, środowiska, sposób użycia

**Poziom:** junior+  
**Charakterystyka:** rozumienie zasad działania relacyjnych baz danych, nie tylko samej składni zapytań.

---

## Bazy danych z poziomu Pythona i ORM

- Połączenie Python ↔ MySQL:
  - `mysql.connector`
  - połączenie, `cursor()`, `execute()`, `fetchall()`, `commit()`
- Operacje CRUD z poziomu aplikacji
- Bezpieczeństwo zapytań:
  - użycie placeholderów `%s`
  - świadomość ochrony przed *SQL injection*
- ORM:
  - rozumienie idei *Object-Relational Mapping*
  - praktyczne podstawy `SQLAlchemy`
  - definicja modeli
  - filtrowanie, dodawanie, aktualizacja i usuwanie rekordów
  - podstawy relacji między tabelami i nawigacji po relacjach

**Poziom:** junior+  
**Mocna strona:** łączenie rozumienia SQL z pierwszym praktycznym użyciem ORM bez utraty kontroli nad tym, co dzieje się po stronie bazy.

---

## Modelowanie danych i serializacja

- `@dataclass`:
  - tworzenie lekkich klas danych
  - ograniczanie boilerplate
  - prostsze modelowanie encji
- Serializacja danych:
  - zamiana obiektów na format JSON
  - świadomość potrzeby jawnej serializacji obiektów niestandardowych
  - praktyczne użycie `jsonify(...)` w warstwie webowej

**Poziom:** junior  
**Do rozwoju:** bardziej zaawansowana walidacja i serializacja danych wejściowych / wyjściowych.

---

## Git i kontrola wersji

- Codzienna praca z Git:
  - `git add`, `git commit`, staging area
  - `git branch`, `merge`
  - `git log --oneline --graph`
- Praca z repozytoriami zdalnymi (GitHub):
  - `remote`, `push`, `fetch`
- Rozwiązywanie realnych problemów:
  - pager (`git diff` / `less`)
  - edytor commitów w CLI
  - konflikty merge
- `.gitignore`:
  - ignorowanie katalogów i plików
  - wyjątki (*negation patterns*)
- Świadomość problemów systemowych:
  - LF vs CRLF w środowisku Windows

**Poziom:** junior+  
**Mocna strona:** praktyczny workflow i dobra orientacja w codziennej pracy z repozytorium.

---

## Testowanie i jakość kodu

- Podstawy testów:
  - `unittest`
  - `pytest`
- Rozróżnienie poziomów testów:
  - unit tests
  - integration tests
  - functional tests
  - świadomość E2E
- Praca z Selenium:
  - testy funkcjonalne
  - debugowanie problemów `setup / teardown`
- TDD (*Test-Driven Development*):
  - test jako specyfikacja zachowania
  - model `RED → GREEN → REFACTOR`
- Świadomość BDD i DSL:
  - myślenie o testach z perspektywy zachowania systemu
- Dbałość o jakość:
  - czytelność kodu
  - logiczne funkcje
  - minimalizacja duplikacji

**Poziom:** junior  
**Do rozwoju:** regularne stosowanie testów w projektach webowych, automatyzacja i CI.

---

## Debugging i diagnostyka

- Czytanie i analiza tracebacków
- Lokalizowanie źródła błędu: linia → przyczyna
- Debugger w IDE
- Świadomość typowych problemów:
  - brak aktywnego virtualenv
  - brak zmiennych środowiskowych
  - różnice lokalne środowisko vs serwer
  - problemy konfiguracyjne zależności
- Podejście systematyczne:
  - izolowanie problemu
  - testowanie hipotez
  - poprawka → retest

**To jest jedna z najmocniejszych kompetencji.**

---

## Analiza danych i operacje na DataFrame

- `pandas`:
  - `read_csv()`
  - `head()`, `tail()`, `info()`, `describe()`
  - selekcja kolumn i filtrowanie rekordów
  - `sort_values()`
  - `value_counts()`
- Czyszczenie danych:
  - `to_numeric(..., errors='coerce')`
  - `dropna()`
  - `fillna()`
  - `astype()`
- Grupowanie i agregacje:
  - `groupby()`
  - `mean()`, `count()`, `size()`, `agg()`
- Transformacja danych:
  - `melt()`
  - `concat()`

**Poziom:** junior  
**Charakterystyka:** podstawowy, praktyczny workflow pracy z danymi: czyszczenie → filtrowanie → agregacja → interpretacja.

---

## Web scraping i pobieranie danych

- Biblioteki:
  - `requests`
  - `BeautifulSoup`
- Podstawowe techniki:
  - pobieranie HTML
  - parsowanie drzewa dokumentu
  - wyszukiwanie elementów po tagach, klasach i atrybutach
  - ekstrakcja tekstu i linków
- Świadomość zasad:
  - sprawdzanie `robots.txt`
  - respektowanie reguł strony i ograniczeń technicznych

**Poziom:** podstawy / junior  
**Zastosowanie:** pobieranie i porządkowanie danych z prostych stron HTML.

---

## Środowisko pracy, tooling i terminal

- Środowiska wirtualne:
  - `.venv`
  - rozumienie izolacji zależności projektu
- Zarządzanie pakietami:
  - `pip`
  - `pip list`
  - świadomość różnicy między PyPI, Python Standard Library i funkcjami wbudowanymi
- IDE i narzędzia developerskie:
  - praca w IDE
  - debugger, terminal, integracja z Gitem
- Linux / terminal basics:
  - pojęcie katalogu roboczego
  - poruszanie się po systemie plików z poziomu terminala
  - podstawowe polecenia nawigacyjne
- Praca w CLI:
  - rozumienie pagera przy dłuższych wynikach poleceń
  - sprawne przechodzenie między kodem, terminalem i konfiguracją środowiska

**Poziom:** junior+  
**Charakterystyka:** duży nacisk na samodzielność techniczną oraz sprawne działanie w praktycznym środowisku developerskim.

---

## AI / integracje i workflow LLM

- Praca z API modeli językowych (LLM)
- Prompt engineering:
  - kontrola kontekstu
  - wymuszanie formatu odpowiedzi, w tym JSON
- Obsługa błędów API:
  - brak klucza
  - brak odpowiedzi
  - potrzeba walidacji odpowiedzi modelu
- Świadomość ograniczeń modeli:
  - halucynacje
  - potrzeba kontroli źródeł
  - bezstanowość modeli i rola przekazywanego kontekstu
- Znajomość koncepcji:
  - RAG (*Retrieval-Augmented Generation*)
  - embeddings
  - *structured outputs*
  - *prompt management*
  - *function calling / tool calling*
  - MCP (*Model Context Protocol*)
- Orientacja w lokalnym uruchamianiu modeli:
  - podstawowa znajomość `Ollama`

**Poziom:** junior / orientacja praktyczna  
**Charakterystyka:** kompetencja wspierająca projekty AI-enabled i integracje aplikacyjne, szczególnie w obszarze prostych wdrożeń LLM.

---

## Podsumowanie kompetencji (skrót do retrieval)

- Python core: **junior+**
- Python standard library / I/O / organizacja kodu: **junior / junior+**
- Flask / backend / REST API: **junior**
- SQL / relacyjne bazy danych: **junior+**
- MySQL z Pythona / SQLAlchemy: **junior+**
- Git i workflow repozytoryjny: **junior+**
- Testowanie: **junior**
- Debugging i diagnostyka: **mocna strona**
- Pandas / analiza danych: **junior**
- Web scraping: **podstawy / junior**
- Tooling / terminal / środowisko: **junior+**
- AI integracje / LLM workflow: **junior**

Profil oparty na **praktyce, debugowaniu, rozumieniu systemu i pracy na styku: kod ↔ dane ↔ API ↔ środowisko ↔ narzędzia developerskie ↔ AI**.
