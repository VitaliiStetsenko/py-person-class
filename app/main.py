class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    output_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name=name, age=age)
        output_list.append(new_person)
    for person in people:
        name = person["name"]
        obj = Person.people[name]
        if "wife" in person and person["wife"]:
            obj.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            obj.husband = Person.people[person["husband"]]
    return output_list
