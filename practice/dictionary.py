value = dict(name="Mr Sam", age=30)
print(value["name"])
value = {
    "name": "Mr Sam",
    "age": 30,
    "skill": {
        "soft": {"communication": "Writing"},
        "tech": {"1": "Frontend",
                 "2": "Backend"
                 }
    }
}
print(value["skill"]["tech"]["1"])

value["hobby"] = {"1": "Eating",
                  "2": "Talking",
                  "3": ["Presentation", "Coding"]}
value["complexion"] = "dark"
print(value)
