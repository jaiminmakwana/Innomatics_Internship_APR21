def count_substring(s, subs):
    n = len(s)
    count = 0
    for i in range(n):
        for l in range(i + 1, n + 1):
            if s[i: l] == subs:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)