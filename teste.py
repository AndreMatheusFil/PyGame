print(dir(float))
print(int(9.55))



def num_of_digits(num):
    i = []
    if num < 0 and num != 0:
        num = num * -1
    if num == 0:
        return 1
    while num > 0:
        num = int(num / 10)
        i.append(int(num))
    return len(i)


print(num_of_digits(13124))
