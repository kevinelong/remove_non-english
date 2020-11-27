# How to remove non-english words with Python:

# One way to approximate this would be to remove words that contained any high ascii characters.

data = """
Hola = Hello
Adiós = Goodbye
Por favor = Please
Gracias = Thank you
Lo siento = Sorry
Salud = Bless you (after someone sneezes)
Sí = Yes
No = No
¿Quién? = Who?
¿Qué? = What?
¿Por qué? = Why?
¿Dónde? = Where?
"""


def seems_like_english(word):
    for letter in word:
        if ord(letter) > 127:
            return False
    return True


lines = data.split("\n")

for line in lines:
    words = line.split(" ")
    output = []
    for word in words:
        if seems_like_english(word):
            output.append(word)
    print(" ".join(output))

"""
OUTPUT:
Hola = Hello
= Goodbye
Por favor = Please
Gracias = Thank you
Lo siento = Sorry
Salud = Bless you (after someone sneezes)
= Yes
No = No
= Who?
= What?
= Why?
= Where?
"""
