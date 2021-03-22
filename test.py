row_no = 0

file = "input.txt"
fd = open(file, mode = 'r')
li = []
while True:
    data = fd.readline()
    data = data.replace("\n", "")
    if data:
        row_no += 1

        data = data.split(':')
        li.append(data)
    else:
        break

for i in range(len(li)):
    li[i][0] = int(li[i][0])
li2 = li[:-1]
li2.sort()
ans = ''
for i in range(len(li2)):
    if li[-1][0]%li2[i][0] == 0:
        ans = ans + str(li2[i][1])
if ans:
  print(ans)
else:
  print(li[-1][0])
