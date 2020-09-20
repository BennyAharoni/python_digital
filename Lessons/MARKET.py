print("Now we will calculate your marketing:\n----------\nPrices:\nTomato=3NIS\nCucumber=2NIS\n"
      "Cola=5NIS\nChicken-20NIS\n")
tomatoes = int(input("Enter how many tomatoes?"))
cucumbers = int(input("Enter how many cucumbers?"))
colas = int(input("Enter how many colas?"))
chickens = int(input("Enter how many chickens?"))

print("\nSummary of you order:\n----------\ntomatoes: " + str(tomatoes) + "\ncucumbers: " + str(cucumbers) +
      "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

sum1 = tomatoes * 3
sum2 = cucumbers * 2
sum3 = colas * 5
sum4 = chickens * 20

summary = (sum1 + sum2 + sum3 + sum4) * 1.17

print("\nYou have to pay: " + str("%.2f" % summary) + " NIS")
