if __name__ == '__main__':
    s = input()
    if len(s) < 1000:
        alphat = 786

        for i in range(len(s)):
            if s[i].isalnum():
                alphat = 0
                print(True)
                break
        if alphat != 0:
            print(False)

        for i in range(len(s)):
            if s[i].isalpha():
                alphat = 1
                print(True)
                break
        if alphat != 1:
            print(False)

        for i in range(len(s)):
            if s[i].isdigit():
                alphat = 2
                print(True)
                break
        if alphat != 2:
            print(False)

        for i in range(len(s)):
            if s[i].islower():
                alphat = 3
                print(True)
                break
        if alphat != 3:
            print(False)

        for i in range(len(s)):
            if s[i].isupper():
                alphat = 4
                print(True)
                break
        if alphat != 4:
            print(False)