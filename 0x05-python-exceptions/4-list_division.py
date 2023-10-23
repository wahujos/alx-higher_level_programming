#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    div_res = 0
    try:
        if len(my_list_1) < list_length or len(my_list_2) < list_length:
            print("out of range")
        for i in range(list_length):
            v1 = my_list_1[i]
            v2 = my_list_2[i]
            if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
                if v2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    div_res = v1 / v2
                    result.append(div_res)
            else:
                print("wrong type")
                result.append(0)
    except Exception:
        print(end='')
    finally:
        return result
