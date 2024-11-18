def main():

  
  weight = int(input("Insert your weight in Kilograms: "))
  optionMenu = 0
  
  while optionMenu < 5:
    print("\n1. Sedentary \n2. Light \n3. Moderate \n4.Strong \n5. Very strongh \n6. Exit\n")
    optionMenu = int(input("Select your activity level from 1-5  and press 6 to exit " ))
    
    if optionMenu == 6:
      print("Exit")
      break      
    
    calculateMacros(weight,optionMenu)

def calculateMacros(w,act):
  
  activity_type = {
    "sedentary": {
        "id":1,
        "proteins": 1.2,
        "carbos": 3.0,
        "fat": {
            "man": 0.7,
            "woman": 0.8
        }
    },
    "light": {
        "id":2,
        "proteins": 1.6,
        "carbos": 3.5,
        "fat": {
            "man": 0.7,
            "woman": 0.8
        }
    },
    "moderate": {
        "id":3,
        "proteins": 2.0,
        "carbos": 3.9,
        "fat": {
            "man": 0.8,
            "woman": 1.0
        }
    },
    "strong": {
        "id":4,
        "proteins": 2.2,
        "carbos": 4.2,
        "fat": {
            "man": 0.8,
            "woman": 1.0
        }
    },
    "veryStrong": {
        "id":5,
        "proteins": 2.5,
        "carbos": 4.5,
        "fat": {
            "man": 1.0,
            "woman": 1.2
        }
    }
}
  
  if act in activity_type:
    mac_prot = activity_type[act]
  return

if __name__ == "__main__":
  main()