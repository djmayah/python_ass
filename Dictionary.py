students=[
    {"name": "Mary", 
     "phone": "0705808776",
       "age": 32, 
       "location": "Nairobi", 
       "DOB": "27 01 1994"},

    {"name": "Jolie",
      "phone": "0701808996",
       "age": 24, 
       "location": "Nairobi", 
       "DOB": "10 08 2002"},

    {"name": "Miku", 
     "phone": "0702787900", 
     "age": 35, 
     "location": "Nakuru", 
     "DOB": "09 05 1991"},

    {"name": "Neru", 
     "phone": "0725202612", 
     "age": 46, 
     "location": "Mombasa", 
     "DOB": "29 02 1980"},

    {"name": "Liya", 
     "phone": "0722000001", 
     "age": 27, 
     "location": "Kisumu", 
     "DOB": "20 07 1999"},]


students[0]["phone"] = "0700800111"
print(students)
students.append ({
  "name":"Tetu",
  "phone": "076666666",
  "age":25,
  "location": "Nyeri"
  })
print(students)

students.remove(students[5])
print(students)