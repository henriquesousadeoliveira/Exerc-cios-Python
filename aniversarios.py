data1 = int(input())
data2 = int(input())
data3 = int(input())

if data1 == data2 == data3:
    print(1)
elif data1 == data2 or data1 == data3 or data2 == data3:
    print(2)
else:
    print(3)
