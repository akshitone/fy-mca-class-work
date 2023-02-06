# Sets: unordered, mutable, no duplicates

# initialize 01
movies = {"50 shades of grey", "365", "The dictator", "Borat"}
# print(movies)

# initialize 02
web_series = set(["Suits", "Lucifer", "Dark", "Friends"])
# print(web_series)

# empty
# web_series = set()
# print(type(web_series))

# string initialize
hello_set = set("Hello")
# print(hello_set)

# insert value
web_series.add("The 100")
# web_series.add("Friend")
# print(web_series)

# delete value
# web_series.remove("Darkk")

# web_series.discard("Dark")

# clear all values
# web_series.clear()
# print(web_series)

web_series = movies.copy()

movies.add("Ready player one")

# print(web_series)

# union
gangs_of_wasseypur = {"Pankaj T", "Rajkumar R", "Nawazuddin S", "Huma Q"}
mirzapur = {"Pankaj T", "Ali Fazal", "Divyenndu", "Huma Q"}

# anurag_cast = gangs_of_wasseypur.union(mirzapur)

# print(anurag_cast)

# # intersection
# anurag_cast = gangs_of_wasseypur.intersection(mirzapur)
# print(anurag_cast)

# difference
anurag_cast = gangs_of_wasseypur.difference(mirzapur)
# print(anurag_cast)

# gangs_of_wasseypur = ["Pankaj T", "Rajkumar R", "Nawazuddin S", "Huma Q"]
# mirzapur = ["Pankaj T", "Ali Fazal", "Divyenndu", "Huma Q"]
# # anurag_cast = list()

# output = ["Rajkumar R", "Nawazuddin S", "Ali Fazal", "Divyenndu"]

# for cast in gangs_of_wasseypur:
#     if cast not in mirzapur:
#         anurag_cast.append(cast)

# anurag_cast = [cast for cast in gangs_of_wasseypur if cast not in mirzapur]

# print(anurag_cast)

# symmetric difference
anurag_cast = gangs_of_wasseypur.symmetric_difference(mirzapur)
# print(anurag_cast)

# update
web_series.update(gangs_of_wasseypur)
# print(web_series)

# intersection update
# mirzapur.intersection_update(gangs_of_wasseypur)
# print(mirzapur)

# difference update
# mirzapur.difference_update(gangs_of_wasseypur)
# print(mirzapur)

# symmetric difference update
# mirzapur.symmetric_difference_update(gangs_of_wasseypur)
# print(mirzapur)

# is subset
animated_movies = {"Big Hero 6", "Kung Fu Panda",
                   "Tangled", "Coco", "The Good Dinosaur"}

disney_movies = {"Tangled", "Coco"}

print(disney_movies.issubset(animated_movies))

# is superset
print(animated_movies.issuperset(disney_movies))

# is disjoint
print(animated_movies.isdisjoint(disney_movies))

# frozenset

numbers = frozenset({"a", "b"})
print(numbers)
