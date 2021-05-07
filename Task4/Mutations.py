def mutate_string(s, position, character):
    s = s[:position] + character + s[position + 1:]

    # Alternative way #
    # l = list(s)
    # l[5] = 'k'
    # s = ''.join(l)
    # print(s)
    return s


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)