# Metodyka testów

### Nasze zmienne:
- poprawność odpowiedzi: kategoryczna binarna (w przypadku analizowania każdej grafiki osobno lub kolekcji); kategoryczna (w przypadku analizowania sumy grafik);
- pewność/trudność odpowiedzi: kategoryczna;
- czas odpowiedzi: ilościowa ciągła;
- questions 1,2: kategoryczne;
- cechy osobowe (płeć, rok urodzenia, kierunek studiów, rok studiów, specjalność, wady wzroku, ilość snu, wyniki matur, umiejętności, typ uczenia poznawczego): kategoryczne;
- całkowita długość fiksacji/wizyty, średnia długość fiksacji/wizyty, średnia wielkość źrenicy: ilościowe ciągłe;
- liczba fiksacji/wizyty: ilościowa dyskretna;
- ostatnie odwiedzone AOI: kategoryczna;

*kategoryczna - zmienna o charakterze jakościowym, skończona liczba osiąganych wartości

### Jakie testy chcemy przeprowadzić?

**H0:** brak istotnej statystycznie zależności między A a B

**H1:** istnieje istotna statystycznie zależność między A a B

**Poziom istotności:** $\alpha = 0.05$

1. A = poprawność odpowiedzi; B = trudność --> kategoryczna binarna / kategoryczna vs kategoryczna --> test chi2 / dokładny test Fishera
2. A = poprawność odpowiedzi; B = czas odpowiedzi --> kategoryczna binarna / kategoryczna vs ilościowa ciągła --> ANOVA/Kruskala-Wallisa
3. A = czas odpowiedzi; B = pewność/trudność --> ilościowa ciągła vs kategoryczna --> ANOVA/Kruskala-Wallisa
4. A = poprawność odpowiedzi; B = quest1/2 --> kategoryczna binarna / kategoryczna vs kategoryczne --> test chi2 / dokładny test Fishera
5. A = poprawność odpowiedzi; B = cechy osobowe --> kategoryczna binarna / kategoryczna vs kategoryczne --> test chi2 / dokładny test Fishera
6. A = trudność; B = cechy osobowe --> kategoryczna vs kategoryczne --> test chi2 / dokładny test Fishera
7. A = czas odpowiedzi; B = cechy osobowe --> ilościowa ciągła vs kategoryczne --> ANOVA/Kruskala-Wallisa
8. A = poprawność odpowiedzi; B = metryki fiksacje/wizyty (całkowita, średnia długość fiksacji/wizyty) --> kategoryczna binarna / kategoryczna vs ilościowe ciągłe --> ANOVA/Kruskala-Wallisa 
9. A = poprawność odpowiedzi; B = średnia wielkość źrenicy --> kategoryczna binarna / kategoryczna vs ilościowa ciągła --> ANOVA/Kruskala-Wallisa
10. A = poprawność odpowiedzi; B = metryki fiksacje/wizyty (liczba fiksacji/wizyt) --> kategoryczna binarna / kategoryczna vs ilościowa dyskretna --> gdy binarna (t-Student/Manna-Whitney'a); gdy nie jest binarna (ANOVA/Kruskala-Wallisa)
11. A = poprawność odpowiedzi; B = ostatnie odwiedzone AOI --> kategoryczna binarna vs kategoryczna --> test chi2 / dokładny test Fishera

### Flow wyboru testu:

**Mamy dwie zmienne kategoryczne:**
1. Założenie: niezależność prób --> spełnione, bo każda osoba odpowiadała na pytania niezależnie od pozostałych
2. Wielkość próbki dla każdej z grup: 
   - jeśli $> 5$ --> test niezależności chi2-Pearsona; 
   - wpp --> dokładny test Fishera; ??? musi być tabela kontyngencji 2x2, więc też nie można... może korelacja rang Spearmana?

**Mamy zmienną kategoryczną i zmienną ilościową dyskretną:**
1. Jeśli zmienna kategoryczna jest binarna (mamy tylko dwie grupy):
   - test t-Studenta 
   - test Manna-Whitney'a
2. Jeśli zmienna katogoryczna przyjmuje więcej niż dwie wartości (zmienna jakościowa dyskretna):
   - test ANOVA
   - test Kruskala-Wallisa

**Mamy zmienną kategoryczną i zmienną ilościową ciągłą:**
- test ANOVA
- test Kruskala-Wallisa

### Założenia dotyczące testów:

**H0:** brak istotnej statystycznie zależności między X a Y

**H1:** istnieje istotna statystycznie zależnośc między X a Y

1. Test niezależności chi2 Pearsona
- niezależność prób
- badamy zmienne kategoryczne
- wielkość próby dla każdej z grup - conajmniej 5

2. Dokładny test Fishera
- niezależność prób
- badamy zmienne kategoryczne
- wielkość próby dla każdej z grup - może być mniejsza równa 5

3. Test t-Studenta --> badanie równości średnich dla grup
- niezależność prób
- rozkład zmiennej zależnej w każdej z analizowanych grup pochodzi z rozkładu normalnego --> Test Shapiro-Wilka
- porówynwane grupy mają zbliżoną liczebność
- homogeniczność wariancji dla porównywanych grup --> Test Levene'a --> jeśli nie zachowana stosujemy poprawkę stopni swobody testu t-Studenta
- zmienna zależna mierzona jest w skali ilościowej

4. Test Manna-Whitney'a --> badanie median dla grup
- niezależność prób
- zmienna zależna mierzona jest w skali conajmniej porządkowej (porządkowa lub ilościowa), można też stosować dla skali dychotomicznej (0-1)
- stosujemy jeśli nie są spełnione założenia testu t-Studenta, nie wymaga żadnego innego założenia

5. Test ANOVA -> badanie równości wariancji między grupami
- niezależność prób
- liczebność dla każdej z grup conajmniej 20
- rozkład zmiennej zależnej w każdej z analizowanych grup pochodzi z rozkładu normalnego
- homogeniczność wariancji dla porównywanych grup 

6. Test Kruskala-Wallisa 
- niezależność prób
- jeśli nie są spełnione założenia testu ANOVA

Testy pomocnicze do implementacji:
- Shapiro-Wilka
- Levene'a
- Test zgodności chi2


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

