import matplotlib.pyplot as plt
import numpy as np


def corr_answer_index(contingency_table):
    wskaznik = []
    trudnosc = []
    for i in contingency_table.columns.tolist():
        popr = contingency_table.loc[1, i]
        niepopr = contingency_table.loc[0, i]
        if popr != 0:
            wsk = (popr - niepopr) / popr
        else:
            continue
        wskaznik.append(wsk)
        trudnosc.append(i)
        print(f"Trudność: {i}, Wskaźnik: {wsk}")

    plt.bar(trudnosc, wskaznik, color='skyblue')
    plt.xlabel('Ocena trudności zadania')
    plt.ylabel('$\\frac{poprawne-niepoprawne}{poprawne}$')
    plt.title('Przewaga poprawnych odpowiedzi nad niepoprawnymi\nw zależności od oceny trudności zadania')

    # Regresja
    coefficients = np.polyfit(trudnosc, wskaznik, 1)
    polynomial = np.poly1d(coefficients)
    x_axis = np.linspace(min(trudnosc), max(trudnosc), 100)
    plt.plot(x_axis, polynomial(x_axis), color='red', label='Regresja liniowa')

    # Średnia
    srednia = np.linspace(np.mean(wskaznik), np.mean(wskaznik), 100)
    plt.plot(x_axis, srednia, color='green', linestyle='dotted', label='Średnia')

    plt.legend()
    plt.grid(which='both')
    plt.show()


def choose_dominant_kind(x):
    k = x['Kinestetyk']
    s = x['Słuchowiec']
    w = x['Wzrokowiec']
    if k > s and k > w:
        return 'Kinestetyk'
    elif s > k and s > w:
        return 'Słuchowiec'
    elif w > k and w > s:
        return 'Wzrokowiec'
    else:
        return "Brak dominującego"


def change_to_ranges_podst(x):
    if x == '30 - 49%':
        return 1
    elif x == '50 - 69%':
        return 2
    elif x == '70 - 89%':
        return 3
    elif x == '90 - 100%':
        return 4


def change_to_ranges_roz(x):
    if x == 'NO_VAL':
        return 0
    elif x == 'poniżej 20%':
        return 1
    elif x == '20 - 49%':
        return 2
    elif x == '50 - 70%':
        return 3
    elif x == 'powyżej 70%':
        return 4

def replace_to_categories(x):
    x = int(x)
    if x < 3:
        return 'niski'
    elif x == 3:
        return 'średni'
    else:
        return 'wysoki'