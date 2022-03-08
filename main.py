import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"),end="")
print("000000")
import yaml

with open(r'C:\Users\DELL\Downloads\DataSet\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)
    # for i in documents.keys():
    #     print(i)
    print(documents['M1SampleWorkFlow']['Activities']['TaskA'])
    f = open("demofile2.txt", "a")
    while True:
        line = documents.readline()
        if not line:
            break
        string=now.strftime("%Y-%m-%d %H:%M:%S.")+"000000;"
        f.write(string)
    file1.close()
