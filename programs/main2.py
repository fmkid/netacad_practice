from sys import path

path.append("packages")

import extra.iota #importar modulo iota

print(extra.iota.FunI())
path.pop()