def apply_coupon(price, discount):
    if discount < 0 or discount > 100:
        return price

    return price - (price * discount / 100)