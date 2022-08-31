files = input().split()
newfiles = []

for i in range(len(files)):
   if '.' in files:
       newfiles.append(files[i].split('.'))

print(newfiles)