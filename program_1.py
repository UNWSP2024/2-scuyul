#By Griffin Corniea 9/8/2025
#InfoPrinter

space = " "
name = "Griffin"
city = "Eagan"
state = "MN"
zipcode = "55124"
major = "Engineering"
phoneNum = "651-260-4296"
address =(city + space + state + space + zipcode)

def personal_information():
    print(name + space + address + space + phoneNum + space + major)

# Line which calls the above function.
personal_information()