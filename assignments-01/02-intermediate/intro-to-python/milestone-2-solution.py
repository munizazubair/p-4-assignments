# Milestone #2: Adding in All Planets

MERCURY: float = 0.38
VENUS: float = 0.89
MARS: float = 0.38
JUPITER: float = 2.36
SATURN: float = 1.08
URANUS: float = 0.82
NEPTUNE: float = 1.14

def all_planets_weight(weight_on_earth,planet_name):
  weight_on_mercury = weight_on_earth * 0.38
  weight_on_venus = weight_on_earth * 0.89
  weight_on_mars = weight_on_earth * 0.38
  weight_on_jupiter = weight_on_earth * 2.36
  weight_on_saturn = weight_on_earth * 1.08
  weight_on_uranus = weight_on_earth * 0.82
  weight_on_neptune = weight_on_earth * 1.14

  if planet_name == "mercury":
    return weight_on_mercury
  elif planet_name == "venus":
    return weight_on_venus
  elif planet_name == "mars":
    return weight_on_mars
  elif planet_name == "jupiter":
    return weight_on_jupiter
  elif planet_name == "saturn":
    return weight_on_saturn
  elif planet_name == "uranus":
    return weight_on_uranus
  elif planet_name == "neptune":
    return weight_on_neptune

def main():
  weight_on_earth = float(input("Enter a weight on Earth: "))
  rounded_weight = round(weight_on_earth, 2)
  planet_name = str(input("Enter a planet: "))
  planet_name = planet_name.strip().lower()
  print("The equivalent on",planet_name,":",all_planets_weight(rounded_weight,planet_name))
main()