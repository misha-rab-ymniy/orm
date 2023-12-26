from datetime import datetime

from Entities import Film, User, FilmGenres, Genre, Schedule, Hall, Cinema, AvailableSeat, Seat, Ticket, Review


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
            print(f"Film Id: {film.film_id}")
            print(f"{film.title}, {film.release_date}, {film.country}")
            print(f"{film.duration}, {film.rating}")
            print(f'{film.description}')
            print(f"Genres: ")
            genres = FilmGenres().select(columns=("genre_id",), condition=f"film_id = {film.film_id}")
            for genre in genres:
                genre_name = Genre().select(columns=("name",), condition=f"genres_id = '{genre[0]}'")[0][0]
                print(f"{genre_name}")
            schedule = Schedule().select(condition=f"film_id = '{film.film_id}'")
            print("Sessions:")
            for sched in schedule:
                print("---------------------------")
                print(f"Schedule Id: {sched.schedule_id}")
                print(f"Start: {sched.start_time}")
                print(f"Price: {sched.value}")
                hall = Hall().select(condition=f"hall_id = '{sched.hall_id}'")[0]
                print(f"Hall name: {hall.hall_name}")
                cinema = Cinema().select(condition=f"cinema_id = '{hall.cinema_id}'")[0]
                print(f"Cinema name: {cinema.name}")
                print(f"Cinema location: {cinema.location}")
                print("---------------------------")
            print("Reviews: ")
            reviews = Review().select(condition=f"film_id = '{film.film_id}'")
            for review in reviews:
                user = User().select(condition=f"user_id = '{review.user_id}'")[0]
                print(f"{user.first_name}: {review.text}")
            print("--------------------------------------------------------------------------------------------------")

    def took_place(self):
        if self._user.is_logged():
            print("Do you want to choose a place? (y/n)")
            choice = input()
            if choice == "y":
                print("Enter an Id of Schedule")
                schedule_id = int(input())
                available_seats = AvailableSeat().select(
                    condition=f"schedule_id = '{schedule_id}' AND available = True")
                for available_seat in available_seats:
                    seat = Seat().select(condition=f"seat_id = '{available_seat.seat_id}'")[0]
                    print(
                        f"Seat id: {available_seat.available_seat_id}, Seat number: {seat.seat_number}, Row number: {seat.row_number}, Available: {available_seat.available}")
                print("Enter Id of Seat to take a ticket")
                seat_id = int(input())
                values = []
                values.append(self._user.user_id)
                values.append(datetime.now().date().strftime("%Y-%m-%d"))
                values.append(schedule_id)
                values.append(seat_id)
                Ticket().insert(tuple(values))

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
            film_id = Film().select(columns=("film_id",), condition=f"title = '{values[0]}'")[0][0]
            for genre in genres:
                genre_id = Genre().select(columns=("genres_id",), condition=f"name = '{genre}'")[0][0]
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
