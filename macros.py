def main():

  
  optionMenu = 0
  
  while optionMenu < 5:
    
    print("\n1. Sedentary \n2. Light \n3. Moderate \n4. Strong \n5. Very strongh \n6. Exit\n")
    optionMenu = int(input("Select your activity level from 1-5  and press 6 to exit " ))
    
    if optionMenu == 6:
      print("Exit")
      break      
    
    weight = int(input("Insert your weight in Kilograms: "))
    
    calculateMacros(weight,optionMenu)

def calculateMacros(w,act):
  
  activity_type = {
        1:{ # sedentary
    "requirements": {
        "proteins": 1.2,
        "carbos": 3.0,
        "fat": {
            "man": 0.7,
            "woman": 0.8
        }
    }
    },
        2:{ # light
    "requirements": {
        "proteins": 1.6,
        "carbos": 3.5,
        "fat": {
            "man": 0.7,
            "woman": 0.8
        }
    }},
        3:{# moderate
    "requirements": { 
        "proteins": 2.0,
        "carbos": 3.9,
        "fat": {
            "man": 0.8,
            "woman": 1.0
        }
    }},
        4:{ # strong
    "requirements": {
        "proteins": 2.2,
        "carbos": 4.2,
        "fat": {
            "man": 0.8,
            "woman": 1.0
        }
    }},
        5:{
    "requirements": { # very strong
        "proteins": 2.5,
        "carbos": 4.5,
        "fat": {
            "man": 1.0,
            "woman": 1.2
        }
    }}
}

  activity = activity_type.get(act)
  
  if activity:
    prot = w * activity["requirements"]["proteins"]
    carbs = w * activity["requirements"]["carbos"]
    fatsMan = w * activity["requirements"]["fat"]["man"]
    fatsWoman = w * activity["requirements"]["fat"]["woman"]
    print(f"\nThe nutritional requirements for a person of {w}Kgs. are: \n Proteins: {prot}grs., Carbohydrates: {carbs}grs, Fats for man: {fatsMan}grs., Fats for woman: {fatsWoman}grs.")
  else:
    print("Invalid activity")
  return
  

if __name__ == "__main__":
  main()