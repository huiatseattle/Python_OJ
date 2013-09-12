class ExcelNumber:
    #????????excel?,decNum???,????????
    def decToExcel(self, decNum):
        result=''
        while decNum:
            temp=decNum%26
            if not temp:
                decNum-=26
                decNum=decNum/26
                c='Z'
            else:
                decNum=decNum/26
                c=chr(temp+64)
            result=c+result
            
        return result

    #?excel????????,excelNum????,???????
    def excelToDec(self, excelNum):
        l=len(excelNum)
        if l<=0:
            return 0
        i=0
        result=0
        temp=0
        while i<l:
            temp=ord(excelNum[i])-64
            result=result*26+temp
            i+=1
        return result