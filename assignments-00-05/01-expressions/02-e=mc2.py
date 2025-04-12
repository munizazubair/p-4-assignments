C = 299792458
def main():
  kilos_in_mass = float(input("Enter kilos of mass: "))
  e = kilos_in_mass*C**2
  print(f"{e} joules of energy!")
main()