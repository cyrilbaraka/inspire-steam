#Name :Cyril Baraka
#Date :16/02/2026
#A program to calculate the income tax of the employees 
#if bs <50,000 = 2.5% as tax , 50,000 to 100,000 =4.5% tax above 100,000 7.5% tax

salary=int(input("Enter your gross salary"))

if salary <50000:
    tax=0.025*salary
elif salary>=50000:
    tax=0.045*salary
elif salary>1*100000:
    tax=0.075*salary

net_salary=salary-tax

print(F"Gross salary={salary}")
print(f"Net Salary={net_salary}")
print(f"Tax={tax}")

