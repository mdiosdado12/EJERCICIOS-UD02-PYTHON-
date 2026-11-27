productos = [
    {"nombre": "Ratón", "precio": 15, "stock": 20},
    {"nombre": "Teclado", "precio": 30, "stock": 10},
    {"nombre": "Monitor", "precio": 150, "stock": 5}
]

print (productos[0]["nombre"])
print (productos[1]["precio"])
print (productos[2]["stock"])

productos[1]["precio"] = 60
print  ("precio cambiado:", productos[1]["precio"])