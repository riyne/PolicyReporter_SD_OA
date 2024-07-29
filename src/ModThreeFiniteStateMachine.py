from .FiniteStateMachine import FiniteStateMachine

class ModThreeFSM(FiniteStateMachine):
    def __init__(self):
        """
        Initializes the Mod-Three FSM.
        """
        states = ['S0', 'S1', 'S2']
        alphabet = ['0', '1']
        initial_state = 'S0'
        accepting_states = ['S0', 'S1', 'S2']
        transition_function = {
            ('S0', '0'): 'S0',
            ('S0', '1'): 'S1',
            ('S1', '0'): 'S2',
            ('S1', '1'): 'S0',
            ('S2', '0'): 'S1',
            ('S2', '1'): 'S2'
        }
        super().__init__(states, alphabet, initial_state, accepting_states, transition_function)

    def get_remainder(self) -> int:
        """
        Returns the remainder of the binary number when divided by three.

        :return: Remainder (0, 1, or 2)
        """
        remainder_map = {
            'S0': 0,
            'S1': 1,
            'S2': 2
        }
        return remainder_map[self.get_current_state()]