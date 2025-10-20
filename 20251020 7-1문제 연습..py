def search_list(a,x):
      n = len(a)
      list=[]
      for i in range(0,n):
            if x == a[i]:
                  list.append(i)

      return []

v=[17,92,18,33,58,7,33,42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900)) 