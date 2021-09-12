while True:
    try:
        n,k=map(int,input().split())
        result = n + (n // k)
        coupon = n % k + (n // k)
        if coupon >= k:
            while coupon >= k:
                result = result + (coupon // k)
                coupon = coupon % k + (coupon // k)
        print(result)
    except EOFError:
        break