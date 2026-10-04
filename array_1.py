import numpy as numpy
students = ["Mary", "Sarah", "Jolie", "Ben", "Anita"]
students_array = numpy.array(students)
print(students_array)


import numpy as numpy
students_2d = numpy.array([
    ["Mary", "Nairobi", "0705808776"],
    ["Jolie", "Nairobi", "0701808996"],
    ["Liya", "Kisumu", "072000001"],
    ["Miku", "Mombasa", "0702787900"]
])
print(students_2d)


import numpy as numpy
students_3d = numpy.array([
    [
    ["Mary", "Nairobi", "0705808776" ],
    ["Jolie", "Nairobi", "0701808996"],
    ],
    [
    ["Liya", "Kisumu", "072000001"],
    ["Miku", "Mombasa", "0702787900"]
    ]
])
print(students_3d)