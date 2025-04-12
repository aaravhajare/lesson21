student_data = {
    "id_1" : {
        "name" : "aarav",
        "class" : "7",
        "subject" : "maths"
    },

    "id_2" : {
        "name" : "aahan",
        "class" : "5",
        "subject" : "english"
    },

    "id_3" : {
        "name" : "aarav",
        "class" : "7",
        "subject" : "maths"
    },

    "id_4" : {
        "name" : "k",
        "class" : "7",
        "subject" : "science"
    }
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)