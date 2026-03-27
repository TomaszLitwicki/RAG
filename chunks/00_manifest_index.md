---
id: manifest_index_01
category: manifest
type: retrieval_index
language: pl
audience:
  - rag_system
  - recruiter_chatbot
  - maintainer
last_updated: 2026-03-24
version: 1.0
source_set: profile_chunks_v1
chunks_total: 8
canonical_order:
  - 01_skills_technical_chunk.md
  - 02_projects_chunk.md
  - 03_tools_and_stack_chunk.md
  - 04_learning_path_chunk.md
  - 05_career_transition_chunk.md
  - 06_work_style_chunk.md
  - 07_goals_and_direction_chunk.md
  - 08_background_selected_chunk.md
retrieval_priority:
  A:
    - 01_skills_technical_chunk
    - 02_projects_chunk
    - 03_tools_and_stack_chunk
    - 06_work_style_chunk
  B:
    - 04_learning_path_chunk
    - 05_career_transition_chunk
    - 07_goals_and_direction_chunk
  C:
    - 08_background_selected_chunk

query_routing:
  technical:
    - 01_skills_technical_chunk
    - 03_tools_and_stack_chunk
    - 02_projects_chunk
  projects:
    - 02_projects_chunk
    - 01_skills_technical_chunk
    - 03_tools_and_stack_chunk
  work_style:
    - 06_work_style_chunk
    - 05_career_transition_chunk
    - 01_skills_technical_chunk
  learning_path:
    - 04_learning_path_chunk
    - 01_skills_technical_chunk
    - 07_goals_and_direction_chunk
  career_transition:
    - 05_career_transition_chunk
    - 06_work_style_chunk
    - 08_background_selected_chunk
  goals:
    - 07_goals_and_direction_chunk
    - 04_learning_path_chunk
    - 02_projects_chunk
  background:
    - 08_background_selected_chunk
    - 05_career_transition_chunk
    - 02_projects_chunk

intent_categories:
  technical:
    - skills_technical
    - tools_and_stack
    - projects
  projects:
    - projects
    - skills_technical
    - tools_and_stack
  work_style:
    - work_style
    - career_transition
    - skills_technical
  learning_path:
    - learning_path
    - skills_technical
    - goals_and_direction
  career_transition:
    - career_transition
    - work_style
    - background_selected
  goals:
    - goals_and_direction
    - learning_path
    - projects
  background:
    - background_selected
    - career_transition
    - projects

default_bundles:
  technical_summary:
    - 01_skills_technical_chunk
    - 03_tools_and_stack_chunk
    - 02_projects_chunk
  recruiter_profile_summary:
    - 05_career_transition_chunk
    - 06_work_style_chunk
    - 07_goals_and_direction_chunk
  portfolio_evidence:
    - 02_projects_chunk
    - 01_skills_technical_chunk
    - 06_work_style_chunk
  motivation_and_background:
    - 05_career_transition_chunk
    - 08_background_selected_chunk
    - 07_goals_and_direction_chunk
  learning_narrative:
    - 04_learning_path_chunk
    - 01_skills_technical_chunk
    - 07_goals_and_direction_chunk

intent_keywords:
  technical:
    - python
    - flask
    - sql
    - sqlite
    - mysql
    - api
    - rest
    - git
    - linux
    - debugging
    - testing
    - technologie
    - technologia
    - technol
    - stack
    - narzedzi
    - backend
    - rag
    - sztuczna
    - inteligencja
    - umiejętności
  projects:
    - projekt
    - projekty
    - portfolio
    - horseowner
    - mvp
    - mission-aipossible
    - aplikacja
    - aplikacje
    - app
    - plp
    - www
    - personal
    - landing
    - page
    - horse
    - konie
  work_style:
    - pracuje
    - styl
    - debugowanie
    - samodzielnie
    - ownership
    - iteracyjnie
    - współpraca
    - wspolpraca
  learning_path:
    - nauka
    - learning
    - ścieżka
    - sciezka
    - progres
    - kolejność
    - kolejnosc
    - uczy
    - wiedzę
    - wiedza
  career_transition:
    - przebranżowienie
    - przebranzowienie
    - zmiana
    - zmienia
    - branz
    - motywacja
    - transferable
  goals:
    - cel
    - cele
    - stanowisko
    - rola
    - kierunek
    - rozwój
    - rozwoj
    - plany
  background:
    - wcześn
    - tło
    - doświadcz
    - koni
    - ranczo
    - soft
    - kon
    - jeździectwo
    - western
    - natural
    - szkolenia
    - aikido
    - spadan
    - psy
    - pies
    - psa

---

# manifest/index

## Rola dokumentu

Ten plik pełni funkcję **warstwy organizującej cały zestaw chunków pod system RAG**. Nie jest osobnym chunkem biograficznym, tylko dokumentem sterującym, który opisuje:

- jakie pliki wchodzą do zestawu,
- za co odpowiada każdy chunk,
- jak kierować zapytania (*query routing*) do właściwych źródeł,
- które chunki są podstawowe, a które pomocnicze,
- jak utrzymać spójność odpowiedzi generowanych przez chatbota.

Najprościej: to **mapa informacji** dla całej paczki profilowej Tomasza.

---

## Cel całego zestawu

Zestaw chunków ma wspierać chatbota osadzonego w projekcie **Personal Landing Page** i umożliwiać odpowiadanie na pytania dotyczące:

- kompetencji technicznych,
- projektów i portfolio,
- używanego stacku i narzędzi,
- ścieżki nauki,
- przebranżowienia,
- stylu pracy,
- kierunku zawodowego,
- wybranego tła osobistego i zawodowego.

Domyślny profil odpowiedzi powinien być:

- **factual** — oparty na rzeczywistych materiałach,
- **recruiter-oriented** — przydatny dla rekrutera lub hiring managera,
- **grounded** — bez dopisywania niepotwierdzonych sukcesów,
- **junior-calibrated** — bez przeszacowywania poziomu seniority,
- **portfolio-aware** — z naturalnym odwołaniem do projektów jako dowodów pracy.

---

## Architektura zbioru

Cały zestaw można podzielić na 3 warstwy:

### 1. Warstwa kompetencyjno-dowodowa (*capability & evidence layer*)
To najważniejsze źródła do pytań o realne umiejętności i dowody pracy:

- `01_skills_technical_chunk.md`
- `02_projects_chunk.md`
- `03_tools_and_stack_chunk.md`

### 2. Warstwa narracyjno-profilowa (*profile narrative layer*)
Źródła opisujące rozwój, sposób działania i kierunek zawodowy:

- `04_learning_path_chunk.md`
- `05_career_transition_chunk.md`
- `06_work_style_chunk.md`
- `07_goals_and_direction_chunk.md`

### 3. Warstwa kontekstowa selektywna (*selective background layer*)
Źródło używane tylko wtedy, gdy pytanie naprawdę wymaga tła osobistego lub wcześniejszego doświadczenia:

- `08_background_selected_chunk.md`

---

## Rejestr chunków

| Nr | Plik | Kategoria | Funkcja główna | Kiedy używać |
|---|---|---|---|---|
| 01 | `01_skills_technical_chunk.md` | `skills_technical` | Opis realnych kompetencji technicznych | Gdy pytanie dotyczy umiejętności, backendu, Pythona, SQL, API, testów, AI |
| 02 | `02_projects_chunk.md` | `projects` | Najmocniejsze dowody pracy projektowej | Gdy pytanie dotyczy portfolio, projektów, MVP, HorseOwner, Mission-AIpossible |
| 03 | `03_tools_and_stack_chunk.md` | `tools_and_stack` | Narzędzia, frameworki, środowisko, stack | Gdy pytanie dotyczy technologii, narzędzi, środowiska, deployu, workflow |
| 04 | `04_learning_path_chunk.md` | `learning_path` | Chronologia nauki i logika rozwoju | Gdy pytanie dotyczy nauki, progresu, kolejności rozwijanych kompetencji |
| 05 | `05_career_transition_chunk.md` | `career_transition` | Wiarygodny opis przebranżowienia | Gdy pytanie dotyczy zmiany branży, motywacji, przenoszalnych kompetencji |
| 06 | `06_work_style_chunk.md` | `work_style` | Styl pracy, debugging, iteracyjność, ownership | Gdy pytanie dotyczy sposobu działania, jakości pracy, współpracy, podejścia do problemów |
| 07 | `07_goals_and_direction_chunk.md` | `goals_and_direction` | Rola docelowa i kierunek rozwoju | Gdy pytanie dotyczy celów zawodowych, roli startowej, kierunku backend + AI + RAG |
| 08 | `08_background_selected_chunk.md` | `background_selected` | Selektywnie używane tło zawodowe i osobiste | Gdy potrzebny jest kontekst wcześniejszej pracy lub geneza projektów domenowych |

---

## Kolejność ważności przy retrieval

### Priorytet A — rdzeń odpowiedzi
Najczęściej od tych chunków warto zaczynać retrieval:

1. `01_skills_technical_chunk.md`
2. `02_projects_chunk.md`
3. `03_tools_and_stack_chunk.md`
4. `06_work_style_chunk.md`

Są to źródła najbardziej konkretne, najbardziej „dowodowe” i najczęściej użyteczne rekrutacyjnie.

### Priorytet B — narracja i pozycjonowanie profilu
Używać jako uzupełnienie lub do pytań profilowych:

5. `04_learning_path_chunk.md`
6. `05_career_transition_chunk.md`
7. `07_goals_and_direction_chunk.md`

### Priorytet C — kontekst selektywny
Używać ostrożnie i tylko wtedy, gdy pytanie tego wymaga:

8. `08_background_selected_chunk.md`

Ten chunk nie powinien dominować odpowiedzi technicznych. Ma wspierać interpretację profilu, nie zastępować kompetencje i projekty.

---

## Query routing — mapowanie pytań do chunków

### Pytania o technologie i kompetencje
Przykłady:
- „Jakie technologie zna Tomasz?”
- „Czy zna Flask / SQL / Git / API?”
- „Jaki ma poziom Pythona?”

Rekomendowana kolejność:
1. `01_skills_technical_chunk.md`
2. `03_tools_and_stack_chunk.md`
3. `02_projects_chunk.md`

### Pytania o projekty i portfolio
Przykłady:
- „Jakie ma projekty?”
- „Co to jest HorseOwner MVP?”
- „Jakie praktyczne rzeczy zbudował?”

Rekomendowana kolejność:
1. `02_projects_chunk.md`
2. `01_skills_technical_chunk.md`
3. `03_tools_and_stack_chunk.md`

### Pytania o sposób pracy
Przykłady:
- „Jak pracuje?”
- „Jak podchodzi do debugowania?”
- „Czy działa samodzielnie?”

Rekomendowana kolejność:
1. `06_work_style_chunk.md`
2. `05_career_transition_chunk.md`
3. `01_skills_technical_chunk.md`

### Pytania o ścieżkę nauki i progres
Przykłady:
- „Jak wyglądała jego nauka?”
- „W jakiej kolejności rozwijał kompetencje?”
- „Jak szybko przeszedł do AI i RAG?”

Rekomendowana kolejność:
1. `04_learning_path_chunk.md`
2. `01_skills_technical_chunk.md`
3. `07_goals_and_direction_chunk.md`

### Pytania o przebranżowienie
Przykłady:
- „Dlaczego zmienia branżę?”
- „Czy to przebranżowienie jest wiarygodne?”
- „Jakie kompetencje wnosi z poprzedniej pracy?”

Rekomendowana kolejność:
1. `05_career_transition_chunk.md`
2. `06_work_style_chunk.md`
3. `08_background_selected_chunk.md`

### Pytania o cele zawodowe i rolę docelową
Przykłady:
- „Na jakie stanowisko celuje?”
- „Gdzie chce się rozwijać?”
- „Backend czy AI?”

Rekomendowana kolejność:
1. `07_goals_and_direction_chunk.md`
2. `04_learning_path_chunk.md`
3. `02_projects_chunk.md`

### Pytania o tło domenowe i genezę projektów
Przykłady:
- „Skąd pomysł na HorseOwner?”
- „Jakie ma wcześniejsze doświadczenie?”
- „Co z poprzedniej pracy przekłada się na IT?”

Rekomendowana kolejność:
1. `08_background_selected_chunk.md`
2. `05_career_transition_chunk.md`
3. `02_projects_chunk.md`

---

## Zalecane domyślne bundle retrieval

Aby ograniczać szum i poprawić trafność odpowiedzi, warto stosować małe zestawy chunków zamiast ładować wszystko naraz.

### Bundle A — technical summary
- `01_skills_technical_chunk.md`
- `03_tools_and_stack_chunk.md`
- `02_projects_chunk.md`

### Bundle B — recruiter profile summary
- `05_career_transition_chunk.md`
- `06_work_style_chunk.md`
- `07_goals_and_direction_chunk.md`

### Bundle C — portfolio evidence
- `02_projects_chunk.md`
- `01_skills_technical_chunk.md`
- `06_work_style_chunk.md`

### Bundle D — motivation and background
- `05_career_transition_chunk.md`
- `08_background_selected_chunk.md`
- `07_goals_and_direction_chunk.md`

### Bundle E — learning narrative
- `04_learning_path_chunk.md`
- `01_skills_technical_chunk.md`
- `07_goals_and_direction_chunk.md`

---

## Zasady generowania odpowiedzi przez chatbota

### 1. Zaczynaj od konkretu
Najpierw kompetencje, projekty, stack lub styl pracy. Dopiero potem narracja i tło.

### 2. Nie przeszacowuj seniority
Domyślny poziom opisu:
- **junior Python Developer**,
- czasem **junior / junior+** w wybranych kompetencjach praktycznych,
- nigdy nie sugerować poziomu mid/senior bez wyraźnego źródła.

### 3. Projekty traktuj jako dowód
Gdy chatbot opisuje umiejętność, dobrze jest domknąć odpowiedź projektem lub praktycznym przykładem, zwłaszcza `HorseOwner MVP`.

### 4. Tło osobiste używaj oszczędnie
`08_background_selected_chunk.md` ma wzmacniać wiarygodność profilu, ale nie powinien przejmować odpowiedzi technicznych.

### 5. Unikaj ozdobników i marketingowego tonu
Odpowiedzi powinny być raczej:
- rzeczowe,
- konkretne,
- spokojne,
- wiarygodne,
- oparte na materiale źródłowym.

### 6. Łącz narrację z dowodem
Najlepszy wzorzec odpowiedzi to:

**tezа → krótki kontekst → konkretny dowód projektowy / techniczny**

Przykład logiki:
- „Tomasz rozwija się backendowo w Pythonie”
- „co widać w jego ścieżce nauki i stacku”
- „a najmocniejszym dowodem jest HorseOwner MVP oparty o Flask, SQLite i integrację OpenAI API”

---

## Zasady bezpieczeństwa semantycznego

Chatbot nie powinien twierdzić rzeczy, których źródła nie potwierdzają. W szczególności należy unikać deklaracji typu:

- że Tomasz ma już komercyjne doświadczenie jako developer, jeśli nie ma na to źródła,
- że pracował w profesjonalnym zespole developerskim, jeśli materiał tego nie potwierdza,
- że zna zaawansowane system design, DevOps lub production-scale ML na poziomie praktyki zawodowej,
- że jest ekspertem od RAG, jeśli źródła pokazują raczej etap budowania i wdrażania portfolio w tym kierunku.

Bezpieczna formuła to:

- „rozwija kompetencje w kierunku...”,
- „buduje projekty obejmujące...”,
- „najmocniej pozycjonuje się jako...”,
- „na obecnym etapie jego profil najlepiej odpowiada roli...”.

---

## Kanoniczne byty i nazwy

Dla spójności odpowiedzi warto używać tych samych nazw własnych i etykiet:

- **Tomasz** / **Tomasz Litwicki**
- **Personal Landing Page**
- **HorseOwner MVP**
- **Mission-AIpossible**
- **junior Python Developer**
- **backend + AI + RAG**
- **portfolio techniczne**
- **career transition / przebranżowienie**

Nie należy mieszać wielu wariantów tej samej nazwy, jeśli nie ma takiej potrzeby.

---

## Słowa-klucze wysokiej wartości dla retrieval

### Kompetencje techniczne
`Python`, `Flask`, `REST API`, `SQL`, `SQLite`, `MySQL`, `SQLAlchemy`, `Git`, `debugging`, `testing`, `Linux`, `Pandas`, `BeautifulSoup`, `OpenAI API`, `Ollama`, `RAG`

### Projekty
`HorseOwner`, `HorseOwner MVP`, `Mission-AIpossible`, `FridgeAI`, `StoryReview`, `portfolio`, `Python web app`, `domain-driven MVP`

### Profil i przebranżowienie
`career transition`, `transferable skills`, `self-learning`, `iterative development`, `ownership`, `work style`, `junior backend`, `AI integration`

### Kierunek zawodowy
`junior Python Developer`, `backend`, `AI-powered web applications`, `RAG systems`, `portfolio chatbot`, `growth direction`

---

## Relacje między chunkami

### Najsilniejsze relacje
- `01_skills_technical` ↔ `03_tools_and_stack`
- `01_skills_technical` ↔ `02_projects`
- `05_career_transition` ↔ `06_work_style`
- `04_learning_path` ↔ `07_goals_and_direction`
- `08_background_selected` ↔ `02_projects`

### Relacje interpretacyjne
- `02_projects` dostarcza **dowodów** dla `01`, `06` i `07`
- `05` wyjaśnia **dlaczego profil jest wiarygodny mimo zmiany branży**
- `08` wyjaśnia **skąd bierze się domenowość projektów**
- `04` pokazuje **logikę progresu**, a `07` pokazuje **dokąd ten progres prowadzi**

---

## Jak rozwijać zestaw dalej

Jeżeli kolekcja będzie rozbudowywana, kolejne pliki warto dodawać tylko wtedy, gdy wnoszą nową warstwę informacji, a nie powielają istniejące treści.

Najbardziej sensowne przyszłe rozszerzenia to przykładowo:

- `09_recruiter_faq_chunk.md` — gotowe odpowiedzi na najczęstsze pytania rekrutacyjne,
- `10_project_case_studies_chunk.md` — głębsze opisy 1–3 projektów,
- `11_education_and_learning_sources_chunk.md` — kursy, książki, źródła nauki,
- `12_english_and_communication_chunk.md` — język angielski i komunikacja w kontekście IT.

Nie ma potrzeby dodawania kolejnych chunków „na siłę”. Lepiej utrzymać mniejszy, dobrze rozdzielony zbiór niż dużą paczkę z wysokim overlapem.

---

## Najkrótsze podsumowanie operacyjne

Jeżeli system ma odpowiedzieć dobrze na pytanie o Tomasza, najczęściej powinien:

1. ustalić, czy pytanie dotyczy **kompetencji**, **projektów**, **stylu pracy**, **przebranżowienia**, **celów**, czy **tła**,
2. pobrać 2–3 najbardziej pasujące chunki,
3. zbudować odpowiedź od konkretu do interpretacji,
4. nie przeszacowywać poziomu,
5. kończyć odpowiedź elementem dowodowym: projektem, stackiem albo konkretnym sposobem działania.

To jest domyślna logika działania dla całego zestawu `profile_chunks_v1`.
