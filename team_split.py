import random
from operator import itemgetter
# import randint

a =  int(input("Enter a team number: "))
lst = [[] for _ in xrange(a)]
sum_list = [0 for i in range(0,a)]

# seed read from file
seed = []
rfile = open("input.txt",'r')
while True:
   data = rfile.readline().split(',')
   if data[0] == '':break
   seed.append((data[0],int(data[1])))
rfile.close()
        

# print seed

for i in range(ord('A'), ord('Z')+1):
   seed.append((chr(i),random.randrange(5)+1))
# print seed

for i in range(0,a):
   # print i
   # print sum_list[i]
   sum_list[i] = sum( ( pair[0] for pair in lst[i] ) )
# print 'final sum_list:',sum_list


for value in sorted(seed, key=itemgetter(1), reverse=True):
   # print value
   for i in range(0,a):
      # print i
      # print sum_list[i]
      sum_list[i] = sum( [ pair[1] for pair in lst[i] ] )
   # print 'sum_list:',sum_list
   # sum_list.append(lst[i] for i in a)
   # print 'sum_lst:',sum_list
   index = sum_list.index(min(sum_list))
   # print index
   flag = False
   for i in range(index+1,a):
      if sum_list[index] == sum_list[i]:
         if bool(random.getrandbits(1)):
            lst[i].append(value)
            flag = True
            break
   if flag == False:
      lst[index].append(value)

wfile = open("team_list.txt",'w').close()
wfile = open("team_list.txt",'a')
for i in range(0,a):
   print 'Team',i+1,':',lst[i]
   wfile.writelines('Team'+`i+1`+':'+`lst[i]`)
   wfile.write('\n')
   # print '\n'
   print 'Member:',len(lst[i]),'Total Point:', sum_list[i]
   wfile.writelines('Member:'+`len(lst[i])`+'     Total Point:'+ `sum_list[i]`)
   wfile.write('\n******************************\n')
   # print '\n'
   # print 'Total Point:', sum_list[i]