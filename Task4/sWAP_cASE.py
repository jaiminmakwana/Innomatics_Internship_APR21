def swap_case(s):
    a = str()
    if len(s) <= 1000:
        for i in s:
            if i.isupper():
                print(str(a + i.lower()), end='')
            else:
                print(str(a + i.upper()), end='')

    return a


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
