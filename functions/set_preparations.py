import pandas as pd


def prepare_row(list_of_cols):
    """
    Prepare single row for data set.
    """
    new_row = list_of_cols[0]
    for i in list_of_cols[1:]:
        new_row = pd.concat([new_row, i], ignore_index=True)

    return new_row

def prepare_row_df(df):
    """
    Prepare single row for data set.
    """
    new_row = df[df.columns[0]]
    for i in range(1, len(df.columns)):
        new_row = pd.concat([new_row, df[df.columns[i]]], ignore_index=True)

    return new_row

def prepare_set_changes_questions(list_of_cols, quest1, quest2, name_list_of_cols):
    new_row = list_of_cols[0]
    for i in list_of_cols[1:]:
        new_row = pd.concat([new_row, i], ignore_index=True)

    new_row_quest1 = quest1[0]
    for i in quest1[1:]:
        new_row_quest1 = pd.concat([new_row_quest1, i], ignore_index=True)

    new_row_quest2 = quest2[0]
    for i in quest2[1:]:
        new_row_quest2 = pd.concat([new_row_quest2, i], ignore_index=True)

    return pd.DataFrame({name_list_of_cols: new_row, 'quest1': new_row_quest1, 'quest2': new_row_quest2})


def sum_rows(row, pattern, specify, flag=False):
    if flag:
        pref = pattern
        suf = ''
    else:
        pref, suf = pattern.split()
    el1 = pref + specify[0] + suf
    el2 = pref + specify[1] + suf
    if len(specify) == 3:
        el3 = pref + specify[2] + suf
        return row[el1] + row[el2] + row[el3]
    elif len(specify) == 2:
        return row[el1] + row[el2]
    else:
        return ValueError
