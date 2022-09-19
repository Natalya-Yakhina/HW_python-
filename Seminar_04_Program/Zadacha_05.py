# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

with open('file1.txt', 'w') as data: # первый файл
    data.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

path = 'file1.txt'
data = open(path, 'r')
line = data.read()
data.close

def copmpression(line): # функция сжатия
    compress_result = ' '
    count = 1
    for i in range(len(line) - 1):
        if line[i + 1] == line[i]:
            count += 1
        else:
            compress_result += str(count) + line[i]
            count = 1
    compress_result += str(count) + line[i]
    return compress_result

compressed_line = copmpression(line)
print('Текст до сжатия: ', line)
print('Текст после реализации RLE алгоритма сжатия: ', compressed_line)

with open('file2.txt', 'w') as data:
    data.write(compressed_line)