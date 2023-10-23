#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0;
    try:
        for y in my_list:
            if(count < x):
                print("{}".format(y),end='');
                count = count + 1
            else:
                break
        print()
        return count
    except Exception as err:
        print("Error occured", err)
