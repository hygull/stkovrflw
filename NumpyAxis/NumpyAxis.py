import numpy as np



a = np.random.random((3, 3, 3)) + 1j * np.random.random((3, 3, 3))
print(a, '\n\n')

amp3d = np.abs(a)
print(amp3d, '\n\n')

amp2d = np.max(amp3d, axis=2)
print(amp3d, '\n\n')

angle2d =  np.zeros_like(amp2d)
print(angle2d, '\n\n')

print(a.shape[0], "**********")
print(a.shape[1], "::::::::::::::")
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            if amp3d[i, j, k] == amp2d[i,j]:
                angle2d[i, j] = np.angle(a[i, j, k])

print(angle2d)