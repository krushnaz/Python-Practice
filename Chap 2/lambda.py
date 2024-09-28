# lambda function : 
# anonomus function 
# accept any number of variable 
# anonomus function does not have any name

# s = lambda x,y,z : x + y + z;
# print(s(10,20,30))

# calculate square of given number 
sqr = lambda x : x * x;
print("square :", sqr(5))

# calculate area of triangle 
areaOfTriangle = lambda base, height : (base * height)/2;
print("area of triangle is :",areaOfTriangle(10,20));

# calculate area rectangle 
areaOfRect = lambda length, bredth : length * bredth;
print("area of rectangle is :",areaOfRect(20,10));

# calculate percentage 
# (obtain marks / total marks ) * 100
percentage = lambda sub1,sub2,sub3, sub4 : ((sub1 + sub2 + sub3 + sub4) / 400) * 100;
print("percentage :",percentage(60,70,80,40));

# calculate average of given number 
average = lambda mark1,mark2,mark3,mark4 : ( mark1+mark2+mark3+mark4 )/4;
print("average :",average(60,70,80,40));