sum = 0;
# for i in range(0, 21, 2) :
#     sum += i;
# print(sum);

for i in range(0, 21, 2) :
    if(i % 2 == 0) :
        sum += i;
print(sum);