# Master_thesis
Analysis for master's thesis.

## I. General tests:

| Zmienna zależna    | Zmienna/e niezależna/e              | H0, H1                                                                                                                                                                                                                                                                                                                                                            | Analizowane serie grafik                                                                                                                                                     | Metodyka                                                                               | Wykresy                                                           |
|--------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| poprawność         | pewność / trudność                  | **H0:** Nie ma istotnej statystycznie zależności między poziomem trudności a poprawnością odpowiedzi. <br/>**H1:** Istnieje istotna statystycznie zależność między poziomem trudności a poprawnością odpowiedzi.                                                                                                                                                  | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3, każda osobno;<br/>+ trudność dla trzech grup 1,2,3 | test chi2 - dwie zmienne dyskretne                                                     | index poprawne/niepoprawne odpowiedzi                             |
| poprawność         | czas                                | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a czasem odpowiedzi.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a czasem odpowiedzi.                                                                                                                                                     | Zsumowany wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3;<br/>Powielony wynik: wszystkie grafiki, grafiki A, B, 1, 2, 3, każda osobno                                       | test - regresja logistyczna (zmienna zależna - dyskretna, zmienna niezależna - ciągła) | scatter plot + logit regression, roc, residuals, efekty warunkowe |
| poprawność         | pewność / trudność i czas           | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a czasem odpowiedzi i trudnością zadania.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a czasem odpowiedzi i trudnością zadania.                                                                                                           |                                                                                                                                                                              |                                                                                        |                                                                   |
| czas               | pewność / trudność                  | **H0:** Nie ma istotnej statystycznie zależności między czasem odpowiedzi a trudnością zadania.<br/>**H1:** Istnieje istotna statystycznie zależność między czasem odpowiedzi a trudnością zadania.                                                                                                                                                               |                                                                                                                                                                              |                                                                                        |                                                                   |
| poprawność         | Quest1, Quest2 - przed i po badaniu | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a wybraną preferowaną formą (mapa vs mapa + inne elementy; mapa vs tabela vs wykres vs tekst).<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a wybraną preferowaną formą (mapa vs mapa + inne elementy; mapa vs tabela vs wykres vs tekst). |                                                                                                                                                                              |                                                                                        |                                                                   |
| poprawność         | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między poprawnością odpowiedzi a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między poprawnością odpowiedzi a wartością cechy X.                                                                                                                                                     |                                                                                                                                                                              |                                                                                        |                                                                   |
| pewność / trudność | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między trudnością zadania a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między trudnością zadania a wartością cechy X.                                                                                                                                                               |                                                                                                                                                                              |                                                                                        |                                                                   |
| czas               | cechy osobowe                       | **H0:** Nie ma istotnej statystycznie zależności między czasem odpowiedzi a wartością cechy X.<br/>**H1:** Istnieje istotna statystycznie zależność między czasem odpowiedzi a wartością cechy X.                                                                                                                                                                 |                                                                                                                                                                              |                                                                                        |                                                                   |

**Poziom istotności:** $\alpha=0.05$
