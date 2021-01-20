# def input_words():
#     i = int(input())
#     words = []
#     for i in range(i):
#         temp = input()
#         words.append(temp if len(temp)<=4 else (temp[0]+str(len(temp[1:-1])) + temp[-1]))
#     return words

# if __name__ == "__main__":
#     words = input_words()
#     print(words)

i = int(input())

for i in range(i):
    w = input()
    print(w if len(w)<=10 else (w[0]+str(len(w[1:-1])) + w[-1]))
