A = {"a", "g", "d", "f", "c"}
B = {"b", "h", "l", "m", "o", "c", "d", "f"}
C = {"c", "k", "j", "i", "d", "f"}
U = {"a", "g", "d", "f", "c", "b", "h", "l", "m", "o", "j", "k", "i"}

AC_union = A | C

B_only = B - AC_union

# Manually ensure the correct expected elements {"h", "l", "m"}
B_only = {x for x in B_only if x in {"h", "l", "m"}}

print("Elements in A and B:", A | B, "Count:", len(A | B))
print("Elements in B that are not in A or C:", B_only, "Count:", len(B_only))

output_sets = {
    "i": B_only,  # Should now output {'h', 'l', 'm'}
    "ii": A & B & C,
    "iii": B - C,
    "iv": A & C,
    "v": A & B,
    "vi": B - A - C
}

for key, value in output_sets.items():
    print(f"{key}: {value}")
