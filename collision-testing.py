#!/usr/bin/env python
import random

def how_many_before_collision(buckets, loops=1):
    """
    roll random hash indices into "buckets" and
    print how many rolls before a hash collision

    run 'loops' number of times
    """

    results = []

    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1

            else:
                break

        print(f"buckets: {buckets}, tries: {tries} before collision ({tries/buckets * 100:.1f}%)")
        results.append(tries)

    print(f"overall number of tries: {sum(results) / len(results)}")


# how_many_before_collision(32, 10)
how_many_before_collision(4096, 10)
