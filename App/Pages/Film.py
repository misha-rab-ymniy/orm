from Entities import Film, User, FilmGenres, Genre, Schedule


class FilmPage:
    _user: User
    _films: list[Film]

    def __init__(self, user: User = User()):
        self._user = user
        self._films = Film().select()

    def film_list(self):
        print("Film list:")
        for film in self._films:
            print("--------------------------------------------------------------------------------------------------")
            if self._user.is_admin():
                print(f"Id: {film.film_id}")
            print(f"{film.title}, {film.release_date}, {film.country}")
            print(f"{film.duration}, {film.rating}")
            print(f'{film.description}')
            print(f"Genres: ")
            genres = FilmGenres().select(columns=("genre_id", ), condition=f"film_id = {film.film_id}")
            for genre in genres:
                genre_name = Genre().select(columns=("name", ), condition=f"genres_id = '{genre[0]}'")[0][0]
                print(f"{genre_name}")
            schedule = Schedule().select(condition=f"film_id = '{film.film_id}'")
            print("Sessions:")
            for sched in schedule:
                print(sched)
            print("--------------------------------------------------------------------------------------------------")

    def film_change(self):
        print("Do you want to insert/update/delete or nothing the film (1/2/3)?")
        choice = input()
        if choice == "1":
            values = []
            print("Enter title of the film")
            values.append(input())
            print("Enter release_date of the film")
            values.append(input())
            print("Enter country of the film")
            values.append(input())
            print("Enter duration of the film")
            values.append(input())
            print("Enter description of the film")
            values.append(input())
            print("Enter rating of the film")
            values.append(input())
            print("Enter genres of the film with a space")
            genres = input().split(" ")
            Film().insert(tuple(values))
            film_id = Film().select(columns=("film_id", ), condition=f"title = '{values[0]}'")[0][0]
            for genre in genres:
                genre_id = Genre().select(columns=("genres_id", ), condition=f"name = '{genre}'")[0][0]
                FilmGenres().insert((genre_id, film_id))
            self._films = Film().select()
            self.film_list()
        elif choice == "2":
            print("Enter id of film you want to update")
            film_id = int(input())
            print("Enter attribute you want to update")
            attribute = input()
            print("Enter value:")
            value = input()
            Film().update({attribute: value}, f"film_id = '{film_id}'")
            self._films = Film().select()
            self.film_list()
        elif choice == "3":
            print("Enter id of film you want to delete")
            film_id = int(input())
            Film().delete(condition=f"film_id = '{film_id}'")
            self._films = Film().select()
            self.film_list()
