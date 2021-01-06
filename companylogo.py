def companyLogo(a):

  for i in a:
    count=0 
    x=len(a)
    for j in range(i+1,x):
      if(a[i]==x[j]):
        count=count+1
        print(a[i]+ " "+count)
      elif(a[i]!=x[j]):
        companyLogo()


if __name__ == '__main__':
  s = str(input())
  companyLogo(s)
