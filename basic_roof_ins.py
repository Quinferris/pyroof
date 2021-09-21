def insurance():
    global total_ins_price
    global collect_deduc
    global deductible
    global sales_tax
    paperwork = input("Do you have paperwork: ")
    if paperwork.lower() == 'yes':
        collect_deduc = input("Are you collecting deductible?")
        if collect_deduc.lower() == "yes":
            deductible = input("Deductible: ")
            ins_price = input("RCV( Replacement Cost Value): ")
            total_ins_price = float(ins_price) + int(deductible)
            print(total_ins_price)
        elif collect_deduc.lower() == "no":
            deductible = input("Deductible: ")
            ins_price = input("RCV( Replacement Cost Value): ")
            sales_tax =input("Material Sales Tax")
            total_ins_price = float(ins_price) + int(deductible)
    elif paperwork.lower() == 'no':
        measure = input("Do you have measurements: ")
        if measure.lower() == 'yes':
            dimensions()
        elif measure.lower() == 'no':
            sq_ft = input("How many sqft is the house?")
            sleep(3)
            quit()
    else:
        print("-------")

dict_measurements = {
                     "Squares": "",
                     "Perimeter":"",
                     "Pitch": "",
                     "Hip": "",
                     "Ridge": "",
                     "Valley":"",
                                    }

def dimensions():
    global perimeter
    squares = input("SQ's: ")
    perimeter = input("Perimeter length: ")
    pitch = input("Pitch of roof: ")
    hip = input("Hip length: ")
    ridge = input("Ridge length:  ")
    valley = input("Valley length: ")
    dict_measurements["Perimeter"] = perimeter
    dict_measurements["Pitch"] = pitch
    dict_measurements["Hip"] = hip
    dict_measurements["Ridge"] = ridge
    dict_measurements["Valley"] = valley

dict_crew_pay = {
                 "High Pitch":"",
                 "Low Pitch": "",
                 "Ridge Pay": "",
                 "Starter Shingle Pay":"",
                 "Drip Edge Pay": "",
                 "Dumpster Fee": "",
}

def basic_pay():
    crew_pay_low = input("Crew Pay Low: ")
    crew_pay_high = input("Crew Pay High: ")
    additional_ridge = input("Ridge Pay: ")
    additional_starter = input("Starter Shingle Pay: ")
    additional_dripedge = input("Drip Edge Pay: ")
    dumpster_fee = input("Dumpster Fee: ")
    dict_crew_pay["High Pitch"] = crew_pay_high
    dict_crew_pay["Low Pitch"] = crew_pay_low
    dict_crew_pay["Ridge Pay"] = additional_ridge
    dict_crew_pay["Starter Shingle Pay"] = additional_starter
    dict_crew_pay["Drip Edge Pay"] = additional_dripedge
    dict_crew_pay["Dumpster Fee"] = dumpster_fee



dict_supplier_price = {
                        "Shingles":85,
                        "Ridge Cap Shingle": 60,
                        "Start Strip Shingle": 60,
                        "Roofing underlayment": 60,
                        "Ice & Water Sheild": 55,
                        "Ridge vent": 8.73,
                        "Drip Edge": 1.05,
                        "NP1": 5,
                        "OSB": 30,
                        "Coil Nails": 30,
                        "Cap Nails": 30,
                        "Pipe Vents": 10,
                        "Spray Paint": 6,

}






### Calculate the crew pay, shingles from supplier 




insurance()

# how_many_sqs = input("How many squares: ")
# crew_sqs = input("High or low pitch: ")
# material_sq = (int(how_many_sqs) * 90) * 1.08

# #material_tax = 1.08

# if crew_sqs.lower() == 'high' or 'h':
#     crew_per_sq = 65
# else:
#     crew_per_sq = 60

# crew_pay = crew_per_sq * int(how_many_sqs)

# insurance_pay_sq = total_ins_price // int(how_many_sqs)
# print(insurance_pay_sq)

# # I need to add another for retail and when measuring based on measurements only

# total_expenses = material_sq + crew_pay + 375
# if collect_deduc == 'no':
#     total_profit = total_ins_price - total_expenses - int(deductible)
# elif collect_deduc == 'yes':
#     total_profit = total_ins_price - total_expenses



# print("The total profit for this job is $" + str(total_profit))
# print("")
# # print("We can export this to excel ")
# print("")
# print("You material total with trailer is $" + str(material_sq))
# # print("Would you like me to send an order to supplier via email")
# # print("")
# print("You will pay your crew $" + str(crew_pay))
# print("I can setup an automatic email with total and payment reminder via email")