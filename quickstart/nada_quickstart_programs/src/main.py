from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
   
    # Perform some operations
    sum_ab = a + b
   

    # Apply some conditional logic
    

    # Define outputs for each party
    output1 = Output(sum_ab, "sum_ab_output", party1)
   
    return [output1]