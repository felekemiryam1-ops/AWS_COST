prices = {"t2.micro": 0.0116, "t3.micro": 0.0104, "t3.small": 0.0208}

def main():
 calcualte_cost()
  


def calcualte_cost():
 while True:
  try:
  
   instances = input("instance type : ")
   if instances=="quit":
    print("goodbye")
    break

   hours = int(input("Hours: "))
   servers= int(input("Servers: "))
   hourly_prices=prices[instances]
   Total_cost=hourly_prices*hours*servers
   daily_estimate=Total_cost/30
   
   print(f"Average daily estimate: {daily_estimate:.2f}")
   print(f"monthly estimate: {Total_cost:.2f}")
   #print(f"{cost:.2f}")
   break
   
    
   
   
    
  except ValueError:
   print("pleae type the hours")
  except KeyError:
   print("Unknown instance type")


main()

  
  





