#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up. 
#where runner up score means second largest number
#hint just remove largest number then another largest number will be runner-up score


# score=list(map(int,input().split()))



#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
     new_item = item * 2
     b_list.append(new_item)
#   print(b_list)
  return b_list
newlist=mutate([1,2,3,5,8,13])
print(newlist)
