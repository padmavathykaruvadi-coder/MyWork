import numpy as np

np.random.seed(0)
a = np.random.randint(5, 51, size=(5, 50))

print("Avg per cycle:", a.mean(axis=1))
mx_idx = np.unravel_index(np.argmax(a), a.shape)
print("Max value & at (cycle,test):", a[mx_idx], mx_idx)
print("Std per cycle:", a.std(axis=1))

print("Cycle1 first10:", a[0, :10])
print("Cycle5 last5:", a[4, -5:])
print("Cycle3 alternate:", a[2, ::2])

print("C1+C2:", a[0] + a[1])
print("C1-C2:", a[0] - a[1])
print("C4*C5:", a[3] * a[4])
print("C4/C5:", a[3] / a[4])

print("Square:\n", np.power(a, 2))
print("Cube:\n", np.power(a, 3))
print("Sqrt:\n", np.sqrt(a.astype(float)))
print("Log:\n", np.log(a + 1))

b = a.view()
v1 = a[1, 0]
b[1, 0] += 1
print("Shallow changed original:", a[1, 0] != v1)
c = a.copy()
v2 = a[2, 0]
c[2, 0] += 1
print("Deep left original unchanged:", a[2, 0] == v2)

print("Cycle2 >30:", a[1, a[1] > 30])
mask = np.all(a > 25, axis=0)
print("Tests >25 in all cycles (indices):", np.where(mask)[0])
a_thresh = a.copy()
a_thresh[a_thresh < 10] = 10
print("Min-thresholded (first row):", a_thresh[0])
