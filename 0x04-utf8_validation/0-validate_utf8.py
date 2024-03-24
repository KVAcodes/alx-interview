#!/usr/bin/python3
"""Module contains the solution to the UTF8 Validation problem.
"""

def validUTF8(data):
    """Returns True if the data is a valid UT8-encoding, else returns False.
    """
    # converts the data list to a list of 8 least significant 
    # bits of each integer in the list
    encoding = [bin(integer)[-8:] for integer in data]
    print(encoding)
    #Test for Validity.
    string = 0
    while string < len(encoding):
        if encoding[string][0] == '0':
            string += 1
            continue
        elif encoding[string][:2] == '10':
            return False
        else:
            idx = 1
            while encoding[string][idx] != '0':
                string += 1
                if string < len(encoding) and encoding[string][:2] == '10':
                    idx += 1
                    continue
                else:
                    return False
        string += 1
    return True