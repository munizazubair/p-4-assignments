def main():
  print("This program collects an adjective , noun, and verb from the user to create a creative Mad Libs-style sentence (programming edition)")
  adjective = str(input("Please type an adjective and press enter. "))
  noun = str(input("Please type a noun and press enter. "))
  verb = str(input("Please type a verb and press enter. "))
  sentence_start = "Through creative coding, I developed a tool that empowered my"
  print(f"{sentence_start} {adjective} {noun} {verb}!")
main()