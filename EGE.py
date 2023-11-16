
# for n in range(10, 101):                         # Решение 5 задания
#     bin_n = bin(n)[2:]
#     if bin_n.count('1') % 2 == 0:
#         bin_n = '10' + bin_n[2:] + '0'
#     else:
#         bin_n = '11' + bin_n[2:] + '1'
#     if int(bin_n, 2) > 40:
#         print(n)
#         break

# for x in range(0, 2):                 #Решения задания 2
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not((x and not(y)) or (y == z) or w):
#                     print(x, y, z, w)

# for n in range(1, 100):
#     A = 0
#     bin_n = bin(n)[2:]
#     for i in bin_n:
#         A += int(i)
#     F = A % 2
#     bin_n = str(bin_n) + str(F)
#     A += 1
#     F = A % 2
#     bin_n = str(bin_n) + str(F)
#     v = int(bin_n, 2)
#     if v < 100:
#         print(v)
#         break

for n in range(100, 1, -1):
    binn = bin(n)[2:]
    binn += str(binn.count('1') % 2)
    binn += str(binn.count('1') % 2)
    v = int(binn, 2)
    if v < 100:
        print(v)
        break


