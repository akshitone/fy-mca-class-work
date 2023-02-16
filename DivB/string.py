# string: ordered, ____, text representation

# init
from timeit import default_timer as timer
movie_name = "The murder on the orient express"

# single quote
fav_quote = 'That\'s what she said'
# print(fav_quote)

# double quote
fav_quote = "That's what she said"
# print(fav_quote)

quote = "Where should I go? \
To the left where nothing is right \
or to the right where nothing is left."
# print(quote)

# triple quote

quote = """Where should I go? 
To the left where nothing is right 
or to the right where nothing is left."""
# print(quote)

# indexing
movie_name = "The murder on the orient express"


# reverse string
# print(movie_name[::-1])

# slicing
# print(movie_name[4:10])
# print(movie_name[11:17])
# print(movie_name[-4])
# print(movie_name[9:3:-1])

# concate
greetings = "Good morning"
student_name = "John"

greetings = greetings + " " + student_name
# print(greetings)

# interation
# for char in student_name:
#     if char == 'o':
#         print("o in name")
#     else:
#         print("o not in name")

# print(char)

# check
# if 'o' in student_name:
#     print('o in name')
# else:
#     print('o not in name')

# white space
hello = "     hello     "
# print(hello.strip())

# upper lower
# print(hello.upper())
upper_hello = "HELLO"
# print(upper_hello.lower())

# startswith
akshit_email = "akshit.mithaiwala@techbulls.in"
aditya_name = "techbullsaditya"
anushka_name = "techbullsanushka"

# print(anushka_name.startswith("techbulls"))

# domain_name = [".com", ".in"]

# print(akshit_email.endswith(".com"))

# find
akshit_name = "akshit"
# print(akshit_name.find('s'))

# SHIT
s_index = akshit_name.find('s')
shit_name = akshit_name[s_index:]
upper_shit = shit_name.upper()
# print(upper_shit)
# print(akshit_name[akshit_name.find('s'):].upper())

# count
series_name = "The Woman in the House Across the Street from the Girl in the Window"
# print(series_name.count('the'))

# replace
# series_name = series_name.replace('the', 'anything')
# print(series_name)

# split
series_name_list = series_name.split(" ")
# print(series_name_list)

# join
series_name_join_with_comma = ",".join(series_name_list)
# print(series_name_join_with_comma)

# print(series_name.replace(" ", ","))

number_of_a = ['a'] * 100

# print(number_of_a)

# 01
start = timer()
a_join = "".join(number_of_a)
end = timer()

print(end-start)

# 02
start = timer()
a_join_using_loop = ""
for char_a in number_of_a:
    a_join_using_loop += char_a
end = timer()

print(end-start)


# print(a_join)
# print(a_join_using_loop)


# % .format() f-string

name = "akshit"
greetings = "Good morning"
student_roll_no = 123

print(f"{greetings}, this is my name: {name} roll no: {student_roll_no}")

# print("{} yello {}".format(greetings, name))

# print(greetings + " " + name + " " + str(student_roll_no))
# print(1+student_roll_no)
