def process_order1(order_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    shipping = 100
    handling_fee = 20
    insurance = 10

    subtotal = total - discount
    subtotal += shipping
    subtotal += handling_fee
    subtotal += insurance

    print(order_id)
    print(amount)
    print(tax)
    print(discount)
    print(shipping)
    print(handling_fee)
    print(insurance)
    print(subtotal)

    return subtotal
    
def process_order2(order_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    shipping = 100
    handling_fee = 20
    insurance = 10

    subtotal = total - discount
    subtotal += shipping
    subtotal += handling_fee
    subtotal += insurance

    print(order_id)
    print(amount)
    print(tax)
    print(discount)
    print(shipping)
    print(handling_fee)
    print(insurance)
    print(subtotal)

    return subtotal