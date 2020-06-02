# FUNCTION to check for PRIME NUMBER

def prime_number():
    global num

    num = input("Enter a number:")
    num = int(num)

    if (num > 1):
        for i in range(2, (num + 1)):
            if (num % i) == 0 and i < num:
                print(f"{num} is NOT a Prime Number!")
                break
            elif i == num:
                print(f"{num} is a Prime Number!")
                break
    else:
        print(f"{num} is NOT a Prime Number!")

prime_number()