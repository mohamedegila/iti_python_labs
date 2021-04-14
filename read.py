import os

if os.path.isfile("./log1.txt"):
    file1 = open('log1.txt', 'r')
    num = int(file1.readline().split(':')[1])
    print(num)
    num = int(file1.readline().split(':')[1])
    print(num)
    file1.close
else:
    logfile = open('log1.txt', 'a')
    logfile.write("win:{}\nlose:{}".format(1,10))
    logfile.close()