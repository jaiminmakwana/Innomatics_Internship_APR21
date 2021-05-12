def split_and_join(line):
    slist = line.split(" ")
    # print(slist)

    jlist = '-'.join(slist)
    # print(jlist)

    return jlist


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
