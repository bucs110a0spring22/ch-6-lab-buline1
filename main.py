import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
      if(n % 2) == 0:        # n is even
          n = n // 2
      else:                 # n is odd
          n = n * 3 + 1
      count += 1
    return count              # the last print is 1
print(seq3np1(3))

def iterationGraph(myscreen=None, upper_limit=0):
  turtle_write = turtle.Turtle()
  turtle_graph = turtle.Turtle()
  turtle_graph.goto(1,0)
  turtle_graph.pendown()
  turtle.speed(0)
  myscreen.setworldcoordinates(0,0,10,10)

  max_so_far = 0

  start = 1
  while(start <= upper_limit):
    result = seq3np1(start)
    if result > max_so_far:
      max_so_far = result
      turtle_write.goto(0, max_so_far)
      turtle_write.clear()
      turtle_write.write("Maximum so far:" + str(start) +  ", " + str(max_so_far))
    myscreen.setworldcoordinates(0,0,start+10, max_so_far+10)
    turtle_graph.goto(start, result)
    start += 1
  
def main():
#PART A
  upper_bound = int(input("\nPlease input a value for the upper bound of the range:  "))
  if 0 > upper_bound:
    print("Error")
    exit()
  else:
    start = 1
    while(start <= upper_bound):
      print("Start:",start,"Iterations:",seq3np1(start))
      start += 1
#PART B
  myscreen = turtle.Screen()
  iterationGraph(myscreen, upper_bound)
  myscreen.exitonclick()  
  #seq3np1(3)
main()
