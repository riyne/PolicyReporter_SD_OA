import unittest

from src.ModThreeFiniteStateMachine import ModThreeFSM

class TestModThreeFSM(unittest.TestCase):
    def setUp(self):
        """ 
        Initializes a ModThreeFSM instance for each test.
        """
        self.fsm = ModThreeFSM()

    def test_initial_state(self):
        """
        Test that the FSM starts in the correct initial state.
        """
        print("\nRunning ModThreeFSM initial state tests...\n")
        self.assertEqual(self.fsm.get_current_state(), 'S0')
        self.assertTrue(self.fsm.is_accepting())
        print("ModThreeFSM initial state tests passed!")

    def test_process_input_valid(self):
        """
        Test processing of valid inputs.
        """
        print("\nRunning ModThreeFSM process input tests...\n")
        test_cases = [
            ('0', 'S0', 0),
            ('1', 'S1', 1),
            ('10', 'S2', 2),
            ('11', 'S0', 0),
            ('110', 'S0', 0),
            ('111', 'S1', 1),
            ('10101', 'S0', 0)
        ]

        for input_str, expected_state, expected_remainder in test_cases:
            self.fsm.reset()
            self.fsm.process_input(input_str)
            self.assertEqual(self.fsm.get_current_state(), expected_state)
            self.assertEqual(self.fsm.get_remainder(), expected_remainder)
        print("ModThreeFSM process input tests passed!")

    def test_invalid_input(self):
        """
        Test that invalid input raises a ValueError.
        """
        print("\nRunning ModThreeFSM invalid input tests...\n")
        with self.assertRaises(ValueError):
            self.fsm.process_input('2')
        with self.assertRaises(ValueError):
            self.fsm.process_input('a')
        print("ModThreeFSM invalid input tests passed!")

    def test_transitions(self):
        """
        Test the FSM transitions for all valid inputs.
        """
        print("\nRunning ModThreeFSM transition tests...\n")
        self.fsm.reset()
        self.assertEqual(self.fsm.get_current_state(), 'S0')

        self.fsm.process_input('1')
        self.assertEqual(self.fsm.get_current_state(), 'S1')
        self.assertEqual(self.fsm.get_remainder(), 1)

        self.fsm.process_input('0')
        self.assertEqual(self.fsm.get_current_state(), 'S2')
        self.assertEqual(self.fsm.get_remainder(), 2)

        self.fsm.process_input('1')
        self.assertEqual(self.fsm.get_current_state(), 'S2')
        self.assertEqual(self.fsm.get_remainder(), 2)

        self.fsm.process_input('0')
        self.assertEqual(self.fsm.get_current_state(), 'S1')
        self.assertEqual(self.fsm.get_remainder(), 1)

        self.fsm.process_input('1')
        self.assertEqual(self.fsm.get_current_state(), 'S0')
        self.assertEqual(self.fsm.get_remainder(), 0)
        print("ModThreeFSM transition tests passed!")

    def test_get_remainder(self):
        """
        Test the FSM get_remainder method.
        """
        print("\nRunning ModThreeFSM get remainder tests...\n")
        self.fsm.reset()
        self.assertEqual(self.fsm.get_remainder(), 0)

        self.fsm.process_input('1')
        self.assertEqual(self.fsm.get_remainder(), 1)

        self.fsm.process_input('0')
        self.assertEqual(self.fsm.get_remainder(), 2) 
        print("ModThreeFSM get remainder tests passed!")

if __name__ == '__main__':
    unittest.main()