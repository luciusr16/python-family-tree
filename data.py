from models import Person, FamilyTree

family = FamilyTree()


robert = Person("Robert Carter", 78)
helen = Person("Helen Carter", 76)

george = Person("George Mitchell", 80)
patricia = Person("Patricia Mitchell", 77)

john = Person("John Carter", 52)
susan = Person("Susan Carter", 49)

mary = Person("Mary Mitchell", 50)
michael = Person("Michael Mitchell", 47)

david = Person("David Wilson", 50)
laura = Person("Laura Thompson", 45)

alice = Person("Alice Carter", 24)
james = Person("James Carter", 21)

emily = Person("Emily Wilson", 20)
daniel = Person("Daniel Wilson", 17)

chloe = Person("Chloe Mitchell", 19)
ethan = Person("Ethan Mitchell", 15)

oliver = Person("Oliver Bennett", 26)
sophia = Person("Sophia Bennett", 3)

# =========================================================
# SPOUSE RELATIONSHIPS
# =========================================================

# Robert Carter and Helen Carter are married.
# Parents of John Carter and Susan Carter.
robert.add_spouse(helen)

# George Mitchell and Patricia Mitchell are married.
# Parents of Mary Mitchell and Michael Mitchell.
george.add_spouse(patricia)

# John Carter and Mary Mitchell are married.
# Parents of Alice Carter and James Carter.
john.add_spouse(mary)

# Susan Carter and David Wilson are married.
# Parents of Emily Wilson and Daniel Wilson.
susan.add_spouse(david)

# Michael Mitchell and Laura Thompson are married.
# Parents of Chloe Mitchell and Ethan Mitchell.
michael.add_spouse(laura)

# Alice Carter and Oliver Bennett are married.
# Parents of Sophia Bennett.
alice.add_spouse(oliver)


# =========================================================
# ROBERT CARTER + HELEN CARTER
# =========================================================

# John Carter is the son of Robert and Helen.
robert.add_child(john)
helen.add_child(john)

# Susan Carter is the daughter of Robert and Helen.
# This makes John and Susan siblings.
robert.add_child(susan)
helen.add_child(susan)


# =========================================================
# GEORGE MITCHELL + PATRICIA MITCHELL
# =========================================================

# Mary Mitchell is the daughter of George and Patricia.
george.add_child(mary)
patricia.add_child(mary)

# Michael Mitchell is the son of George and Patricia.
# This makes Mary and Michael siblings.
george.add_child(michael)
patricia.add_child(michael)


# =========================================================
# JOHN CARTER + MARY MITCHELL
# =========================================================

# Alice Carter is the daughter of John and Mary.
john.add_child(alice)
mary.add_child(alice)

# James Carter is the son of John and Mary.
# This makes Alice and James siblings.
john.add_child(james)
mary.add_child(james)


# =========================================================
# SUSAN CARTER + DAVID WILSON
# =========================================================

# Emily Wilson is the daughter of Susan and David.
susan.add_child(emily)
david.add_child(emily)

# Daniel Wilson is the son of Susan and David.
# This makes Emily and Daniel siblings.
susan.add_child(daniel)
david.add_child(daniel)


# =========================================================
# MICHAEL MITCHELL + LAURA THOMPSON
# =========================================================

# Chloe Mitchell is the daughter of Michael and Laura.
michael.add_child(chloe)
laura.add_child(chloe)

# Ethan Mitchell is the son of Michael and Laura.
# This makes Chloe and Ethan siblings.
michael.add_child(ethan)
laura.add_child(ethan)


# =========================================================
# ALICE CARTER + OLIVER BENNETT
# =========================================================

# Sophia Bennett is the daughter of Alice and Oliver.
alice.add_child(sophia)
oliver.add_child(sophia)


people = [
    robert,
    helen,
    george,
    patricia,
    john,
    susan,
    mary,
    michael,
    david,
    laura,
    alice,
    james,
    emily,
    daniel,
    chloe,
    ethan,
    oliver,
    sophia
]

for person in people:
  family.add_person(person)



aus = person.get_aunts_uncles()
for au in aus:
  print(f"{au.name}")

