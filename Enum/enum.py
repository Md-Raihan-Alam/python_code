from enum import Enum
# only way to create constant
class State(Enum):
    INACTIVE=0
    ACTIVE=1
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])