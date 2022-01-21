# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)


conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_intercept = conjunto.intersection(conjunto2)
print(conjunto_intercept)

conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)


