from .State import State

class FiniteStateMachine:
    def __init__(self, states: dict[str, State], alphabet: list[str], initial_state: str, accepting_states: list[str], transition_function: dict[tuple[str, str], str]):
        """
        Initializes the finite state machine.

        :param states: List of state names
        :param alphabet: List of input symbols
        :param initial_state: Initial state name
        :param accepting_states: List of accepting/final state names
        :param transition_function: Dictionary representing the state transitions
        """
        self.__states = {name: State(name, name in accepting_states) for name in states}
        self.__alphabet = alphabet
        self.__initial_state = self.__states[initial_state]
        self.__current_state = self.__initial_state

        # Set up transitions
        for (state_name, char), next_state_name in transition_function.items():
            self.__states[state_name].add_transition(char, self.__states[next_state_name])

    def reset(self):
        """
        Resets the FSM to its initial state.
        """
        self.__current_state = self.__initial_state

    def process_input(self, input_str: str):
        """
        Processes an input string and updates the current state accordingly.

        :param input_str: String of input characters
        :raises ValueError: If an invalid input character is encountered or there is no transition state defined for the state
        """
        for char in input_str:
            if char not in self.__alphabet:
                raise ValueError(f"Invalid input character: {char}")
            next_state = self.__current_state.get_next_state(char)
            if next_state is None:
                raise ValueError(f"No transition defined for state {self.__current_state.name} on input {char}")
            self.__current_state = next_state

    def get_current_state(self) -> str:
        """
        Returns the current state of the FSM.

        :return: Current state
        """
        return self.__current_state.get_name()
    
    def get_alphabet(self) -> list[str]:
        """
        Returns the alphabet of the FSM.

        :return: Alphabet
        """
        return self.__alphabet
    
    def get_states(self) -> dict[str, State]:
        """
        Returns the states of the FSM.

        :return: States
        """
        return self.__states
    
    def get_initial_state(self) -> str:
        """
        Returns the initial state of the FSM.

        :return: Initial state
        """
        return self.__initial_state.get_name()

    def is_accepting(self) -> bool:
        """
        Checks if the current state is an accepting state.

        :return: True if the current state is accepting, else False
        """
        return self.__current_state.get_is_accepting()