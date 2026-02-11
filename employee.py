class Employee:
    def __init__(self, empId, empName, basicSal):
        self._empId = empId
        self._empName = empName
        self.__basicSal = basicSal
        
    def calculate_salary(self):
        _salary = self.__basicSal
        return _salary
    
    def display(self):
        print(f"Employee Id: {self._empId}\nEmployee Name: {self._empName}\nBasic Salary: {self.__basicSal}\nCalculated Salary: {self.calculate_salary()}")
    
class PermanentEmployee(Employee):
    def __init__(self,empId,empName,basicSal,allowances):
        self.allowances = allowances
        super().__init__(empId,empName,basicSal)

    def calculate_salary(self):
        salary = self.__basicSal + self.allowances
        return salary

class ContractEmployee(Employee):
    def __init__(self,empId,empName,basicSal,hours):
        self.hours = hours
        super().__init__(empId,empName,basicSal)

    def calculate_salary(self):
        salary = self.__basicSal*self.hours
        return salary
    
class PayrollSystem:
    def main(self):
        em = Employee(123,"Hello",1000)
        em.display()
        

codeDriver = PayrollSystem()
codeDriver.main()