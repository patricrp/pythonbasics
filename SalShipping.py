def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.5 + 20
  elif weight <= 6:
    cost = weight * 3 + 20
  elif weight <= 10:
    cost = weight * 4 + 20
  else:
    cost = weight *4.75 + 20
  return cost

print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.5 
  elif weight <= 6:
    cost = weight * 9 
  elif weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25
  return cost

print(drone_shipping(1.5))

def cost_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)
  if drone < premium and drone < ground:
    method = "drone"
    cost = drone
  elif ground < premium and ground < drone:
    method = "ground"
    cost = ground
  else:
    method = "premium"
    cost = premium
  
  
  print(f"The cheapest shipping method is {method} and it would cost you {cost} dollars.")
  
cost_shipping(4.8)
cost_shipping(41.5)