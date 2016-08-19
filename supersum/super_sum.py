def super_sum(*alist):          #can accept any number of arguments user key in separated by commas
    supsum = 0
    valid_types = [list, int, float] #Data types accepted for the summation

    for number in alist:
        if type(number) not in valid_types:
            return 'There is a Type Error'

        if type(number) == list:
            number = sum(number)
            supsum += number

        else:
            supsum += number

    return supsum
