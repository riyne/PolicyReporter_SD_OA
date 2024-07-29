class State:
    def __init__(self, name: str, is_accepting: bool = False):
        """
        Initializes a state.

        :param name: Name of the state
        :param is_accepting: Boolean indicating if this is an accepting state
        """
        self.__name = name
        self.__is_accepting = is_accepting
        self.__transitions = {}

    def add_transition(self, input_char: str, next_state: 'State'):
        """
        Adds a transition for this state.

        :param input_char: Input character that triggers the transition
        :param next_state: The state to transition to
        """
        self.__transitions[input_char] = next_state

    def get_next_state(self, input_char: str) -> 'State':
        """
        Returns the next state for a given input character.

        :param input_char: Input character
        :return: Next state
        """
        return self.__transitions.get(input_char)
    
    def get_name(self) -> str:
        """
        Getter for the name of the state.

        :return: The name of the state
        """
        return self.__name
    
    def get_is_accepting(self) -> bool:
        """
        Getter for whether the state is accepting.

        :return: True if the state is an accepting state, else False
        """
        return self.__is_accepting