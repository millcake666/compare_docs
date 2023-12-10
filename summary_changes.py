import os
import json


def get_item(data: dict, key: int, keys: list):
    if key == len(keys) - 1:
        return data
    return get_item(data[keys[key]], key + 1, keys)


def get_summary(json_path_old: str, json_path_new: str):
    summary = []

    with open(json_path_old, 'r', encoding='utf-8') as f_old:
        json_old_data: dict = json.load(f_old)
    with open(json_path_new, 'r', encoding='utf-8') as f_new:
        json_new_data: dict = json.load(f_new)

    differences = compare_json_values(json_old_data, json_new_data)

    for dif in differences:
        j_keys = dif.split('.')
        target_old = get_item(json_old_data, 0, j_keys)
        target_new = get_item(json_new_data, 0, j_keys)

        value_old = target_old[j_keys[-1]]
        value_new = target_new[j_keys[-1]]

        summary.append([dif, [value_old, value_new]])

    return summary


def compare_json_values(obj1, obj2, path=""):
    """
    Рекурсивно сравнивает значения в двух словарях JSON.
    """
    differences = []

    for key in obj1:
        current_path = f"{path}.{key}" if path else key

        if key not in obj2:
            differences.append(current_path)
        elif isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
            differences.extend(compare_json_values(obj1[key], obj2[key], current_path))
        elif obj1[key] != obj2[key]:
            differences.append(current_path)

    return differences


if __name__ == '__main__':
    old = os.path.join(os.getcwd(), r'data/data_fields/fields_from_form.json')
    new = os.path.join(os.getcwd(), r'data/data_fields/fields_from_form2.json')

    res = get_summary(old, new)
    print(res)
