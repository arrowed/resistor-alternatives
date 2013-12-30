__author__ = 'simon'

values = ['ooo',
          'brbkgogo',
          'ooygo',
          'brgybr',
          'brgnr',
          'gyro',
          'gnbubr',
          'brbugn',
          'buwbk',
          'brbkbk',
          'wrr',
          'wrbr',
          'owr',
          'rvbr',
          'brwr',
          'rbrbk',
          'brgnbk',
          'brbkr',
          'oogogo',
          'rry',
          'grbubk',
          'oobk',
          'brgngogo',
          'gnbur',
          'brrbr',
          'brro',
          'bugrbr',
          'brgno',
          'brrbk',
          'brgny',
          'gnbugogo',
          'rrgogo',
          'rpo',
          'rvy',
          'gnbuo',
          'rrbk',
          'brgyo',
          'oobk',
          'brbky',
          'rrr',
          'rrbr',
          'buwo',
          'oor',
          'owbk',
          'brbkbr',
          'rro',
          'brbkbu',
          'brrr',
          'brbko',
          'wrbk',
          'owo',
          'brry',
          'rvbk',
          'yvgo',
          'yvbr',
          'yvo',
          'yvy',
          'yvgn',
]

patterns = {'bk': 0,
            'br': 1,
            'r': 2,
            'o': 3,
            'y': 4,
            'gn': 5,
            'gr': 5,
            'bu': 6,
            'v': 7,
            'p': 7, # purple == violet
            'gy': 8,
            'w': 9,

            'go': 5,
            'si': 2
            }

def convert_code(colour_code):
    '''
    Convert a colour code into its representative values.
    No logic is applied (ie using 3rd digit to multiply.
    >>> assert convert_code('oobkgo') == [3, 3, 0, 5]
    >>> assert convert_code('ooo') == [3, 3, 3]

    '''
    digit = 0
    ret = []
    pos = 0

    while pos < len(colour_code):

        hit = False
        for pat in patterns:

            if (len(colour_code) - pos) >= len(pat) and colour_code[pos:pos+len(pat)] == pat:
                ret.append(patterns[pat])
                digit += 1
                hit = True

                pos += len(pat)
                break

        if not hit:
            raise Exception('Unable to convert remainder of %s' % (colour_code[pos:]))


    return ret

def convert(code):
    '''Convert an array of values into a single number'''
    return convert_4(code)

def convert_4(code):
    '''Convert an array of 3 or 4 values into a single number
    >>> assert convert([3, 3, 0, 5]) == 33
    >>> assert convert([3, 3, 3, 5]) == 33000

    '''

    return ((code[0] * 10) + code[1]) * (10 ** code[2])

def find_alternatives(target):
    '''Find combinations of available resistors that
    can be put in series or parallel to suit the target
    value
    '''

    # 3% tolerance
    target_min = target - ((target/100)*3)
    target_max = target + ((target/100)*3)

    for r1 in values:
        for r2 in values:
            # dont combine with self
            r1v = convert(convert_code(r1))
            r2v = convert(convert_code(r2))

            if r1 == r2 == target:
                print '[Match] You have an exact match: %s (%s)' % (r1, r1v)
                break

            if r1 == r2 and r1 > target_min and r2 < target_max:
                print '[Close] You have close single-resistor match: %s (%s) for target %s' % (r1, r1v, target)
                break

            # see if we can put in series
            v = r1v + r2v
            if v > target_min and v < target_max:
                print '[Series] Putting %s (%s) in series with %s (%s) ' \
                      'gives close to the target value %s' % (r1, r1v, r2, r2v, v)

            # see if we can put in parallel
            v = (r1v*r2v)/(r1v+r2v)
            if v > target_min and v < target_max:
                print '[Parallel] Putting %s (%s) in parallel with %s (%s) ' \
                      'gives close to the target value %s' % (r1, r1v, r2, r2v, v)


def __main__():
    find_alternatives(100)



if __name__ == '__main__':
    __main__()