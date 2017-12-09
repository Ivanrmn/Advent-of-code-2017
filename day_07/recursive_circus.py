# --- Day 7: Recursive Circus ---

# Wandering further through the circuits of the computer, you come upon
# a tower of programs that have gotten themselves into a bit of trouble.
# A recursive algorithm has gotten out of hand, and now they're balanced
# precariously in a large tower.

# One program at the bottom supports the entire tower. It's holding a
# large disc, and on the disc are balanced several more sub-towers. At
# the bottom of these sub-towers, standing on the bottom disc, are other
# programs, each holding their own disc, and so on. At the very tops of
# these sub-sub-sub-...-towers, many programs stand simply keeping the
# disc below them balanced but with no disc of their own.

# You offer to help, but first you need to understand the structure of
# these towers. You ask each program to yell out their name, their
# weight, and (if they're holding a disc) the names of the programs
# immediately above them balancing on that disc. You write this
# information down (your puzzle input). Unfortunately, in their panic,
# they don't do this in an orderly fashion; by the time you're done,
# you're not sure which program gave which information.

# For example, if your list is the following:

# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
# ...then you would be able to recreate the structure of the towers that looks like this:

#                 gyxo
#               /
#          ugml - ebii
#        /      \
#       |         jptl
#       |
#       |         pbga
#      /        /
# tknk --- padx - havc
#      \        \
#       |         qoyq
#       |
#       |         ktlj
#        \      /
#          fwft - cntj
#               \
#                 xhth

# In this example, tknk is at the bottom of the tower (the bottom
# program), and is holding up ugml, padx, and fwft. Those programs are,
# in turn, holding up other programs; in this example, none of those
# programs are holding up any other programs, and are all the tops of
# their own towers. (The actual tower balancing in front of you is much
# larger.)

# Before you're ready to help them, you need to make sure your
# information is correct. What is the name of the bottom program?

def format_input(input_name):
    '''
    Reads a txt line per line and format each line into an python dict
    IN LINE => foo (90) -> foo1, foo2, foo3
    OUTPUT+= => {"name": "foo", "childs": ["foo1", "foo2", "foo3"]}
    '''
    filename = input_name
    output = []
    with open(filename) as f:
        data = f.readlines()
    for line in data:
        log = {}
        parenthesis_index = line.find("(")
        log["name"] = line[:parenthesis_index-1]
        childs_delimitator = line.find(">")
        if childs_delimitator != -1:
            childs = line[childs_delimitator+1:].rstrip().replace(" ", "")
            childs = childs.split(",")
            log["childs"] = childs
        output.append(log)
    return output

def recursive_circus(logs):
    childs = []
    parents = []
    for log in logs:
        if "childs" in log:
            parents.append(log)
            childs.append(log["name"])
        else:
            childs.append(log["name"])
    for parent in parents:
        for child in parent["childs"]:
            childs.remove(child)
    return(childs[0])
