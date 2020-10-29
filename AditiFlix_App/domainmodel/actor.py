
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__actor_colleague_list = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_colleague_list(self) -> str:
        return self.__actor_colleague_list
        #return iter(self.__actor_colleague_list)

    def get_next_colleague(self):
        return iter(self.__actor_colleague_list)

    @actor_colleague_list.setter
    def actor_colleague_list(self, new_list):  # Only adds in legitimate actors. Completely replaces the original
        self.__actor_colleague_list = list()
        if type(new_list) == list:
            for element in new_list:
                if not isinstance(element, Actor):
                    raise ValueError
                    return -1
                elif element.actor_full_name is not None:
                    self.__actor_colleague_list.append(element)
        return 1

    def add_actor_colleague(self, colleague: 'Actor'):
        if not isinstance(colleague, Actor):
            return -1
        elif self.check_if_this_actor_worked_with(colleague):
            return 0
        elif colleague.actor_full_name is None:
            return 0
        else:
            self.__actor_colleague_list.append(colleague)
        return 1

    def check_if_this_actor_worked_with(self, colleague: 'Actor'):
        if colleague in self.__actor_colleague_list:
            return True
        else:
            return False

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        return False

    def __hash__(self):
        return hash((self.actor_full_name,))
