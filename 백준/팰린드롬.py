word = input()
bword = list(reversed(word))
bword = "".join(bword)
if word == bword:
    print(1)
else:
    print(0)