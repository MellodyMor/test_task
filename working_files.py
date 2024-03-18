# -*- coding: utf-8 -*-
import os

def open_file():
    location = '/'
    for filename in os.listdir(location):
        f = open(os.path.join(location, 'person.log'), "r")
        t = f.read()
    r = t.split("********************************************************************************")
    return r
def day(n,k,b):
    if k[2] > b[2] and b[2] >= n[2]:
        return True
    elif k[2] == b[2]:
        if k[1] > b[1] and b[1] >= n[1]:
            return True
        elif k[1] == b[1]:
            if k[0] >= b[0]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def sum(time):
    otv = ""
    otv_mas = []
    for i in time.values():
        rr = [0, 0, 0]
        for y in i:
            t3 = [0, 0, 0]
            t1 = list(map(int, y[0].split(":")))
            t2 = list(map(int, y[1].split(":")))
            if t2[2] - t1[2] >= 0:
                t3[2] = t2[2] - t1[2]
            else:
                t3[2] = 60 + (t2[2] - t1[2])
                t2[1] -= 1
            if t2[1] - t1[1] >= 0:
                t3[1] = t2[1] - t1[1]
            else:
                t3[1] = 60 + (t2[1] - t1[1])
                t2[0] -= 1
            t3[0] = t2[0] - t1[0]
            if rr[2] + t3[2] >= 60:
                rr[1] += 1
                rr[2] = (rr[2] + t3[2]) - 60
            else:
                rr[2] += t3[2]
            if rr[1] + t3[1] >= 60:
                rr[0] += 1
                rr[1] = (rr[1] + t3[1]) - 60
            else:
                rr[1] += t3[1]
            rr[0] += t3[0]
            # print(":".join(list(map(str, t3))))
        otv = print_data(rr)
        otv_mas.append(otv[:-1])
        otv = ""
    return otv_mas
def print_data(rr):
    otv=""
    for i in rr:
        if i < 10:
            otv+="0"+str(i)
        else:
            otv+=str(i)
        otv+=":"
    return otv
def print_on(time,otv,ch_2):
    f = open('otvet.txt', 'w',encoding='utf-8')
    f.write("число включенных элементов: "+str(ch_2)+"\n")
    c=0
    for i in time:
        f.write(str(i)+" Общее время: "+otv[c]+ u"\n")
        c+=1
        ch=0
        for y in time[i]:
            ch+=1
            f.write(str(ch)+". Начал:"+str(y[0])+"; Закончил:"+str(y[1])+ u"\n")
    f.close()
def prov(n,k):
    if k[2] >= n[2]:
        if k[1] >= n[1]:
            if k[0] >= n[0]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def rech(z1,z2):
    if prov(z1.split("."),z2.split(".")):
        r = open_file()
        ch=1
        flag=0
        st,kt,n="",'',''
        q=[]
        for i in r[1:]:
            i=i.split("\n")
            for y in i[1:]:
                if "Начало работы" in y:
                    st = y
                elif "Работа завершена" in y:
                    kt = y
                elif "Оператор" in y and flag==0:
                    flag = 1
                    n=y
            ch+=1
            if flag == 0:
                n="Оператор - нет имени"
            flag=0
            q.append([st,kt,n])
            st,kt,n="",'',''
        s={}
        time={}
        data={}
        ch_2=0
        for i in q:
            n=(i[0].split(" :")[1].split(" "))
            k=(i[1].split(": ")[1].split(" "))
            zz=i[2].split(" - ")
            zzz=zz[1].strip()
            n_new = n[0].split(".")
            if len(n[0].split(".")[-1]) == 4:
                n_new[-1]=n_new[-1][-2:]
            if day(z1.split("."),z2.split("."),n_new):
                ch_2+=1
                if zzz not in s:
                    s[zzz.strip()] = 1
                    time[zzz] =[[n[1],k[1]]]
                    data[zzz] = [[n[0], k[0]]]
                else:
                    s[zzz] +=1
                    time[zzz].append([n[1], k[1]])
                    data[zzz].append([n[0], k[0]])
        otv_mas = sum(time)
        print_on(time,otv_mas,ch_2)
    else:
        print("error")