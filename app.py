print("Would you like to play again?")
pAgain = input("(Y) or (N): ")
if pAgain == "Y":
  board = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]
  gameRunning = True
elif pAgain == "N":
  print()
  menu()
  option = int(input("Enter an option: "))