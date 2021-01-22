import re

def repeat(File):                 #to find the duplicated number
    num_repeat={}
    for r in File:
        if File.count(r)>1:
            num_repeat[r]=File.count(r)
    if bool(num_repeat) is True:
        return num_repeat
    else:
        return "沒有重複數值"

file_name= str(input("請輸入檔案名稱："))

try:
    with open(file_name+'.txt',"r",encoding="utf-8") as file:
        contents=file.readlines()   
        num_in_contents=[]
        num_contain=[]

    for x in contents:
        num=re.findall("\d+\.\n", x)
        for X in num:
            num_in_contents.append(X)
            number=contents.index(X)
            num_contain.append(number)    #the location of number in contents
    if repeat(num_in_contents) != "沒有重複數值":
        print(repeat(num_in_contents))
    else:
        first_line=[y+1 for y in num_contain]    
        for z in first_line:
            gla=contents[z] 
            glb=contents[z+1]
            glc=contents[z+2]
            glpre=re.sub(r'([\^\<\>]|(L[\d@].)|(\b\=\b)|\-\b|[\[\]]|)', "", gla)    #replace things without space
            glpre=re.sub(r"(?<=a)\.\b|[\s]+"," ", glpre)        #space filter
            contents[z]=glpre+"\n"+gla+""   #glpre+gla
            
    with open(file_name+'.txt', "w", encoding="utf-8") as a_file:   
        a_file.writelines(contents)

except FileNotFoundError:          
    print("file is not found")
        
