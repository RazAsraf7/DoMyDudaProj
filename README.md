# DoMyDuda - Local Hobby Matchmaking 🤝

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**DoMyDuda** is a Python-based Object-Oriented matchmaking system designed to connect people based on shared hobbies and geographical proximity within Israel. 

The system maps users to specific districts based on their city and prioritizes matching them with local hobbyists first. If no local matches are found, it expands the search to the broader regional district.

## 🌟 Features
* **Location-Based Matching:** Automatically maps users to Israeli districts (Northern, Haifa, Central, Tel Aviv, Jerusalem, Southern, Judea & Samaria) based on their home city.
* **Proximity Priority Algorithm:** Searches for potential matches in the exact same city first, before expanding the search to the entire district.
* **Hobby Management:** Allows adding multiple hobbies with individual proficiency/interest ratings.
* **Contact Retrieval:** Securely fetches the contact information (phone numbers) of matched users.
* **Object-Oriented Design:** Clean architecture utilizing base classes (`Person`) and subclasses (`Male`, `Female`) with shared in-memory data structures.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Concepts:** OOP (Inheritance, Encapsulation), Data Structures (Dictionaries, Lists, Tuples).

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your local machine.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/RazAsraf7/DoMyDudaProj.git](https://github.com/RazAsraf7/DoMyDudaProj.git)
   cd DoMyDudaProj
