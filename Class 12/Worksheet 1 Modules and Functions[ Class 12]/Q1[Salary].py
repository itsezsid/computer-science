exp = []
print("Question 1 by Siddharth")
salary = int(input("Enter your Salary: "))


def total_expenditure(main_dict, salary):
    expense = 0
    global exp
    res = []
    for i in main_dict.keys():  # Calculate total expenses
        exp.append(expense)
        expense = 0
        for j in main_dict[i].values():
            for k in j:

                expense = expense + k

    exp.append(expense)
    del exp[0]
    for i in range(0, len(exp)):
        if salary - exp[i] > 0:
            res.append("Surplus")

        elif salary - exp[i] < 0:
            res.append("Deficit")

    return res


def suggest(result, salary):
    for i in range(0, len(result)):
        if result[i] == "Surplus":
            amt = salary - exp[i]
            print("Invest", amt)
        elif result[i] == "Deficit":
            amt = exp[i] - salary
            print("Change plan or stop spending", amt)


main_dict = {
    'Jan': {
        'Monthly': [15000, 2000],
        'Variable': [2000, 0]
    },
    'Feb': {
        'Monthly': [15000, 800],
        'Variable': [1500, 100]
    }
}

result = total_expenditure(main_dict, salary)
suggest(result, salary)
