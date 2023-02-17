# string: ordered, ____, text representation

# init
series_name = "The Woman in the House Across the Street from the Girl in the Window"
# print(series_name)

# single quote
fav_quote = 'That\'s what she said'
# print(fav_quote)

# double quote
fav_quote = "That's what she said"
# print(fav_quote)

# triple quote
quote = """Where should I go?
To the left where nothing is right or
to the right where nothing is left."""
# print(quote)

web_series = ["GOT", "HIMYM", "Suits", "Friends", "You", "Elite"]

reversed_web_series = list()
# print(web_series[2:5])
for series in web_series[3:0:-1]:
    reversed_web_series.append(series[::-1])

# print(reversed_web_series)

# indexing
fav_quote = "That's what she said"


# reverse string
# print(fav_quote[::-1])

# slicing
# print(fav_quote[-1])
# print(fav_quote[7:15])
# print(fav_quote[10:6:-1])

# concate
greeting = "Good morning, "
name = "John Doe"

greeting = greeting + name
# print(greeting)

# interation
# for char in name:
#     print(char)

# check
# print("mornning" in greeting)

# white space
hello = "     hello"
# print(hello)

# upper lower
# print(hello.upper())

username = "aKsHItOnE"
# print(username.lower())

# startswith
akshit_email = "akshit.mithaiwala"

aditya_name = "techbullsaditya"
anushka_name = "techbullsanushka"

# print(aditya_name.startswith("techbulls"))

# print(akshit_email.endswith("techbulls.com"))

# find
akshit_name = "mihaiwalaakshitdasdasfaf"

# SHIT
s_index = akshit_name.find("s")
t_index = akshit_name.find("t")
# print(s_index)
splited_name = akshit_name[s_index:t_index+1]
# print(splited_name)
upper_splited_name = splited_name.upper()
# print(upper_splited_name)

# count
series_name = "The Woman in the House Across the Street from the Girl in the Window"
# print(series_name.count("The"))

# replace
# series_name = series_name.replace("the", "anything")
# print(series_name)

# split
# print(series_name)
splited_string_list = series_name.split()
# print(splited_string_list)

# join
joining_list = ", ".join(splited_string_list)
# print(joining_list)

a_list = ['a'] * 10
print(a_list)

# 01 Method
a_string = "".join(a_list)
print(a_string)

# 02 Method
a_string_2 = ""

for a_char in a_list:
    a_string_2 += a_char

print(a_string_2)

# % .format() f-string
greeting = "Good morning,"
name = "John Doe"

print(greeting + " " + name)
print("{} whatever {} adasd".format(greeting, name))
print(f"{greeting} adasdsa {name} asdasd {10+20}")
