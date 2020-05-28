#実行方法：①このファイルを　「　任意の名前.py　」　の形式で保存します。
#　　　　　②ファイルと同じPATHのターミナルを起動します。
#　　　　　③ターミナルに、「　./任意の名前.py　任意の数字　」　を入力して実行します。　　

import numpy, sys, time

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n)) # Matrix A
b = numpy.zeros((n, n)) # Matrix B
c = numpy.zeros((n, n)) # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0
begin = time.time()

######################################################
  # 行列積
A = list(a)
B = list(b)
C = list(c)
    
from operator import mul
C = [[sum(map(mul, row, col)) for col in zip(*A)] for row in B]
print (C)

#######################################################

end = time.time()
print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
print("sum: %.6f" % total)
