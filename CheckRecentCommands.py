from subprocess import Popen, PIPE, STDOUT
import re
import operator


def read_file(n):
    '''
    :param n < 500
    :return: a list of string that contains the most recent n commands executed
    '''
    e = Popen("bash -i -c  'history -r;history' ", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    string_list = e.communicate()[0].decode("utf-8").split("\n")[1:-1]
    return_list = string_list[len(string_list) - n:]
    return list(map(lambda x: re.split("[0-9]+", x, 2)[1][2:], return_list))


def analysis(list, char_lim):
    '''
    :param list: a list of commands that are being analyzed
    :param char_lim: the minimum number of characters in commands returned
    :return: a list of commands that are most used
    '''
    dic = {}
    for i in list:
        if len(i) >= char_lim:
            if i not in dic.keys():
                dic[i] = 0
            dic[i] = dic[i] + 1
    sorted_dict = iter(sorted(dic.items(), reverse=True, key=operator.itemgetter(1)))
    result = []
    for key, value in sorted_dict:
        result.append(key)
    return result


def alias(list):
    '''
    :param list: the list of top most used commands
    :return: null
    '''
    print(list)
    return


def main():
    num = input("How many recent commands do you want to check? (Enter a number between 1 and 500)")
    top = input("How many most frequently used commands would you like to alias? "
                "(Must be smaller than the number entered previously)")
    char_limit = input("What's the shortest command that you are willing to check? (Enter number of characters)")
    # TODO: throw exception if num < top or num/top are not numbers
    # TODO: add command length limit
    item_list = read_file(int(num))
    alias(analysis(item_list, int(char_limit))[:int(top)])


if __name__ == '__main__':
    main()
