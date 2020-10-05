#strings
name="compaqc"
#string indexing
print(name[-1])
# string slicing
print(name[-1:0:-1])
# take user input
user_name,age=input("enter your name and age: ").split(",")
print(user_name)
print(age)
# len function
print(len(name))
# lower,upper,title methods
print(name.title())
# upper method
print(name.upper())
# find,replace,center method
print(name.find("c",1))
# center method
print(name.center(11,"*"))
# strings are immutable
# mutable=changable
# immutable= can't be change
