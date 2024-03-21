# Python code to show the reciprocal of the given number to highlight the difference between def() and lambda().  
def reciprocal( num ):  
    return 1 / num  
   
lambda_reciprocal = lambda num: 1 / num  
   
# using the function defined by def keyword  
print( "Def keyword: ", reciprocal(6) )  
   
# using the function defined by lambda keyword  
print( "Lambda keyword: ", lambda_reciprocal(6) )  
