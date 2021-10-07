from constants import *


def lex_string(string):
    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string

    json_string = ''
    for c in string:
        if c == JSON_QUOTE:
            return json_string, string[len(json_string)+1:]
        else:
            json_string += c

    raise Exception('Expected end-of-string quote')


def lex_number(string):
    num_string = ''
    num_chars = [str(n) for n in range(10)] + ['-', '+', 'e', '.']

    for c in string:
        if (c in num_chars):
            num_string += c
        else:
            break

    if len(num_string) == 0:
        return None, string

    return float(num_string) if '.' in num_string else int(num_string), string[len(num_string):]


def lex_bools(string):
    TRUE = 'true'
    LEN_TRUE = len(TRUE)
    FALSE = 'false'
    LEN_FALSE = len(FALSE)

    if len(string) >= LEN_TRUE and string[:LEN_TRUE] == TRUE:
        return True, string[LEN_TRUE:]
    elif len(string) >= LEN_FALSE and string[:LEN_FALSE] == FALSE:
        return False, string[LEN_FALSE:]

    return None, string


def lex_null(string):
    NULL = 'null'
    LEN_NULL = len(NULL)

    if len(string) >= LEN_NULL and string[:LEN_NULL] == NULL:
        return 1, string[LEN_NULL:]

    return None, string


def lexer(string):
    tokens = []

    while (string):
        json_string, string = lex_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_bool, string = lex_bools(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue

        c = string[0]
        if c in JSON_WHITESPACE:
            string = string[1:]
        elif c in JSON_SYNTAX:
            tokens.append(c)
            string = string[1:]
        else:
            raise Exception('Uncaught character: {}'.format(c))
    print(string)
    return tokens
