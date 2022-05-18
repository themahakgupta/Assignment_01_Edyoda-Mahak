#Count number of vowels in a given string

string=input("Enter a statement:")
vowels=['a','e','i','o','u']
count_vowels=0
for i in string:
    for j in vowels:
        if i==j:
            count_vowels+=1
print("Count of vowels in:",string,"are:",count_vowels)


    