# sf_population, sf_area = 864816, 231.89
# rio_population, rio_area = 6453682, 486.5

# san_francisco_pop_density = sf_population / sf_area
# rio_de_janeiro_pop_density = rio_population / rio_area

# # Write code that prints True if San Francisco is denser than Rio, and False otherwise

# san_francisco_pop_density = 864816 / 231.89
# rio_de_janeiro_pop_density = 6453682 / 486.5

# if (san_francisco_pop_density > rio_de_janeiro_pop_density):
#   print(True)
# else:
#   print(False)

# #string
# that_string = "Simon\'s swimming clothes is in the pool side"
# print(that_string)

# first_word = 'Hello'
# second_word = 'There'
# print(first_word + second_word)
# #HelloThere

# print(first_word + ' ' + second_word)

# #Hello There

# print(first_word * 5)

# #HelloHelloHelloHelloHello

# print(len(first_word))

# #5

#type-type conversion
# house_number = "13"
# street_name = "The Crescent"
# town_home = "Belmont"
# print(type(house_number)) # <class 'int'="">

# address = str(house_number + "  " + street_name + ", " + town_home)
# print(address) # 13 The Crescent, Belmont

#exercise

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(
    thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!

weekly_sales = str(weekly_sales)

print("This week\'s total sales" + " " + weekly_sales)
