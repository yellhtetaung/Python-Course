students = {"role-1": "Mg Mg", "role-2": "Aung Aung", "role-3": "Aung Hla"}

print(
    "Dictionary ", students
)  # {'role-1': 'Mg Mg', 'role-2': 'Aung Aung', 'role-3': 'Aung Hla'}

print("Get role-1 ", students.get("role-1"))  # Mg Mg

students["role-2"] = "Hla Maung"
print(
    "Dictionary ", students
)  # {'role-1': 'Mg Mg', 'role-2': 'Hla Maung', 'role-3': 'Aung Hla'}
