"""COMBINATION
Combination means selecting items from a collection where the order of selection does not matter."""

# Python does not have a special combination loop,
# However, provides a useful tool:
"""itertools where you import combinations"""

from itertools import combinations

musiscians = ["John", "Mary", "Peter"]
pairs = combinations(musiscians, 2)

print(list(pairs))


"""NOTE: The principle of COmbination: The identity of the group maters, not the orderd in whih its members were selected."""

"""itertools.combinations() generate selections without replacement. that means
once an item has been selected in a particular combination, it cannot appear agin in that same combination."""

filters = ["Warm", "Cool", "Vintage", "Natural"]

result = combinations(filters, 2)

print(list(result))
print(list(result))