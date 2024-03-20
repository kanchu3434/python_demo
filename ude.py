# user define exception
class salaryInRangeError(Exception):
    def __init__(self, salary,message="salary is not in (5000,1500) range"):
        self.salary=salary
        self.message=message
        super.__init__(self.message)
salary=int(input("enter salary amount"))
if not 5000<salary<1500:
    raise salaryInRangeError(salary)
else:
    print("enter salary amount is",salary)        
        