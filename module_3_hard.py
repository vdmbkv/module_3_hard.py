def data_type_calculator(*args):
    sum_ = 0
    for item in args:
        if isinstance(item, (list, tuple, set)):
            for elem in item:
                sum_ += data_type_calculator(elem)
        elif isinstance(item, dict):
            for key, value in item.items():
                sum_ += data_type_calculator(key) + data_type_calculator(value)
        else:
            if isinstance(item, str):
                sum_ += len(item)
            elif isinstance(item, int):
                sum_ += item
    return sum_

data_structure = {
'int': 1,
'list': [2, 3],
'dict': {"d": 4, "e": 5},
'tuple': (6, {"cube": 7, "drum": 8}),
'string': "Hello",
"tuple, list, dict": ((), [{("Urban", 2), ("Urban2", 35)}])
}

result = data_type_calculator(data_structure)
print(result)