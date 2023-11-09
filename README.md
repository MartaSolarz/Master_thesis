# Metodyka testów

## Zmienne:

| Nazwa                                                                                                                                                        | Typ                                                                  |
|:-:|:-:|
| poprawność odpowiedzi                                                                                                                                        | porządkowa (sumy), kategoryczna binarna (kolekcje, osobne grafiki), ilościowa (średnie) |
| trudność zadania                                                                                                                                             | porządkowa (poszczególne wartości, sumy), ilościowa (średnie)                                                        |
| czas odpowiedzi                                                                                                                                              | ilościowa ciągła                                                     |
| questions 1,2 (preferencje A vs B) oraz (mapa, tabela, tekst, wykres)                                                                                        | nominalne                                                         |
| cechy osobowe (płeć, kierunek studiów, specjalność, wady wzroku, wyniki matur (pisał vs. nie pisał), dominujący typ uczenia poznawczego) | nominalne                                                       |
| cechy osobowe (rok urodzenia, rok studiów, ilość snu, wyniki matur (rangowo), umiejętności, siła poszczególnych typów uczenia poznawczego) | porządkowe                                                         |
| całkowita długość fiksacji/wizyty, średnia długość fiksacji/wizyty, średnia wielkość źrenicy                                                                 | ilościowe ciągłe                                                     |
| liczba fiksacji/wizyty                                                                                                                                       | ilościowe dyskretne                                                  |
| ostatnie odwiedzone AOI                                                                                                                                      | nominalne                                                         |

## Zbiory testowe:

### Ogólne testy:
- każda grafika osobno: 1a, 1b, 2a, 2b, 3a, 3b → 40 próbek w każdym zbiorze → GRUPY NIEZALEŻNE
- zsumowane grafiki: wszystkie, A, B, 1, 2, 3 → sumujemy wyniki poszczególnych badanych, czyli 40 próbek w każdym zbiorze → GRUPY NIEZALEŻNE
- (tylko do wizualizacji) kolekcje grafik: wszystkie, A, B, 1, 2, 3 → “powielamy” wyniki tzn. zbieramy wszystkie odpowiedzi do jednej kolumny (np. jeśli rozważamy kolekcję grafik 1 to wówczas do jednej kolumny ustawiamy wyniki z 1a i 1b czyli mamy 80 próbek; a dla np. kolekcji A – 120 próbek itd.) → GRUPY ZALEŻNE

### Redundancja (A vs B):
- zsumowane wyniki A vs zsumowane wyniki B → 40 próbek → GRUPY ZALEŻNE
- kolekcja grafik A vs kolekcja grafik B → 120 próbek → GRUPY ZALEŻNE
- 1a vs 1b → 40 próbek → GRUPY ZALEŻNE
- 2a vs 2b → 40 próbek → GRUPY ZALEŻNE
- 3a vs 3b → 40 próbek → GRUPY ZALEŻNE

## Ogólne testy

### 1. Porównanie trzech grup: → test dla grup zależnych (test Friedmana)
- Czy istnieje zależność w poprawności odpowiedzi dla trzech grup grafik (grafiki 1, 2, 3; grafiki 1a, 2a, 3a; grafiki 1b, 2b, 3b)? **(general-0)**
- Czy istnieje zależność w ocenie trudności zadania dla trzech grup grafik (grafiki 1, 2, 3; grafiki 1a, 2a, 3a; grafiki 1b, 2b, 3b)? **(general-0)**
- Czy istnieje zależność w czasie odpowiedzi dla trzech grup grafik (grafiki 1, 2, 3; grafiki 1a, 2a, 3a; grafiki 1b, 2b, 3b)? **(general-0)**

### 2. Korelacje: → test dla grup niezależnych (sumy grafik, każda grafika osobno)

**Poprawność:**

→ korelacja punkt-biserial (dla każdej grafiki osobno)/korelacja Pearsona/ korelacja rang Spearmana (jeśli nie są spełnione założenia korelacji Pearsona tj. normalność, homogeniczność wariancji)

- Czy istnieje istotna statystycznie korelacja między poprawnością odpowiedzi a czasem odpowiedzi? **(general-2)**
- Czy istnieje istotna statystycznie korelacja między poprawnością odpowiedzi a całkowitą/ średnią długością fiksacji/wizyt? **(general-8/9)**
- Czy istnieje istotna statystycznie korelacja między poprawnością odpowiedzi a średnią wielkością źrenicy? **(general-8)**
- Czy istnieje istotna statystycznie korelacja między poprawnością odpowiedzi a liczbą fiksacji / wizyt? **(general-8/9)**

**Trudność zadania:**

→ korelacja rang Spearmana (dane uporządkowane)

- Czy istnieje istotna statystycznie korelacja między oceną trudności zadania a czasem odpowiedzi? **(general-3)**
- Czy istnieje istotna statystycznie korelacja między oceną trudności zadania a całkowitą/ średnią długością fiksacji/wizyt? **(general-8/9)**

- Czy istnieje istotna statystycznie korelacja między oceną trudności zadania a średnią wielkością źrenicy? **(general-8)**
- Czy istnieje istotna statystycznie korelacja między trudnością zadania a liczbą fiksacji / wizyt? **(general-8/9)**

### 3. Dla dwóch grup: → grupy niezależne (sumy grafik, każda grafika osobno)

| Typ zmiennej  |  Test | Dane testowane  |
|:-:|---|---|
| nominalna  | test Chi2, jeśli liczebność próbki dla każdej grupy co najmniej 5, dokładny test Fishera w p.p.  | Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi dla każdej grafiki osobno między <br/>- mężczyznami a kobietami? **(general-5)** <br/>- osobami z wadami wzroku a osobami bez wad wzroku? **(general-5)** <br/>- osobami, które pisały daną maturę a osobami, które nie pisały? **(general-5)** <br/>- osobami które w pytaniu 1 o preferencję przed badaniem wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które w pytaniu 1 o preferencję po badaniu wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 1 a osobami, które nie zmieniły zdania? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 2 a osobami, które nie zmieniły zdania? **(general-4)** <br/>Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi w zależności od ostatniego odwiedzonego AOI? (1a, 2a, 3a) **(general-8)**  |
| porządkowa  | test Manna-Whitney’a  | Czy istnieje istotna statystycznie różnica w ocenie trudności zadania w zależności od poprawności? **(general-1)** <br/>Czy istnieje istotna statystycznie różnica w ocenie trudności zadania między <br/>- mężczyznami a kobietami? **(general-6)** <br/>- osobami z wadami wzroku a osobami bez wad wzroku? **(general-6)** <br/>- osobami, które pisały daną maturę a osobami, które nie pisały?  **(general-6)** <br/>- osobami które w pytaniu 1 o preferencję przed badaniem wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które w pytaniu 1 o preferencję po badaniu wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 1 a osobami, które nie zmieniły zdania? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 2 a osobami, które nie zmieniły zdania? **(general-4)** <br/>Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi dla zsumowanych grafik (poprawność traktujemy rangowo) między <br/>- mężczyznami a kobietami? **(general-5)** <br/> -osobami z wadami wzroku a osobami bez wad wzroku? **(general-5)** <br/>- osobami, które pisały daną maturę a osobami, które nie pisały? **(general-5)** <br/>Czy istnieje istotna statystycznie różnica w ocenie trudności zadania w zależności od ostatniego odwiedzonego AOI? (1a, 2a, 3a) **(general-8)** |
| ilościowa   | test t-Studenta dla grup niezależnych (jeśli rozkład normalny dla obu grup, zachowana homogeniczność wariancji, zbliżona liczebność grup); test Manna-Whitney’a w p.p.  | Czy istnieje istotna statystycznie różnica w czasie odpowiedzi między <br/>- mężczyznami a kobietami? **(general-7)** <br/>- osobami z wadami wzroku a osobami bez wad wzroku? **(general-7)** <br/>- osobami, które pisały daną maturę a osobami, które nie pisały? **(general-7)** <br/>- osobami które w pytaniu 1 o preferencję przed badaniem wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które w pytaniu 1 o preferencję po badaniu wybrały A a osobami, które wybrały B? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 1 a osobami, które nie zmieniły zdania? **(general-4)** <br/>- osobami które zmieniły zdanie w pytaniu 2 a osobami, które nie zmieniły zdania? **(general-4)**  |
### 4. Dla więcej niż dwóch grup: → grupy niezależne (sumy grafik, każda grafika osobno)

| Typ zmiennej  |  Test | Dane testowane  |
|:-:|---|---|
| nominalna  | test Chi2, jeśli założenia nie są spełnione: test Chi2 z korektą Yate’s  | Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi w zależności od oceny trudności zadania? **(general-1)** <br/>Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi dla każdej grafiki osobno między <br/>- osobami urodzonymi w różnych latach? **(general-5)** <br/>- osobami na różnych latach studiów? **(general-5)** <br/>- osobach na różnych kierunkach studiów? **(general-5)** <br/>- osobach na różnych specjalnościach? **(general-5)** <br/>- osobami które w pytaniu 2 o preferencję przed badaniem wybrały różne formy? **(general-4)** <br/>- osobami które w pytaniu 2 o preferencję po badaniu wybrały różne formy? **(general-4)** <br/>- osobami, u których dominuje dany typ uczenia poznawczego? **(general-5)** <br/>- osobami, które uzyskały różne wyniki matur (rangowo)? **(general-5)** <br/>- osobami o różnych poziomach samopoczucia? **(general-5)** <br/>- osobami o różnych poziomach stresu? **(general-5)** <br/>- osobami o różnych poziomach zmęczenia? **(general-5)** <br/>- osobami o różnych umiejętnościach czytania map? **(general-5)** <br/>- osobami o różnych umiejętnościach analitycznego myślenia? **(general-5)** <br/>- osobami o różnej spostrzegawczości? **(general-5)** <br/>- osobami o różnej podzielności uwagi? **(general-5)** <br/>- osobami o różnych umiejętnościach czytania ze zrozumieniem? **(general-5)** <br/>Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi w zależności od ostatniego odwiedzonego AOI? (1b, 2b, 3b) **(general-8)**  |
| porządkowa  | test Kruskala-Wallisa  | Czy istnieje istotna statystycznie różnica w ocenie trudności zadania między <br/>- osobami urodzonymi w różnych latach? **(general-6)** <br/>- osobami na różnych latach studiów? **(general-6)** <br/>- osobach na różnych kierunkach studiów? **(general-6)** <br/>- osobach na różnych specjalnościach? **(general-6)** <br/>- osobami które w pytaniu 2 o preferencję przed badaniem wybrały różne formy? **(general-4)** <br/>- osobami które w pytaniu 2 o preferencję po badaniu wybrały różne formy? **(general-4)** <br/>- osobami, u których dominuje dany typ uczenia poznawczego? **(general-6)** <br/>- osobami, które uzyskały różne wyniki matur (rangowo)? **(general-6)** <br/>- osobami o różnych poziomach samopoczucia? **(general-6)** <br/>- osobami o różnych poziomach stresu? **(general-6)** <br/>- osobami o różnych poziomach zmęczenia? **(general-6)** <br/>- osobami o różnych umiejętnościach czytania map? **(general-6)** <br/>- osobami o różnych umiejętnościach analitycznego myślenia? **(general-6)** <br/>- osobami o różnej spostrzegawczości? **(general-6)** <br/>- osobami o różnej podzielności uwagi? **(general-6)** <br/>- osobami o różnych umiejętnościach czytania ze zrozumieniem?  **(general-6)** <br/>Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi dla zsumowanych grafik (poprawność nabiera rangowego charakteru) między <br/>- osobami urodzonymi w różnych latach? **(general-5)** <br/>- osobami na różnych latach studiów? **(general-5)** <br/>- osobach na różnych kierunkach studiów? **(general-5)** <br/>- osobach na różnych specjalnościach? **(general-5)** <br/>- osobami, u których dominuje dany typ uczenia poznawczego? **(general-5)** <br/>- osobami, które uzyskały różne wyniki matur (rangowo)? **(general-5)** <br/>- osobami o różnych poziomach samopoczucia? **(general-5)** <br/>- osobami o różnych poziomach stresu? **(general-5)** <br/>- osobami o różnych poziomach zmęczenia? **(general-5)** <br/>- osobami o różnych umiejętnościach czytania map? **(general-5)** <br/>- osobami o różnych umiejętnościach analitycznego myślenia? **(general-5)** <br/>- osobami o różnej spostrzegawczości? **(general-5)** <br/>- osobami o różnej podzielności uwagi? **(general-5)** <br/>- osobami o różnych umiejętnościach czytania ze zrozumieniem? **(general-5)** <br/>Czy istnieje istotna statystycznie różnica w ocenie trudności zadania w zależności od ostatniego odwiedzonego AOI? (1b, 2b, 3b) **(general-8)**  |
| ilościowa   | test ANOVA dla grup niezależnych (jeśli rozkład normalny dla wszystkich grup, zachowana homogeniczność wariancji, liczebność każdej grupy co najmniej 20); test Kruskala-Wallisa w p.p.  | Czy istnieje istotna statystycznie różnica w czasie odpowiedzi między <br/>- osobami urodzonymi w różnych latach? **(general-7)** <br/>- osobami na różnych latach studiów? **(general-7)** <br/>- osobach na różnych kierunkach studiów? **(general-7)** <br/>- osobach na różnych specjalnościach? **(general-7)** <br/>- osobami które w pytaniu 2 o preferencję przed badaniem wybrały różne formy? **(general-4)** <br/>- osobami które w pytaniu 2 o preferencję po badaniu wybrały różne formy? **(general-4)** <br/>- osobami, u których dominuje dany typ uczenia poznawczego? **(general-7)** <br/>- osobami, które uzyskały różne wyniki matur (rangowo)? **(general-7)** <br/>- osobami o różnych poziomach samopoczucia? **(general-7)** <br/>- osobami o różnych poziomach stresu? **(general-7)** <br/>- osobami o różnych poziomach zmęczenia? **(general-7)** <br/>- osobami o różnych umiejętnościach czytania map? **(general-7)** <br/>- osobami o różnych umiejętnościach analitycznego myślenia? **(general-7)** <br/>- osobami o różnej spostrzegawczości? **(general-7)** <br/>- osobami o różnej podzielności uwagi? **(general-7)** <br/>- osobami o różnych umiejętnościach czytania ze zrozumieniem? **(general-7)**  |

## Testy dla redundancji (czyli dla dwóch grup zależnych):

| Typ zmiennej  |  Test | Dane testowane  |
|:-:|---|---|
| nominalne  | test McNemara https://www.ncbi.nlm.nih.gov/books/NBK560699/#:~:text=The%20McNemar%20test%20is%20a,variable%20with%20two%20dependent%20groups.  | Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi między grupami A vs B? **(redundancy-1)** <br/> Czy istnieje istotna statystycznie różnica w poprawności odpowiedzi dla: <br/>- kobiet/mężczyzn  <br/>- danego roku urodzenia <br/>- danego roku studiów <br/>- danego kierunku studiów <br/>- danej specjalności <br/>- wady wzroku / braku wady <br/>- osób piszących maturę z przedmiotu X / osób nie piszących <br/>- dominującego typu uczenia poznawczego <br/>- ilości snu <br/>- poziomu samopoczucia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu stresu (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu zmęczenia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności czytania map (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- podzielności uwagi (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności analitycznego myślenia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu spostrzegawczości (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności czytania ze zrozumieniem (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- odpowiedzi na pytanie 1 przed badaniem (preferencja A vs B) <br/>- odpowiedzi na pytanie 1 po badaniu (preferencja A vs B) <br/>- odpowiedzi na pytanie 2 przed badaniem (preferencja mapa, tabela, tekst, wykres) <br/>- odpowiedzi na pytanie 2 po badaniu (preferencja mapa, tabela, tekst, wykres) <br/>- osób które zmieniły zdanie w pytaniu 1 / osób, które nie zmieniły <br/>- osób które zmieniły zdanie w pytaniu 2 / osób, które nie zmieniły <br/>między grupami A vs B? **(redundancy-3)**  |
| porządkowe | test Wilcoxona  | Czy istnieje istotna statystycznie różnica w ocenie trudności zadania między grupami A vs B? **(redundancy-1)** <br/> Czy istnieje istotna statystycznie różnica w ocenie trudności zadania dla: <br/>- kobiet/mężczyzn  <br/>- danego roku urodzenia <br/>- danego roku studiów <br/>- danego kierunku studiów <br/>- danej specjalności <br/>- wady wzroku / braku wady <br/>- osób piszących maturę z przedmiotu X / osób nie piszących <br/>- <br/>- dominującego typu uczenia poznawczego <br/>- ilości snu <br/>- poziomu samopoczucia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu stresu (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu zmęczenia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności czytania map (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- podzielności uwagi (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności analitycznego myślenia (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- poziomu spostrzegawczości (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- umiejętności czytania ze zrozumieniem (niski = 1,2; średni = 3; wysoki = 4,5) <br/>- odpowiedzi na pytanie 1 przed badaniem (preferencja A vs B) <br/>- odpowiedzi na pytanie 1 po badaniu (preferencja A vs B) <br/>- dpowiedzi na pytanie 2 przed badaniem (preferencja mapa, tabela, tekst, wykres) <br/>- odpowiedzi na pytanie 2 po badaniu (preferencja mapa, tabela, tekst, wykres) <br/>- osób które zmieniły zdanie w pytaniu 1 / osób, które nie zmieniły <br/>- osób które zmieniły zdanie w pytaniu 2 / osób, które nie zmieniły  <br/>między grupami A vs B? **(redundancy-4)**  |
| ilościowe  | test t-Studenta dla grup zależnych (jeśli rozkład normalny dla obu grup); test Wilcoxona w p.p. | Czy istnieje istotna statystycznie różnica w czasie odpowiedzi między grupami A vs B? **(redundancy-1)** <br/> Czy istnieje istotna statystycznie różnica w całkowitej długości fiksacji/wizyt między grupami A vs B? **(redundancy-2)** <br/> Czy istnieje istotna statystycznie różnica w średniej długości fiksacji/wizyt między grupami A vs B? **(redundancy-2)** <br/> Czy istnieje istotna statystycznie różnica w liczbie fiksacji/wizyt między grupami A vs B? **(redundancy-2)** <br/> Czy istnieje istotna statystycznie różnica w średniej poprawności odpowiedzi między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średniej ocenie trudności zadania między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średnim czasie odpowiedzi między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średniej całkowitych długości fiksacji/wizyt między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średniej średnich długości fiksacji/wizyt między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średniej średnich wielkości źrenicy między grupami A vs B? <br/> Czy istnieje istotna statystycznie różnica w średniej liczbie fiksacji/wizyt między grupami A vs B? <br/> <br/> ANALIZA MAPA A VS MAPA B <br/> Czy istnieje istotna statystycznie różnica w całkowitej długości fiksacji/wizyt między grupami mapa A vs mapa B? <br/> Czy istnieje istotna statystycznie różnica w średniej długości fiksacji/wizyt między grupami mapa A vs mapa B? <br/> Czy istnieje istotna statystycznie różnica w liczbie fiksacji/wizyt między grupami mapa A vs mapa B?  <br/> Czy istnieje istotna statystycznie różnica w średniej całkowitych długości fiksacji/wizyt między grupami mapa A vs mapa B? <br/> Czy istnieje istotna statystycznie różnica w średniej średnich długości fiksacji/wizyt między grupami mapa A vs mapa B? <br/> Czy istnieje istotna statystycznie różnica w średniej średnich wielkości źrenicy między grupami mapa A vs mapa B? <br/> Czy istnieje istotna statystycznie różnica w średniej liczbie fiksacji/wizyt między grupami mapa A vs mapa B?|

### Analiza wieloczynnikowa 

#### 1. Szczegółowe wartości zmiennych zależnych:
→ Metoda: Linear Mixed Effects Models - statsmodels 0.14.0 → OK

**Zmienne zależne:**
- poprawność
- trudność
- czas odpowiedzi
- całkowita długość fiksacji/wizyt
- średnia długość fiksacji/wizyt
- średnia wielkość źrenicy
- liczba fiksacji/wizyt

**Zmienne niezależne: – cechy osobowe z ankiety + grupa (A, B)**

Stosujemy dwa podejścia:
- zmienne objaśniające: grupa (A/B) + cecha osobowa (oddzielnie) → jako dwie oddzielne kolumny
- zmienna objaśniająca: grupa (A/B) + cecha osobowa (razem) → jako scalenie kolumn

#### 2. Średnie wartości zmiennych zależnych (liczymy średnie dla 1, 2, 3 w grupach A, B dla każdej osoby)  - kolekcja - 80 wierszy

→ Metoda: Linear Mixed Effects Models - statsmodels 0.14.0 → OK

**Zmienne zależne:**
- poprawność
- trudność
- czas odpowiedzi
- całkowita długość fiksacji/wizyt
- średnia długość fiksacji/wizyt
- średnia wielkość źrenicy
- liczba fiksacji/wizyt

**Zmienne niezależne: – cechy osobowe z ankiety + grupa (A, B)**

Stosujemy dwa podejścia:
- zmienne objaśniające: grupa (A/B) + cecha osobowa (oddzielnie) → jako dwie oddzielne kolumny
- zmienna objaśniająca: grupa (A/B) + cecha osobowa (razem) → jako scalenie kolumn

#### 3. Analiza mapa vs tabela vs tekst vs wykres - grafiki B

→ Metoda: ANOVA statsmodels.stats.anova.AnovaRM - statsmodels 0.14.0 → OK

**POSZCZEGÓLNE DANE:**
– Czy istnieje istotna statystycznie różnica w całkowitej długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej wielkości źrenicy między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w liczbie fiksacji/wizyt między poszczególnymi formami prezentacji danych? 

**SUMY:**
– Czy istnieje istotna statystycznie różnica w sumie całkowitych długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w sumie średnich długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w sumie liczb fiksacji/wizyt między poszczególnymi formami prezentacji danych? 

**ŚREDNIE:**
– Czy istnieje istotna statystycznie różnica w średniej całkowitych długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej średnich długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej średnich wielkości źrenicy między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej liczbie fiksacji/wizyt między poszczególnymi formami prezentacji danych?

## Założenia dotyczące testów

1. Test niezależności chi2-Pearsona
- niezależność prób
- badamy zmienne kategoryczne
- wielkość próby dla każdej z grup - conajmniej 5

2. Test t-Studenta
- niezależność prób
- rozkład zmiennej zależnej w każdej z analizowanych grup pochodzi z rozkładu normalnego --> Test Shapiro-Wilka
- porówynwane grupy mają zbliżoną liczebność
- homogeniczność wariancji dla porównywanych grup --> Test Levene'a --> jeśli nie zachowana stosujemy poprawkę stopni swobody testu t-Studenta
- zmienna zależna mierzona jest w skali ilościowej

3. Test Manna-Whitney'a
- niezależność prób
- zmienna zależna mierzona jest w skali conajmniej porządkowej (porządkowa lub ilościowa), można też stosować dla skali dychotomicznej (0-1)
- stosujemy jeśli nie są spełnione założenia testu t-Studenta, nie wymaga żadnego innego założenia

4. Test ANOVA
- niezależność prób
- liczebność dla każdej z grup conajmniej 20
- rozkład zmiennej zależnej w każdej z analizowanych grup pochodzi z rozkładu normalnego
- homogeniczność wariancji dla porównywanych grup 

5. Test Kruskala-Wallisa 
- niezależność prób
- jeśli nie są spełnione założenia testu ANOVA

Testy pomocnicze do implementacji:
- Shapiro-Wilka
- Levene'a
- Testy posthoc

### Wykresy:

Dwie zmienne kategoryczne: heatmapa na tabeli kontyngencji

Jedna kategoryczna druga ilościowa dyskretna: punktowy z regresją; wykres pudełkowy

Jedna kategoryczna druga ilościowa ciągła: density plot; wykres pudełkowy

References: 
- Chi2/Fisher tests: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5426219/#:~:text=The%20chi%2Dsquared%20test%20applies,especially%20for%20small%2Dsized%20samples.
- T-student test: https://www.jmp.com/en_ch/statistics-knowledge-portal/t-test.html
- Manna-Whitney'a: https://www.researchgate.net/publication/5147446_Nonparametric_Tests_of_Differences_in_Medians_Comparison_of_the_Wilcoxon-Mann-Whitney_and_Robust_Rank-Order_Tests; https://statistics.laerd.com/spss-tutorials/mann-whitney-u-test-using-spss-statistics.php
- ANOVA/ Kruskal-Wallis: https://www.researchgate.net/publication/361988408_Power_comparison_of_ANOVA_and_Kruskal-Wallis_tests_when_error_assumptions_are_violated
- skrypt SAD, Stata MIMUW --> poszukać literatury z prezentacji

### Czy próbki są niezależne?

- Kolekcja (powielenie) --> NIE
- Suma wyników --> TAK bo każdy badany to osobny wiersz
- Każda grafika --> TAK bo każdy badany to osobny wiersz

Założenie: niezależność prób --> spełnione, bo każda osoba odpowiadała na pytania niezależnie od pozostałych
