import requests,json
url='http://saral.navgurukul.org/api/courses'
x = requests.get(url)
k=x.json()
def req1():
    with open("ws.json","w") as f:
        json.dump(k,f,indent=6)
    for i in k:
        d=1
        for j in k[i]:
            print(d,":",j["name"],j["id"])
            d+=1
req1()
with open("ws.json","w") as f:
    json.dump(k,f,indent=6)
    emp=[]
    id=[]
    for i in k:
        d=1
        for j in k[i]:
            emp.append(j["name"])
            id.append(j["id"])
            d+=1
user=int(input("enter chapter number:"))-1
print(emp[user],id[user])
url2="http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises"
y=requests.get(url2)
m=y.json()
def req():
    with open("ws2.json","w") as f:
        json.dump(m,f,indent=6)
    for i in m:
        d=1
        for j in m[i]:
            print(d,":",j["name"],j["id"])
            d+=1
req()
with open("ws2.json","w") as f:
    json.dump(m,f,indent=6)
    emp1=[]
    id1=[]
    slug=[]
    for i in m:
        d=1
        for j in m[i]:
            emp1.append(j["name"])
            id1.append(j["id"])
            slug.append(j["slug"])
            d+=1
user1=int(input("enter exercise number:"))-1
print(slug[user1],id1[user1])
url3="http://saral.navgurukul.org/api/courses/"+str(id[user1])+"/exercise/getBySlug?slug="+str(slug[user1])
r=requests.get(url3)
n=r.json()
def req3():
    with open("ws3.json","w") as f:
        json.dump(n,f,indent=6)
req3()
with open("ws3.json","r") as f:
    s=json.load(f)
    print(s['content'])

