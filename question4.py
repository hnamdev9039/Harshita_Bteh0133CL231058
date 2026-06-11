class underageerror(Exception):
     pass
class invalidageerror(Exception):
     pass      

class AgeVerification:
    def set_age(self,age):
        
            try:
                if age<0:
                     raise ValueError("age cannot be negative")
                elif age<18:
                     raise "invalid age"
                elif age<100:
                     raise("not define")

                else:
                     print("valid age")
            except ValueError as e:
                 print(e)
obj=AgeVerification()
obj.set_age(int(input("enter age")))

                     
            
            