
eng = int(input())
engroll = input().split()
engroll = set(map(int, engroll))

fre = int(input())
freroll = input().split()
freroll = set(map(int, freroll))

if 0 < len(engroll) and len(freroll) < 1000:
    symdiff = engroll ^ freroll    # A.symmetric_difference(B)
    print(len(symdiff))