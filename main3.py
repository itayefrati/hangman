
def last_early(my_str):
    my_str.lower()
    if len(my_str) == 0:
        return False
    if my_str[-1] in my_str[0:-2]:
        return True
    return False


def distance(num1, num2, num3):
    if abs(num1 - num2) == 1 or abs(num1 - num3) == 1:
        if abs(num2 - num3) > 2 and abs(num2 - num1) > 2:
            return True
        elif abs(num3 - num2) > 2 and abs(num3 - num1) > 2:
            return True
    return False


def filter_teens(a=13, b=13, c=13):
    age1 = fix_age(a)
    age2 = fix_age(b)
    age3 = fix_age(c)
    return age1 + age2 + age3


def fix_age(age):
    if 13 <= age <= 19:
        if age != 15 and age != 16:
            age = 0
        else:
            pass
    return age


def chocolate_maker(small, big, x):
    if small * 1 + big * 5 >= x:
        return True
    return False


def func(num1, num2):
    """this function returns the sum of num1 and num2
    :param num1
    :param num2
    :returns num1 + num2"""
    return num1 + num2


def shift_left(my_list):
    """this function is given a list and returns
    a new list that is moved one step left
    :param: my_list
    :return: new_list
    """
    new_list = my_list[1:] + my_list[:1]
    return new_list


def format_list(my_list):
    """
    The function takes a list of even-length strings.
    Returns a string containing the list members in the even positions,
    separated by a , and a space, plus the last member with the inscription and before it.
    :param my_list:
    :return: new_str1 + new_str2
    """
    new_str1 = ', '.join(my_list[0:-1:2])
    new_str2 = ' and ' + my_list[-1]
    return new_str1 + new_str2


def extend_list_x(list_x, list_y):
    """
    this function gets two lists and combines them
    :param list_x: a list of any type
    :type list_x: list
    :param list_y: a list of any type
    :type list_y: list
    :return: list_x combined with list_y before it
    :rtype: list
    """
    list_x[:0]  = list_y
    return list_x


def are_lists_equal(list1, list2):
    """
    this function gets two lists and checks if they are equal
    order don't matter
    :param list1: a list of ints and floats
    :type list1: list
    :param list2: a list of ints and floats
    :type list2: list
    :return: true if the lists are equal false if not
    :rtype: bool
    """
    list1.sort()
    list2.sort()
    if list1 == list2 and len(list1) == len(list2):
        return True
    return False


def longest(my_list):






    \\\

def main():
    x = [0.6, 1, 2, 3]
    y = [3, 2, 0.6, 1]
    z = [9, 0, 5, 10.5]
    print(are_lists_equal(x, z))


if __name__ == "__main__":
    main()
