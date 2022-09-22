# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


with open('before.txt', 'r') as data:
    before = data.read()

def rle_alg(before):
    encod_str = ''
    i = 0
    while i < len(before):
        counter = 1
        while i+1 < len(before) and before[i] == before[i+1]:
            counter += 1
            i += 1
        encod_str += str(counter) + before[i]
        i += 1
    return encod_str

print(rle_alg(before))

with open('after.txt', 'w') as data:
    data.write(rle_alg(before))





