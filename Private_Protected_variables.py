class PrivateVariable:
    def privateVariable(self, x, y):
        self.__data1 = x #--> Private Variable
        self._data2 = y #--> Protected Variable
        #This can print the value of __data1
        print(self.__data1)
        
#Inherting PrivateVariable
class PrivateVariableNew(PrivateVariable): 
    def callingClassPrivateVariable(self):
        pass

obj1 = PrivateVariable()
#print(obj1.__data1) #--> This will throw an error
obj2 = PrivateVariableNew()
#--> Passing arguments to the method privateVariable
obj2.privateVariable(10,14) 
print(obj2._data2) #--> This will return 14