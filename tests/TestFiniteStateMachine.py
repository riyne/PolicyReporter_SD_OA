import unittest

from src.FiniteStateMachine import FiniteStateMachine

class TestFiniteStateMachine(unittest.TestCase):
    def setUp(self):
        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['a', 'b']
        self.initial_state = 'q0'
        self.accepting_states = ['q2']
        self.transition_function = {
            ('q0', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q0'
        }
        self.fsm = FiniteStateMachine(self.states, self.alphabet, self.initial_state, self.accepting_states, self.transition_function)

    def test_initialization(self):
        """
        Tests the FSM's initialization. Checks states, alphabet, initial state, current state, and accepting states.
        """
        print("\nRunning FiniteStateMachine initialization tests...\n")
        state_names = [state for state in self.fsm.get_states()]
        self.assertEqual(state_names, self.states)

        self.assertEqual(self.fsm.get_alphabet(), self.alphabet)

        self.assertEqual(self.fsm.get_initial_state(), self.initial_state)

        self.assertEqual(self.fsm.get_current_state(), self.initial_state)

        self.assertTrue(self.fsm.get_states()['q2'].get_is_accepting())
        self.assertFalse(self.fsm.get_states()['q0'].get_is_accepting())
        self.assertFalse(self.fsm.get_states()['q1'].get_is_accepting())
        print("FiniteStateMachine initialization tests passed!")

    def test_reset(self):
        """
        Tests the FSM's reset method.
        """
        print("\nRunning FiniteStateMachine reset tests...\n")
        self.fsm.process_input('a')
        self.fsm.reset()
        self.assertEqual(self.fsm.get_current_state(), self.initial_state)
        print("FiniteStateMachine reset tests passed!")

    def test_transitions(self):
        """
        Tests the FSM's transitions for all valid inputs.
        """
        print("\nRunning FiniteStateMachine transition tests...\n")
        self.assertEqual(self.fsm.get_states()['q0'].get_next_state('a').get_name(), 'q1')
        self.assertEqual(self.fsm.get_states()['q1'].get_next_state('b').get_name(), 'q2')
        self.assertEqual(self.fsm.get_states()['q2'].get_next_state('a').get_name(), 'q0')
        print("FiniteStateMachine transition tests passed!")

if __name__ == '__main__':
    unittest.main()