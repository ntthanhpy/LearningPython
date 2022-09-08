def fibonacci(n):
    if (n < 1):
        return -1;
    elif (n == 1 or n == 2):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
print("Những số trong dãy số fibonacci dưới 4 triệu: ");
sb = "";
i=1
while (fibonacci(i)<4000000):
    sb = sb + str(fibonacci(i)) + ", ";
    i=i+1

print(sb)
print("===================================================");
print("Những số chẵn trong dãy số fibonacci dưới 4 triệu: ");
sbc = "";
i=1
while (fibonacci(i)<4000000):
    if (fibonacci(i) %2==0):
        sbc = sbc + str(fibonacci(i)) + ", ";
    i=i+1

print(sbc)
print("===================================================");
sumeven=0
print("Tổng giá trị những số chẵn trong dãy số fibonacci dưới 4 triệu: ");
sbc = "";
i=1
while (fibonacci(i)<4000000):
    if (fibonacci(i) %2==0):
        sumeven = sumeven + fibonacci(i)
        sbc = sbc + str(fibonacci(i)) + ", ";
    i=i+1

print(sumeven)