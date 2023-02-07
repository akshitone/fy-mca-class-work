# Sets: unordered, mutable, no duplicates

# initialize 01
movies = {"Phir Hera Pheri", "Dhol", "Chup Chup Ke", "Golmaal"}
# print(movies)
# print(type(movies))

# initialize 02
web_series = set(["Suits", "Friends", "Sex Education", "Elite"])
# print(web_series)

# empty
whatever = set()

# string initialize
hello_set = set("Hello")
# print(hello_set)

# insert value
web_series.add("Manifest")
web_series.add("The 100")

# print(web_series)

# delete value
web_series.remove("Manifest")
# print(web_series)

# clear all values
web_series.clear()
# print(web_series)

# union
gangs_of_wasseypur = {"Pankaj T", "Rajkumar R", "Nawazuddin S", "Huma Q"}
mirzapur = {"Pankaj T", "Ali Fazal", "Divyenndu", "Huma Q"}

anurag_new_movie_cast = gangs_of_wasseypur.union(mirzapur)
# print(anurag_new_movie_cast)


# anurag_new_movie_cast = set(gangs_of_wasseypur+mirzapur)
# print(anurag_new_movie_cast)

# # intersection
# anurag_new_movie_cast = gangs_of_wasseypur.intersection(mirzapur)
# print(anurag_new_movie_cast)


# for cast in gangs_of_wasseypur:
#     if cast in mirzapur and cast not in anurag_new_movie_cast:
#         anurag_new_movie_cast.append(cast)

# print(anurag_new_movie_cast)

# difference
# gangs_of_wasseypur = ["Pankaj T", "Rajkumar R", "Nawazuddin S", "Huma Q"]
# mirzapur = ["Pankaj T", "Ali Fazal", "Divyenndu", "Huma Q"]

anurag_new_movie_cast = gangs_of_wasseypur.difference(mirzapur)
# print(anurag_new_movie_cast)

# symmetric difference
# anurag_new_movie_cast = ["Rajkumar R",
#                          "Nawazuddin S", "Ali Fazal", "Divyenndu"]

anurag_new_movie_cast = gangs_of_wasseypur.symmetric_difference(mirzapur)
# print(anurag_new_movie_cast)

# update
# mirzapur.update(gangs_of_wasseypur)
# print(mirzapur)

# intersection update
# gangs_of_wasseypur.intersection_update(mirzapur)
# print(gangs_of_wasseypur)

# difference update
# gangs_of_wasseypur.difference_update()

# symmetric difference update
# gangs_of_wasseypur.symmetric_difference_update(mirzapur)

# is subset
animated = {"Kung fu panda", "The family guy",
            "Shinchan", "Tangled", "Coco"}

disney_movies = {"Kung fu panda", "Tangled"}

print(disney_movies.issubset(animated))

# is superset
print(disney_movies.issuperset(animated))


# is disjoint
print(gangs_of_wasseypur.isdisjoint(animated))

# frozenset
frozen_set = frozenset([1, 2, 3, 2, 4, 5, 1])
print(frozen_set)
