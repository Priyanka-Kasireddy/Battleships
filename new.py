# s="nee estam vachindhi thisuko"
# for i in range(len(s)):
#     print(s[i])

# table=["priyusha, priyanka, bhavana"]
# table.append("chay")
# print(table)

# i=0
# s="bye prends"
# while i<len(s):
#     print(s[i])
#     i+=1

# def highestNumber(lst):
# print(highestNumber([1,2,3]))

# c="priyanka"
# print(c[len(c)-1])

# list=[[1,2,3],[4,5,6]]
# for i in range(len(list)): 
#     x=list[i]
#     for j in range(len(x)):
#         print(x[j])

# result = 0
# lst=[1,2,5,8]
# for item in lst:
#     result = result + item
# print(result)

# result = 0
# for i in range(len(lst)):
#     result = result + lst[i]
# print(result)

# def countByCollege(studentLst):
#     collegeDict = { }
#     for student in studentLst:
#         name = student.split(",")[0]
#         college = student.split(",")[1]
#         if college not in collegeDict:
#             collegeDict[college] = 0
#         collegeDict[college] += 1
#     return collegeDict
# print(countByCollege(["priyanka, GMRIT" , "bhavas, CMRIT" , "priyush, GMRIT"]))

# def mostPopularCollege(collegeDict):
#     best = None
#     bestScore = -1
#     for college in collegeDict:
#         if collegeDict[college] > bestScore:
#             bestScore = collegeDict[college]
#             best = college
#     return best
# print(mostPopularCollege({"priyanka":10000, "kasi":1000, "reddy":500}))

# def createMultDict(n):
#     d = { }
#     for x in range(1, n+1):
#         innerD = {}
#         for y in range(1, n+1):
#             innerD[y] = x * y
#         d[x] = innerD
#     return d
# m = createMultDict(4)
# print(m[2][3])

# foodCounts = { "apples" : 5, "beets" : 2, "lemons" : 1 }
# def countItems(foodCounts):
#     totalfood=0 
#     for food in foodCounts:
#         print(foodCounts[food],food)
#         totalfood=totalfood+foodCounts[food]
#     return totalfood
# print(countItems(foodCounts))


# s="do you have a voting plan for the election happening next month" 
# def mostCommonFirstLetter(): 
#     words=s.split() 
#     print(words)
#     firstletter={} 
#     for letter in words: 
#         if letter[0] in firstletter: 
#             firstletter[letter[0]]=firstletter[letter[0]]+1 
#         else: 
#             firstletter[letter[0]]=1 
#         MaxKey=max(firstletter,key=firstletter.get) 
#     return MaxKey 
# print(mostCommonFirstLetter())


# def makeModel(data):
#     data["no.of rows"]=10
#     data["no.of cols"]=10
#     data["board size"]=500
#     data["cell size"]=50
#     data["computer Ships"]=5
#     data["user Ships"]=5
#     data["computer board"]=emptyGrid(data["no.of rows"],data["no.of cols"])
#     data["user board"]=emptyGrid(data["no.of rows"],data["no.of cols"])
#     data["computer board"]=addShips(data["computer board"],data["computer Ships"])
#     return data

# def drawGrid(data, canvas, grid, showShips): 
#     for row in range(data["no.of rows"]): 
#         for col in range(data["no.of cols"]): 
#             if grid[row][col]==SHIP_UNCLICKED: 
#                 canvas.create_rectangle(data["cell size"]*row,data["cell size"]*col,data["cell size"]*(row+1),data["cell size"]*(col+1),fill="yellow") 
#             else: 
#                 canvas.create_rectangle(data["cell size"]*row,data["cell size"]*col,data["cell size"]*(row+1),data["cell size"]*(col+1),fill="blue") 


# def makeView(data, userCanvas, compCanvas): 
        # userCanvas=drawGrid(data,userCanvas,data["user board"],True) 
        # compCanvas=drawGrid(data,compCanvas,data["computer board"],True)
        
# def drawGrid(data, canvas, grid, showShips):
#     for row in range(10):
#         for col in range(10):
#             if grid[row][col]==2:
#                 data["cell size"]=50
#                 a=canvas.create_rectangle(data["cell size"]*row,data["cell size"]*col,data["cell size"]*(row+1),data["cell size"]*(col+1),fill="yellow") 
#             else: 
#                 a=canvas.create_rectangle(data["cell size"]*row,data["cell size"]*col,data["cell size"]*(row+1),data["cell size"]*(col+1),fill="blue") 
#     return a
# print(drawGrid(data, canvas, grid, showShips))


# d={1,2,3,4,5,6}
# for i in d:
#     print(i)

# d={"apple":1,"banana":2}
# d={6:"5"}
# d["6"]="cat"
# print(d)
# for i in d:
#         print(i, d[i])

# d={"apple":1, "banana":2}
# for i in d:
#     print(i+":"+str(d[i]))
    
# d={1:"a",2:"b",3:"c",4:"c"}
# for i in d:
#     if d[i]=="c":
#         print(i,d[i])
    