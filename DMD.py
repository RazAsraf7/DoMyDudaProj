from fastapi import FastAPI, HTTPException
import json
import uvicorn
from person import Person
import re
import os

# Load existing users from new_users.json
new_users = {}
with open('new_users.json', 'r') as new_users_json:
    json_dict = json.load(new_users_json)
    for key, val in json_dict.items():
        new_users[int(key)] = val

# Create an in-memory dictionary of users
users_dictionary = {}
for key, val in new_users.items():
    users_dictionary[len(users_dictionary) + 1] = Person(**val)

# Function to convert Person object to dictionary
def person_to_dict(person: Person):
    return {
        'firstname': person.firstname,
        'lastname': person.lastname,
        'gender': person.gender,
        'phone_number': person.phone_number,
        'full_address': person.full_address,
        'hobbies': person.hobbies,
        'city': person.city,
        'region': person.region
    }

# Write initial users to user_details.json
with open('user_details.json', 'w') as user_details:
    json.dump([person_to_dict(v) for v in users_dictionary.values()], user_details, indent=4)

app = FastAPI()

@app.get('/')
async def show_all_users():
    return {"users": [person_to_dict(v) for v in users_dictionary.values()]}

@app.post('/register')
async def register(First_Name: str, Last_Name: str, User_Name: str, Password: str, Email: str, Address: str, City: str, Gender: str, Phone_Number: str):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
        raise HTTPException(status_code=400, detail='Email is not valid. Please try again')
    if not Password.isalnum():
        raise HTTPException(status_code=400, detail='Only letters and numbers are supported. (A-Z, a-z, 0-9)')
    if not User_Name.isidentifier():
        raise HTTPException(status_code=400, detail='User name must only contain letters, numbers, or underscores, and cannot start with a number.')

    user = {
        "firstname": First_Name,
        "lastname": Last_Name,
        "gender": Gender,
        "phone_number": Phone_Number,
        "full_address": f'{Address}, {City}'
    }
    user_email_password = f'UserName: {User_Name}, Password: {Password}, E-Mail: {Email}'
    temp_user_dict = {user_email_password: user}
    
    # Load existing passwords
    if os.path.exists('users_passwords.json'):
        with open('users_passwords.json', 'r') as users_passwords_json:
            try:
                users_passwords = json.load(users_passwords_json)
            except json.JSONDecodeError:
                users_passwords = []
    else:
        users_passwords = []

    users_passwords.append(temp_user_dict)
    
    # Save updated passwords
    with open('users_passwords.json', 'w') as users_passwords_json:
        json.dump(users_passwords, users_passwords_json, indent=4)

    # Check if user already exists
    if user not in [person_to_dict(v) for v in users_dictionary.values()]:
        person = Person(**user)
        users_dictionary[len(users_dictionary) + 1] = person

        # Update user_details.json
        with open('user_details.json', 'w') as user_details:
            json.dump([person_to_dict(v) for v in users_dictionary.values()], user_details, indent=4)

        return f'Successfully created user {User_Name}'
    else:
        raise HTTPException(status_code=400, detail='User already exists')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5500)
