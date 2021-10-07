from constants import *


def parse_array(tokens):
    json_array = []

    t = tokens[0]
    if t == JSON_RIGHT_BRACKET:
        return json_array, tokens[1:]

    while True:
        json, tokens = parser(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == JSON_RIGHT_BRACKET:
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]


def parse_object(tokens):
    json_object = {}

    t = tokens[0]
    if t == JSON_RIGHT_BRACE:
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is not str:
            raise Exception('Expected string key, got: {}'.format(json_key))
        else:
            tokens = tokens[1:]

        if tokens[0] == JSON_COLON:
            tokens = tokens[1:]
        else:
            raise Exception(
                'Expected colon after key in object, got: {}'.format(t))

        json_value, rest = parser(tokens)
        json_object[json_key] = json_value

        t = rest[0]
        if t == JSON_RIGHT_BRACE:
            return json_object, rest[1:]
        elif t != JSON_COMMA:
            raise Exception(
                'Expected comma after pair in object, got: {}'.format(t))

        tokens = rest[1:]


def parser(tokens, root=False):
    token = tokens[0]
    if root and token != JSON_LEFT_BRACE:
        raise Exception('Root must be an object')

    if token == JSON_LEFT_BRACKET:
        return parse_array(tokens[1:])
    elif token == JSON_LEFT_BRACE:
        return parse_object(tokens[1:])
    else:
        return token, tokens[1:]
