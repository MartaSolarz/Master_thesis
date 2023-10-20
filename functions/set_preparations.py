import pandas as pd

def prepare_row(list_of_cols):
    """
    Prepare single row for data set.
    """
    new_row = list_of_cols[0]
    for i in list_of_cols[1:]:
        new_row = pd.concat([new_row, i], ignore_index=True)

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