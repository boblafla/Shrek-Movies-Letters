import time
from time import perf_counter

letters = []
for i in range(26):
    letters.append(0)

with open('1.txt', 'r') as f:
    for line in f:
        for char in line:
            if char == 'a':
                letters[0] += 1
            elif char == 'b':
                letters[1] += 1
            elif char == 'c':
                letters[2] += 1
            elif char == 'd':
                letters[3] += 1
            elif char == 'e':
                letters[4] += 1
            elif char == 'f':
                letters[5] += 1
            elif char == 'g':
                letters[6] += 1
            elif char == 'h':
                letters[7] += 1
            elif char == 'i':
                letters[8] += 1
            elif char == 'j':
                letters[9] += 1
            elif char == 'k':
                letters[10] += 1
            elif char == 'l':
                letters[11] += 1
            elif char == 'm':
                letters[12] += 1
            elif char == 'n':
                letters[13] += 1
            elif char == 'o':
                letters[14] += 1
            elif char == 'p':
                letters[15] += 1
            elif char == 'q':
                letters[16] += 1
            elif char == 'r':
                letters[17] += 1
            elif char == 's':
                letters[18] += 1
            elif char == 't':
                letters[19] += 1
            elif char == 'u':
                letters[20] += 1
            elif char == 'v':
                letters[21] += 1
            elif char == 'w':
                letters[22] += 1
            elif char == 'x':
                letters[23] += 1
            elif char == 'y':
                letters[24] += 1
            elif char == 'z':
                letters[25] += 1

    print(f'Shrek 1: {letters}')
    print(perf_counter(), '\n')

letters_2 = []
for i in range(26):
    letters_2.append(0)

with open('2.txt', 'r') as f:
    for line in f:
        for char in line:
            if char == 'a':
                letters_2[0] += 1
            elif char == 'b':
                letters_2[1] += 1
            elif char == 'c':
                letters_2[2] += 1
            elif char == 'd':
                letters_2[3] += 1
            elif char == 'e':
                letters_2[4] += 1
            elif char == 'f':
                letters_2[5] += 1
            elif char == 'g':
                letters_2[6] += 1
            elif char == 'h':
                letters_2[7] += 1
            elif char == 'i':
                letters_2[8] += 1
            elif char == 'j':
                letters_2[9] += 1
            elif char == 'k':
                letters_2[10] += 1
            elif char == 'l':
                letters_2[11] += 1
            elif char == 'm':
                letters_2[12] += 1
            elif char == 'n':
                letters_2[13] += 1
            elif char == 'o':
                letters_2[14] += 1
            elif char == 'p':
                letters_2[15] += 1
            elif char == 'q':
                letters_2[16] += 1
            elif char == 'r':
                letters_2[17] += 1
            elif char == 's':
                letters_2[18] += 1
            elif char == 't':
                letters_2[19] += 1
            elif char == 'u':
                letters_2[20] += 1
            elif char == 'v':
                letters_2[21] += 1
            elif char == 'w':
                letters_2[22] += 1
            elif char == 'x':
                letters_2[23] += 1
            elif char == 'y':
                letters_2[24] += 1
            elif char == 'z':
                letters_2[25] += 1

    print(f'Shrek 2: {letters_2}')
    print(perf_counter(), '\n')

letters_3 = []
for i in range(26):
    letters_3.append(0)

with open('3.txt', 'r') as f:
    for line in f:
        for char in line:
            if char == 'a':
                letters_3[0] += 1
            elif char == 'b':
                letters_3[1] += 1
            elif char == 'c':
                letters_3[2] += 1
            elif char == 'd':
                letters_3[3] += 1
            elif char == 'e':
                letters_3[4] += 1
            elif char == 'f':
                letters_3[5] += 1
            elif char == 'g':
                letters_3[6] += 1
            elif char == 'h':
                letters_3[7] += 1
            elif char == 'i':
                letters_3[8] += 1
            elif char == 'j':
                letters_3[9] += 1
            elif char == 'k':
                letters_3[10] += 1
            elif char == 'l':
                letters_3[11] += 1
            elif char == 'm':
                letters_3[12] += 1
            elif char == 'n':
                letters_3[13] += 1
            elif char == 'o':
                letters_3[14] += 1
            elif char == 'p':
                letters_3[15] += 1
            elif char == 'q':
                letters_3[16] += 1
            elif char == 'r':
                letters_3[17] += 1
            elif char == 's':
                letters_3[18] += 1
            elif char == 't':
                letters_3[19] += 1
            elif char == 'u':
                letters_3[20] += 1
            elif char == 'v':
                letters_3[21] += 1
            elif char == 'w':
                letters_3[22] += 1
            elif char == 'x':
                letters_3[23] += 1
            elif char == 'y':
                letters_3[24] += 1
            elif char == 'z':
                letters_3[25] += 1

    print(f'Shrek 3: {letters_3}')
    print(perf_counter(), '\n')

letters_4 = []
for i in range(26):
    letters_4.append(0)

with open('4.txt', 'r') as f:
    for line in f:
        for char in line:
            if char == 'a':
                letters_4[0] += 1
            elif char == 'b':
                letters_4[1] += 1
            elif char == 'c':
                letters_4[2] += 1
            elif char == 'd':
                letters_4[3] += 1
            elif char == 'e':
                letters_4[4] += 1
            elif char == 'f':
                letters_4[5] += 1
            elif char == 'g':
                letters_4[6] += 1
            elif char == 'h':
                letters_4[7] += 1
            elif char == 'i':
                letters_4[8] += 1
            elif char == 'j':
                letters_4[9] += 1
            elif char == 'k':
                letters_4[10] += 1
            elif char == 'l':
                letters_4[11] += 1
            elif char == 'm':
                letters_4[12] += 1
            elif char == 'n':
                letters_4[13] += 1
            elif char == 'o':
                letters_4[14] += 1
            elif char == 'p':
                letters_4[15] += 1
            elif char == 'q':
                letters_4[16] += 1
            elif char == 'r':
                letters_4[17] += 1
            elif char == 's':
                letters_4[18] += 1
            elif char == 't':
                letters_4[19] += 1
            elif char == 'u':
                letters_4[20] += 1
            elif char == 'v':
                letters_4[21] += 1
            elif char == 'w':
                letters_4[22] += 1
            elif char == 'x':
                letters_4[23] += 1
            elif char == 'y':
                letters_4[24] += 1
            elif char == 'z':
                letters_4[25] += 1

    print(f'Shrek 4: {letters_4}')
    print(perf_counter(), '\n')
