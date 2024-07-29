import unittest

from src.State import State

class TestState(unittest.TestCase):
    def setUp(self):
        """
        Initializes a State instance for each test.
        """
        self.unaccepting_state = State('q0', False)
        self.accepting_state = State('q1', True)

    def test_initialization(self):
        """
        Tests the State's initialization. Checks name, is_accepting, and transitions.
        """
        print("\nRunning State initialization tests...\n")
        self.assertEqual(self.unaccepting_state.get_name(), 'q0')
        self.assertFalse(self.unaccepting_state.get_is_accepting())

        self.assertEqual(self.accepting_state.get_name(), 'q1')
        self.assertTrue(self.accepting_state.get_is_accepting())
        print("State initialization tests passed!")

    def test_add_transition(self):
        """
        Tests the State's add_transition method.
        """
        print("\nRunning State add transition tests...\n")
        self.accepting_state.add_transition('b', self.unaccepting_state)
        self.assertEqual(self.accepting_state.get_next_state('b'), self.unaccepting_state)

        next_state = State('q2', True)
        self.unaccepting_state.add_transition('a', next_state)
        self.assertEqual(self.unaccepting_state.get_next_state('a'), next_state)
        print("State add transition tests passed!")

if __name__ == '__main__':
    unittest.main()
    

    
