#my solution
car_running = False
car_initially_started = False
while True:
  user_input = input("> ").lower()
  if user_input == "start":
    if car_running:
      print("Car already running!")
    else:
      car_running = True
      car_initially_started = True
      print("Car started... Ready to go!")
  elif user_input == "stop":
    if not car_initially_started:
      print("Car hasn't started yet!")
    elif not car_running:
      print("Car already stopped!")
    else:
      car_running = False
      print("Car stopped.")
  elif user_input == "help":
    print(f'''start - to start the car 
stop - to stop the car 
quit - to exit''')
  elif user_input == "quit" or user_input == "exit":
    print("Exiting...")
    break
  else: 
    print("I don't understand that...")