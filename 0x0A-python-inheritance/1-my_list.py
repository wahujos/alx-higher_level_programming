#!/usr/bin/python3
''' Defining the module'''


class MyList(list):
    '''MyList inherits from list'''
    def print_sorted(self):
        '''defining function'''
        sorted_ascending = sorted(self)
        print(sorted_ascending)
