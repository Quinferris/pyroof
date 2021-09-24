
# def dimensions():
#     dict_measurements["Squares"] = input("SQ's: ")
#     dict_measurements["Perimeter"] = input("Perimeter length: ")
#     dict_measurements["Pitch"] = input("Pitch of roof: ")
#     dict_measurements["Hip"] = input("Hip length: ")
#     dict_measurements["Ridge"] = input("Ridge length:  ")
#     dict_measurements["Valley"] = input("Valley length: ")

# dict_measurements = {
#                      "Squares": "",
#                      "Perimeter":"",
#                      "Pitch": "",
#                      "Hip": "",
#                      "Ridge": "",
#                      "Valley":"",
#                                     }


# def basic_pay():
#     # crew_pay_low = input("Crew Pay Low: ")
#     # crew_pay_high = input("Crew Pay High: ")
#     # additional_ridge = input("Ridge Pay: ")
#     # additional_starter = input("Starter Shingle Pay: ")
#     # additional_dripedge = input("Drip Edge Pay: ")
#     # dumpster_fee = input("Dumpster Fee: ")
#     dict_crew_pay["High Pitch"] = input("Crew Pay High: ")
#     dict_crew_pay["Low Pitch"] = input("Crew Pay Low: ")
#     dict_crew_pay["Ridge Pay"] = input("Ridge Pay: ")
#     dict_crew_pay["Starter Shingle Pay"] = input("Starter Shingle Pay: ")
#     dict_crew_pay["Drip Edge Pay"] =  input("Drip Edge Pay: ")
#     dict_crew_pay["Dumpster Fee"] = input("Dumpster Fee: ")


# dict_crew_pay = {
#                  "High Pitch":"",
#                  "Low Pitch": "",
#                  "Ridge Pay": "",
#                  "Starter Shingle Pay":"",
#                  "Drip Edge Pay": "",
#                  "Dumpster Fee": "",
# }
# dimensions()
# print("- - - - - - - - - - - - -")
# basic_pay()
# print("- - - - - - Doing some math, BRB - - - - - -")


# calc_crew_pay = 0
# sq_ft = 25
# sq_fts = 100


# if dict_crew_pay["High Pitch"] != "":
#     a = int(dict_measurements["Squares"]) * int(dict_crew_pay["High Pitch"])
#     b = (int(dict_measurements["Ridge"]) + int(dict_measurements["Hip"])) * float(dict_crew_pay["Ridge Pay"]) or int(dict_crew_pay["Ridge Pay"])
#     c = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Starter Shingle Pay"]) or int(dict_crew_pay["Starter Shingle Pay"])
#     d = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Drip Edge Pay"]) or int(dict_crew_pay["Ridge Pay"])
#     e = int(dict_crew_pay["Dumpster Fee"])
#     calc_crew_pay = a + b + c + d + e
#     print("For job ____ you will be the pay crew" + str(calc_crew_pay))
# elif dict_crew_pay["Low Pitch"] != "":
#     a = int(dict_measurements["Squares"]) * int(dict_crew_pay["Low Pitch"])
#     b = (int(dict_measurements["Ridge"]) + int(dict_measurements["Hip"])) * float(dict_crew_pay["Ridge Pay"]) or int(dict_crew_pay["Ridge Pay"])
#     c = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Starter Shingle Pay"]) or int(dict_crew_pay["Starter Shingle Pay"])
#     d = int(dict_measurements["Perimeter"]) * float(dict_crew_pay["Drip Edge Pay"]) or int(dict_crew_pay["Ridge Pay"])
#     e = int(dict_crew_pay["Dumpster Fee"])
#     calc_crew_pay = a + b + c + d + e
#     print("For job ____ you will be the pay crew" + str(calc_crew_pay))



def dimensions():
    dict_measurements["Squares"] = input("SQ's: ")
    dict_measurements["Perimeter"] = input("Perimeter length: ")
    # dict_measurements["Pitch"] = input("Pitch of roof: ")
    # dict_measurements["Hip"] = input("Hip length: ")
    # dict_measurements["Ridge"] = input("Ridge length:  ")
    # dict_measurements["Valley"] = input("Valley length: ")

dict_measurements = {
                     "Squares": "",
                    #  "Perimeter":"",
                    #  "Pitch": "",
                    #  "Hip": "",
                    #  "Ridge": "",
                    #  "Valley":"",
                                    }


dict_supplier_price = {
                        "Shingles":85,
                        "Ridge Cap Shingle": 60,
                        "Start Strip Shingle": 50,
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

calc_material_list = {
                        "Shingles":0,
                        "Ridge Cap Shingle": 0,
                        "Start Strip Shingle": 0,
                        "Roofing underlayment": 0,
                        "Ice & Water Sheild": 0,
                        "Ridge vent": 0,
                        "Drip Edge": 0,
                        "NP1": 0,
                        "OSB": 0,
                        "Coil Nails": 0,
                        "Cap Nails": 0,
                        "Pipe Vents": 0,
                        "Spray Paint": 0,
}

bundles = 3
ridgecap = 29
valleys = 100
ridgevent = 10
coilnls = 17
starterstrip = 100

calc_total_material_cost = 0
while calc_total_material_cost == 0:

        squs = int(dict_measurements["Squares"]) * int(dict_supplier_price["Shingles"])
        #srtstrip = (int(dict_measurements["Perimeter"]) / int(starterstrip))  * int(dict_supplier_price["Start Strip Shingle"])




        calc_total_material_cost = squs 




print(squs)
#print(srtstrip)



# if __name__ == '__main__':
#     dimensions()