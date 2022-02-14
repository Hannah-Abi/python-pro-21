# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_dic = {}
    movie_dic["name"] = name
    movie_dic["director"] = director
    movie_dic["year"] = year
    movie_dic["runtime"] = runtime
    database.append(movie_dic)
if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)