import re
def my_grep(word,file):
    with open(file,'r') as f:
        f_=f.read()
        patn=re.compile(r'.+{}.+'.format(word))
        li=patn.findall(f_)
        for i in li:
            print(re.sub('{}'.format(word),'\033[31m{}\033[0m'.format(word),i,))
a=1
count=1
file=input("输入文件路径：\n")
while a==1 and count<3:
    try:    
        f=open(file,'r')
        f.close()
        word=input("输入需要查找的词：\n")
        my_grep(word,file) 
        a=2
    except FileNotFoundError:
        print("输入的文件路径有误，请重新输入！")
        file=input("输入文件路径：\n")
        count=count+1
        if count==3:
            print("连续错误3次，已自动退出！")
else:pass