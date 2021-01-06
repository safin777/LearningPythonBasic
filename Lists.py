if __name__ == '__main__':
    x = int(input())
    listA=[]
    for i in range (x):
       command = list(input("").split(" "))\
       
       if command[0]=="insert":
         a,b = map(int,(command[1],command[2]))
         listA.insert(a,b)
       
       elif command[0]=="print":
         print(listA)
       
       elif command[0]=="remove":
         listA.remove(int(command[1]))
       
       elif command[0]=="append":
            listA.append(int(command[1]))
            
       elif command[0]=="sort":
            listA.sort()
        
       elif command[0]=="pop":
            
           listA.pop()
       elif command[0]=="reverse":
            listA.reverse()
