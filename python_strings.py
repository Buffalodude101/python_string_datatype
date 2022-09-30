# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
first_name = 'Hayden'
#   - my_last_name
#       -set this equal to your last name
last_name = 'Hart'
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
birth_year = 1999
#   - current_year
#       -set this equal to 2020
current_year = 2022




# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)
# print(first_name)
# print(last_name)
# print(first_name[0])
# print(last_name[-3])
# print(first_name[0 : 2])
# print(last_name[ -2: ])


#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
# print(first_name, last_name)
# #       -first name six times
# print((first_name + '\n')* 6)




# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
birth_year_statement = (f"{first_name} {last_name} was born in {birth_year}")
print(birth_year_statement)

birth_year_celebration = (f"{birth_year_statement}. {first_name} enjoyed celebrating {current_year}. ")
print(birth_year_celebration)

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year
escape_ex = f"{first_name}'s birth year is {birth_year}"
print(escape_ex)

tab_ex = f"\t{last_name} {current_year}"
print(tab_ex)
# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case
print(f"{first_name.casefold()} {last_name.casefold()}")
print(len(last_name))
print(f"{first_name.upper()} {last_name.upper()}")