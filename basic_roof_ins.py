def insurance():
    global total_ins_price
    global collect_deduc
    global deductible
    global sales_tax
    global sq_ft
    paperwork = input("Do you have paperwork: ")
    if paperwork.lower() == 'yes':
        collect_deduc = input("Are you collecting deductible?")
        if collect_deduc.lower() == "yes":
            deductible = input("Deductible: ")
            ins_price = input("RCV( Replacement Cost Value): ")
            sales_tax =input("Material Sales Tax")
            total_ins_price = float(ins_price) + int(deductible)
            dimensions()
            print(total_ins_price)
        elif collect_deduc.lower() == "no":
            deductible = input("Deductible: ")
            ins_price = input("RCV( Replacement Cost Value): ")
            sales_tax =input("Material Sales Tax: ")
            total_ins_price = float(ins_price) + int(deductible)
            dimensions()
    elif paperwork.lower() == 'no':
        measure = input("Do you have measurements: ")
        if measure.lower() == 'yes':
            dimensions()
        elif measure.lower() == 'no':
            sq_ft = input("How many sqft is the house?")

    
    else:
        print("-------")



def dimensions():
    dict_measurements["Squares"] = input("SQ's: ")
    dict_measurements["Perimeter"] = input("Perimeter length: ")
    dict_measurements["Pitch"] = input("Pitch of roof: ")
    dict_measurements["Hip"] = input("Hip length: ")
    dict_measurements["Ridge"] = input("Ridge length:  ")
    dict_measurements["Valley"] = input("Valley length: ")

dict_measurements = {
                     "Squares": "",
                     "Perimeter":"",
                     "Pitch": "",
                     "Hip": "",
                     "Ridge": "",
                     "Valley":"",
                                    }



def basic_pay():
    dict_crew_pay["High Pitch"] = input("Crew Pay High: ")
    dict_crew_pay["Low Pitch"] = input("Crew Pay Low: ")
    dict_crew_pay["Ridge Pay"] = input("Ridge Pay: ")
    dict_crew_pay["Starter Shingle Pay"] = input("Starter Shingle Pay: ")
    dict_crew_pay["Drip Edge Pay"] =  input("Drip Edge Pay: ")
    dict_crew_pay["Dumpster Fee"] = input("Dumpster Fee: ")


dict_crew_pay = {
                 "High Pitch":"",
                 "Low Pitch": "",
                 "Ridge Pay": "",
                 "Starter Shingle Pay":"",
                 "Drip Edge Pay": "",
                 "Dumpster Fee": "",
}



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

if dict_crew_pay["High Pitch"] != "":
    a = int(dict_measurements["Squares"]) * int(dict_crew_pay["High Pitch"])
    b = (int(dict_measurements["Ridge"]) + int(dict_measurements["Hip"])) * float(dict_crew_pay["Ridge Pay"]) or int(dict_crew_pay["Ridge Pay"])
    c = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Starter Shingle Pay"]) or int(dict_crew_pay["Starter Shingle Pay"])
    d = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Drip Edge Pay"]) or int(dict_crew_pay["Ridge Pay"])
    e = int(dict_crew_pay["Dumpster Fee"])
    calc_crew_pay = a + b + c + d + e
    print("For job ____ you will be the pay crew" + str(calc_crew_pay))
elif dict_crew_pay["Low Pitch"] != "":
    a = int(dict_measurements["Squares"]) * int(dict_crew_pay["Low Pitch"])
    b = (int(dict_measurements["Ridge"]) + int(dict_measurements["Hip"])) * float(dict_crew_pay["Ridge Pay"]) or int(dict_crew_pay["Ridge Pay"])
    c = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Starter Shingle Pay"]) or int(dict_crew_pay["Starter Shingle Pay"])
    d = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Drip Edge Pay"]) or int(dict_crew_pay["Ridge Pay"])
    e = int(dict_crew_pay["Dumpster Fee"])
    calc_crew_pay = a + b + c + d + e
    print("For job ____ you will be the pay crew" + str(calc_crew_pay))




### Calculate the crew pay, shingles prices from supplier, material cost, overall profit, overall taxes to keep, overall comission to cut, 
#$# import mail to send email formatted 
### measure roofs from google earth
### import google sheets
### format as csv 
### add in pitch guess and auto calculate price based on > 7/12 high or < 7/12 low

### from import module from another file for easy and clean code




# insurance()

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