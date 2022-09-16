# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# # Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file1.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

# path = 'file1.txt'
# data = open(path, 'r')
# line = data.read()
# data.close

# def copmpression(line):
#     compress_result= ''
#     count = 1
#     for i in range(len(line)-1):
#         if line[i+1]==line[i]:
#             count+=1
#         else:
#             compress_result+= str(count)+line[i]
#             count=1
#     compress_result+= str(count)+line[i]
#     return compress_result

# compressed_line = copmpression(line)
# print('Исходный текст до сжатия: ', line)
# print('Текст после реализации RLE алгоритма сжатия: ', compressed_line)

# with open('file2.txt', 'w') as data:
#     data.write(compressed_line)

# with open('file2.txt', 'r') as data:
#     new_line = data.read()

# def restoration(new_line):
#     number = ''
#     line_restore = ''
#     for i in range(len(new_line)):
#         if new_line[i].isdigit():
#             number+=new_line[i]
#         else:
#             line_restore+= int(number)*new_line[i]
#             number = ''
#     return line_restore        

# with open('file1.txt', 'w') as data:
#     data.write(restoration(new_line))