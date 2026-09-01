signal = input("Enter traffic signal color (Red/Yellow/Green): ")

signal = signal.lower()

if signal == "red":
    print("STOP - Do not move.")

elif signal == "yellow":
    print("WAIT - Get ready to stop.")

elif signal == "green":
    print("GO - You can move.")

else:
    print("Invalid signal color.")
