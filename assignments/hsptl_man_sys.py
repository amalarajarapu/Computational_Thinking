patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    level = int(input("Enter emergency level (1-Normal, 2-Serious, 3-Critical): "))

    if level == 3:
        priority = "HIGH"
    elif level == 2:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    patients.append([name, age, level, priority])


print("\n----- EMERGENCY PATIENT LIST -----")

# Critical patients first
patients.sort(key=lambda x: x[2], reverse=True)

for patient in patients:
    print("Name:", patient[0])
    print("Age:", patient[1])
    print("Emergency Level:", patient[2])
    print("Priority:", patient[3])
    print("----------------------")
