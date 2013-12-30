__author__ = 'simon'

values = ['oobkg']

patterns = {'bk': 0,
            'br': 1,
            'r': 2,
            'o': 3,
            'y': 4,
            'g': 5,
            'bl': 6,
            'v': 7,
            'gr': 8,
            'w': 9,

            'go': 5,
            'si': 2
            }

def convert_code(colour_code):
    '''
    Convert a colour code into its representative values.
    No logic is applied (ie using 3rd digit to multiply.
    >>> assert convert_code('oobkg') == [3, 3, 0, 5]
    '''
    digit = 0
    ret = []
    pos = 0

    while pos < len(colour_code):
        for pat in patterns:
            if (len(colour_code) - pos) >= len(pat) and colour_code[pos:pos+len(pat)] == pat:
                ret.append(patterns[pat])
                digit += 1

                pos += len(pat)
                break


    return ret

def convert(code):
    '''Convert an array of values into a single number'''
    if len(code) == 4 or len(code) == 3:
        return convert_4(code)

    raise Exception('Cant handle code with %d digits' % len(code))

def convert_4(code):
    '''Convert an array of 3 or 4 values into a single number
    >>> assert convert([3, 3, 0, 5]) == 33
    '''

    return ((code[0] * 10) + code[1]) ** (code[2]+1)

