# string is a sequence of characters  used to store data which includes letters,digits and special characters "" ' ' for single line triple quotes for multi line string
# every character in  the string has an index starts from 0 string slicing and other operations can be done by using the index numbers
def string_functions():
                        l="python"
                        print (len(l))# prints length of the string
                        print(max(l))# prints max value of the string by ascii value
                        print(min(l))#prints min value of the string by ascii value
                        print(sorted(l))#sorts small to big by ascii value into seperate strings in a list
                        for i in l:
                                    print (ord(i))# prints ascii value of the string
#string addition:
#string_functions()
def string_operations():
                        a="good "
                        b="morning"
                        print(a+" "+b)# string can be added + concatination
                        print(b+" "+a)
                        print(a*4) #string can be repeated by using the number and *repetiiton
                        print(b*3)
                        print("m"in b) # membership operator checks the value present in string or not returns true or false
                        print("g"in a)# "string value to find" in (membership operators) in the string
                        print("A"in a)
                        print("goo"in a) #check multiple if they are in the same order
                        c="4"# multiplying two strings raises a type error
                        g="5"
                        print(c+g) # does not add 4+5= 9 prints both 4 and 5 as 45 as they are in string format
                        #print(c*g) #TypeError: can't multiply sequence by non-int of type 'str
                        t=4
                        r="5"
                        print(r*t) # print 5 4 times
#string_operations()
def string_indexing_and_slicing():
                                    g="ABCD EFGHI"
                                    print(g[8]) #string indexing starts from 0 
                                    print(g[0])#spaces are counted
                                    print(g[1])#to print single digit by the index number
                                    print(g[-1])# negative indexing prints values from reverse
                                    print (g[:]) #string slicing (start stop step) default values are start=0 ,stop= until the end,step=1
                                    print(g[::-1])# here step is -1 so the cursor moves backwards  positive moves left to right
                                    print(g[1::-1])# negative moves from right to left so output start from 1 which is B and -1 goes to 0 index(A) and stops
                                    s = "HELLO"
                                    print(s[1:4])

#string_indexing_and_slicing()
#strings are immuntable meaning we cant modifiy after creation attempting to change raises a type error
def string_modification():
                            j="python"
                            j[1]="t" # raises a type error because string is immuttable
                            del j[3] #TypeError: 'str' object does not support item assignment
                            s="python"#
                            result="P"+ s[1:]
                            print(result)
#string_modification()
def string_formatting():
                        a=4
                        b=5.11
                        c="python"
                        print(f"integer value is {a},float is {b},string is {c}")
                        #escape sequence 
                        s=  'a \t b'#tab space in a string
                        t='a\n b'# new line in a string
                        r='a\' b'# colon in a string
                        print(s)
                        print(t)
                        print(r)
                        #raw string : ignores the escape sequence using r or R
                        path=R'C:\Windows\Containers'
                        path1="C:\Windows\Containers"
                        print(path)
                        #print(path1)# "\W" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\W"? A raw string is also an option.
                        
#string_formatting()
def string_methods():
                        #1.lower 2.upper 3.split 4. join 5.count 6.find 7.strip 8.replace
    #1 lower converts all upper case letters to lower
    s="PYTHON1"
    print(s.lower())
    t="networK"
    print(t.upper())
    print(t.swapcase())
    print(t.isdigit())#checks if the t is digit false
    print(t.isspace())#checks if the t is space false
    print(t.isalnum())# checks if the string has alphabets and numericals
    print(t.isupper())
    print(t.islower())
    

    

    
    






string_methods()
