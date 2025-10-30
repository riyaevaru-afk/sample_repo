lower_value=int(input("Enter lower range value="))
upper_value=int(input("Enter upper range value="))
print("The prime number in the range of=")
for number in range(lower_value,upper_value+1):
    if (number>1) :
        for i in range (2,number):
            if (number%i)==0 :
                break
        else :
            print(number)
