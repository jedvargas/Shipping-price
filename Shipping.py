weight = float(input("Enter weight: "))

#Ground shipping
if weight <= 2:
  print("Price per pound of ground shipping is $1.50")
  price_per_pound = 1.50
elif weight > 2 and weight <=6:
  print("Price per pound shipping is $3.00")
  price_per_pound = 3
elif weight > 6 and weight <=10:
  print("Price per pound shipping is $4:00")
  price_per_pound = 4
else:
  print("Price per pound shipping is $4.75")
  price_per_pound = 4.75

ground_shipping = (weight*price_per_pound) + 20

print("Total ground shipping cost is " + str(ground_shipping))

#Ground shipping premium
ground_shipping_premium = 125

print("Total ground shipping premium cost is " + str(ground_shipping_premium))

#Drone Shipping

if weight <= 2:
  print("Price per pound of drone shipping is $4.50")
  price_per_pound = 4.50
elif weight > 2 and weight <=6:
  print("Price per pound of drone shipping is $9.00")
  price_per_pound = 9
elif weight > 6 and weight <=10:
  print("Price per pound of drone shipping is $12:00")
  price_per_pound = 12
else:
  print("Price per pound of drone shipping is $14.25")
  price_per_pound = 14.25

drone_shipping = weight*price_per_pound

print("Total drone shipping cost is " + str(drone_shipping))
