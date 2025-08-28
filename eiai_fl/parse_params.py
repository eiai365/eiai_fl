import os
import pandas as pd


def parse_parameters(*, parameters, log):
    fl_left_delimiter = os.environ.get('EIAI_FL_LEFT_DELIMITER')
    if fl_left_delimiter is None or fl_left_delimiter == '':
        fl_left_delimiter = '('
    fl_right_delimiter = os.environ.get('EIAI_FL_RIGHT_DELIMITER')
    if fl_right_delimiter is None or fl_right_delimiter == '':
        fl_right_delimiter = ')'
    fl_field_separator = os.environ.get('EIAI_FL_FIELD_SEPARATOR')
    if fl_field_separator is None or fl_field_separator == '':
        fl_field_separator = ','
    parameters_df = pd.DataFrame(columns=['Key', 'Value'],)
    parameter_list = parameters.split(f'{fl_left_delimiter}{fl_field_separator}')
    log.debug(f"Parameter list: {parameter_list}")
    for parameter in parameter_list:
        key = parameter.split(f'{fl_left_delimiter}')[0].lower()
        value = parameter.split(f'{fl_left_delimiter}')[1].split(f'{fl_right_delimiter}')[0]
        parameters_df.loc[len(parameters_df.index)] = [key, value]
    return parameters_df
