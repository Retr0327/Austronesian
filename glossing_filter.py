{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sdqNr-frog_lubi 2020 sung.mp3\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "file_name=str(input(\"請輸入檔案名稱：\"))\n",
    "try:\n",
    "    file=open(file_name+'.txt',\"r\",encoding=\"utf-8\")    \n",
    "except FileNotFoundError:          \n",
    "    print(\"file is not found\")\n",
    "else:\n",
    "    contents = file.readlines()  \n",
    "    contain=[]\n",
    "    for x in contents:\n",
    "        x.replace(\"XX\",\" \")\n",
    "        c=re.findall(\"\\d+\\.\\n\", x)\n",
    "        for X in c:\n",
    "            number=contents.index(X)\n",
    "            contain.append(number)\n",
    "    contain_1=[y+1 for y in contain]\n",
    "    contain_2=[]\n",
    "    for z in contain_1:\n",
    "        original_line=contents[z]\n",
    "        clean_data=re.sub(r'[<>]', \"\", original_line).replace(\"^\",\"\")\n",
    "        clean_data=re.sub(r'(L\\d.)', \"\", clean_data)\n",
    "        clean_data=re.sub(r\"\\b\\=\\b\", \"\", clean_data) \n",
    "        clean_data=re.sub(r\"[\\[\\]]\", \"\", clean_data) \n",
    "        clean_data=re.sub(r\"\\-\\b\", \"\", clean_data) \n",
    "        clean_data=re.sub(r\"(?<=a)\\.\\b\",\" \", clean_data)      #delete the dot between words (e.g. daha.ka)\n",
    "        contents[z]=clean_data.replace(\"L@\",\"\")+original_line\n",
    "    a_file = open(file_name+\".txt\", \"w\", encoding=\"utf-8\")\n",
    "    a_file.writelines(contents)\n",
    "    a_file.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
