#answer of question 2 
# def most_common(b):
#     element_count = {}  
#     for x in b: 
#         if x in element_count:
#             element_count[x] += 1
#         else:
#             element_count[x] = 1 


#     most_common = None  
#     max_count= 0

#     for x , meghdaresh in element_count.items():
#         if meghdaresh > max_count:
#             most_common = x
#             max_count = meghdaresh

#     return most_common

# b = ["a","a","a",2,3,"a",3,"a",2,4,9,3,3]
# result = most_common(b)
# print(result)

#answer of question 3:
# def tekrar(c):
#     element_count = {}      

#     for x in c:
#         if x in element_count:
#             element_count[x] += 1
#         else:
#             element_count[x] = 1

#     tekrar = []
#     for x, addadeshon in element_count.items():
#         if addadeshon >= 2 :
#             tekrar.append(x)
#     return tekrar 


# c = ["apple","watermelon","apple","banana","cherry","coconut","cherry","cherry"]
# result = tekrar(c)
# print(result)


 
      
