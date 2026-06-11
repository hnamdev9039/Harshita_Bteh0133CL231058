import json
student1 ={
    "name":"harshita",
    "age":"19",
    "city":"bhopal",
    "marks":"92",
}
student2 ={
    "name":"harsha",
    "age":"20",
    "city":"ujjain",
    "marks":"88",
}

student3 ={
    "name":"aadi",
    "age":"25",
    "city":"bhel",
    "marks":"55",
}
json_data1 = json.dumps(student1)
json_data2 = json.dumps(student2)
json_data3 = json.dumps(student3)
print(json_data1)
print(json_data2)
print(json_data3)

with open("students.json","w") as f:
    json.dump(student1,f)
    json.dump(student2,f)
    json.dump(student3,f)

print("Json file created")
