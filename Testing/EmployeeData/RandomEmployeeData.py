import random

f = open("names.txt")
w = open("words.txt")
f = eval(f.read())
w = eval(w.read())
table = input("Table name : ")
#f = open(table + '.txt', 'a')
col = ['id','name','age','salary','did','email','phone']
l = int(input('start id :'))
n = int(input("end id : "))

rows = []
for i in range(n-l+1):
    rows.append([])

q = list(range(1,n+1))

for i in range(n-l+1):
    #print('-'*30)
    for j in range(len(col)):
        #print(str(col[j]) + " : ", end = '')
        if(col[j]=='id'):
            x = 'E' + str(l+i)
        elif(col[j] == 'name'):
            x = f[random.randrange(0,len(f))].lower().title()
        elif(col[j] == 'age'):
            x = str(random.randrange(19, 67))
        elif(col[j] == 'salary'):
            x = str(random.randrange(6, 200)) + '000'
        elif(col[j] == 'did'):
            x = 'D' + str(random.randrange(1, 5))
        elif(col[j] == 'email'):
            x = rows[i][1].lower() + w[random.randrange(0,len(w))].lower() + '@' + random.choice(['gmail.com','yahoo.com','rediffmail.com','mailru.com'])
        elif(col[j] == 'phone'):
            x = str(random.randrange(7616301829,9999999999))
        m = list(x)
        if('.' in m):
            m.remove('.')
        m = "".join(m)
        if(m.isdigit()):
            x=eval(x)
        elif(x==''):
            x = 'NULL'
        rows[i].append(x)
    rows[i] = tuple(rows[i])


print('\n\nINSERT INTO ' + table +' VALUES')
for i in rows:
    print('     ', end = '')
    #print('     ', end = '', file = f)
    if('NULL' in i):
        print('(',end = '')
        for j in i:
            if(i[-1]!=j):
                if(j == 'NULL'):
                    print(str(j) + ', ', end = '')
                    continue;
                if(type(j)==str):
                    print("'"+str(j)+"', ",end = '')
                else:
                    print(str(j)+', ', end = '')
            elif(rows[-1]==i):
                if(j == 'NULL'):
                    print(str(j), end = ');\n')
                    continue;
                if(j.isalnum()):
                    print("'"+str(j)+"'",end = ');\n')
                else:
                    print(str(j), end = ');\n')
            else:
                if(j == 'NULL'):
                    print(str(j), end = '),\n')
                    continue;
                if(j.isalnum()):
                    print("'"+str(j)+"'",end = '),\n')
                else:
                    print(str(j), end = '),\n')
    else:
        if(rows[-1]!=i):
            print(i,', ',sep = '')
            #print(i,', ',sep = '', file = f)
        else:
            print(i,';',sep = '')
            #print(i,';',sep = '',file = f)
        

while 1:
    rows  = 0

