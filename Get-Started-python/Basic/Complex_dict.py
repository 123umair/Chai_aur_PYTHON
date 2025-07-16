
complex_dict = {
    "company": "TechNova",
    "founded": 2010,
    "is_public": True,
    "employees": {  #first enterance
        "total": 250,
        "departments": { # 2nd entry 
            "Engineering": {
                "teams": [    # 3rd entry list 
                    {
                        "name": "Backend",
                        "lead": "Alice",
                        "members": ["Bob", "Charlie", "David"],
                        "projects": [
                            {
                                "name": "API Revamp",
                                "budget": 120000,
                                "status": "Ongoing",
                                "milestones": {
                                    "design": "Completed",
                                    "development": "In Progress",
                                    "testing": "Pending"
                                }
                            },
                            {
                                "name": "Auth Service",
                                "budget": 50000,
                                "status": "Completed",
                                "milestones": {
                                    "design": "Completed",
                                    "development": "Completed",
                                    "testing": "Completed"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Frontend",
                        "lead": "Eve",
                        "members": ["Frank", "Grace"],
                        "projects": []
                    }
                ]
            },
            "HR": {
                "head": "Mallory",
                "policies": {
                    "leave_policy": {
                        "annual_leave": 20,
                        "sick_leave": 10,
                        "work_from_home": True
                    },
                    "recruitment": {
                        "open_positions": ["Data Scientist", "DevOps Engineer"],
                        "interview_process": ["Screening", "Technical Round", "HR Round"]
                    }
                }
            }
        }
    },
    "offices": [
        {
            "city": "New York",
            "address": "123 Madison Ave",
            "employees_count": 100
        },
        {
            "city": "Berlin",
            "address": "Alexanderplatz 4",
            "employees_count": 50
        }
    ],
    "stock_prices": {
        "2022": [120.5, 123.0, 125.8],
        "2023": [130.2, 128.0, 135.5]
    },
    "partners": None
}

# ✅ Questions on complex_dict
# Q1️⃣:Print the name of the lead of the Backend team at TechNova.

# Expected output: "Alice"

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["lead"])  # Successfully Attempt 

# Q2️⃣:Print the list of members in the Backend team.

# Expected output: ["Bob", "Charlie", "David"]

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["members"]) # Successfully Attempt

# Q3️⃣:Print the budget of the API Revamp project.

# Expected output: 120000

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][0]["budget"]) # Successfully Attempt

# Q4️⃣:What is the status of the Auth Service project?

# Expected output: "Completed"

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][1]["status"]) # Successfully Attempt


# Q5️⃣:Print the milestones dictionary of the API Revamp project.

# Expected output:
# {
#     "design": "Completed",
#     "development": "In Progress",
#     "testing": "Pending"
# }
print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][0]["milestones"]) # Successfully Attempt

# Q6️⃣:Print the name of the lead of the Frontend team.

# Expected output: "Eve"

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][1]["lead"]) # Successfully Attempt

# Q7️⃣:Print the name of the head of the HR department.

# Expected output: "Mallory"
print(complex_dict["employees"]["departments"]["HR"]["head"]) # Successfully Attempt

# Q8️⃣:How many days of annual leave are there in the HR policies?

# Expected output: 20
print(complex_dict["employees"]["departments"]["HR"]["policies"]["leave_policy"]["annual_leave"]) # Successfully Attempt


# Q9️⃣:Print the list of open positions in HR recruitment.

# Expected output: ["Data Scientist", "DevOps Engineer"]
print(complex_dict["employees"]["departments"]["HR"]["policies"]["recruitment"]["open_positions"]) # Successfully Attempt


# Q🔟:How many employees are there in the New York office?

# Expected output: 100
print(complex_dict["offices"][0]["employees_count"])    # Successfully Attempt

# Q1️⃣1️⃣:Print the name of the city of the second office.

# Expected output: "Berlin"
print(complex_dict["offices"][1]["city"]) # Successfully Attempt

# Q1️⃣2️⃣:Print the list of stock prices for the year 2023.

# Expected output: [130.2, 128.0, 135.5]
print(complex_dict["stock_prices"]["2023"])

# Q1️⃣3️⃣:Print a list of the project names in the Backend team.

# Expected output: ["API Revamp", "Auth Service"]
Api_Revamp = complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][0]["name"] 
Auth_Service = complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][1]["name"]
blank_list = []
blank_list.insert(0,Api_Revamp)    
blank_list.insert(1, Auth_Service)        # Successfully Attempt
print(blank_list)



# Q1️⃣4️⃣:What is the status of the testing milestone in the Auth Service project?

# Expected output: "Completed"

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][1]["milestones"]["testing"] ) # Successfully Attempt

# Q1️⃣5️⃣:Print a list of the cities for all offices.

# Expected output: ["New York", "Berlin"]
city_one = complex_dict["offices"][1]["city"]
city_two = complex_dict["offices"][0]["city"]
city_list = []
city_list.insert(0,city_one)
city_list.insert(1,city_two)
print(city_list)             # Successfully Attempt

# Q1️⃣6️⃣:Print the status of the development milestone for the first project of the Backend team.

# Expected output: "In Progress"

print(complex_dict["employees"]["departments"]["Engineering"]["teams"][0]["projects"][0]["milestones"]["development"] ) # Successfully Attempt



# Q1️⃣7️⃣:Print the steps in the HR recruitment interview process.

# Expected output: ["Screening", "Technical Round", "HR Round"]

print(complex_dict["employees"]["departments"]["HR"]["policies"]["recruitment"]["interview_process"])  # Successfully Attempt

# Q1️⃣8️⃣ : Is the company public? (Print True/False)

# Expected output: True

print(complex_dict["is_public"]) # Successfully attempt


# Q1️⃣9️⃣:Print all department names (e.g. Engineering, HR).

# Expected output: ["Engineering", "HR"]

list_complex_dict=list(complex_dict["employees"]["departments"]) # Type_Casting Technique Successfully Attempt
print(list_complex_dict) 



# Q2️⃣0️⃣: Print the value of the partners field in the company dictionary.

# Expected output: None

print(complex_dict["partners"])  # Successfully attempt