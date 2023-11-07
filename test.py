class PasswordFormatError(Exception):
    pass


class LengthError(PasswordFormatError):
    pass


class LetterError(PasswordFormatError):
    pass


class DigitError(PasswordFormatError):
    pass


class SequenceError(PasswordFormatError):
    pass


nabor = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
         'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
         'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
         'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
         'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
         'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё']


def check_password(password):
    if len(password) < 9:
        raise LengthError()

    if password.lower() == password or password.upper() == password:
        raise LetterError()

    for el1 in '1234567890':
        if el1 in password:
            break
    else:
        raise DigitError()

    for el in nabor:
        if el in password.lower():
            raise SequenceError()

    return 'ok'
