# Write your solution here:
class Series():
    def __init__(self, title: str, season: int, type: list):
        self.title = title
        self.name = title
        self.season = season
        self.type = type
        self.rate_list = []
        self.count = 0
    
    def __str__(self) -> str:
        str_series = ""
        str_series += f"{self.name} ({self.season} seasons)\n"
        str_series += f"genres: " + ", ".join(self.type) + "\n"
        if len(self.rate_list) == 0:
            str_series += "no ratings"
        else:
            str_series += f"{len(self.rate_list)} ratings, average {(sum(self.rate_list)/len(self.rate_list)):.1f} points"
        return str_series
    
    def rate(self, rating: int):
        self.rate_list.append(rating)


def minimum_grade(rating: float, series_list: list):
    s = []
    for movie in series_list:
        if min(movie.rate_list) >= rating:
            s.append(movie)
    return s

def includes_genre(genre: str, series_list: list):
    g = []
    for movie in series_list:
        if genre in movie.type:
            g.append(movie)
    return g

if __name__=="__main__":    
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.name)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.name)
