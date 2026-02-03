# Neck
head:
- [6, 1, AVG, []]
- [[-1, 8], 1, Concat, [1]]
- [-1, 1, C2f, [512, 2, 1, 3, 9]]

- [-1, 1, nn.Upsample, [None, 2, "nearest"]]
- [8, 1, nn.Upsample, [None, 2, "nearest"]]
- [4, 1, AVG, []]
- [[-1, 6, -2, -3], 1, Concat, [1]]
- [-1, 1, C2f, [384, 2, 1, 3, 7]]

- [-1, 1, nn.Upsample, [None, 2, "nearest"]]
- [6, 1, nn.Upsample, [None, 2, "nearest"]]
- [2, 1, AVG, []]
- [[-1, 4, -2, -3], 1, Concat, [1]]
- [-1, 1, C2f, [384, 2, 1, 3, 5]]

- [16, 1, nn.Upsample, [None, 2, "nearest"]]
- [[-1, -2], 1, Concat, [1]]
- [-1, 1, C2f, [384, 2, 1, 3, 5]]

- [-1, 1, Conv, [384, 3, 2]]
- [21, 1, AVG, []]
- [11, 1, nn.Upsample, [None, 2, "nearest"]]
- [[-2, -1, 16, -3], 1, Concat, [1]]
- [-1, 1, C2f, [384, 2, 1, 3, 7]]

- [-1, 1, Conv, [384, 3, 2]]
- [16, 1, AVG, []]
- [[-2, -1, 11], 1, Concat, [1]]
- [-1, 1, C2f, [512, 2, 1, 3, 9]]

- [[24, 29, 33], 1, Detect, [nc]]  # Detect(P3, P4, P5)