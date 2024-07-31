# checking the employee salary using if else

Basic_salary=int(input("enter the basic pay:"))
if Basic_salary <= 30000:
    HRA=(Basic_salary*(20/100))
    DA=(Basic_salary*(10/100))
    I_tax=(Basic_salary*(5/100))
    Gross_salary=Basic_salary+HRA+DA
    Net_salary=Gross_salary-I_tax
    print("the employee basic pay after deductions is:",Net_salary)
elif Basic_salary > 30000 and Basic_salary <= 50000:
    HRA=(Basic_salary*(25/100))
    DA=(Basic_salary*(15/100))
    I_tax=(Basic_salary*(10/100))
    Gross_salary=Basic_salary+HRA+DA
    Net_salary=Gross_salary-I_tax
    print("the employee basic pay after deductions is:",Net_salary)
elif Basic_salary > 50000 and Basic_salary <= 100000:
    HRA=(Basic_salary*(35/100))
    DA=(Basic_salary*(20/100))
    I_tax=(Basic_salary*(15/100))
    Gross_salary=Basic_salary+HRA+DA
    Net_salary=Gross_salary-I_tax
    print("the employee basic pay after deductions is:",Net_salary)
elif Basic_salary>100000:
    HRA=(Basic_salary*(40/100))
    DA=(Basic_salary*(25/100))
    I_tax=(Basic_salary*(20/100))
    Gross_salary=Basic_salary+HRA+DA
    Net_salary=Gross_salary-I_tax
    print("the employee basic pay after deductions is:",Net_salary)
else:
    print("enter the valid amount to check the salary")
