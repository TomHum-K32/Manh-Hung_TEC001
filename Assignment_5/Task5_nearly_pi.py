import random

def around_pi():
    N = int(input("Enter the number of random points you want: "))
    
    inside = 0
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x*x + y*y < 1:
            inside += 1
    
    pi = 4 * inside / N
    print("Approximate value of pi:", f"{pi:.5f}")

around_pi()