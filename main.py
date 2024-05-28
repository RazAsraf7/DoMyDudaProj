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
        northern_district = ["Safed", "Tiberias", "Nazareth", "Nof HaGalil", "Acre", "Karmiel", "Nahariya",
                             "Migdal HaEmek", "Ma'alot-Tarshiha", "Shfar'am", "Sakhnin", "Kiryat Shmona",
                             "Yokneam Illit", "Kiryat Ata", "Kiryat Bialik", "Kiryat Yam", "Tamra"]
        haifa_district = ["Haifa", "Hadera", "Or Akiva", "Nesher", "Tirat Carmel", "Baqa al-Gharbiyye",
                          "Umm al-Fahm", "Zikhron Ya'akov", "Pardes Hanna-Karkur"]
        central_district = ["Petah Tikva", "Netanya", "Raanana", "Herzliya", "Kfar Saba", "Hod HaSharon",
                            "Rosh HaAyin", "Tira", "Ramat HaSharon", "Bat Yam", "Holon", "Rishon LeZion",
                            "Givatayim", "Or Yehuda", "Yavne", "Lod", "Ramla", "Modiin-Maccabim-Reut",
                            "Kiryat Ono", "Yehud-Monosson"]
        tel_aviv_district = ["Tel Aviv-Yafo", "Bnei Brak", "Ramat Gan", "Givatayim", "Bat Yam", "Holon"]
        jerusalem_district = ["Jerusalem", "Beit Shemesh", "Ma'ale Adumim", "Modi'in Illit"]
        southern_district = ["Beersheba", "Ashdod", "Ashkelon", "Eilat", "Dimona", "Kiryat Gat",
                             "Netivot", "Ofakim", "Sderot", "Arad", "Rahat"]
        judea_samaria_area = ["Modi'in Illit", "Ariel", "Ma'ale Adumim", "Beitar Illit", "Kiryat Arba", "Giv'at Ze'ev"]
        
        if city in northern_district:
            return 'northern_district'
        elif city in haifa_district:
            return 'haifa_district'
        elif city in central_district:
            return 'central_district'
        elif city in tel_aviv_district:
            return 'tel_aviv_district'
        elif city in jerusalem_district:
            return 'jerusalem_district'
        elif city in southern_district:
            return 'southern_district'
        elif city in judea_samaria_area:
            return 'judea_samaria_area'
        else:
            return 'unknown'

    def save_to_db(self):
        cursor.execute(
            "INSERT INTO users (firstname, lastname, full_name, gender, phone_number, full_address, city, region) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (self.firstname, self.lastname, self.name, self.gender, self.phone_number, self.full_address, self.city, self.region)
        )
        db.commit()

    def add_hobby(self, hobby: str, rating: str):
        if ' ' in hobby:
            splitted_hobbies = hobby.split()
            splitted_ratings = rating.split()
            if len(splitted_hobbies) != len(splitted_ratings):
                return f'There are missing arguments because {len(splitted_hobbies)} hobbies don\'t match {len(splitted_ratings)} ratings.'
            else:
                for i in range(len(splitted_hobbies)):
                    self.hobbies[splitted_hobbies[i]] = int(splitted_ratings[i])
                    person_hobbies.setdefault(splitted_hobbies[i], []).append(self.name)
                return f'{" and ".join(splitted_hobbies)} have been successfully added.'
        else:
            self.hobbies[hobby] = int(rating)
            person_hobbies.setdefault(hobby, []).append(self.name)
            return f'{hobby} has been successfully added.'

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
            return f'Unfortunately, no matches were found in {self.city} or {self.region}.'

    def contact_matches(self):
        if self.matching_people:
            contact_info = [f'{matcher}\'s phone number is: {person_phone_number[matcher]}' for matcher in self.matching_people]
            return '\n'.join(contact_info)
        else:
            return 'Unfortunately, there are no matches.'

class Male(Person):
    def __init__(self, firstname: str, lastname: str, ID: int, phone_number: str, full_address: str):
        super().__init__(firstname, lastname, ID, phone_number, full_address, gender='male')

    def info(self):
        return f'Here is all the information we know about you:\nYour name is {self.firstname} {self.lastname}, You are living at {self.full_address},\nYour phone number is {self.phone_number}.\nYour hobbies are {self.hobbies}'

class Female(Person):
    def __init__(self, firstname: str, lastname: str, ID: int, phone_number: str, full_address: str):
        super().__init__(firstname, lastname, ID, phone_number, full_address, gender='female')

    def info(self):
        return f'Here is all the information we know about you:\nYour name is {self.firstname} {self.lastname}, You are living at {self.full_address},\nYour phone number is {self.phone_number}.\nYour hobbies are'
