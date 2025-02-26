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