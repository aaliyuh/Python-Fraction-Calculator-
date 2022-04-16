frs = []
operations = ["+","-","*","/"]

def getInput():

    while True:
        error = False
        global operation
        operation = str(input("Choose an operation (+, -, *, /): "))

        for o in operations:
            if operation == o:
                break
            elif o == operations[len(operations) - 1]:
                error = True
                print("Error, please try again (+, -, *, /)")
                break

        if error:
            continue
        
        break

    q = 0

    while True:
        fr = str(input("Type a fraction: "))
        frs.append(fr)

        if q > 0:
            while True:
                cont = str(input("Include more fractions? (Y/N): "))
                if cont == "Y" or cont == "N":
                    break
                else:
                    print("Error, please try again (Y/N)")
                    continue
                
            if cont == "N":
                break
            else:
                continue
        
        q += 1
    
    print(f"Fractions: {frs}; Operation: {operation}")
    return frs, operation

def num():
    global nums
    nums = []
    for fr in frs:
        ns = fr.split("/")
        nums.append(ns[0])

    nums = [int(n) for n in nums]

    global isUndefined
    isUndefined = False
    if operation == "*" or "/":
        for n in nums:
            if n == 0:
                isUndefined = True
                return

    return nums, isUndefined
            
def den():
    global dens
    dens = []

    for fr in frs:
        ds = fr.split("/")
        dens.append(ds[0])

    dens = [int(d) for d in dens]

    global isUndefined
    if isUndefined:
        return
    elif operation == "*" or "/":
        for d in dens:
            if d == 0:
                isUndefined = True
                return

    return dens

def multiply():
    n = 0
    product_nums = 1
    for n in range(0, len(nums)):
        product_nums *= nums[n]

    d = 0
    product_dens = 1
    for d in range(0, len(dens)):
        product_dens *= dens[d]
    
    global answer
    answer = f"{product_nums}/{product_dens}"
    print(f"Product: {answer}")
    return answer

def divide():
    swap = []
    v = 1
    for v in range(1, len(nums)):
        swap.append(nums[v])
        nums[v] = dens[v]

    n = 0
    quotient_nums = 1
    for n in range(0, len(nums)):
        quotient_nums *= nums[n]

    v = 1
    for v in range(1, len(dens)):
        for s in swap:
            dens[v] = s

    d = 0
    quotient_dens = 1
    for d in range(0, len(dens)):
        quotient_dens *= dens[d]

    global answer
    answer = f"{quotient_nums}/{quotient_dens}"
    print(f"Quotient: {answer}")
    return answer

def add():
    sameDens = True
    i1 = 0
    while i1 < len(dens) - 1:
        i2 = i1 + 1
        if dens[i1] != dens[i2]:
            sameDens = False
            break
        i1 += 1
    
    sum_nums = 0

    if sameDens:
        sum_dens = dens[0]
        for n in nums:
            sum_nums += n
    else:
        sum_dens = 1
        for d in range(0, len(dens)):
            sum_dens *= dens[d]
        nx = 0
        for n in nums:
            x = 0
            for x in range(0, len(nums)):
                if x != nx:
                    nums[nx] *= dens[x]
            nx += 1

        sum_nums = sum(nums)

    global answer
    answer = f"{sum_nums}/{sum_dens}"    
    print(f"Sum: {answer}")
    return answer

def subtract():
    sameDens = True
    i1 = 0
    while i1 < len(dens) - 1:
        i2 = i1 + 1
        if dens[i1] != dens[i2]:
            sameDens = False
            break
        i1 += 1

    if sameDens:
        diff_nums = 2*nums[0]
        diff_dens = dens[0]
        for n in nums:
            diff_nums -= n
    else:
        diff_dens = 1
        for d in range(0, len(dens)):
            diff_dens *= dens[d]
        nx = 0
        for n in nums:
            x = 0
            for x in range(0, len(nums)):
                if x != nx:
                    nums[nx] *= dens[x]
            nx += 1

        diff_nums = 2*nums[0]
        for n in nums:
            diff_nums -= n
        
    global answer
    answer = f"{diff_nums}/{diff_dens}"
    print(f"Difference: {answer}")
    return answer

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def Reduce(answer):
    ans_fr = answer.split("/")
    global a,b
    a,b = int(ans_fr[0]),int(ans_fr[1])
    global gcd
    gcd = gcd(a,b)

    b /= gcd
    a /= gcd

    answer = f"{round(a)}/{round(b)}"
    return answer

def main():

    getInput()
    num()
    den()
    
    if isUndefined:
        print("Undefined")
        return

    if operation == "*":
        multiply()
    if operation == "/":
        divide()
    if operation == "+":
        add()
    if operation == "-":
        subtract()

    global smp_ans
    smp_ans = Reduce(answer)
    print(f"Simplified Answer: {smp_ans}")

main()
