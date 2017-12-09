# --- Day 6: Memory Reallocation ---

# A debugger program here is having an issue: it is trying to repair a
# memory reallocation routine, but it keeps getting stuck in an infinite
# loop.

# In this area, there are sixteen memory banks; each memory bank can hold
# any number of blocks. The goal of the reallocation routine is to balance
# the blocks between the memory banks.

# The reallocation routine operates in cycles. In each cycle, it finds the
# memory bank with the most blocks (ties won by the lowest-numbered memory
# bank) and redistributes those blocks among the banks. To do this, it
# removes all of the blocks from the selected bank, then moves to the next
# (by index) memory bank and inserts one of the blocks. It continues doing
# this until it runs out of blocks; if it reaches the last memory bank, it
# wraps around to the first one.

# The debugger would like to know how many redistributions can be done
# before a blocks-in-banks configuration is produced that has been seen
# before.

# For example, imagine a scenario with only four memory banks:

# The banks start with 0, 2, 7, and 0 blocks. The third bank has the
# most blocks, so it is chosen for redistribution. Starting with the
# next bank (the fourth bank) and then continuing to the first bank, the
# second bank, and so on, the 7 blocks are spread out over the memory
# banks. The fourth, first, and second banks get two blocks each, and
# the third bank gets one back. The final result looks like this: 2 4 1
# 2. Next, the second bank is chosen because it contains the most blocks
# (four). Because there are four memory banks, each gets one block. The
# result is: 3 1 2 3. Now, there is a tie between the first and fourth
# memory banks, both of which have three blocks. The first bank wins the
# tie, and its three blocks are distributed evenly over the other three
# banks, leaving it with none: 0 2 3 4. The fourth bank is chosen, and
# its four blocks are distributed such that each of the four banks
# receives one: 1 3 4 1. The third bank is chosen, and the same thing
# happens: 2 4 1 2. At this point, we've reached a state we've seen
# before: 2 4 1 2 was already seen. The infinite loop is detected after
# the fifth block redistribution cycle, and so the answer in this
# example is 5.

# Given the initial block counts in your puzzle input, how many
# redistribution cycles must be completed before a configuration is
# produced that has been seen before?


def memory_reallocation(bank):
    cycles = []
    steps = 0
    current_cycle = bank
    while (cycles.count(current_cycle) < 2):
        greatest = max(bank)
        i = current_cycle.index(greatest)
        current_cycle[i] = 0
        i += 1
        slots = len(bank)
        while (i <= slots and greatest > 0):
            if i == slots:
                i = 0
            greatest -= 1
            current_cycle[i] += 1
            i += 1
        steps += 1
        log = current_cycle[:]
        cycles.append(log)
    return steps


def get_indexes_of_item_in_array(item, array):
    indexes = ()
    mirror = array[:]
    try:
        while (mirror.index(item) != -1):
            i = mirror.index(item)
            indexes += (i, )
            mirror[i] = None
    except ValueError:
        return indexes


def memory_reallocation_v2(bank):
    cycles = []
    current_cycle = bank
    while (cycles.count(current_cycle) < 2):
        greatest = max(bank)
        i = current_cycle.index(greatest)
        current_cycle[i] = 0
        i += 1
        slots = len(bank)
        while (i <= slots and greatest > 0):
            if i == slots:
                i = 0
            greatest -= 1
            current_cycle[i] += 1
            i += 1
        log = current_cycle[:]
        cycles.append(log)
    indexes = get_indexes_of_item_in_array(cycles[-1], cycles)
    loops = indexes[1] - indexes[0]
    return loops
