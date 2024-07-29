from src.ModThreeFiniteStateMachine import ModThreeFSM

def mod_three(input_str):
    """
    Computes the remainder of a binary number when divided by three using a Mod-Three FSM.

    :param input_str: Binary string input
    :return: Remainder (0, 1, or 2)
    """
    fsm = ModThreeFSM()
    fsm.process_input(input_str)
    return fsm.get_remainder()

if __name__ == "__main__":
    examples = ['1101', '1110', '1111', '110', '1010', '0']
    for example in examples:
        print(f"Input: '{example}' ({int(example, 2)}), Output: {mod_three(example)}")