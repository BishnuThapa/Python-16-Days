coffee_prices = [('cappuccino', 1.5),
                 ('espresso', 1.2),
                 ('mocha', 1.9)

                 ]

# for element in coffee_prices:
#     print(element)

# for coffee, price in coffee_prices:
#     print(coffee)

# for coffee, price in coffee_prices:
#     print(price)

# to find most expensive coffee


def most_expensive_coffee(list_of_prices):

    highest_price = 0
    my_most_expensive_coffee = ''

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price = price
            my_most_expensive_coffee = coffee
        else:
            pass

    return (my_most_expensive_coffee, highest_price)


print(most_expensive_coffee(coffee_prices))
