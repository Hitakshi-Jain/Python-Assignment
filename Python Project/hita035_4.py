# To convert dd/mm/yyyy to dd-mm-yyyy

#Taking the date in dd/mm/yyyy format as input
date = input("Enter the date: ")

#Coverting in dd-mm-yyyy format
given_date = date.replace("/", "")
formatted_date = given_date[:2] + "-" + given_date[2:4] + "-" + given_date[4:]

# Printing the date in dd-mm-yyyy format
print(f"Date in dd-mm-yyyy format: {formatted_date}")











