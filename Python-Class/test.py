
weight_input = input("Enter weight: ")
kg_lb_input = input("(K)g or (L)bs: ")

if kg_lb_input == "k":
    kg_result = int(weight_input) * 2.205
    kg_result_rounded = round(kg_result)
    print("Weight in Lbs: " + str(kg_result_rounded))
elif kg_lb_input == "K":
    kg_result = int(weight_input) * 2.205
    kg_result_rounded = round(kg_result)
    print("Weight in Lbs: " + str(kg_result_rounded))
elif kg_lb_input == "l":
    lb_result = int(weight_input) / 2.205
    lb_result_rounded = round(lb_result)
    print("Weight in Kgs: " + str(lb_result_rounded))
elif kg_lb_input == "L":
    lb_result = int(weight_input) / 2.205
    lb_result_rounded = round(lb_result)
    print("Weight in Kgs: " + str(lb_result_rounded))
else:
    print("Invalid input! Please type in L or K for Lbs or Kgs.")
print("Done")