def is_suspicious(quantity, unit):

    if quantity < 0:
        return True

    if quantity > 100000:
        return True

    if not unit:
        return True

    return False