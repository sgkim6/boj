T = int(input())

for test_case in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        planets.append((cx, cy, r))

    for planet in planets:
        d_start = ((planet[0]-x1)**2 + (planet[1]-y1)**2)**0.5
        d_end = ((planet[0]-x2)**2 + (planet[1]-y2)**2)**0.5
        if min(d_start, d_end) < planet[2] < max(d_start, d_end):
            count += 1
    print(count)
