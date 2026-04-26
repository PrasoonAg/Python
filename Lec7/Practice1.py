#05
#P-1
#=========================================================================#
#Practice Questions
#=========================================================================#
#@1# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java.

# WAF that replace all occurrences of "java" with "python" in above file.
# (here replace means first read then do changes then overwrite)

# Search if the word "learning" exists in the file or not.

def replace_java_with_python():
    with open("practice1.txt","w") as f:
     data = f.write("Hi everyone\nwe are learning File I/O \nusing Java\nI like programming in Java.")

    with open("practice1.txt","r") as f: #read
     data = f.read()

    new_data = data.replace("Java","python") # replace() works because data is a string.
    print(new_data)

    with open("practice1.txt","w") as f: # Write updated content back to file (overwrite)
        f.write(new_data) # "w" mode truncates (clears) file first, then writes new data
            
def check_for_word():
    word = "learning"
    with open("practice1.txt","r") as f:
        data2 = f.read()
        
    #(by apna collage method better way too)
    if word in data2:
        print("exist")
    else:
        print("not exist")
        
    #or
    #(by apna collage method)
    #if data2.find(word) != -1: # If word is found the index will be (0,1,2,3...) but if not then -1.
    #     print("exist")
    # else:
    #     print("not exist")
    

#@1# WAF to findin which line of the file does the word "learning" occur first
# Print -1 if word not found.

# from a file conating numbers separated by comma, print the ocunt of even numbers.

def check_for_line():
    word = "learning"
    data = True # true beacuse we wanna create a loop
    line_no  = 1
    with open("practice1.txt","r") as f:
        while data:# loop run intil readline() returns empty string
            #Loop is not infinite because data keeps changing and becomes empty at end of file
            data = f.readline()
            if(word in data): # auto check if the word exist
                print(line_no)
                # return
            line_no += 1
    return -1 # -1 at end of the loop
#print(check_for_line())

#@3#WAF # from a file conating numbers separated by comma, print the ocunt of even numbers.
# 1,2,45,55,86,76


# these values are in string format
 
count = 0
with open("practice2.txt","r") as f:
    data = f.read()
    print(data)
    
    #not using count 
    # num = ""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
            
#or
    # used count here
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1
print(count)

# individual number
# pause/ casting to int