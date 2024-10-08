from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())
bullets_copy = bullets.copy()
locks_copy = locks.copy()
current_barrel = 0
shots = 0
while len(locks) and len(bullets):
    current_bullet = bullets[-1]
    current_lock = locks[0]
    if current_barrel >= size_barrel:
        print("Reloading!")
        current_barrel = 0
        continue
    if current_bullet <= current_lock:
        print("Bang!")
        bullets.pop()
        locks.popleft()
        shots += 1
        current_barrel += 1
    else:
        print("Ping!")
        bullets.pop()
        shots += 1
        current_barrel += 1


if bullets and current_barrel >= size_barrel:
    print("Reloading!")
    current_barrel = 0

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${abs(shots * bullet_price - intelligence)}")
