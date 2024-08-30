# for layer in range(1,5):
#    count = 0
#    for num in range(1,11):
#        while layer > count:
#            print(num, end=" ")
#            count += 1
#    print()

# ---------------------------------------------------------------------

# maximumValueLoop = 9
# for columns in range(1, maximumValueLoop, 2):
#     multiplierSpace = (maximumValueLoop - columns) // 2
#     tempString = " " * multiplierSpace
#     tempString += "*" * columns
#     tempString += " " * multiplierSpace
#     print(tempString)
#
# for columns2 in range(maximumValueLoop,0,-2):
#     multiplierSpace2 = (maximumValueLoop - columns2) // 2
#     tempString2 = " " * multiplierSpace2
#     tempString2 += "*" * columns2
#     tempString2 += " " * multiplierSpace2
#     print(tempString2)

# string = "repetitive repetitive words words words may not not be suitable suitable"
# stringArr = string.split(" ")
# savedCollection = []
#
#
# for elements in stringArr:
#     word = 0
#     for elements2 in range(len(stringArr)):
#         if elements.lower() == stringArr[elements2].lower():
#             word += 1
#         if elements2 == len(stringArr)-1:
#             savedCollection.append(f"{elements} comes {word} time(s)")
#
# lastWord = ""
# for index in savedCollection:
#     if lastWord != index:
#         print(index)
#         lastWord = index
#


# ----------------------------------------------------------------------------------

# def newProd(dict):
#     productName = input("What's the name of the product to be added:")
#     productVal = int(input("What's the amount of the product:"))
#     dict[productName.lower()] = productVal
#
# def updateQuan(dict):
#     productFind = input("What's the name of the product whose amount has to be updated:")
#     if productFind.lower() in dict:
#         newVal = int(input("What is the new amount:"))
#         dict[productFind.lower()] = newVal
#     else:
#         print("Error! That does not exist in the inventory")
#
#
#
# inv = {
#     "canned":47,
#     "frozen":34,
#     "mutton":21,
#     "chicken":10,
#     "beef": 56,
#     "brain": 32
#
# }
# command = 1
#
# while command < 4 and command > 0:
#     command = int(input("Type 1 to add a new product, 2 to update quantities, 3 to check stock levels, any other number to quit:"))
#
#     if command == 1:
#         newProd(inv)
#     elif command == 2:
#         updateQuan(inv)
#     elif command == 3:
#         print(inv)

# -----------------------------------------------------------------------------------------------------------


# bookInfo = {
#     "0001":{
#         "title":"All the Bright Places",
#         "author":"Jennifer Niven",
#         "genre":"Novel",
#         "availability":False
#     },
#     "0002":{
#         "title":"Holding up the Universe",
#         "author":"Jennifer Niven",
#         "genre":"Novel",
#         "availability":True
#     },
#     "0003":{
#         "title":"Harry Potter:Chamber of Secrets",
#         "author":"J.K Rowling",
#         "genre":"Fantasy Novel",
#         "availability":True
#     },
#     "0004":{
#         "title":"Harry Potter:Goblet of Fire",
#         "author":"J.K Rowling",
#         "genre":"Fantasy Novel",
#         "availability":False
#     },
#     "0005":{
#         "title":"Breathless",
#         "author":"Jennifer Niven",
#         "genre":"Novel",
#         "availability":True
#     }
# }
#
# print(bookInfo)


# ---------------------------------------------------------------------------------------------------

# trafficMon = {
#     "1ASE":21,
#     "1BSE":10,
#     "1CSE":5,
#     "1DSE":34,
#     "2ASE":45,
#     "2BSE":26,
#     "2CSE":2,
#     "2DSE":32
# }
#
# answer = input("Write the intersection ID to check its Traffic count:")
#
# if answer in trafficMon:
#     print(f"There are an average of {trafficMon[answer]} in the intersection {answer}")
# else:
#     print(f"There is no intersection such as {answer}")


# ---------------------------------------------------------------------------------------------

# def newPat(dict):
#     tempDic = {}
#     patientName = input("What's the name of the patient:")
#     patientID = int(input("What's the ID of the patient:"))
#     patientAge = int(input("What's the age of the patient:"))
#     patientApp = int(input("How many appointments does the patient have:"))
#     patientRec = input("Patient's medical history:")
#     tempDic["name"] = patientName
#     tempDic["age"] = patientAge
#     tempDic["medicalrecord"] = patientRec
#     tempDic["appointments"] = patientApp
#
#     dict[patientID] = tempDic
#
# def updateDet(dict):
#     patientID = int(input("What's the patient's ID:"))
#     if patientID in dict:
#         tempDic = {}
#         patientName = input("What is the updated name of the patient:")
#         patientAge = int(input("What is the updated age of the patient:"))
#         patientRec = input("What is the updated medical history of the patient:")
#         patientApp = input("What is the updated appointments of the patient:")
#
#         tempDic["name"] = patientName
#         tempDic["age"] = patientAge
#         tempDic["medicalrecord"] = patientRec
#         tempDic["appointments"] = patientApp
#
#         dict[patientID] = tempDic
#     else:
#         print("Invalid")
#
#
#
#
#
#
#
#
# patientDetails = {
#     1011:{
#         "name":"Arthur Morgan",
#         "age":42,
#         "medicalrecord":"Tuberculosis",
#         "appointments":1
#     },
#     1012:{
#         "name":"Micah Bell",
#         "age":49,
#         "medicalrecord":"Cholera",
#         "appointments":0
#     },
#     1013:{
#         "name":"Dutch VanderLinde",
#         "age":56,
#         "medicalrecord":"None",
#         "appointments":3
#     },
#     1014:{
#         "name":"John Marston",
#         "age":32,
#         "medicalrecord":"None",
#         "appointments":1
#     }
# }
#
# userInput = int(input("1 to add a patient record to dictionary, 2 to update patient records, 3 to display details of a patient:"))
#
# if userInput == 1:
#     newPat(patientDetails)
# elif userInput == 2:
#     updateDet(patientDetails)
# elif userInput == 3:
#     userID = int(input("What's the ID of the patient:"))
#     if userID in patientDetails:
#         print(patientDetails[userID])
#     else:
#         print("Invalid")
# else:
#     print("Invalid")


# ------------------------------------------------------------------------------------------------------------------


# def evenorodd(num):
#     if num % 2 == 0:
#         print(f"The {num} is an even number")
#     else:
#         print(f"The {num} is an odd number")
#
# def palindromecheck(word):
#     wordReverse = word[::-1]
#     if wordReverse == word:
#         print(f"The {word} is a palindrome word")
#     else:
#         print(f"The {word} is not a palindrome word")
#
# def primeChecker(num):
#     primes = [2, 3, 5, 7, 11, 13, 17]
#     compositeCounter = 0
#
#     for index in primes:
#         if num % index == 0:
#             compositeCounter += 1
#
#     if (compositeCounter == 0 or num in primes) and num != 1:
#         print(f"{num} is a prime number")
#     elif compositeCounter != 0 or num == 1:
#         print(f"{num} is a composite number")
#
# def freqcounter(words):
#     dict = {
#
#     }
#     for letter in words.lower():
#         if letter in dict:
#             dict[letter] += 1
#         elif letter not in dict and letter != " ":
#             dict[letter] = 1
#
#     print(dict)
#
# def reversestr(word):
#     wordReverse = word[::-1]
#
#     return wordReverse
#
# print("To use Even and odd function press 1")
# print("To use Palindrome checker function press 2")
# print("To use prime number function press 3")
# print("To use Frequency counter function press 4")
# print("To use Reverse String Function press 5")
#
# answer = int(input("Please press your required function now:"))
#
# if answer == 1:
#     numUser = int(input("Type a number:"))
#     evenorodd(numUser)
# elif answer == 2:
#     wordUser = input("Enter a word:")
#     palindromecheck(wordUser)
# elif answer == 3:
#     numUser = int(input("Type a number:"))
#     primeChecker(numUser)
# elif answer == 4:
#     wordUser = input("Enter a word:")
#     freqcounter(wordUser)
# elif answer == 5:
#     wordUser = input("Enter a word:")
#     reverseWordUser = reversestr(wordUser)
#     print(f"The reverse of the word {wordUser} is {reverseWordUser}")
# else:
#     print("Invalid input")

# -------------------------------------TRY AND EXCEPTION----------------------------------------------------------


# num1 = int(input("Type the first number:"))
# num2 = int(input("Type the second number:"))
#
# try:
#     total = num1/num2
#     print(total)
# except:
#     print("An exception has occured. Perhaps you divided the first number by a zero.")


# --------------------------------------STRING AND LIST FUNCTIONS------------------------------------------------------

# arr = ["Ahmed", "Ali", "Kamran", "Imran"]
# word = "Moaz is great"
#
# print(word.capitalize())
# print(word.casefold())
# print(word.count("a"))
# print(word.encode())
# print(word.index("a"))
# print(word.isalpha())
# print(word.isalnum())
# print(word.isnumeric())
# print(word.strip())
#
# print(" & ".join(arr))
# print(word.split(" "))
# print(type(word))

# -----------------------------STRING TO EXPRESSION---------------------------------------------------------

# def add(num1, num2):
#     total = int(num1) + int(num2)
#
#     return total
#
#
# def sub(num1, num2):
#     total = int(num1) - int(num2)
#
#     return total
#
#
# def multiply(num1, num2):
#     total = int(num1) * int(num2)
#
#     return total
#
#
# def div(num1, num2):
#     total = int(num1) / int(num2)
#
#     return total
#
#
# expressionStr = "2*3/2+6*4-2/1"
# firstNum = ""
# secondNum = ""
# operator = ""
#
# for num in range(len(expressionStr)):
#     if expressionStr[num].isnumeric():
#         if operator == "":
#             firstNum += expressionStr[num]
#         else:
#             secondNum += expressionStr[num]
#     if expressionStr[num].isnumeric() == False or num == (len(expressionStr) - 1):
#         if operator == "":
#             operator = expressionStr[num]
#         else:
#             if operator == "+":
#                 total = add(firstNum, secondNum)
#             elif operator == "-":
#                 total = sub(firstNum, secondNum)
#             elif operator == "*":
#                 total = multiply(firstNum, secondNum)
#             elif operator == "/":
#                 total = div(firstNum, secondNum)
#             firstNum = total
#             secondNum = ""
#             operator = expressionStr[num]
#
# print(firstNum)


# ---------------------------------REMOVING EXTRA DUPLICATES-----------------------------------------------------

# nums = [0,0,1,1,1,2,2,3,3,4]
#
# for num1 in nums:
#     counterNum = 0
#     for num2 in nums:
#         if num2 == num1:
#             counterNum += 1
#             if counterNum > 1:
#                 nums.remove(num2)
#
# print(nums)

# ------------------------------------------FIRST OCCURRENCE OF STRING1 IN STRING2 (INCOMPLETE)-------------------------------

# stringOne = "von"
# stringTwo = "walkvonrunvon"
# firstIndex = 0
# index = 0
#
# if stringOne in stringTwo:
#     for letter in stringOne:
#         for letter2 in stringTwo:
#             if letter2 == letter:
#                 if index == 0:
#                     index = stringTwo.index(letter2)
#                     firstIndex = stringTwo.index(letter2)
#                     sameWord = True
#                 else:
#                     if stringTwo.index(letter2) == (index + 1):
#                         index = stringTwo.index(letter2)
#                     else:
#                         sameWord = False
#                         index = 0
#
#     print(firstIndex,stringTwo[firstIndex])
#
# else:
#     print(-1)


# --------------------------------------ARR SEARCH------------------------------------------------

# arr = [1,3,5,7,9]
# target = 2
# addNum = False
#
# for num in arr:
#     if num == target:
#         print(arr.index(num))
#     elif num > target and target not in arr and addNum == False:
#         addNum = True
#         indexToBeAddedIn = arr.index(num)
#
# if addNum == True:
#     arr.insert(indexToBeAddedIn,target)
#     print(arr)

# --------------------------------------------------------------------------------------------------

# names = ["Von","Moaz","Anby","Billy","Nichole","Seth"]
#
# namesLength = list(map(lambda word: len(word),names))
#
# print(namesLength)


# ---------------------------------------MATRIX ADDITION----------------------------------------------
#
#
# matrix_one = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# matrix_two = [
#     [9,8,7],
#     [6,5,4],
#     [3,2,1]
# ]
#
# matrix_three = []
# tempMat1 = []
# tempMat2 = []
# tempMat3 = []
#
# for index in range(len(matrix_two[0])):
#     currentMat = 0
#     for secondIndex in range(len(matrix_two)):
#         total = matrix_one[secondIndex][index] + matrix_two[secondIndex][index]
#         currentMat += 1
#         if currentMat == 1:
#             tempMat1.append(total)
#         elif currentMat == 2:
#             tempMat2.append(total)
#         elif currentMat == 3:
#             tempMat3.append(total)
#
# matrix_three.append(tempMat1)
# matrix_three.append(tempMat2)
# matrix_three.append(tempMat3)
#
# for indexMat3 in matrix_three:
#     print(indexMat3)


# ---------------------------MATRIX MULTIPLICATION-------------------------------------------------------

# matrix_one = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# matrix_two = [
#     [9,8,7],
#     [6,5,4],
#     [3,2,1]
# ]
#
# matrix_twoChanged = []
# matrix_three = []
#
# for indexTemp in range(len(matrix_two)):
#     tempMat = []
#     for indexTemp2 in range(len(matrix_two[0])):
#         tempMat.append(matrix_two[indexTemp2][indexTemp])
#     matrix_twoChanged.append(tempMat)
#
# for matrix in matrix_one:
#     tempMat = []
#     for matrixTwo in matrix_twoChanged:
#         total = []
#         for num,num2 in zip(matrix,matrixTwo):
#             total.append(num * num2)
#         totalSum = sum(total)
#         tempMat.append(totalSum)
#     matrix_three.append(tempMat)
#
# print(matrix_three)


# ==============================================NUMPY=====================================================

# ----------------------------------------------NUMPY ARRAYS---------------------------------------------

# import numpy as np

# npArr1 = np.array([[1,2,3],[4,5,6]])
# npArr2 = np.array([[[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]]])
#
#
# print(npArr1)
# print(npArr1.ndim, "dim")
# print(type(npArr1), "type")
# print(npArr1.shape, "shape")
# print(npArr1[0:2,1], "sliced")
# print(npArr1.reshape(3,2), "reshaped")
#
# print(npArr2)
# print(npArr2.ndim, "dim")
# print(type(npArr2), "type")
# print(npArr2.shape, "shape")
# print(npArr2[1:2,0:2,2], "sliced")
# print(npArr2.reshape(3,2,2), "reshaped")

# -------------------------------------RANDOM ARRAY OPERATIONS AND MEAN,MEDIAN,STD,VAR------------------------------

# import numpy as npy
#
# arr1 = npy.random.randint(26,75,size=(5,5))
# arr2 = npy.random.randint(1,10,size=(5,5))
#
# arr3 = arr1 + arr2
# arr4 = arr3 / arr1
# resultantArr = arr4 + arr2
#
# resultantArrMean = npy.mean(resultantArr)
# resultantArrMedian = npy.median(resultantArr)
# resultantArrSTD = npy.std(resultantArr)
# resultantArrVar = npy.var(resultantArr)
#
# resultantArrInv = npy.linalg.inv(resultantArr)
# resultantArrDet = npy.linalg.det(resultantArr)
#
# dotArr = npy.dot(arr1,arr2)
#
#
# print(resultantArr, "ResultantArr")
# print(resultantArrMean, "Mean")
# print(resultantArrMedian, "Median")
# print(resultantArrSTD, "STD")
# print(resultantArrVar, "VAR")
# print(resultantArrInv, "Inverse")
# print(resultantArrDet, "Determinant")
# print(dotArr, "Dot arr of arr1 and arr2")


# -------------------------------------------------MEAN, VAR AND STD----------------------------------------------

# import numpy as np
#
# juneWeather = np.array([34,33,33,32,35])
# aprilWeather = np.array([30,28,29,29,30])
#
# juneStd = np.std(juneWeather)
# aprilStd = np.std(aprilWeather)
#
# if juneStd > aprilStd:
#     print(f"The weather in June({juneStd}) was less consistent than April's({aprilStd})")
# else:
#     print(f"The weather in April({aprilStd}) was less consistent than June's({juneStd})")


# -----------------------------------------NORMAILIZATION OF DATA------------------------------------------------

# import numpy as np
#
# employees = np.array(
#     [
#         [25,3000],
#         [21,2400],
#         [45,8000],
#         [30,5000],
#         [50,10000]
#     ]
# )
#
# employeesMax = np.max(employees)
# employeesMin = np.min(employees)
#
# normalizedData = (employees - employeesMin) / (employeesMax - employeesMin)
#
# print(normalizedData)

# -------------------------------------------STD of Bitcoins-------------------------------------------------------

# import numpy as np
#
# Bitcoin = np.array([68202,67573,66018,66066,64520,67556,68642,68224])
# Ethereum = np.array([3531,3477,3457,3386,3132,3259,3251,3275])
# Tether = np.array([1.0001,1.0003,1.0003,0.9999,0.9999,1.0003,0.9999])
# Solana = np.array([184,182,172,179,168,182,180,184])
# BNB = np.array([601,595,582,579,563,579,582,583])
# USDC = np.array([1,1.0001,0.9999,1.0002,0.9999,1.0001,1,0.9999])
# XRP = np.array([0.5994,0.6271,0.594,0.6187,0.6033,0.5987,0.5964,0.604])
# Dogecoin = np.array([0.1403,0.1407,0.1315,0.1298,0.122,0.1318,0.1315,0.1295])
# Toncoin = np.array([7.1431,6.9961,6.8624,6.9247,6.498,6.7235,6.65,6.58])
# Cardano = np.array([0.4387,0.4292,0.4112,0.4084,0.3853,0.415,0.422,0.4069])
#
# bitcoinStd = np.std(Bitcoin)
# ethereumStd = np.std(Ethereum)
# tetherStd = np.std(Tether)
# solanaStd = np.std(Solana)
# bnbStd = np.std(BNB)
# usdcStd = np.std(USDC)
# xrpStd = np.std(XRP)
# dogecoinStd = np.std(Dogecoin)
# toncoinStd = np.std(Toncoin)
# cardanoStd = np.std(Cardano)
#
# cryptCoinSTDs = [bitcoinStd,ethereumStd,tetherStd,solanaStd,bnbStd,usdcStd,xrpStd,dogecoinStd,toncoinStd,cardanoStd]
# cryptCurrencies = ["Bitcoin","Ethereum","Tether","Solana","BNB","USDC","XRP","Dogecoin","Toncoin","Cardano"]
#
# mostStableSTD = min(cryptCoinSTDs)
# print(f"The most stable cryptocurreny is {cryptCurrencies[cryptCoinSTDs.index(mostStableSTD)]}, which has the STD of {mostStableSTD}")


#------------------------------------------------------DataFrames by Pandas------------------------------------------

# import pandas as pd
# import numpy as np
#
# Cost_of_living = np.array(
#     [
#         ["Colombo, Sri Lanka", 35.0, 7.5, 52.4],
#         ["Tehran, Iran", 27.9, 12.6, 24.3],
#         ["Mumbai, India", 26.6, 18.2, 26.0],
#         ["Gurgaon, India", 25.4, 8.4, 28.4],
#         ["Kathmandu, Nepal", 25.2, 4.5, 26.6],
#         ["Bangalore, India", 25.0, 9.1, 29.2],
#         ["Dhaka, Bangladesh", 23.8, 3.4, 29.3],
#         ["Delhi, India", 23.5, 7.5, 25.0],
#         ["Pune, India", 23.5, 6.5, 25.9],
#         ["Noida, India", 23.2, 5.4, 25.8]
#     ]
# )
# indexArr = list(range(1,11))
#
# COL_dataframe = pd.DataFrame(Cost_of_living,columns=["City","Cost of Living Index","Rent Index","Groceries Index"],index=[indexArr])
#
# COL_dataframe.to_excel("Cost of Living.xlsx")
#
# dataFrameImported = pd.read_excel("Cost of Living.xlsx")
# print(dataFrameImported)


# ----------------------------------------------------PANDAS INFO, HEAD, TAIL AND DESCRIBE------------------------------------

# import pandas as pd
# import numpy as np
#
# covidCases = np.array(
#     [
#         ["USA", "111,820,082", "1,219,487", "109,814,428"],
#         ["India", "45,035,393", "533,570", "N/A"],
#         ["France", "40,138,560", "167,642", "39,970,918"],
#         ["Germany", "38,828,995", "183,027", "38,240,600"],
#         ["Brazil", "38,743,918", "711,380", "36,249,161"],
#         ["S. Korea", "34,571,873", "35,934", "34,535,939"],
#         ["Japan", "33,803,572", "74,694", "N/A"],
#         ["Italy", "26,723,249", "196,487", "26,361,218"],
#         ["UK", "24,910,387", "232,112", "24,678,275"],
#         ["Russia", "24,124,215", "402,756", "23,545,818"]
#     ]
# )
#
# indexArr = list(range(1,11))
#
# CC_dataframe = pd.DataFrame(covidCases,columns=["Country, Other","Total Cases","Total Deaths","Total Recovered"],index=indexArr)
#
# print("Head:",CC_dataframe.head())
# print("Tail:",CC_dataframe.tail())
# print("Info:",CC_dataframe.info())
# print("Describe:",CC_dataframe.describe())
#
# activeCases = ["786,167","N/A","0","405,368","1,783,377","0","N/A","165,544","0","175,641"]
#
# CC_dataframe['Active Cases'] = activeCases
# CC_dataframe.drop("Total Recovered",axis=1, inplace=True)
#
# print("Info After Changes:",CC_dataframe.info())


# ------------------------------------------- NULL VALUES IN DATAFRAMES --------------------------------------------

# import pandas as pd
# import numpy as np
#
#
# sampleData = pd.DataFrame(
#     [
#         [20,43,56,np.nan,76,34],
#         [np.nan, 99, 20, 63, 13, 26],
#         [57, 10, 74, 14, 55, 33],
#         [80, 11, 91, 36, np.nan, 98],
#         [18, np.nan, 38, np.nan, 54, 83]
#
#     ]
# ,columns=[1,2,3,4,5,6])
#
# sampleDataFillWithZero = sampleData.fillna(0)
# sampleDataFillWithMean = sampleData.fillna(sampleData.mean())
# sampleDataFillWithMedian = sampleData.fillna(sampleData.median())
# sampleDataFillWithLowerVal = sampleData.fillna(method="bfill")
# sampleDataFillWithForVal = sampleData.fillna(method="ffill")
#
#
# print(sampleData)
# print(sampleDataFillWithZero)
# print(sampleDataFillWithMean)
# print(sampleDataFillWithMedian)
# print(sampleDataFillWithLowerVal)
# print(sampleDataFillWithForVal)


# -----------------------------------------DATA FILTRATION------------------------------------------------

# import pandas as pd
#
# sampleDict = data = {
#
#     "Names": ["Alice", "Bob", "Charlie","Candace", "David", "Eve", "Frank"],
#     "Age": [32, 45, 51, 34 , 37, 43, 58],
#     "Salaries": [2500, 4000, 3200, 4200 , 2900, 4700, 3100],
#     "Occupation": ["Engineer", "Doctor", "Artist", "Surgeon" , "Teacher", "Lawyer", "Scientist"]
#
# }
#
# sampleDF = pd.DataFrame(sampleDict)
#
# specificName = sampleDF[sampleDF["Names"] == "Charlie"]
# specificNames = sampleDF[sampleDF["Names"].isin(["Bob","Eve"])]
# startsWith = sampleDF[sampleDF["Names"].str.startswith("C")]
#
# print(specificName)
# print(specificNames)
# print(startsWith)

# ----------------------------------------DATAFRAME SUMMARY------------------------------------------------------

# import pandas as pd
#
# companyData = {
#
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
#     "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
#     "Salary": [12000, 18000, 15000, 20000, 25000, 16000],
#     "Bonus": [5000, 3000, 1500, 2500, 4000, 3000]
#
# }
#
# companyDF = pd.DataFrame(companyData)
#
# totalDeptSal = companyDF.groupby("Department").agg({"Salary":"sum"})
# sameDept = companyDF.groupby("Department").agg({"Name":"count"})
# totalSalandBon = companyDF.groupby("Department").agg({
#     "Salary":["sum","mean"],
#     "Bonus":["sum","mean"]
# })
#
# print(companyDF)
#
# print(totalDeptSal)
# print(sameDept)
# print(totalSalandBon)


# ------------------------------------------PIVOT TABLES 1 ---------------------------------------------------------

# import pandas as pd
#
# data = {
#     'Roles':["Intern","Manager","Senior Manager","Prod Manager","Senior Manager","Intern","Manager","Prod Manager"],
#     'Branch':["North","North","South","East","West","West","South","East"],
#     'Quarter':["Q1","Q3","Q4","Q2","Q2","Q1","Q3","Q4"],
#     'Expenses':[1000,2200,950,1500,3000,2500,2000,1350],
#     'ProfitsMade':[14000,10000,5000,6423,1000,30021,22302,42203]
# }
#
# dataFrame = pd.DataFrame(data)
#
# pivotTable = dataFrame.pivot_table(values=["ProfitsMade","Expenses"], index=["Roles"], aggfunc='sum', fill_value=0)
#
# print(dataFrame)
# print(pivotTable)

# ------------------------------------------PIVOT TABLES 2----------------------------------------------------------

# import pandas as pd
#
# data = {
#     'Product': ['Laptop', 'Laptop', 'Smartphone', 'Smartphone', 'Tablet', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet'],
#     'Store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B', 'Store C', 'Store C', 'Store C', 'Store D', 'Store D', 'Store D'],
#     'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2024, 2024],
#     'Sales': [300, 400, 500, 450, 250, 350, 320, 480, 260, 330, 510, 370],
#     'Profit': [50, 70, 80, 60, 40, 50, 55, 75, 45, 60, 85, 65]
# }
#
# dataFrame = pd.DataFrame(data)
#
# pivotTableProd = dataFrame.pivot_table(values=["Sales","Profit"],index="Product",aggfunc='sum',fill_value='mean')
# pivotTableStore = dataFrame.pivot_table(values=["Sales","Profit"],index="Store",aggfunc='sum',fill_value='mean')
# pivotTableYear = dataFrame.pivot_table(values=["Sales","Profit"],index="Year",aggfunc='sum',fill_value='mean')
#
# print(f"Sales and Profits of Products: \n {pivotTableProd}")
# print(f"Sales and Profits of Stores: \n {pivotTableStore}")
# print(f"Sales and Profits of Year: \n {pivotTableYear}")


# ====================================================matplotlib LIBRARY========================================================

# --------------------------------------------------Making Graphs in Python-----------------------------------------------------

# import matplotlib.pyplot as mplp
#
# x = list(range(1,11))
# y = list(range(2,21,2))
#
# mplp.plot(x,y, marker="x", color="purple", linestyle="dotted")
# mplp.grid()
# mplp.title("How different forces affect elasticity")
# mplp.xlabel("Force")
# mplp.ylabel("Elasticity")
#
# mplp.show()


# ------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as mplp
#
# data = {
#     "Date":["1/10/2024","2/10/2024","2/10/2024","3/10/2024","3/10/2024"],
#     "Store Branch":["Karachi","Lahore","Islamabad","Hyderabad","Peshawar"],
#     "Product":["Pencil Case","Pencil","Cardboard","Pen","Lunch Box"],
#     "Sales":[4500,20000,2000,25000,10000],
#     "Profit":[9000,40000,4000,50000,20000]
# }
#
# dataFrame = pd.DataFrame(data)
#
# pivotTable = dataFrame.pivot_table(values=["Sales","Profit"],index="Date",aggfunc="sum")
#
# pivotTable.plot(marker="x")
# mplp.grid()
#
# mplp.show()


# ---------------------------------------------------SCATTER GRAPHS------------------------------------------------------------
#
# import matplotlib.pyplot as mplp
# import pandas as pd
#
# studentData = {
#     'StudentID':list(range(1101,1111)),
#     'StudyHRS':[4,2,1,6,4,7,3,9,1,5],
#     'ExamScores':[69,51,24,79,71,85,60,97,20,50]
# }
#
# SDdataframe = pd.DataFrame(studentData)
#
# mplp.scatter(SDdataframe["StudyHRS"],SDdataframe["ExamScores"],color="red")
# mplp.title("How Exam Scores differ with Study Hours")
# mplp.xlabel("Study Hours")
# mplp.ylabel("Exam Scores")
# mplp.grid()
#
# mplp.show()


#------------------------------------------------BAR GRAPHS------------------------------------------------------------------

# import matplotlib.pyplot as mplp
# import pandas as pd
#
# storeData = {
#     'Item':["Monitors","CPUs","Keyboards","Mouse","Headphones","SmartWatches","TVs","Consoles"],
#     'Sales':[24000,15000,30000,32000,41000,13000,39000,20000]
# }
#
# sdDataFrame = pd.DataFrame(storeData)
#
# mplp.bar(sdDataFrame["Item"],sdDataFrame["Sales"], color="blue")
# mplp.title("Sales of different items")
# mplp.xlabel("Items")
# mplp.ylabel("Sales")
# mplp.grid()

# mplp.show()


# ---------------------------------------------------PIE CHARTS----------------------------------------------------------------

# import matplotlib.pyplot as mplp
# import pandas as pd
#
# smartphoneData = {
#     'SmartphoneBrand':["Samsung","Apple","Xiaomi","Oppo","Vivo","Others"],
#     'MarketShare':[36.96,32.78,11.8,5.88,5.42,7.43]
# }
#
# smartphoneDataFrame = pd.DataFrame(smartphoneData)
#
# mplp.pie(smartphoneDataFrame["MarketShare"],labels=smartphoneDataFrame["SmartphoneBrand"])
# mplp.title("MarketShare of different smartphone brands")
#
# mplp.show()


# --------------------------------------------------HISTOGRAMS------------------------------------------------------------------

# import matplotlib.pyplot as mplp
# import pandas as pd
#
# employeeData = {
#     "Age": [32, 35, 38, 41, 45, 48, 52, 55, 57, 60],
#     "Salary": [15000, 18000, 21000, 24000, 28000, 32000, 35000, 40000, 45000, 48000]
# }
#
# employeeDataFrame = pd.DataFrame(employeeData)
#
# mplp.hist(employeeDataFrame["Age"],bins=6,color="blue",edgecolor="black")
# mplp.title("Spreading of Age")
# mplp.xlabel("Age")
# mplp.ylabel("Frequency")
# mplp.show()


# ---------------------------------------------------------------------------------------------------------------------------
#
# import matplotlib.pyplot as mplp
# import pandas as pd
#
#
# storeData = {
#     "Product":["Laptop","CPUs","Monitors","Keyboards","Mouse","Earphones"],
#     "Price":[25000,35000,10000,5000,3500,6000],
#     "UnitsSold":[200,304,250,478,699,948],
#     "CustomerRating":[3.8,3.5,4.0,4.7,4.9,4.2],
#     "Region":["North","South","East","North","West","East"]
# }
#
# storeDataFrame = pd.DataFrame(storeData)
#
# pivot = storeDataFrame.pivot_table(values=["UnitsSold"],index="Region",aggfunc="sum")
#
# print(pivot)
#
#
# mplp.plot(storeDataFrame["Price"],storeDataFrame["CustomerRating"],marker="x")
# mplp.grid()
# mplp.xlabel("ProductPrice")
# mplp.ylabel("Rating")
# mplp.title("Relation of product prizes and customer ratings")
#
# mplp.show()

# --------------------------------------------------------------------------------------------------------------------------------

# ================================================BEAUTIFUL SOUP==================================================================

# from bs4 import BeautifulSoup
# import requests
#
# url = "https://www.imdb.com/chart/top/"
# openWeb = requests.get(url)
# openWebText = openWeb.text
# print(openWeb.text)
# webFind = BeautifulSoup(openWebText,"html.parser")
# # tagFindAll = webFind.find_all("img")
# #
# # for index in tagFindAll:
# #     print(index)


# ---------------------------------------------FINDING ELEMENTS IN A SITE USING TAGS----------------------------------------------

# from bs4 import BeautifulSoup as bs
# import requests as rq
# import pandas as pd
#
# url = "https://www.numbeo.com/property-investment/rankings_current.jsp"
# openWeb = rq.get(url).text
# webFind = bs(openWeb,"html.parser")
# all_tables = webFind.select("#t2 tbody tr")
# mainData = []
#
# for table in all_tables:
#     all_td = table.find_all("td")
#     allDataList = []
#     for td in all_td:
#         allDataList.append(td.getText())
#     mainData.append(allDataList)
#
# all_th = webFind.select('#t2 thead tr th')
# headings = []
# for th in all_th:
#     headings.append(th.text)
#
# dataFrame = pd.DataFrame(mainData,columns=headings,index=list(range(1,302)))
#
# print(dataFrame)


# ---------------------------------------------TASK: MAKE A DATAFRAME FROM COVID WEBSITE--------------------------------------

from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
openWeb = rq.get(url).text
webFind = bs(openWeb,"html.parser")
all_tables = webFind.select("#main_table_countries_today tbody tr")
mainData = []

for table in all_tables:
    count = 0
    # print(table)
    all_td = table.find_all("td")
    allDataList = []
    # print(all_td)
    for td in all_td:
        allDataList.append(td.getText())
    mainData.append(allDataList)

mainDataSliced = []
for index in range(len(mainData)):
    if (index >= 7 and index <= 238) or index == len(mainData)-1:
        mainDataSliced.append(mainData[index])



all_th = webFind.select('#main_table_countries_today thead tr th')

headings = []
for th in all_th:
    headings.append(th.text)

dataFrame = pd.DataFrame(mainDataSliced,columns=headings)

print(dataFrame)
# for temp in headings:
#     print(temp)