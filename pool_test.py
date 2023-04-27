from csv import DictWriter
import pandas as pd
titles = ['address','allotted']
df = pd.read_csv('Pool.csv')
s = '127.0.0.156'
x = df.index[df['address']==s].values
if(len(x)>0):
    print(x)
    l = list(df['allotted'].iloc[x])[0]
    print(l)
else:
    print('nah')
    l = df["allotted"].iloc[-1]
    print(l)
    l = l.split('.')
    print(l)
    x = int(l[3])
    x+=1
    x  = str(x)
    while len(x) <3:
         x = '0'+x
    print(x)
    ip = l[0]+'.'+l[1]+'.'+l[2]+'.'+x
    
    entry = {'address':s,'allotted':ip}
    with open('Pool.csv','a',newline='') as f_object:
            writerObject = DictWriter(f_object,fieldnames=titles)
            writerObject.writerow(entry)
            f_object.close()

# # Print the contents of the dictionary
# print(person_dict)