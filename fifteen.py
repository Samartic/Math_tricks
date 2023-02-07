import time

def main():
    threes = 0
    with open("result.txt", "a") as f:
        while True:
            start = time.time()
            f.write(f"{start}\n")
            # get a b n
            print("\n")
            print("nb of 3: ", threes)
            a = int(get_a(threes))
            print("step A")
            b = int(get_b(threes))
            print("step B")
            n = str(a) + str(b)
            print(n)
            print("summing...")
            sum = get_sum(a, b)
            test = assertion(n, sum)
            end = time.time()
            lapse = end - start
            print("process took %.2f seconds" %lapse)
            report(threes,n, test,lapse, f)
            threes += 1

def get_a(threes):
    a = str("1")
    if int(threes) != 0:
        for _ in range(0, int(threes)):
            a = str(a) + str("3")
    return a
def get_b(threes):
    b = str("5")
    if threes != "0":
        for _ in range(0, int(threes)):
            b = str(b) + str("3")
    return b

def get_sum(a, b):
# getting to the sum
    sumy = sum(range(a,(b+1)))
    return sumy

def assertion(n, sum):
    if int(n) == sum:
        return "pass"
    else:
        return "fails"
def report(threes,n, test,lapse, f):
    f.write(f"{threes}\n")
    f.write(f"{n}\n)
    f.write(f"{test}\n")
    f.write(f"{lapse}\n\n")


    
if __name__ == "__main__":
    main()
