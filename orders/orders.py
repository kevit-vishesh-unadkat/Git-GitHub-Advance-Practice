orders = []


def create_order(username, product):
    order = {
        "username": username,
        "product": product
    }

    orders.append(order)
    return order