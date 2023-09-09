import json
import os
db={}
def put(key,value):   
    if db.get(key,None)!=None:
        str=input("该键值对已存在！是否覆盖原有的值？Y/N")
        if str=='Y'or'y':
            db[key]=value
        elif str=="N"or"n":
            pass
        else :print("请输入Y/N！")
    elif db.get(key,None)==None:
            db[key]=value
            print ("OK")
    else :pass
def main():
    ori=input()
    ori=ori.split()
    if "put" in ori:
        if len(ori)!=3:
            print("格式错误！")     
        else:     
            put(ori[1],ori[2])
    elif "get" in ori:
        if len(ori)!=2:
            print ("格式错误！")
        else:    
            if ori[1] in db:
                print ("key:"+ori[1]+" "+"value:"+db["{}".format(ori[1])])
            else :print ("NOT_FOUND")
    elif "del" in ori :
        if len(ori)!=2:
            print ("格式错误！")
        else:
            if ori[1] in db:
                del db["{}".format(ori[1])]
                print ("OK")
            else : print("输入的键无效！")
    else : print("格式错误！")
try:
    f=open('db.json','r')
    data=json.load(f)
    db=data
    f.close()
    f=open('db.json','w+')
except FileNotFoundError:
    f=open('db.json','w+')
judge=1
while judge==1:
    main()
    data=json.dumps(db)
    judge=input("按1继续执行，按其他键退出")
    try:
        a=float(judge)
    except ValueError:
        f.write(data)
        f.close()
        print("已成功退出")
        break
    judge=int(judge)
else:
    f.write(data)
    f.close()
    print("已成功退出")