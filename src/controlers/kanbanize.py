import pandas as pd

# Mocka os valores dos CustomFields

custom_field_mock = [{'field_id': 453, 'other_value': None, 'values': [{'value_id': 1627, 'position': 0}]},
                     {'field_id': 494, 'other_value': None, 'values': [{'value_id': 1695, 'position': 0}]},
                     {'field_id': 486, 'other_value': None, 'values': [{'value_id': 1634, 'position': 0}]},
                     {'field_id': 487, 'other_value': None, 'values': [{'value_id': 1639, 'position': 0}]},
                     {'field_id': 488, 'other_value': None, 'values': [{'value_id': 1641, 'position': 0}]}]


def recupera_position_do_custom_fields_tentando(campo, valores):
    valores_dataframe = pd.DataFrame(valores)
    df = pd.DataFrame.from_records(valores_dataframe)
    return df
    # if campo in valores_dataframe.values:
    #     return valores_dataframe.values
    # else:
    #     return posicao


posicao = recupera_position_do_custom_fields_tentando(453, custom_field_mock)
print(posicao)
