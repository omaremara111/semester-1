# Week 1.2, Session 2: Task 6

#Inputs:
print("Welcome!")
temp = int(input("Enter the machine's temperature: "))
pressure = int(input("Enter the machine's pressure: "))
status = int(input("What is the machine's operational status? enter '1' for operating or '0' for stopped: "))

### Step 2: Evaluate Operating Conditions

#Use conditional statements involving `if`, `elif` and `else` to evaluate
#the operating temperature and pressure of the machine.

#### Temperature
if temp > 80:
    print("Machine's temerature is too high! Shut the machine down to cool off.")
elif 50 <= temp <= 80:
    print("Machine's temperature is safe")
else:
    print("Machine's temperature is low. No action needed.")


#### Pressure
if pressure > 100:
    print("High pressure detected! Maintenance recommended.")
elif 70 <= pressure <= 100:
    print("Pressure is stable")
else:
    print("Pressure low. System operating normally.")

### Step 3: Determine Status
if status == 1:
    if temp>80 or pressure>100:
        print("Machine is running in unsafe conditions. Try shutting it down.")
    else:
        print("Machine is running normally.")
else:
    print("Machine is not currently running. No immediate action needed. ")

