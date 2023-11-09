# Metodyka testów

## Zmienne:

| Nazwa                                                                                                                                                        | Typ                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
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

### 4. Dla więcej niż dwóch grup: → grupy niezależne (sumy grafik, każda grafika osobno)

## Testy dla redundancji (czyli dla dwóch grup zależnych):

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

Zmienne zależne:
poprawność
trudność
czas odpowiedzi
całkowita długość fiksacji/wizyt
średnia długość fiksacji/wizyt
średnia wielkość źrenicy
liczba fiksacji/wizyt
Zmienne niezależne: – cechy osobowe z ankiety + grupa (A, B)
Stosujemy dwa podejścia:
zmienne objaśniające: grupa (A/B) + cecha osobowa (oddzielnie) → jako dwie oddzielne kolumny
zmienna objaśniająca: grupa (A/B) + cecha osobowa (razem) → jako scalenie kolumn

Analiza mapa vs tabela vs tekst vs wykres - grafiki B
→ Metoda: ANOVA statsmodels.stats.anova.AnovaRM - statsmodels 0.14.0 → OK

SUMY:
– Czy istnieje istotna statystycznie różnica w sumie całkowitych długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w sumie średnich długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w sumie liczb fiksacji/wizyt między poszczególnymi formami prezentacji danych? 

POSZCZEGÓLNE DANE:
– Czy istnieje istotna statystycznie różnica w całkowitej długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej wielkości źrenicy między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w liczbie fiksacji/wizyt między poszczególnymi formami prezentacji danych? 

ŚREDNIE:
– Czy istnieje istotna statystycznie różnica w średniej całkowitych długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej średnich długości fiksacji/wizyt między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej średnich wielkości źrenicy między poszczególnymi formami prezentacji danych?
– Czy istnieje istotna statystycznie różnica w średniej liczbie fiksacji/wizyt między poszczególnymi formami prezentacji danych?



## Założenia dotyczące testów:

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
