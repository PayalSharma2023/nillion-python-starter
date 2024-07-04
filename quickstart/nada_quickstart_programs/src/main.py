from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")

    # Inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))
    my_int3 = SecretInteger(Input(name="my_int3", party=party3))

    # Operations
    sum_ab = my_int1 + my_int2
    diff_ac = my_int1 - my_int3
    product_bc = my_int2 * my_int3

    # Constant
    constant_200 = ConstantInteger(200)

    # Conditional logic
    condition = (sum_ab + product_bc) > constant_200
    final_result = Select(condition, sum_ab * diff_ac, product_bc + my_int3)

    # Outputs
    return [
        Output(sum_ab, "sum_ab_output", party1),
        Output(diff_ac, "diff_ac_output", party2),
        Output(product_bc, "product_bc_output", party3),
        Output(final_result, "final_result_output", party4)
    ]
