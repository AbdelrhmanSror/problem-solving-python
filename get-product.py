# given arrays of integers,return a new array such that each element at index i of the new array is the product of
# all element in the original array. e.g. input : [1 , 2 , 3 ,4 , 5]    output:[120 ,60 ,40 , 30 ,24]
# e.g. input : [3 , 2 , 1 ]   output :[2 ,3 , 6]

def product_with_division(input):
    multiplication = 1
    for number in input:
        multiplication *= number

    output = [multiplication / number for number in input]

    return output

def product_without_division(input):
    product_before = [1]
    product_after = [1]
    output = []
    current_product = input[0]
    for item in input[1:]:
        product_before.append(current_product)
        current_product *= item
    current_product = input[-1]
    for i in reversed(range(len(input)-1)):
        product_after.append(current_product)
        current_product *= input[i]
    product_after.reverse()
    output=[before*after for before, after in zip(product_before, product_after)]

    print(output)


product_without_division([1, 2, 3, 4, 5])
