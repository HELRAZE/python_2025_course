input_string = input("Введите высоты линий через пробел: ")
string_list = input_string.split()

box = []
try:
    for s in string_list:
        box.append(int(s))
except ValueError:
    print("Ошибка: введите только числа, разделенные пробелами.")
    exit()


p1, p2 = 0, len(box) - 1

def square(a, b, diff):
    return min(a, b) * diff

res = []
while True:
    diff = abs(p1 - p2)
    res.append(square(box[p1], box[p2], diff))
    if box[p1] < box[p2]:
        p1 += 1
    else:
        p2 -= 1
    if p1 == p2:
        break

print(max(res))