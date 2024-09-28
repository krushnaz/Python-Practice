class VotingException (Exception):
    pass

def checkEligibility(age) :
    if age <= 18 :
        raise VotingException("You are not eligible for voting")
    else :
        print("you are eligible for voting")
    
try :
    age = int(input("enter age :"))
    checkEligibility(age)

except Exception as ve :
    print(ve)
   

