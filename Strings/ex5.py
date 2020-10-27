#Text and Strings
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # scrive 10 volte il carattere

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
#Lasciando la variabile, il testo viene scritto di seguito, in caso contrario
#il testo va a capo
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#Con questo particolare operatore di inizio stringa, viene mantenuta la
#formattazione del testo al suo interno
print("""
    what the hell is this?
let's try
""")
