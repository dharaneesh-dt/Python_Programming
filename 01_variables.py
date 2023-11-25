##########################Variables#########################

#Rule1: variable name must start with a letter or the underscore character
          #Example:name="Dharaneesh"
#Rule2:variable name cannot start with a number
          #Example:7name="Dharaneesh"----->invalid variable
#Rule3:variable name can only contain alpha-numeric characters and underscores
          #Example:mark_1=100
#Rule4:variable names are case sensitive
          #Example:(sports,Sports)
#Rule5:variable name cannot contain any python keywords
          #Example:if="Dharaneesh is happy")------>invalid variable
             #(total 33 keywords)

#Variable programs
name="dharaneesh"
print(name)

# Check the type of variable
print(type(name))

# anything between double quote will be a string and it will be displayed as it is. (output will be name not dharaneesh)
print("name")

#Integer variable
age=16
print(age)

# Check the type of variable
print(type(age))

#float variable
weight=43.0
print(weight)

height=158

print(height)

# type of variable
print(type(weight))
print(type(height))

#Boolean variable
is_male=True
print(is_male)

#type of vairable
print(type(is_male))

#Many values to Mulitple variables

(a,b,c)=("cricket","football","kabadi")
print(a,b,c)

######Note: no of values should match with no. of variables###

#One value to multiple variables

x=y=z="cricket"
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


#Unpack a collection
Games=["cricket","football","kabadi"]
v1,v2,v3=Games
print(v1)
print(v2)
print(v3)



