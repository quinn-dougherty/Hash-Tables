#!/usr/bin/env python

import random

def longest_linked_list_chain(keys, buckets, loops=10, useSHA=False):
    """ rolls keys number of random keys into buckets buckets.
    and counts the collisions.
    it runs loops number of times.
    """

    for i in range(loops):
        key_counts = {}
        for j in range(buckets):
            key_counts[j] = 0

        for j in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"longest linked list chain for {keys} keys and {buckets} buckets (Load Factor {keys / buckets :.2f}): {largest_n}")

longest_linked_list_chain(4, 16, 5)
