#1. Přepsání stringu na velká písmena
text = "Program"
print(text.upper()) 

#2. Přepsání stringu na malá písmena
text = "Python"
print(text.lower())  

#3. Počet výskytů p, k, y ve slově Program, Python
slovo1 = "Program"
slovo2 = "Python"
print(slovo1.count("p") + slovo1.count("k") + slovo1.count("y")) 
print(slovo2.count("p") + slovo2.count("k") + slovo2.count("y")) 

#4. Vypište 3. písmeno ze slova Python
slovo = "Python"
print(slovo[2]) 

#5. Vypište prostřední 3 písmena slova Program
slovo = "Program"
middle_index = len(slovo) // 2
print(slovo[middle_index - 1:middle_index + 2])  

#6. Spojte string "Ahoj" a "Slunce"
pozdrav = "Ahoj" + " " + "Slunce"
print(pozdrav)

#7. Program, který se zeptá na jméno, příjmení a vypíše iniciály
jmeno = input("Zadejte jméno: ")
prijmeni = input("Zadejte příjmení: ")
inicialy = jmeno[0].upper() + prijmeni[0].upper()
print("Iniciály jsou:", inicialy)

#Cvičení č. 2

#1 
mesta = ["Ostrava", "Londyn", "Malmo", "Stockholm", "Kosice"]

#2
print(mesta)

#3
print(mesta[3])

#4
for mesta in mesta:
    print(mesta)

#5
for index, mesto in enumerate(mesta, start=1):
    print(f"{index}. {mesto}")

#6
mesta.append("BanskaBystrica")
print(mesta)

#7
mesta.pop(1)

#8
print(mesta)

#9
mesta.sort()

#10
def mesto2(mesto3, mesto4):
    if mesto4 in mesto3:
        return True
    else:
        return False
mesto5 = "Praha"

if mesto2(mesta, mesto5):
    print(f"{mesto5} se nachází v seznamu.")
else:
    print(f"{mesto5} není v seznamu.")

#11
mesta_na_a = [mesto for mesto in mesta if mesto.lower().startswith('a')]
print(mesta_na_a)

#12
slova_vetsi_nez_5 = [mesto for mesto in mesta if len(mesto) > 5]

for slovo in slova_vetsi_nez_5:
    print(slovo)