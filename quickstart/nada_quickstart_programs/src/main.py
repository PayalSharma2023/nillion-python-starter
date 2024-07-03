from nada_dsl import *

def nada_main():
    # Define the parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")

    # Define secret inputs for each party
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Perform some operations
    sum_ab = a + b
    product = sum_ab * c
    sum_all = a + b + c
    product_all = a * b * c

    # Apply some conditional logic
    condition = sum_all > 100
    result = condition.select(product_all, sum_all)

    # Define outputs for each party
    output1 = Output(sum_ab, "sum_ab_output", party1)
    output2 = Output(product, "product_output", party2)
    output3 = Output(result, "result_output", party4)

    return [output1, output2, output3]
