from parser import parser
from lexer import lexer


def stringify_list(arr):
    string = ''
    for i in range(len(arr)):
        item = arr[i]

        if type(item) != list or type(item) != dict:
            string += str(item) + ',' if i != len(arr) - 1 else str(item)
        else:
            string += _stringify(item)

    return '[{}]'.format(string)


def stringify_object(obj):
    string = ''

    for key in obj.keys():
        if type(obj[key]) == list:
            string += '"{}"'.format(key) + ':' + _stringify(obj[key])
        else:
            string += '"{}"'.format(key) + ':' + str(obj[key])

    return '{' + string + '}'


def _stringify(your_dict):
    json_string = ''

    if type(your_dict) == dict:
        json_string += stringify_object(your_dict)
    elif type(your_dict) == list:
        json_string += stringify_list(your_dict)

    return json_string


class JSON:
    def stringify(self, your_dict):
        return _stringify(your_dict)

    def parse(self, json_string):
        json_object, _ = parser(lexer(json_string), root=True)
        return json_object


test_file = open('example.json', 'r')
data = test_file.read()
print(JSON().parse(data))
