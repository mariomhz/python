key = "eureka"
for attempt in range(3):
    if input("enter the key: ") == key:
        print("correct key! exiting program...")
        break
    print(f"incorrect key. {2 - attempt} attempts remaining.")
else:
    print("you have exhausted all attempts.")