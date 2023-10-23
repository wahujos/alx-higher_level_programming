#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    turns = 0
    counter = 0
    try:
        for y in my_list:
            if (turns >= x):
                break
            else:
                if (isinstance(y, int)):
                    print("{:d}".format(y), end='')
                    printed = printed + 1
                    turns = turns + 1
                else:
                    turns = turns + 1
        for i in my_list:
            counter += 1
        if counter < x:
            raise IndexError
        print()
        return printed
    except Exception as err:
        print("Error occurred", err)
