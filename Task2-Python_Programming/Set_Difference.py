
eng = int(input())
engroll = input().split()
engroll = set(map(int, engroll))

fre = int(input())
freroll = input().split()
freroll = set(map(int, freroll))

if 0 < len(engroll) and len(freroll) < 1000:
    diff = engroll - freroll    # A.difference(B)
    print(len(diff))