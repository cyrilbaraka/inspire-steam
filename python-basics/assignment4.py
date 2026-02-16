#Name : Cyril Baraka 
#Date : 13/02/2026
#Program to carry out mathematical operations(arithmetic progression)

#calculation of nth term

a=int(input("Enter the number of terms"))
n=int(input("Enter the number of terms"))
d=int(input("Enter the common difference"))

nth_term=a+(n-1)*d
sn=(n/2)*(2*a+(n-1)*d)
print(f"The nth term is{nth_term}")
print(f"The sum of n is:{sn}")
