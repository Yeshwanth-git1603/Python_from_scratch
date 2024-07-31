# electricity bill checking using if else

meter_no=int(input("enter the meter number:"))
previous_reading=int(input("enter the previous reading:"))
current_reading=int(input("enter the current_reading:"))
total_units=current_reading-previous_reading
total_amount=total_units*unit_charge


if units <=100:
    unit_charge=2.50
    print("the total units consumed is:",total_units)
    print("the total amount is:",total_amount)
elif units > 100 and units <= 150:
    unit_charge=3.50
    print("the total units consumed is:",total_units)
    print("the total amount is:",total_amount)
elif units > 150 and units <=200:
    unit_charge=4.50
    print("the total units consumed is:",total_units)    
    print("the total amount is:",total_amount)
        
        
elif units >200 and units <=300:
    unit_charge=5.50
    print("the total units consumed is:",total_units)
    print("the total amount is:",total_amount)
        
elif units >300:
    unit_charge=6.50
    print("the total units consumed is:",total_units)
    print("the total amount is:",total_amount)

else:
    print("enter the valid units to check:")
