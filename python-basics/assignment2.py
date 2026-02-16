#Name :Cyril Baraka
#Date :12/02/2025
#String formatting

#Get string length
sentence = "I watch anime"

string_length=len(sentence)

print(f"The length of the string is : {string_length}")

#Splitting a string
sentence_2 ="Mathematics Physics"
split=sentence_2.split(" ")

print(f"the first subject is :",split[0])

print(f"the second subject is ",split[1])

#Make everything CAPITALIZED

code_mpesa ="uu78y88ugu"

capitalized =code_mpesa.upper()

print(f"capitalized mpesa code:",capitalized)

small_letters=capitalized.lower()
print(f"Capitalized code in small letters:",small_letters)

#Replacement of characters in a string

balance="1000KES"
amount_deposited ="250KES"

cleaned_balance =balance.replace("KES","")

print("Cleaned balance: ",cleaned_balance)

cleaned_amount_deposited =amount_deposited.replace("KES","")

print("Cleaned amount added:" ,cleaned_amount_deposited)

final_balance=int(cleaned_balance)+float(cleaned_amount_deposited)

print(f"The final balance is:",final_balance)

print(f"{capitalized} CONFIRMED You have Received {amount_deposited} from James Onyango New Balance is {final_balance}")

#ASSIGNMENT
balance="12.02KES"
amount_deposited ="40KES"

cleaned_balance =balance.replace("KES","")

print("Cleaned balance: ",cleaned_balance)

cleaned_amount_deposited =amount_deposited.replace("KES","")

print("Cleaned amount added:" ,cleaned_amount_deposited)

final_balance=float(cleaned_balance)+float(cleaned_amount_deposited)

print(f"The final balance is:",final_balance)

print(f"{capitalized} CONFIRMED You have Received {amount_deposited} from James Onyango New Balance is {final_balance}")

