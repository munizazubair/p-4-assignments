voting_age_Peturksbouipo:int = 16
voting_age_Stanlau:int = 25
voting_age_Mayengua:int = 48
def main():
  age = int(input("How old are you? "))

  if age >= voting_age_Mayengua:
    print(f"You can vote in Mayengua where the voting age is {voting_age_Mayengua}." , end="")
  else:
    print(f"You cannot vote in Mayengua where the voting age is {voting_age_Mayengua}." , end="")

  if age >= voting_age_Stanlau:
    print(f"You can vote in Stanlau where the voting age is {voting_age_Stanlau}." , end="")
  else:
    print(f"You cannot vote in Stanlau where the voting age is {voting_age_Stanlau}." , end="")

  if age >= voting_age_Peturksbouipo:
    print(f"You can vote in Peturksbouipo where the voting age is {voting_age_Peturksbouipo}." , end="")
  else:
    print(f"You cannot vote in Peturksbouipo where the voting age is {voting_age_Peturksbouipo}." , end="")
main()

