#简易可存储键值对数据库
import json
db={}
def put(key,value):   
    if db.get(key,None)!=None:
        str=input("该键值对已存在！是否覆盖原有的值？Y/N\n")
        if str=='Y'or'y':
            db[key]=value
        elif str=="N"or"n":
            pass
        else :print("请输入Y/N！\n")
    elif db.get(key,None)==None:
            db[key]=value
            print ("OK")
    else :pass
def main():
    ori=input("请输入命令：\n")
    ori=ori.split()
    if "help" in ori:           #help
        print("输入指令：put <key> <value>")
        print("查询指令：get <key>")
        print("删除指令：del <key>")
        print("列出所有键值对：getall")
    elif "getall" in ori:
        print(db)
    elif "put" in ori:          #put
        if len(ori)!=3:
            print("格式错误！")     
        else:     
            put(ori[1],ori[2])
    elif "get" in ori:          #get
        if len(ori)!=2:
            print ("格式错误！")
        else:    
            if ori[1] in db:
                print ("key:"+ori[1]+" "+"value:"+db["{}".format(ori[1])])
            else :print ("NOT_FOUND")
    elif "del" in ori:         #del
        if len(ori)!=2:
            print ("格式错误！")
        else:
            if ori[1] in db:
                del db["{}".format(ori[1])]
                print ("OK")
            else : print("输入的键无效！")
    else : print("格式错误或输入了未知指令，请再次输入！")

try:                #open the file
    f=open('db.json','r')
    data=json.load(f)
    db=data
    f.close()
    f=open('db.json','w+')
except FileNotFoundError:
    f=open('db.json','w+')
judge=1             #main program start     
print("输入/help以查询指令")
while judge==1:     
    main()
    data=json.dumps(db)
    judge=input("按1继续执行，按其他键退出\n")
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