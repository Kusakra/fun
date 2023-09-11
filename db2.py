#简易可存储键值对数据库alpha2
import json
import os
db:dict
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
def prog():
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
default=0
try:
    f=open('db.json','r')     #file content check
    if len(f.read()) !=0:
        fi=1
    else:fi=0
    f.close()
except FileNotFoundError:
    fi=0
    default=1 #file not exist
try:
    f=open('tmp_db.json','r') #tmp_file content check
    if len(f.read()) !=0:
        fi_=1
        save=input("检测到未保存的数据，是否保存？Y/N")
        if 'Y'or'y' in save:
            pass
        elif 'N'or'n' in save:
            fi_=0
    else:fi_=0
    f.close()
except FileNotFoundError:
    fi_=0

if fi_==1:          #write unsaved data
    f=open('tmp_db.json','r')
    tmp_db=json.load(f)
    f.close()
    f=open('db.json','r')
    db=json.load(f)
    f.close()
    db.update(tmp_db)
    data=json.dumps(db)
    f=open('db.json','w')
    f.write(data)
    f.close()
try:                #open the file
    f=open('db.json','r')
    if fi==1:       #file is not blank
        data=json.load(f)
        db.update(data)
        f.close()
        f=open('tmp_db.json','w+')
    else:           #file is blank
        f.close()
        f=open('tmp_db.json','w+')
except FileNotFoundError:
        f=open('tmp_db.json','w+')

judge=1             #main program start     
print("输入/help以查询指令")
while judge==1:     
    prog()
    data=json.dumps(db)
    judge=input("按1继续执行，按其他键退出\n")
    try:    
        a=float(judge)
    except ValueError:
        f.write(data)
        f.close()
        if default==0:
            os.remove('db.json')
            os.rename('tmp_db.json','db.json')
        else: 
            os.rename('tmp_db.json','db.json')
        print("已成功退出")
        break
    judge=int(judge)
else:
    f.write(data)
    f.close()
    if default==0:
        os.remove('db.json')
        os.rename('tmp_db.json','db.json')
    else: 
        os.rename('tmp_db.json','db.json')
    print("已成功退出")