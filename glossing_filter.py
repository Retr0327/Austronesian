import re
import homemade.duplicated

def num_index(src):
    container=[]
    for index, value in enumerate(contents):
        num=re.findall('\d+\.\n', value)
        if num:
            container.append(index)
    return container

file_name= str(input("請輸入檔案名稱："))
dialect=str(input("代名詞空開？"))

with open(file_name+".txt", mode='r', encoding='utf-8') as file:
    contents=file.readlines()
    num_contain=num_index(contents)
    first_line_index=[y+1 for y in num_contain]
    for i in first_line_index:
        gla=contents[i] 
        glb=contents[i+1]
        glc=contents[i+2]
        if dialect=='n' or dialect=='n':        # 決定代名詞是否空開
            glpre=re.sub(r'([\^\<\>]|(L[\d@].)|(\b\=\b)|\-\b|[\[\]]|)', "", gla)    # replace things without space   (for rukai)
            glpre=re.sub(r"(?<=a)\.\b|[\s]+"," ", glpre)                            # space filter (for rukai)
        else:
            glpre=re.sub(r'([\^\<\>]|(L[\d@].)\-\b|[\[\]]|)', "", gla)          # replace things without space  (for atayal)
            glpre=re.sub(r"(?<=a)\.\b|[\s]|(\b\=\b)+"," ", glpre)               # space filter (for atayal)
        contents[i]=glpre+"\n"+gla                                              # glpre+gla

with open(file_name+'.txt', "w", encoding="utf-8") as a_file:   
        a_file.writelines(contents)
 
