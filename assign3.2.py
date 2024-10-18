def generateSentence1(list1,num1,str1): 
      
    if num1==0:
        print(str1)
        return
    for element in list1:
        generateSentence1(list1, num1-1 ,str1+element)

        
#example

list1=["a","b","c"]
num1=2
generateSentence1(list1,num1,"")
