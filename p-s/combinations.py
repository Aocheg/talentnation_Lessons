"""COMBINATION
Combination means selecting items from a collection where the order of selection does not matter."""

# Python does not have a special combination loop,
# However, provides a useful tool:
"""itertools where you import combinations"""

from itertools import combinations

musiscians = ["John", "Mary", "Peter"]
pairs = combinations(musiscians, 2)

print(list(pairs))


"""NOTE: The principle of COmbination: The identity of the group maters, 
not the orderd in whih its members were selected."""

"""itertools.combinations() generate selections without replacement. that means
once an item has been selected in a particular combination, it cannot appear 
agin in that same combination."""

filters = ["Warm", "Cool", "Vintage", "Natural"]

result = combinations(filters, 2)

# If you want to reuse combinations, save them in a list so it can be reuseable.
saved_results = list(combinations(filters, 2))

print(list(result))
print(list(saved_results))

players = ["John", "Mary", "Peter"]
result = combinations(players, 4)

print(list(result))

"""From the COmbination, i have been able to learn the following:
1. Understanding Combinations
2. Order-independent selection
3. Manually identifying iterators
4. understnanding iterators
5. Comsumed iterators
6. Select more items than available

5 IMPORTANT LESSONS TO RETAIN FROM THIS TOPIC
1. Combination select items without considering their order.
2. itertools.combinations() generate combinations.
3. combinations() returns an iterator.
5. An iterator that has been exhausted cannot produce its previous results again."""