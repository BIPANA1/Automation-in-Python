# abclist = ["sandip","bipana","dipika","samarpan"]
# print(len(abclist))
#
# mixlist = ["dipika","punam",2057,True,"sandip","bikash","samir","bijay"]
#
# print(mixlist)
# print(mixlist[2])
# print(mixlist[-3])
# print(mixlist[2:5])
#
# if "sangita" in mixlist:
#     print("Yes, present")
#     if "bikash" in mixlist:
#         print("not present")
# elif "sandip" in mixlist:
#     print("Great")
# else:
#     print("Not present")


# a= 200
# b= 600
# # short hand
# print ("A is greater than B") if a>b else print("b is greater than a") if a<b else print("They are equal")



day = 6
match day:
    case 1:
        print("This is first")
    case 2:
        print("This is second")
    case 3:
        print("This is third")

    case 4:
        print("This is fourth")

    case 5:
        print("This is fifth")
    case _:
        print("Default Case")

while(day < 12):
    print("Hello")
    day +=1
else:
    print("This is the end")

num_list =[1,2,3,4,5,6]

for num in num_list:
    print(num)

string_name = 'Sandip Driver a friend of us'

for char in string_name:
    print(char)