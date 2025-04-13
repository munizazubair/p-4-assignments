# Milestone #1: Mars Weight

def mars_weight(weight_on_earth):
  weight_on_mars = weight_on_earth * 0.378  
  return weight_on_mars

def main():
  weight_on_earth = float(input("Enter a weight on Earth: "))
  rounded_weight = round(weight_on_earth, 2)
  print("The equivalent on Mars:", round(mars_weight(rounded_weight), 2), "kg")

main()
