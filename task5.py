# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
# rəqəmlər yoxdursa -1 cavabı qaytarın. 

class Numbers:
    
    def method1(self, mylist : list):
        self.mylist = mylist
        
    def method2(self, number: int):
        for number1 in self.mylist:
            for number2 in self.mylist[1:]:
                if number1 + number2 ==number:
                    index1 =self.mylist.index(number1)
                    index2 =self.mylist.index(number2)
                    return index1, index2
        
        return -1        
    
 
            
            
obj = Numbers()
obj.method1([6, 1, 2, 3, 4, 5])
results = obj.method2(int(input('Rəqəm daxil edin:')))
print(results)
    
        
        


        