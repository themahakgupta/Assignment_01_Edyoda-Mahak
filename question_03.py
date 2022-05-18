# To cehck wheather a given strings contains special character or not
string=input("Enter a statement: ")
replace=string.replace(" ","1")
if replace.isalnum():
    print(string,": 'String is accepted',as special characters are not present hence")
else:
    print(string,":'String is not accepted',as special characters are present")









