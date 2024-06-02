import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    port=3307,  # Use port 3307 if MySQL is running on this port
    user="raz",
    password="123456",
    database="DMD_users"
)

cursor = db.cursor()

# Define the Person class with database integration
class Person:
    def __init__(self, firstname: str, lastname: str, ID: int, phone_number: str, full_address: str, gender: str):
        self.firstname = firstname
        self.lastname = lastname
        self.name = f'{self.firstname} {self.lastname}'
        self.gender = gender
        self.phone_number = phone_number
        self.full_address = full_address
        self.ID = ID
        self.city = full_address.split()[-1]
        self.hobbies = {}

        self.region = self.determine_region(self.city)
        self.save_to_db()

    def determine_region(self, city: str) -> str:
        districts_cities = {
            'Jerusalem District': ['Jerusalem', 'Mevaseret Zion'],
            'Tel Aviv District': ['Tel Aviv', 'Holon', 'Bnei Brak', 'Bat Yam', 'Herzliya', 'Ramat Gan', 'Giv''atayim', 'Or Yehuda', 'Ramat HaSharon'],
            'Haifa District': ['Haifa', 'Kiryat Ata', 'Kiryat Bialik', 'Kiryat Motzkin', 'Nesher', 'Tira', 'Kiryat Yam', 'Kiryat Gat'],
            'Central District': ['Rishon LeZion', 'Petah Tikva', 'Netanya', 'Rehovot', 'Kfar Saba', 'Modiin-Maccabim-Reut', 'Ra''anana', 'Be''er Ya''akov', 'Hod HaSharon', 'Giv''at Shmuel', 'Rosh HaAyin', 'Yavne', 'Qalansawe', 'Nazareth Illit', 'Yehud-Monosson', 'Tzfat'],
            'Southern District': ['Ashdod', 'Beer Sheva', 'Ashkelon', 'Dimona', 'Sderot', 'Kiryat Malakhi', 'Eilat', 'Ofakim', 'Yeruham', 'Netivot'],
            'Northern District': ['Nahariya', 'Ra''at', 'Karmiel', 'Afula', 'Nof Hagalil', 'Umm al-Fahm', 'Beit She''an', 'Nazareth Illit', 'Sakhnin', 'Kiryat Shmona', 'Tiberias', 'Tzfat', 'Dimona']
        }

        for district_name, cities in districts_cities.items():
            if city in cities:
                return district_name

        return 'unknown'

    def save_to_db(self):
        cursor.execute(
            "INSERT INTO users (firstname, lastname, full_name, gender, phone_number, full_address, city, region) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (self.firstname, self.lastname, self.name, self.gender, self.phone_number, self.full_address, self.city, self.region)
        )
        db.commit()

    def add_hobby(self, hobby: str, rating: int):
        self.hobbies[hobby] = rating
        person_hobbies.setdefault(hobby, []).append(self.name)
        self.sort_hobbies()

    def sort_hobbies(self):
        sorted_hobbies = sorted(self.hobbies.items(), key=lambda item: item[1])
        self.hobbies = dict(sorted_hobbies)

    def matchmaking(self):
        self.nearby_people = [p for p in persons_cities.get(self.city, []) if p != self.name]
        self.matching_people = []

        if self.nearby_people:
            for hobby in self.hobbies:
                if hobby in person_hobbies:
                    for p in person_hobbies[hobby]:
                        if p != self.name and p in self.nearby_people:
                            self.matching_people.append(p)
            if self.matching_people:
                return f'{", ".join(self.matching_people)} are your matches. You can now contact them!'
        else:
            regional_people = [p for p in persons_regions.get(self.region, []) if p != self.name]
            if regional_people:
                for hobby in self.hobbies:
                    if hobby in person_hobbies:
                        for p in person_hobbies[hobby]:
                            if p in regional_people:
                                self.matching_people.append(p)
                if self.matching_people:
                    return f'{", ".join(self.matching_people)} are your regional matches. You can now contact them!'
            print(f'Unfortunately, no matches were found in {self.city} or {self.region}.')
            all_country_search = input('Would you like to search for people in farther places?')
            if 'n' in all_country_search.lower():
                return 'Understood. Maybe next time!'
            else:
                for hobby in person_hobbies.keys():
                    if hobby == self.hobbies.keys():
                        print("There might be someone in your country who shares the same hobbies!")
                        for person in person_hobbies[hobby]:
                            if person != self.name and person not in self.matching_people:
                                self.matching_people.append(person)
                                return f'{person} is a match for you!'
            if len(self.matching_people) == 0:
                return 'Unfortunately, we couldn\'t find anyone with the same hobbies as you.'

    def contact_matches(self):
        if self.matching_people:
            contact_info = [f'{matcher}\'s phone number is: 0{person_phone_number[matcher]}' for matcher in
                            self.matching_people]
            return '\n'.join(contact_info)
        else:
            return 'Unfortunately, there are no matches.'

    def info(self):
        return f'Here is all the information we know about you:\nYour name is {self.firstname} {self.lastname}, You are living at {self.full_address},\nYour phone number is {self.phone_number}'


raz = Person('Raz','Asraf',323838110,'0545973537','Rabinovich Yehoshua 55 Holon', 'Male')
    