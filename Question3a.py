#translates module code to name
def modName(code):
    if(code == "CSC1006"):
       return "Mathematics 2"
    elif(code == "CSC1007"):
        return "Operating Systems"
    elif(code == "CSC1008"):
        return "Data Structures and Algorithms"
    elif(code == "CSC1009"):
        return "Object Oriented Programming"
    elif(code == "CSC1010"):
        return "Computer Networks"
    else:
        return "No such mod!"

choice = str(input("Enter module code>: "))
print(modName(choice))