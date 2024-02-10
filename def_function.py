#first lesson
def name(x): #you can name the function what ever you like
    print(x)
    print("Lol")
print("Troll") #this is outside the function, now try to delete the end of the function and run again
name("Hello")
####################
def name(firstname): #inside this can not have numbers in or it will be error
    print(firstname, "Lol")
name("yourname") #you place yourname in the end of function then it become the function

#another example
def name(fname, lname): #you have as much thing in function as you want, but the end you must have the same or it will be error. Please try to delete one and test
    print(fname, "lol" ,lname)
name("Hoaz", "Troll")

#testing
def name(fname, lname, oname):
    print(fname, lname, oname)
name(True, 1, 3.14) #str, int, float, bool can become the variables
#another testing
def name(x, y, z): #look here
    print(z, y, x) #this is backward
name(1,2,3) #look up
name(x = 3, y = 2, z = 1) #you can change variables to the function

#for the variables not know yet, you can add it in at the end
def name(**here):
    print("Hoaz", here['lname'], here["fname"])
name(fname = "Troll", lname = "Lol")

#return in function
def func1(x):
    return 2*x
a = func1(5) #you can set the variables in the function, but you can not leave it empty
print(a)
#the end of the lesson, now it your turn to test it out on different stuff. This is just the basic BTW.