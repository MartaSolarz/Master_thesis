# Master thesis
Analysis for master's thesis.

## I. General tests:

| Zmienna zależna    | Zmienna/e niezależna/e              | H0, H1                                                                                                                                                                                                                                                                                                                                                            | Analizowane serie grafik                                                                                                                                                                                                                                                         | Metodyka                                                                                                                                                 | Wykresy                                                                   |
|--------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| poprawność         | pewność / trudność                  | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a poziomem trudności. <br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a poziomem trudności.                                                                                                                                                                    | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>każda osobno;<br/>+ trudność dla trzech grup 1,2,3;                                                                                                | test chi2 - dwie zmienne dyskretne                                                                                                                       | index poprawne/niepoprawne odpowiedzi                                     |
| poprawność         | czas                                | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a czasem odpowiedzi.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a czasem odpowiedzi.                                                                                                                                                     | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>każda osobno;                                                                                                                                      | test - regresja logistyczna (zmienna zależna - dyskretna, zmienna niezależna - ciągła)                                                                   | scatter plot + logit regression, roc, residuals, efekty warunkowe         |
| poprawność         | pewność / trudność i czas           | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a czasem odpowiedzi i trudnością zadania.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a czasem odpowiedzi i trudnością zadania.                                                                                                           | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>każda osobno;                                                                                                                                      | test - regresja logistyczna (zmienna zależna - dyskretna, zmienne niezależne - ciągła i dyskretna)                                                       | scatter plot + logit regression, roc, residuals, efekty warunkowe         |
| czas               | pewność / trudność                  | **H0:** Nie ma istotnej statystycznie zależności między czasem odpowiedzi a trudnością zadania.<br/>**H1:** Istnieje istotna statystycznie zależność między czasem odpowiedzi a trudnością zadania.                                                                                                                                                               | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>każda osobno;                                                                                                                                      | test - normalności (Shapiro-Wilka), jeśli rozkład normalny -> homogeniczność wariancji Levene'a, jeśli spełniona --> test ANOVA; w.p.p. Kruskala-Wallisa | scatter plot + regresja liniowa, residuals, histogram rozkładu normalnego |
| poprawność         | Quest1, Quest2 - przed i po badaniu | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a wybraną preferowaną formą (mapa vs mapa + inne elementy; mapa vs tabela vs wykres vs tekst).<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a wybraną preferowaną formą (mapa vs mapa + inne elementy; mapa vs tabela vs wykres vs tekst).<br/>**H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a zmianą zdania w pytaniu 1/2.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a zmianą zdania w pytaniu 1/2. | Dla 4 pytań: powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Zmiany: powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>osobno: 1a, 1b (wyszła istotnośc statystyczna dla 1); |      test chi2 - dwie zmienne dyskretne                                                                                                                                                | brak                                                                      |
| poprawność         | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a wartością cechy X.                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                          |                                                                           |
| pewność / trudność | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między trudnością zadania a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między trudnością zadania a wartością cechy X.                                                                                                                                                               |                                                                                                                                                                                                                                                                                  |                                                                                                                                                          |                                                                           |
| czas               | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między czasem odpowiedzi a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między czasem odpowiedzi a wartością cechy X.                                                                                                                                                                 |                                                                                                                                                                                                                                                                                  |                                                                                                                                                          |                                                                           |

**Poziom istotności:** $\alpha=0.05$
