import sys

class Employee:
    def __init__(self, employeeId, employeeName):
        self.employeeId = employeeId
        self.employeeName = employeeName
    
    def getEmployeeId(self):
        print("The employee id is:", self.employeeId)
        return 0
    
    def setEmployeeId(self, employeeId):
        self.employeeId = employeeId
        print("Enter employee id:",end=""+"")
        self.employeeId = int(input())
    
    def getEmployeeName(self):
        print("\n**********************")
        print("Hi", self.employeeName,end="")
        return 0
    
    def setEmployeeName(self, employeeName):
        self.employeeName = employeeName
        print("Enter employee name:",end="")
        self.employeeName = input()
    
    def getSalary(self):
        print(", your salary is $:", self.salary)
        print("**********************\n")
        return 0
    
    def setSalary(self, salary):
        self.salary = salary
        print("Enter your salary:", end="")
        self.salary = float(sys.stdin.readline())
    
    def __del__(self):
        print(".")

class ContractEmployee(Employee):
    def __init__(self, empId, name, wage, hoursWorked):
        super().__init__(empId, name)
        self.wage = wage
        self.hoursWorked = hoursWorked
    
    def calculateSalary(self):
        self.salary = self.hoursWorked * self.wage
    
    def getWage(self):
        print("The wage is:", self.wage)
        return 0
    
    def setWage(self, wage):
        self.wage = wage
        print("Enter wage:", end="")
        self.wage = float(input())
    
    def getHoursWorked(self):
        print("The hours worked is:", self.hoursWorked)
        return 0
    
    def setHoursWorked(self, hoursWorked):
        self.hoursWorked = hoursWorked
        print("Enter the hours worked:", end="")
        self.hoursWorked = float(input())
    
    def __del__(self):
        print(".")

class PermanentEmployee(Employee):
    def __init__(self, empId, name, basicPay, hra, experience):
        super().__init__(empId, name)
        self.basicPay = basicPay
        self.hra = hra
        self.experience = experience
    
    def calculateMonthlySalary(self):
        variableComponent = 0
        if self.experience >= 3 and self.experience < 5:
            variableComponent = 5
        if self.experience >= 5 and self.experience < 10:
            variableComponent = 7
        if self.experience >= 10:
            variableComponent = 12
        variableComponent = variableComponent / 100
        variableComponent = variableComponent * self.basicPay
        self.salary = self.hra + self.basicPay + variableComponent
    
    def getBasicPay(self):
        print("The basic pay is:", self.basicPay)
        return 0
    
    def setBasicPay(self, basicPay):
        self.basicPay = basicPay
        print("Enter basic pay:", end="")
        self.basicPay = float(input())
    
    def getHra(self):
        print("The House Rent Allowance (HRA):", self.hra)
        return 0
    
    def setHra(self, hra):
        self.hra = hra
        print("Enter House Rent Allowance (HRA):", end="")
        self.hra = float(input())
    
    def getExperience(self):
        print("The experience is:", self.experience)
        return 0.0
    
    def setExperience(self, experience):
        self.experience = experience
        print("Enter experience (in years):", end="")
        self.experience = float(input())
    
    def __del__(self):
        print(".")

def main():
    from os import system
    system('color F0')
    system('cls')
    
    print("Contract Employee:-")
    print("============================================")
    ce = ContractEmployee(None, "\0", None, None)
    ce.setEmployeeId(None)
    ce.setEmployeeName("\0")
    ce.setWage(None)
    ce.setHoursWorked(None)
    ce.calculateSalary()
    ce.getEmployeeName()
    ce.getSalary()
    
    print("\nPermanent Employee:-")
    print("============================================")
    pe = PermanentEmployee(None, "\0", None, None, None)
    pe.setEmployeeId(None)
    pe.setEmployeeName("\0")
    pe.setBasicPay(None)
    pe.setHra(None)
    pe.setExperience(None)
    pe.calculateMonthlySalary()
    pe.getEmployeeName()
    pe.getSalary()
    print("exiting...")
    input()

main()
"""
Output of the code:
Contract Employee:-
============================================
Enter employee id:1
Enter employee name:Hassan
Enter wage:500
Enter the hours worked:5

**********************
Hi Hassan, your salary is $: 2500.0
**********************


Permanent Employee:-
============================================
Enter employee id:2
Enter employee name:ks
Enter basic pay:1855
Enter House Rent Allowance (HRA):115
Enter experience (in years):3.5

**********************
Hi ks, your salary is $: 2062.75
**********************

exiting...
"""