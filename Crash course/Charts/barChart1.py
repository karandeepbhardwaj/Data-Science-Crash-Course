from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-hurl", "casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title("My Favourite movies")
plt.ylabel("# of Academy awards")
plt.xticks(range(len(movies)), movies)

plt.show()