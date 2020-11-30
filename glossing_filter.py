import re
file_name=str(input("請輸入檔案名稱："))
try:
    file=open(file_name+'.txt',"r",encoding="utf-8")    
except FileNotFoundError:          
    print("file is not found")
else:
    contents = file.readlines()  
    contain=[]
    for x in contents:
        x.replace("XX"," ")
        c=re.findall("\d+\.\n", x)
        for X in c:
            number=contents.index(X)
            contain.append(number)
    contain_1=[y+1 for y in contain]
    contain_2=[]
    for z in contain_1:
        original_line=contents[z]
        clean_data=re.sub(r'[<>]', "", original_line).replace("^","")
        clean_data=re.sub(r'(L\d.)', "", clean_data)
        clean_data=re.sub(r"\b\=\b", "", clean_data) 
        clean_data=re.sub(r"[\[\]]", "", clean_data) 
        clean_data=re.sub(r"\-\b", "", clean_data) 
        clean_data=re.sub(r"(?<=a)\.\b"," ", clean_data)      #delete the dot between words (e.g. daha.ka)
        contents[z]=clean_data.replace("L@","")+original_line
    a_file = open(file_name+".txt", "w", encoding="utf-8")
    a_file.writelines(contents)
    a_file.close()