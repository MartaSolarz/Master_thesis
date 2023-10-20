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