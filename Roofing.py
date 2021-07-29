from time import sleep
# print("""HELLO
# THERE ARE A FEW TASK THAT TAKE LESS THAN 2 MINUTES TO COMPLETE:
# -Define your crew pay for low pitch, usually roofs with no harness
# -Define your crew pay for high pitch, usually roof with harness
# -Define your cost per square on BASIC roof system
# -Define cost for dumpster/trailer
#     - Pick as many as needed
#     - Different supplies roofing systems you sell
#     - GAF Timberline, GAF HDZ, GAF Natural Shadow
# - Email verification for emailing supplier order list
# - Decide if you want to export job details to excel
# - Tax rate
# - Optional Drip Edge Factored into material per sq or add it """)
def measurements():
    global perimeter
    perimeter = input("Perimeter length: ")
    hip = input("Hip length: ")
    ridge = input("Ridge length: ")


def measure():
    amount_sqs = perimeterrin


def insurance():
    global total_ins_price
    global collect_deduc
    global deductible
    paperwork = input("Do you have paperwork: ")
    if paperwork.lower() == 'yes':
        collect_deduc = input("Are you collecting deductible?")
        if collect_deduc.lower() == "yes":
            deductible = input("Deductible: ")
            ins_price = input("Total Amount Claim If Incurred:")
            total_ins_price = float(ins_price) + int(deductible)
            print(total_ins_price)
        elif collect_deduc.lower() == "no":
            deductible = input("Deductible: ")
            ins_price = input("Total Amount Claim If Incurred:")
            total_ins_price = float(ins_price) + int(deductible)
    elif paperwork.lower() == 'no':
        measure = input("Do you have measurements: ")
        if measure.lower() == 'yes':
            measurements()
        elif measure.lower() == 'no':
            sq_ft = input("how much sqft is the house?")
            sleep(3)
            quit()
    else:
        print("-------")



def retail():
    paperwork = input("Do you have paperwork: ")

    if paperwork == 'yes':
        sqs = int(input(""))
    elif paperwork == 'no':
        measure = input("Do you have measurements: ")
        if measure.lower() == 'yes':
            pass



job_type = input("""
                    Insurance(I) or RETAIL(R)
                    -------------------------
                    What kind of job is this: """)
if job_type.lower() == 'insurance' or 'i':
    insurance()
elif job_type.lower() == 'retail' or 'r':
    retail()
#     paperwork = input("Do you have paperwork: ")
#     if paperwork.lower() == 'yes':
#         collect_deduc = input("Are you collecting deductible?")
#         if collect_deduc.lower() == "yes":
#             deductible = input("Deductible: ")
#             ins_price = input("Total Amount Claim If Incurred:")
#             total_ins_price = float(ins_price) + int(deductible)
#             print(total_ins_price)
#         elif collect_deduc.lower() == "no":
#             deductible = input("Deductible: ")
#             ins_price = input("Total Amount Claim If Incurred:")
#             total_ins_price = float(ins_price) + int(deductible)
#     elif paperwork.lower() == 'no':
#         print("Please get paperwork for instant profit & details")
#
#
# if job_type.lower() == 'retail':

how_many_sqs = input("How many squares: ")
crew_sqs = input("High or low pitch: ")

material_sq = (int(how_many_sqs) * 90) * 1.08
#material_tax = 1.08

if crew_sqs.lower() == 'high' or 'h':
    crew_per_sq = 65
else:
    crew_per_sq = 60

crew_pay = crew_per_sq * int(how_many_sqs)

insurance_pay_sq = total_ins_price // int(how_many_sqs)
print(insurance_pay_sq)

# I need to add another for retail and when measuring based on measurements only

total_expenses = material_sq + crew_pay + 375
if collect_deduc == 'no':
    total_profit = total_ins_price - total_expenses - int(deductible)
elif collect_deduc == 'yes':
    total_profit = total_ins_price - total_expenses



print("The total profit for this job is $" + str(total_profit))
print("")
# print("We can export this to excel ")
print("")
print("You material total with trailer is $" + str(material_sq))
# print("Would you like me to send an order to supplier via email")
# print("")
print("You will pay your crew $" + str(crew_pay))
print("I can setup an automatic email with total and payment reminder via email")

