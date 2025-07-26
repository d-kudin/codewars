def delete_nth(order,max_e):
    new_order = order.copy()
    new_order.reverse()
    for i in order:
        if new_order.count(i) > max_e:
            new_order.remove(i)
    new_order.reverse()
    return new_order