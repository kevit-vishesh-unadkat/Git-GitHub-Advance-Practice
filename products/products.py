products = []


def add_product(name, price):
    product = {
        "name": name,
        "price": price
    }

    products.append(product)
    return product