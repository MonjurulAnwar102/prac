people=[
    {"name":"monjur","House":"kaxipara"},
    {"name":"hrid","House":"shew"},
    {"name":"siyam","House":"mir"}
]

people.sort(key=lambda person:person["name"])
print(people)