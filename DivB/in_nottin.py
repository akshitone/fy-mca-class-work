print("How you doing?")

artists = ["Post Malone", "Taylor Swift", "Drake", "MC Stan", "Raga"]

# is_mc_stan = False

for artist in artists:
    if artist == "Drake":
        is_mc_stan = True
        break

# print(is_mc_stan)

artist_name = "Divine"
new_artist_name = "MC"

print(artist_name is not new_artist_name)
