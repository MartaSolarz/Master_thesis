# Metodyka testów

## Zmienne:

| Nazwa                                                                                                                                                        | Typ                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| poprawność odpowiedzi                                                                                                                                        | kategoryczna (sumy), kategoryczna binarna (kolekcje, osobne grafiki) |
| trudność zadania                                                                                                                                             | kategoryczna                                                         |
| czas odpowiedzi                                                                                                                                              | ilościowa ciągła                                                     |
| questions 1,2 (preferencje A vs B) oraz (mapa, tabela, tekst, wykres)                                                                                        | kategoryczne                                                         |
| cechy osobowe (płeć, rok urodzenia, kierunek studiów, rok studiów, specjalność, wady wzroku, ilość snu, wyniki matur, umiejętności, typ uczenia poznawczego) | kategoryczne                                                         |
| całkowita długość fiksacji/wizyty, średnia długość fiksacji/wizyty, średnia wielkość źrenicy                                                                 | ilościowe ciągłe                                                     |
| liczba fiksacji/wizyty                                                                                                                                       | ilościowe dyskretne                                                  |
| ostatnie odwiedzone AOI                                                                                                                                      | kategoryczna                                                         |


*kategoryczna - zmienna o charakterze jakościowym, skończona liczba osiąganych wartości

## Testy ogólne

**H0:** Brak istotnej statystycznie zależności między X a Y.

**H1:** Istnieje istotna statystycznie zależność między X a Y.

**Poziom istotności:** $\alpha = 0.05$.

| NR TESTU | X                                                | Y                                                                                                       | TEST                                               |
|----------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 1        | poprawność odpowiedzi                            | trudność zadania                                                                                        | chi2                                               |
| 2        | poprawność odpowiedzi                            | czas odpowiedzi                                                                                         | ANOVA/Kruskal-Wallis                               |
| 3        | czas odpowiedzi                                  | trudność zadania                                                                                        | ANOVA/Kruskal-Wallis                               |
| 4        | poprawność odpowiedzi                            | quest1/2                                                                                                | chi2                                               |
| 5        | poprawność odpowiedzi                            | cechy osobowe                                                                                           | chi2                                               |
| 6        | trudność zadania                                 | cechy osobowe                                                                                           | chi2                                               |
| 7        | czas odpowiedzi                                  | cechy osobowe                                                                                           | ANOVA/Kruskal-Wallis                               |
| 8        | 1) poprawność odpowiedzi<br/>2) trudność zadania | całkowita, średnia długość fiksacji, średnia wielkość źrenicy, liczba fiksacji, ostatnie odwiedzone AOI | ANOVA/Kruskal-Wallis, t-Student/Mann-Whitney, chi2 |
| 9        | 1) poprawność odpowiedzi<br/>2) trudność zadania | całkowita, średnia długość wizyty, liczba wizyt                                                         | ANOVA/Kruskal-Wallis, t-Student/Mann-Whitney       |


## Flow wyboru testu:

### Case'y:

**Mamy dwie zmienne kategoryczne:**
- test chi2
- jeśli nie można chi2: korelacja rang Spearmana ??? (dokładny test Fishera odpada, bo musi być tabela kontyngencji 2x2, a zazwczaj u nas jest większa...)
- posthoc: test Nemenyi (nieparametryczna)

**Mamy zmienną kategoryczną i zmienną ilościową dyskretną:**
1. Jeśli zmienna kategoryczna jest binarna (mamy tylko dwie grupy):
   - test t-Studenta 
   - jeśli nie można t-Studenta: test Manna-Whitney'a
2. Jeśli zmienna katogoryczna przyjmuje więcej niż dwie wartości:
   - test ANOVA
   - jeśli nie można ANOVA: test Kruskala-Wallisa
   - posthoc: Tukey/Nemenyi (parametryczna vs nieparametryczna)

**Mamy zmienną kategoryczną i zmienną ilościową ciągłą:**
- test ANOVA
- jeśli nie można ANOVA: test Kruskala-Wallisa

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

- Kolekcja (powielenie) --> TAK bo zrobiliśmy losową kolejność grafik dla każdego badanego
- Suma wyników --> TAK bo każdy badany to osobny wiersz
- Każda grafika --> TAK bo każdy badany to osobny wiersz

Założenie: niezależność prób --> spełnione, bo każda osoba odpowiadała na pytania niezależnie od pozostałych
