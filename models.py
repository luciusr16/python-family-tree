
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spouses = []
        self.parents = []
        self.children = []
    def __str__(self):
        return f"{self.name} - Age: {self.age}"

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def add_spouse(self, spouse):
        self.spouses.append(spouse)
        spouse.spouses.append(self)

    def get_siblings(self):
        siblings = []
        for parent in self.parents:
            for child in parent.children:
                if child is not self and not siblings:
                    siblings.append(child)
        return siblings



    def get_grandparents(self):
        grandparents = []
        for parent in self.parents:
            for grandparent in parent.parents:
                if grandparent not in grandparents:
                    grandparents.append(grandparent)
        return grandparents

    def get_aunts_uncles(self):
      aunts_uncles = []
      for parent in self.parents:
          for aunt_uncle in parent.get_siblings():
              if aunt_uncle not in aunts_uncles:
                  aunts_uncles.append(aunt_uncle)
      return aunts_uncles

    def get_cousins(self):
        cousins = []
        for aunt_uncle in self.get_aunts_uncles():
            for child in aunt_uncle.children:
                if child not in cousins:
                    cousins.append(child)
        return cousins

    def get_grandchildren(self):
        grandchildren = []
        for child in self.children:
            for grandchild in child.children:
                if grandchild not in grandchildren:
                    grandchildren.append(grandchild)
        return grandchildren

    def get_family_members(self):
      family_members = {
          "Parents": self.parents,
          "Children": self.children,
          "Siblings": self.get_siblings(),
          "Spouse": self.spouses,
          "Grandparents": self.get_grandparents(),
          "Aunts and uncles": self.get_aunts_uncles(),
          "Cousins": self.get_cousins(),
          "Grandchildren": self.get_grandchildren()
      }
      for relationship, people in family_members.items():
          print(f"\n{relationship}:")
          if people:
              for person in people:
                  print(f"{person.name}")
          else:
              print("- None")


class FamilyTree:
    def __init__(self):
        self.people = {}
    def add_person(self, person):
        self.people[person.name.lower().strip()] = person
    def find_person(self, name):
     search_name = name.lower().strip()
     person = self.people.get(search_name)
     if person is not None:
         return person
     for person in self.people.values():
         first_name = person.name.split()[0].lower()
         if first_name == search_name:
             return person
         return None
    def list_people(self):
        for person in self.people.values():
            print(f"\nFull name: {person.name}")
            print(f"Age={person.age}")
    def delete_person(self, name):
      person = self.find_person(name)
      if person is None:
          return False
      del self.people[person.name.lower()]
      return True




