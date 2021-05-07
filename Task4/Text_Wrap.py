def wrap(s, width):
    ans = str()
    max_len = 0
    for i in range(len(s)):
        if max_len < width:
            ans += s[i]
            max_len += 1
        else:
            ans += '\n'
            ans += s[i]
            max_len = 1

    # print(ans)
    return ans


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
