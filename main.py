persons_cities = {}
persons_in_city = []
persons_regions = {}

class Person:
    def __init__(self, firstname : str, lastname: str, gender: str, phone_number, full_address):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone_number = phone_number
        self.full_address = full_address
        self.city = full_address.split()[-1]
        self.hobbies = {}
        northern_district = (
    "Safed",
    "Tiberias",
    "Nazareth",
    "Nof HaGalil",
    "Acre",
    "Karmiel",
    "Nahariya",
    "Migdal HaEmek",
    "Ma'alot-Tarshiha",
    "Shfar'am",
    "Sakhnin",
    "Kiryat Shmona",
    "Yokneam Illit",
    "Kiryat Ata",
    "Kiryat Bialik",
    "Kiryat Yam",
    "Tamra"
)
        haifa_district = (
    "Haifa",
    "Hadera",
    "Or Akiva",
    "Nesher",
    "Tirat Carmel",
    "Baqa al-Gharbiyye",
    "Umm al-Fahm",
    "Zikhron Ya'akov",
    "Pardes Hanna-Karkur"
)
        central_district = (
    "Petah Tikva",
    "Netanya",
    "Raanana",
    "Herzliya",
    "Kfar Saba",
    "Hod HaSharon",
    "Rosh HaAyin",
    "Tira",
    "Ramat HaSharon",
    "Bat Yam",
    "Holon",
    "Rishon LeZion",
    "Givatayim",
    "Or Yehuda",
    "Yavne",
    "Lod",
    "Ramla",
    "Modiin-Maccabim-Reut",
    "Kiryat Ono",
    "Yehud-Monosson"
)
        tel_aviv_district = (
    "Tel Aviv-Yafo",
    "Bnei Brak",
    "Ramat Gan",
    "Givatayim",
    "Bat Yam",
    "Holon"
)
        jerusalem_district = (
    "Jerusalem",
    "Beit Shemesh",
    "Ma'ale Adumim",
    "Modi'in Illit"
)
        southern_district = (
    "Beersheba",
    "Ashdod",
    "Ashkelon",
    "Eilat",
    "Dimona",
    "Kiryat Gat",
    "Netivot",
    "Ofakim",
    "Sderot",
    "Arad",
    "Rahat"
)
        judea_samaria_area = (
    "Modi'in Illit",
    "Ariel",
    "Ma'ale Adumim",
    "Beitar Illit",
    "Kiryat Arba",
    "Giv'at Ze'ev"
)
        self.region = ''
        if self.city in northern_district:
            self.region = 'northern_district'
        elif self.city in haifa_district:
            self.region = 'haifa_district'
        elif self.city in central_district:
            self.region = 'central_district'
        elif self.city in tel_aviv_district:
            self.region = 'tel_aviv_district'
        elif self.city in jerusalem_district:
            self.region = 'jerusalem_district'
        elif self.city in southern_district:
            self.region = 'southern_district'
        elif self.city in judea_samaria_area:
            self.region = 'judea_samaria_area'
        if self.city in persons_cities.keys():
            persons_cities[self.city].append(f'{self.firstname} {self.lastname}')
        else:
            persons_cities[self.city] = [f'{self.firstname} {self.lastname}']

    def add_hobby(self, hobby: str, rating: str):
            if ' ' in hobby:
                splitted_hobbies = hobby.split()
                splitted_ratings = rating.split()
                if len(splitted_hobbies) != len(splitted_ratings):
                    print(f'There are missing arguments because {len(splitted_hobbies)} hobbies does\'nt match {len(splitted_ratings)} ratings.')
                else:
                    for i in range(len(splitted_hobbies)):
                        self.hobbies[splitted_hobbies[i]] = int(splitted_ratings[i])
            else:
                self.hobbies[hobby] = rating

    def matchmaking(self):
        self.nearby_people = []
        for city in persons_cities.keys():
            if city.upper() == self.city.upper():
                for p in persons_cities[city]:
                    self.nearby_people.append(p)





class Male(Person):
    def __init__(self,firstname :str, lastname :str, phone_number: str, full_address: str):
        super().__init__(firstname, lastname, 'male', phone_number, full_address)

    def info(self):
        return f'Here is all the information we know about you:\nYour name is {self.firstname} {self.lastname}, You are living at {self.full_address},\nYour phone number is {self.phone_number}.\nYour hobbies are {self.hobbies}'

class Female(Person):
    def __init__(self,firstname :str, lastname :str, phone_number: str, full_address: str):
        super().__init__(firstname, lastname, 'male', phone_number, full_address)

    def info(self):
        return f'Here is all the information we know about you:\nYour name is {self.firstname} {self.lastname}, You are living at {self.full_address},\nYour phone number is {self.phone_number}.\nYour hobbies are {self.hobbies}'






raz = Male('Raz','Asraf','0545973537', 'Rabinovich Yehoshua 55 Holon')
anatoly = Male('Anatoly', 'Kirilenko', '0544442232', 'Bnei Brak 2 Ashdod')
adi = Female('Adi', 'Hadad', '0544530109', 'Uri Tzvi Grinberg 23 Holon')


raz.add_hobby('Skiing Riding Surfing', '5 4 6')
print(raz.matchmaking())
