
print("Write a text:")
string=input(); 
words = string.split(" ");
for i in range (0,len(words)):
  count=1;
  listA=[];
  for j in range (i+1,len(words)):
    if (words[i] == words[j] ):
      count=count+1;
      listA.append(words[j])
    if(count>=1):
       for i in range(0,len(listA)):
          final=[];
          for j in range(i+1,len(listA)):
             if(listA[i] >= listA[j]):
               final.append(listA[i]);
             elif(listA[i]<listA[j]):
               final.append(listA[j]);
               print(final);
             else:
               print("-1");

                      
                
              



