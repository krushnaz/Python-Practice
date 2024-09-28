def sum_odd_even(n) :
    sum_even = 0
    sum_odd = 0
    
    for i in range(1,n+1) :
        if i % 2 == 0 :
            sum_even += i
        else :
            sum_odd += i
            
    return sum_even,sum_odd

sum_even, sum_odd = sum_odd_even(10)
print(f"sum of even num {sum_even}")
print(f"sum of odd num {sum_odd}")


