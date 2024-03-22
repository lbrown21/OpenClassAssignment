# task 1 Validating Calculations


expression = "2 + 3 * 4"

result_without_parentheses = eval(expression)

expression_with_parentheses = "(" + expression + ")"
result_with_parentheses = eval(expression_with_parentheses)


if result_without_parentheses == result_with_parentheses:
    print("The results match!")
else:
    print("The results do not match.")
    



# task 2 Mix and Match

result = 10 + 5 > 15 or 2 * 3 == 6
print(result)

