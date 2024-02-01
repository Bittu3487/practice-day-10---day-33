def add(first_num , second_num):
    return first_num + second_num
def sub(first_num , second_num):
    return first_num - second_num
def mutipy(first_num , second_num):
    return first_num * second_num
def divide(first_num , second_num):
    return first_num / second_num
operations = {
    "+":add,
    "-":sub,
    "*":mutipy,
    "/":divide,
}
def calculator():
    first_num = float(input("what was the first number?"))
    is_on = True
    while is_on:
        second_num = float(input("what was the next number?"))
        for symbol in  operations:
            print(symbol)
        operations_symbol = input("what was the operation?")
        calculation = operations[operations_symbol]
        answer = calculation(first_num,second_num)
        result = f"result: {first_num}{operations_symbol}{second_num} = {answer}"
        c = input(f"type 'y' continue calculating with {result}  or type 'n' to start a new calculation")
        if c == "y":
            first_num = answer
        else:
            is_on = False
            calculator()


calculator()
        
