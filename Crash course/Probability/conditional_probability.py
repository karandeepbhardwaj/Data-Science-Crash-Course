import enum, random

class kid(enum.Enum):
    
    BOY = 0
    GIRL = 1
    
def random_kid() -> kid:
    return random.choice([kid.BOY, kid.girl])

both_girls =0
either_girl =0
older_girl =0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    
    if older == kid.GIRL:
        older_girl += 1     
    if older == kid.GIRL  and younger == kid.GIRL:
        both_girls += 1
    if older == kid.GIRL or younger == kid.GIRL:
        either_girl += 1
        
print("P(both | older): ", both_girls / older_girl)
print("P(both | either): ", both_girls / either_girl)