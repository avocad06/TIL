# 4949
"""
"""
import sys
sys.stdin = open("균형.txt")

while True:
      cnt = 0
      open_ = []
      words = input()
      
      if words == '.':
            break
          
      else:
            for char in words:
                  if char in '([':
                        open_.append(char)
      # print(open_)
                  if char == ')':
                        if open_ and open_[-1] == '(':
                                open_.pop()
                                
                        else:
                              print("no")
                              cnt += 1
                              break
                      
                  elif char == ']':
                        if open_ and open_[-1] == '[':
                              open_.pop()
                              
                        else:
                              print("no")
                              cnt += 1
                              break

            if not open_ and cnt == 0:
                  print("yes")
                  
            elif cnt == 0:
                  print("no")
              

                  
                  
    


  