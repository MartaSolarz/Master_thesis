import pandas as pd


# def prepate_set_triple(list_of_cols_czas, list_of_cols_trud, list_of_cols_popr):
#     new_row_czas = list_of_cols_czas[0]
#     for i in list_of_cols_czas[1:]:
#         new_row_czas = pd.concat([new_row_czas, i], ignore_index=True)
#
#     new_row_trud = list_of_cols_trud[0]
#     for i in list_of_cols_trud[1:]:
#         new_row_trud = pd.concat([new_row_trud, i], ignore_index=True)
#
#     new_row_popr = list_of_cols_popr[0]
#     for i in list_of_cols_popr[1:]:
#         new_row_popr = pd.concat([new_row_popr, i], ignore_index=True)
#
#     return pd.DataFrame({'trudnosc': new_row_trud, 'czas': new_row_czas, 'poprawnosc': new_row_popr})

# def prepare_set_double(list_of_cols_1, list_of_cols_2, name_1, name_2):
#     """
#     Prepare double set.
#     """
#     new_row_1 = list_of_cols_1[0]
#     for i in list_of_cols_1[1:]:
#         new_row_1 = pd.concat([new_row_1, i], ignore_index=True)
#
#     new_row_2 = list_of_cols_2[0]
#     for i in list_of_cols_2[1:]:
#         new_row_2 = pd.concat([new_row_2, i], ignore_index=True)
#
#     return pd.DataFrame({name_1: new_row_1, name_2: new_row_2})


def prepare_row(list_of_cols):
    """
    Prepare single row for data set.
    """
    new_row = list_of_cols[0]
    for i in list_of_cols[1:]:
        new_row = pd.concat([new_row, i], ignore_index=True)

    return new_row


# def prepate_set_4questions(list_of_cols, quest1_before, quest1_after, quest2_before, quest2_after, name_list_of_cols):
#     new_row = list_of_cols[0]
#     for i in list_of_cols[1:]:
#         new_row = pd.concat([new_row, i], ignore_index=True)
#
#     new_row_quest1_b = quest1_before[0]
#     for i in quest1_before[1:]:
#         new_row_quest1_b = pd.concat([new_row_quest1_b, i], ignore_index=True)
#
#     new_row_quest2_b = quest2_before[0]
#     for i in quest2_before[1:]:
#         new_row_quest2_b = pd.concat([new_row_quest2_b, i], ignore_index=True)
#
#     new_row_quest1_a = quest1_after[0]
#     for i in quest1_after[1:]:
#         new_row_quest1_a = pd.concat([new_row_quest1_a, i], ignore_index=True)
#
#     new_row_quest2_a = quest2_after[0]
#     for i in quest2_after[1:]:
#         new_row_quest2_a = pd.concat([new_row_quest2_a, i], ignore_index=True)
#
#     return pd.DataFrame({name_list_of_cols: new_row, 'quest1_before': new_row_quest1_b,
#                          'quest2_before': new_row_quest2_b, 'quest1_after': new_row_quest1_a,
#                          'quest2_after': new_row_quest2_a})


# def prepate_set_changes_questions(list_of_cols, quest1, quest2, name_list_of_cols):
#     new_row = list_of_cols[0]
#     for i in list_of_cols[1:]:
#         new_row = pd.concat([new_row, i], ignore_index=True)
#
#     new_row_quest1 = quest1[0]
#     for i in quest1[1:]:
#         new_row_quest1 = pd.concat([new_row_quest1, i], ignore_index=True)
#
#     new_row_quest2 = quest2[0]
#     for i in quest2[1:]:
#         new_row_quest2 = pd.concat([new_row_quest2, i], ignore_index=True)
#
#     return pd.DataFrame({name_list_of_cols: new_row, 'quest1': new_row_quest1, 'quest2': new_row_quest2})