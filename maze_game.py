# Text Based Maze Game

def maze(): # Maze is initialized
    print("-  ------");
    print("|------ |");
    print("|---  --|");
    print("|  -----|");
    print("---------"); # Structure of the maze
    print("Options: left, right, forward, backward") # Options for the user
    start = input("You are in a maze. Where do you want to move?: ") # User input
    if start == "left":
        print("You hit a wall. Try again.") # Message given to the user if they hit a wall
        maze();
    elif start == "right":
        print("You hit a wall. Try again.") # Message given to the user if they hit a wall
        maze();        
    elif start == "backward":
        print("You hit a wall. Try again.") # Message given to the user if they hit a wall
        maze();
    elif start == "forward": # User moves forward in the maze
        print("-  ------");
        print("|------ |");
        print("|---  --|");
        print("|  -----|");
        print("---------"); # Structure of the maze
        print("Options: left, right, forward, backward");
        def mazealt(): # User is taken back to the start of the maze
           print("-  ------");
           print("|------ |");
           print("|---  --|");
           print("|  -----|");
           print("---------"); # Structure of the maze
           print("Options: left, right, forward, backward");
           ma = input("You are back at the beginning of the maze. Where do you want to move?: ")
           if ma == "left":
              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
              mazealt();
           elif ma == "right":
              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
              mazealt();        
           elif ma == "backward":
              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
              mazealt();
           elif ma == "forward": # User moves forward in the maze
              print("-  ------");
              print("|------ |");
              print("|---  --|");
              print("|  -----|");
              print("---------"); # Structure of the maze
              print("Options: left, right, forward, backward");
              move1();         
        def move1(): # First move after the start of the maze
         m1 = input("You move forward to the next part of the maze. What's your next move?: ")
         if m1 == "left":
            print("You hit a wall. Try again.") # Message given to the user if they hit a wall
            move1();
         elif m1 == "forward":
            print("You hit a wall. Try again.") # Message given to the user if they hit a wall
            move1();
         elif m1 == "backward": # User is taken back to the start of the maze
            mazealt();
         elif m1 == "right": # User moves right in the maze
            print("-  ------");
            print("|------ |");
            print("|---  --|");
            print("|  -----|");
            print("---------"); # Structure of the maze
            print("Options: left, right, forward, backward");
            def move1alt(): # User is taken back to the previous part of the maze
             print("-  ------");
             print("|------ |");
             print("|---  --|");
             print("|  -----|");
             print("---------"); # Structure of the maze
             print("Options: left, right, forward, backward");
             mla = input("You move backward to the previous part of the maze. What's your next move?: ")
             if mla == "left":
               print("You hit a wall. Try again.") # Message given to the user if they hit a wall
               move1();
             elif mla == "forward":
               print("You hit a wall. Try again.") # Message given to the user if they hit a wall
               move1();
             elif mla == "backward":
               print("You are now back at the start of the maze.") # Message to the user when they are back at the start of the maze
               maze();
             elif mla == "right": # User moves right in the maze
               print("-  ------");
               print("|------ |");
               print("|---  --|");
               print("|  -----|");
               print("---------"); # Structure of the maze
               print("Options: left, right, forward, backward");
               move2();
            def move2(): # Second move after the start of the maze
             m2 = input("You move right. What's your next move?: ")
             if m2 == "right": # User moves right in the maze
                print("-  ------");
                print("|------ |");
                print("|---  --|");
                print("|  -----|");
                print("---------"); # Structure of the maze
                print("Options: left, right, forward, backward");
                def move2alt(): # User is taken back to the previous part of the maze
                 print("-  ------");
                 print("|------ |");
                 print("|---  --|");
                 print("|  -----|");
                 print("---------"); # Structure of the maze
                 print("Options: left, right, forward, backward");
                 m2a = input("You move backward to the previous part of the maze. What's your next move?: ")
                 if m2a == "right": # User moves right in the maze
                  print("-  ------");
                  print("|------ |");
                  print("|---  --|");
                  print("|  -----|");
                  print("---------"); # Structure of the maze
                  print("Options: left, right, forward, backward");
                  move3();
                 elif m2a == "backward": # User is taken back to the previous part of the maze
                  move1alt();
                 elif m2a == "left":
                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                  move2alt();
                 elif m2a == "forward":
                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                  move2alt();
                def move3(): # Third move after the start of the maze
                   m3 = input("You move right again. What's your next move?: ")
                   if m3 == "right":
                      print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                      move3();
                   elif m3 == "forward":
                      print("You walk for a little bit and hit a wall. Try again.") # Message given to the user if they hit a wall
                      move3();
                   elif m3 == "backward": # User is taken back to the previous part of the maze
                      move2alt();
                   elif m3 == "left": # User moves left in the maze
                     print("-  ------");
                     print("|------ |");
                     print("|---  --|");
                     print("|  -----|");
                     print("---------"); # Structure of the maze
                     print("Options: left, right, forward, backward");
                     def move3alt(): # User is taken back to the previous part of the maze
                      print("-  ------");
                      print("|------ |");
                      print("|---  --|");
                      print("|  -----|");
                      print("---------"); # Structure of the maze
                      print("Options: left, right, forward, backward");
                      m3a = input("You move backward to the previous part of the maze. What's your next move?: ")
                      if m3a == "right":
                        print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                        move3alt();
                      elif m3a == "forward":
                        print("You walk for a little bit and hit a wall. Try again.") # Message given to the user if they hit a wall
                        move3alt();
                      elif m3a == "backward": # User is taken back to the previous part of the maze
                        move2alt();
                      elif m3a == "left": # User moves left in the maze
                        print("-  ------");
                        print("|------ |");
                        print("|---  --|");
                        print("|  -----|");
                        print("---------"); # Structure of the maze
                        print("Options: left, right, forward, backward");
                        move4();                    
                     def move4(): # Fourth move after the start of the maze
                        m4 = input("You move left. What's your next move?: ")
                        if m4 == "left":
                          print("You walk for a while and hit a wall. Try again.") # Message given to the user if they hit a wall
                          move4();
                        elif m4 == "backward": # User is taken back to the previous part of the maze
                          move3alt();
                        elif m4 == "forward":
                          print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                          move4();
                        elif m4 == "right": # User moves right in the maze
                          print("-  ------");
                          print("|------ |");
                          print("|---  --|");
                          print("|  -----|");
                          print("---------"); # Structure of the maze
                          print("Options: left, right, forward, backward");
                          def move4alt(): # User is taken back to the previous part of the maze
                            print("-  ------");
                            print("|------ |");
                            print("|---  --|");
                            print("|  -----|");
                            print("---------"); # Structure of the maze
                            print("Options: left, right, forward, backward");
                            m4a = input("You move backward to the previous part of the maze. What's your next move?: ")
                            if m4a == "left":
                              print("You walk for a while and hit a wall. Try again.") # Message given to the user if they hit a wall
                              move4alt();
                            elif m4a == "backward": # User is taken back to the previous part of the maze
                              move3alt();
                            elif m4a == "forward":
                              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                              move4alt();
                            elif m4a == "right": # User moves right in the maze
                              print("-  ------");
                              print("|------ |");
                              print("|---  --|");
                              print("|  -----|");
                              print("---------"); # Structure of the maze
                              print("Options: left, right, forward, backward");
                              move5();
                          def move5(): # Fifth move after the start of the maze
                            m5 = input("You move right. What's your next move?: ")
                            if m5 == "right":
                              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                              move5();
                            elif m5 == "forward":
                              print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                              move5();
                            elif m5 == "backward": # User is taken back to the previous part of the maze
                              move4alt();
                            elif m5 == "left": # User moves left in the maze
                              print("-  ------");
                              print("|------ |");
                              print("|---  --|");
                              print("|  -----|");
                              print("---------"); # Structure of the maze
                              print("Options: left, right, forward, backward");
                              def move5alt(): # User is taken back to the previous part of the maze
                                print("-  ------");
                                print("|------ |");
                                print("|---  --|");
                                print("|  -----|");
                                print("---------"); # Structure of the maze
                                print("Options: left, right, forward, backward");
                                m5a = input("You move backward to the previous part of the maze. What's your next move?: ")
                                if m5a == "right":
                                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                  move5alt();
                                elif m5a == "forward":
                                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                  move5alt();
                                elif m5a == "backward": # User is taken back to the previous part of the maze
                                  move4alt();
                                elif m5a == "left": # User moves left in the maze
                                  print("-  ------");
                                  print("|------ |");
                                  print("|---  --|");
                                  print("|  -----|");
                                  print("---------"); # Structure of the maze
                                  print("Options: left, right, forward, backward");
                                  move6();
                              def move6(): # Sixth move after the start of the maze
                                m6 = input("You move left. What's your next move?: ")
                                if m6 == "left": # User moves left in the maze
                                  print("-  ------");
                                  print("|------ |");
                                  print("|---  --|");
                                  print("|  -----|");
                                  print("---------"); # Structure of the maze
                                  print("Options: left, right, forward, backward");
                                  def move6alt(): # User is taken back to the previous part of the maze
                                    print("-  ------");
                                    print("|------ |");
                                    print("|---  --|");
                                    print("|  -----|");
                                    print("---------"); # Structure of the maze
                                    print("Options: left, right, forward, backward");
                                    m6a = input("You move backward to the previous part of the maze. What's your next move?: ")
                                    if m6a == "left": # User moves left in the maze
                                      print("-  ------");
                                      print("|------ |");
                                      print("|---  --|");
                                      print("|  -----|");
                                      print("---------"); # Structure of the maze
                                      print("Options: left, right, forward, backward");
                                      move7();
                                    elif m6a == "right":
                                      print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                      move6alt();
                                    elif m6a == "forward":
                                      print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                      move6alt();
                                    elif m6a == "backward": # User is taken back to the previous part of the maze
                                      move5alt();
                                  def move7(): # Seventh move after the start of the maze
                                    m7 = input("You move left again. You see the exit! What's your next move?: ")
                                    if m7 == "left":
                                      print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                      move7();
                                    elif m7 == "forward":
                                      print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                      move7();
                                    elif m7 == "backward": # User is taken back to the previous part of the maze
                                      move6alt();
                                    elif m7 == "right":
                                      print("Congratulations! You have exited the maze!"); # Message to the user when they exit the maze
                                  move7();
                                elif m6 == "right":
                                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                  move6();
                                elif m6 == "forward":
                                  print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                                  move6();
                                elif m6 == "backward": # User is taken back to the previous part of the maze
                                  move5alt();                                     
                              move6();  
                          move5();
                     move4();
                move3();
             elif m2 == "backward": # User is taken back to the previous part of the maze
                move1alt();
             elif m2 == "forward":
                print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                move2();
             elif m2 == "left":
                print("You hit a wall. Try again.") # Message given to the user if they hit a wall
                move2();
            move2();
        move1();
maze();