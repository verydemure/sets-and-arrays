setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("original set elements:")
print(setx)
print(sety)


print("\nintersection of two said sets:")
setz =  setx.intersection(sety)
print(setz)

print("\nIntersection of two said sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two said sets:")
setz =  setx.difference(sety)
print(setz)

print("\nSymmetric Difference of two said sets:")
setz =  setx.symmetric_difference(sety)
print(setz)
