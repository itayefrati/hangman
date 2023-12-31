from operator import itemgetter


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
    list_x[:0] = list_y
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
    """
    this function returns the longest string of a list
    :param my_list: a list of strings
    :type my_list: list
    :return: longest string
    :rtype: str
    """
    new_list = sorted(my_list, key=len)
    longest_str = new_list[-1]
    return longest_str


def squared_numbers(start, stop):
    """
    this function gets 2 numbers and returns a list of all the numbers
    in their range (including them), by the power of 2
    :param start: a number that is the start of the range
    :type: int
    :param stop: a number that is the end of the range
    :type: int
    :return: a list of all the numbers in that range by the power of 2
    :rtype: list
    """
    new_list = list()
    i = start
    while i <= stop:
        new_list.append(i * i)
        i += 1
    return new_list


def is_greater(my_list, n):
    """
    this function gets a list and a number and
    returns a new list with all the numbers from the
    previous list that are bigger than the number
    :param my_list:
    :param n:
    :return: new_list
    """
    new_list = list()
    for i in range(len(my_list)):
        if my_list[i] > n:
            new_list.append(my_list[i])
        i += 1
    return new_list


def numbers_letters_count(my_str):
    """
    this function gets a string and returns a list with the number of numbers
    and the number of letters
    :param my_str:
    :return: new_list
    """
    new_list = list()
    count = 0
    for i in range(len(my_str)):
        if '0' < my_str[i] < '9':
            count += 1
        i += 1
    new_list.append(count)
    for i in range(len(my_str)):
        if my_str[i].isalpha():
            count += 1
        i += 1
    new_list.append(count)
    return new_list


def seven_boom(end_number):
    """
    this function receives a number and returns a list
    of all the numbers until the number that is received
    and the numbers that has 7 or can be divided by it become BOOM
    :param end_number:
    :return: lst
    """
    lst = list()
    i = 0
    while i <= end_number:
        if i == 0 or i % 7 == 0 or i % 10 == 7 or i / 10 == 7:
            lst.append('BOOM')
            i += 1
            continue
        lst.append(i)
        i += 1
    return lst


def sequence_del(my_str):
    """
    this function deletes chars that repeats themselves
    and returns a new string without them
    :param my_str:
    :return:
    """
    i = 0
    new_str = my_str[i]
    for i in range(len(my_str) - 1):
        if my_str[i] != my_str[i + 1]:
            new_str += my_str[i + 1]
            i += 1
        i += 1
    return new_str


def remove_from_list(lst, my_str):
    """
    this function receives a list and a string and removes
    the string from the existing list
    :param lst:
    :param my_str:
    :return: a new list without the string in it
    """
    for i in range(len(lst)):
        if my_str == str(lst[i]):
            lst.remove(lst[i])
            i += 1
        i += 1
    return lst


def print_illegal(lst):
    """
    this function receives a list and returns a new list with all
    the elements that are shorter than 3, or that don't contain letters
    :param lst:
    :return:
    """
    illegal_list = list()
    for i in range(len(lst)):
        if len(lst[i]) <= 3:
            illegal_list.append(lst[i])
            i += 1
        elif not lst[i].isalpha():
            illegal_list.append(lst[i])
            i += 1
        i += 1
    return illegal_list


def delete_sequence(lst):
    """
    this function removes duplicates from a list
    :param lst:
    :return:
    """
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


def arrow(my_char, max_length):
    """
    this function gets a char and a number and prints an arrow
    head when the input number is the longest line
    :param my_char:
    :param max_length:
    :return:
    """
    for i in range(1, max_length + 1):
        print(my_char * i)
    for i in range(max_length - 1, 0, -1):
        print(my_char * i)


def sort_prices(list_of_tuples):
    """
    this function gets a list of tuples and sorts them by price(highest number)
    :param list_of_tuples:
    :return:
    """
    return sorted(list_of_tuples, key=itemgetter(1, 0), reverse=True)


def multi_tuple(tuple1, tuple2):
    """
    this function gets two tuples and returns all the possible
    combinations you can create from them
    :param tuple1:
    :param tuple2:
    :return:
    """
    new_tuple = ()
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            new_tuple = new_tuple + ((tuple1[i], tuple2[j]),)
            new_tuple = new_tuple + ((tuple2[j], tuple1[i]),)
    return new_tuple


def sort_anagrams(list_of_strings):
    """
    this function gets a list of words and returns a list of lists sorted
    by the anagrams of each word
    :param list_of_strings:
    :return:
    """
    new_list = [[list_of_strings[0]]]  # create a list of lists with a string inside it
    flag = False
    list_of_strings.remove(list_of_strings[0])
    for i in list_of_strings:
        for j in range(len(new_list)):
            if sorted(i) == sorted(new_list[j][0]):  # get inside a list that is inside a list
                new_list[j].append(i)
                flag = True
        if not flag:
            new_list.append([i])
        flag = False
    return new_list


def count_chars(my_str):
    """
    this function gets a string and returns a dict
    in the dict each char from the string is a key
    and the value is how many times it appears in the string
    :param my_str:
    :return:
    """
    new_dict = {}
    counter = 0
    for char in my_str:
        if not char.isalpha():
            continue
        for i in range(len(my_str)):
            if char == my_str[i]:
                counter += 1
        new_dict[char] = counter
        counter = 0
    return new_dict


def inverse_dict(my_dict):
    """
    this function gets a dict and returns new reverse dict,
    where all the keys that have the same value are combined
    together into a list inside the dict
    :param my_dict:
    :return:
    """
    new_dict = {}
    for key, value in my_dict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    return new_dict


def are_files_equal(file1, file2):
    """
    this function checks if two files are
    identical
    :param file1:
    :param file2:
    :return:
    """
    with open(file1, "r") as f:
        file_contents = f.read()
    with open(file2, "r") as file:
        file_contents2 = file.read()
    if file_contents == file_contents2:
        return True
    return False


def copy_file_content(source, destination):
    """
    this function copies one file to another
    :param source:
    :param destination:
    :return:
    """
    copy_source = open(source, "r")
    lines = ""
    for line in copy_source:
        lines += line
    copy_source.close()
    paste = open(destination, "w")
    paste.write(lines)
    paste.close()
    num = open(destination, "r")
    new_file = num.read()
    num.close()
    return new_file


def who_is_missing(file_name):
    """
    this function receives a text file with a list of numbers
    from 1 until n, unorganized and with one number missing
    the function will return the missing number and write it
    to a different text file
    :param file_name:
    :return:
    """
    num = 0
    file = open(file_name, "r")
    chat_input_file = open('found.txt', "w")
    lst = file.read().split(',')
    lst = sorted(lst)
    for i in range(len(lst)):
        if str(i) != lst[i]:
            num = i
            chat_input_file.write(str(num))
            chat_input_file.close()
            break
    file.close()
    chat_input_file = open("found.txt", "r")
    print(chat_input_file.read())
    chat_input_file.close()
    return num


def my_mp3_playlist(file_path):
    """
    this function gets a file with songs names lengths and singers,
    it will return the name of the longest song, the number of song in the file
    and the most repeated singer
    :param file_path:
    :return:
    """
    tpl = ()
    count_songs = 0
    longest_song = 0
    list_of_lists = []
    file = open(file_path, "r")
    file_object = file.read()
    split_lines = file_object.split('\n')
    for line in split_lines:
        list_of_lists.append(line.split(';'))
        count_songs += 1
    for list_of_strings in list_of_lists:
        list_of_strings.remove('')
    for i in range(len(list_of_lists)):
        max_num = list_of_lists[0][2]
        if list_of_lists[i][2] > max_num:
            longest_song = i
    lst = []
    for j in list_of_lists:
        for k in j:
            lst.append(k)
    count_max = lst[0]
    for string in range(len(lst)):
        if lst.count(lst[string]) > lst.count(count_max):
            count_max = lst[string]
    tpl = tpl + (list_of_lists[longest_song][0], ) + (count_songs, ) + (count_max, )
    file.close()
    return tpl


def my_mp4_playlist(file_path, new_song):
    """
    this function gets a file and a song name and replaces the 3rd
    song name in the file with the given song name
    :param file_path:
    :param new_song:
    :return:
    """
    with open(file_path, "r+") as file:
        file_object = file.read()
        split_lines = file_object.split('\n')
        if len(split_lines) < 3:
            split_lines.extend('\n' * (3-len(split_lines)))
        split_lines[2] = new_song + ';Unknown;4:15;'
        new_file_content = '\n'.join(split_lines)
        file.seek(0)
        file.write(new_file_content)
    print(new_file_content)


def main():
    # 7.2.6
    """str1 = input("enter a list of groceries with , and no spaces: ")
    lst = str1.split(',')  # convert str to a list
    print(lst)
    while True:
        num = input("enter a number between 1 and 9: ")
        if num == '1':
            print(lst)

        elif num == '2':
            print("there are " + str(len(lst)) + " groceries in the list")

        elif num == '3':
            product = input("enter a product: ")
            if product in str(lst):
                print("yes")
            else:
                print("no")

        elif num == '4':
            product2 = input("enter the product that you want to check how many times it appears in the list: ")
            counter = str(lst).count(product2)
            print("this product appears " + str(counter) + " times in the list")

        elif num == '5':
            product3 = input("enter a product that you wish to remove from the list: ")
            if product3 in str(lst):
                print(remove_from_list(lst, product3))
            else:
                print("this product does not exist in the list")

        elif num == '6':
            product4 = input("enter a product that you want to add to the list: ")
            if str(lst).count(product4) == 0:
                lst.append(product4)
                print(lst)
            else:
                print("this product already exists in the list")

        elif num == '7':
            print("these are the illegal groceries in the list " + str(print_illegal(lst)))

        elif num == '8':
            print("the new list is: " + str(delete_sequence(lst)))

        elif num == '9':
            print("have a good day!")
            break """
    """products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(multi_tuple(first_tuple, second_tuple))"""
    """list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))"""
    """print(are_files_equal(r"C:\\Users\איתי\OneDrive\מסמכים\temp\my text file 2.txt",
                          r"C:\\Users\איתי\OneDrive\מסמכים\temp\my text file.txt"))"""
    """file_path = input("enter a file directory: " '\n')
    action = input("enter an action sort/erv/last: ")
    if action == 'sort':
        with open(file_path, "r"):
            file_object = open(file_path, "r")
            file = file_object.read()
            lst = sorted(file.split())
            lst = list(set(lst))
            lst = sorted(lst)
            print(lst)

    elif action == 'rev':
        with open(file_path, "r"):
            file_object = open(file_path, "r")
            file = file_object.readline()
            file2 = file_object.readline()
            rev_text = file[::-1]
            rev_text2 = file2[::-1]
            print(rev_text)
            print(rev_text2)

    else:
        num = int(input("enter a number: "))
        with open(file_path, "r"):
            file_object = open(file_path, "r")
            lines = file_object.read().splitlines()
            last_line = lines[-num]
            print(last_line)
            i = 1
            while i < num:
                file_object2 = open(file_path, "r")
                lines2 = file_object2.read().splitlines()
                last_line2 = lines2[-num + i]
                i += 1
                print(last_line2)"""
    # print(copy_file_content(r"C:\Users\User\Documents\i am itay efrati.txt",
    #                      r"C:\Users\User\Documents\destination.txt"))
    # print(who_is_missing(r"C:\Users\User\Documents\destination.txt"))
    file = r"C:\Users\User\Documents\destination.txt"
    print(my_mp4_playlist(file, 'bombo'))


if __name__ == "__main__":
    main()
