#Random Password Generator

import random

LetrM1 = chr(random.randint(65,90))
Letrm1 = chr(random.randint(97,122))
Dig1 = chr(random.randint(48,57))
Sin1 = chr(random.randint(32,64))
LetrM2 = chr(random.randint(65,90))
Letrm2 = chr(random.randint(97,122))
Dig2 = chr(random.randint(48,57))
Sin2 = chr(random.randint(32,64))

list = [LetrM1, LetrM2, Dig1, Dig2, Letrm1, Letrm2, Sin1, Sin2]

random.shuffle(list)
print(list)