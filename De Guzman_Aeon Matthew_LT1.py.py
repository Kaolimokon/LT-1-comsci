#Notebook problem

#1
#Data collection
Total_Notebooks = int(input("Enter total number of notebooks."))
Box = int(input("Enter the number of noteboks that can fit inside a box."))

#2
#Give output
print("The total number of notebooks is", Total_Notebooks)
print("The number of notebooks a box can fit is", Box)

#3
#calculation on notebooks (determines number of full boxes and whether or not there are any loose packs)
Full_boxes = Total_Notebooks // Box
Loose_packs = Total_Notebooks % Box

#4
#says what will be concluded from the calculation
print("The number of  full boxes is", Full_boxes)
print("The number of  loose packs is", Loose_packs)

#5
#If there are no full boxes indicated:
if Full_boxes ==  0:
        print("No full box was filled.")
print(Loose_packs, "Loose book(s) will go in the loose packs")