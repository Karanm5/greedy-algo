#!/usr/bin/env python
import click

#build a function that return the minumum number of coins only using quarters and dimes
def greedy_coin(change):

    print(f"Your change for {change}:")
    coins = {0.25,0.10}
    coin_lookup = {0.25:"quarter", 0.10:"dime"}
    coin_dict ={}
    for coin in coins:
        coin_dict[coin]= 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]}{coin_lookup[coin]}")
    return coin_dict

#build a greedy algorithm to find the minimum number of coins but only use pennies,nickles and dimes
def greedy_coin2(change):

    print(f"Your change for {change}:")
    coins = {0.25,0.10}
    coin_lookup = {0.05:"nickel",0.01:"penny", 0.10:"dime"}
    coin_dict ={}
    for coin in coins:
        coin_dict[coin]= 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]}{coin_lookup[coin]}")
    return coin_dict


#build a clock group

@click.group()
def main():

    """Return the minimum number of coins for a given change
    
    Example: ./greedy_coin.py
    """
    pass

#build a click command that only return pennies, nickels and dimes

@main.command("pnd")
@click.argument("change", type=float)
def pnd(change):

    """Return the minimum number of coins for a given change
    
    Example: ./greedy_coin.py
    """

    greedy_coin2(change)

if __name__ =="__main__":
    main()


