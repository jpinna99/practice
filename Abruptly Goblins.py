# create empty list for gamers
gamers = []

# create function that adds a new gamer to a gamers list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") == None:
        print("Not a valid entry.")
    elif gamer.get("availability") == None:
        print("Not a valid entry.")
    else:
        gamers_list.append(gamer)

# add new gamers to gamers list (gamers)
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# creates template for days of week frequency table
def build_daily_frequency_table():
    days_of_week = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    return days_of_week
count_availability = build_daily_frequency_table()

# function for returning day count of availability for all gamers in gamers list
def calculate_availability(gamers_list, available_frequency):
    days_listed = []
    for gamer in gamers_list:
        days_listed.append(gamer["availability"])
    days_unlisted = []
    for days in days_listed:
        for day in days:
            days_unlisted.append(day)
    for day in days_unlisted:
        available_frequency[day] += 1
    return available_frequency

availability = calculate_availability(gamers, count_availability)


# function returns the day with the highest number of corresponding availability of gamers in gamer list
def find_best_night(availability_table):
    day_counts = []
    for day in availability_table:
        day_counts.append(availability_table[day])
    day_counts.sort()
    for day in availability_table:
        if availability_table[day] == day_counts[-1]:
            return day

game_night = find_best_night(count_availability)

# function returns list of all gamers available on most popular day
def available_on_night(gamers_list, day):
    gamers_available_that_day = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            gamers_available_that_day.append(gamer["name"])
    return gamers_available_that_day

attending_game_night = available_on_night(gamers, game_night)


# string with e-mail template
form_email = "Hello, {}! Just wanted to let you know that {} will be held on {}!"

# function to send out (print) email to gamers who can attend game on game night
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(gamer, game, day))


# create list of everyone unable to attend the most popular night
unable_to_attend_best_night = []
for gamer in gamers:
    if gamer["name"] not in attending_game_night:
        unable_to_attend_best_night.append(gamer)

# build template frequency table for second night
second_night_availability = build_daily_frequency_table()

# fill in second frequency table
second_availability = calculate_availability(unable_to_attend_best_night, second_night_availability)

# find second-best night
second_night = find_best_night(second_availability)

# saves gamers available on second game night to list
available_second_game_night = available_on_night(gamers, second_night)

# sends out email to ALL gamers available on the second night
send_email(available_second_game_night, second_night, "Abruptly Goblins!")