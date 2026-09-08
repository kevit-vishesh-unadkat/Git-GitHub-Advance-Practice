categories = []


def add_category(name):
    category = {
        "name": name
    }

    categories.append(category)
    return category


def list_categories():
    return categories