num = []

def solve(choice):
    match choice:
        case 1:
            mean()
        case 2:
            median()
        case 3:
            mode()
        case default:
            return "No option specified"

def mean(): 
    sum = 0
    for i in range(len(num)):
        sum+=num[i]
    men = sum/(len(num))
    print("The mean is " + str(men))

def median():
    num.sort()
    length = int(len(num)/2)
    print(num[length])

def mode():
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] == num[j]:
                mod = num[i]
    print("The mode is: " + str(mod))

n = int(input("Enter the length of the array: "))
for i in range(n): 
    number = int(input("Enter a number: "))
    num.append(number)

print("Enter 1 to calculate the mean\nEnter 2 to calculate the median\nEnter 3 to calculate the mode")
choice = int(input("Enter an option: "))
solve(choice)