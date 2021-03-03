# Lab 2

This is my solutions to exercise lab 2 in the course Artificial Intelligence at SDU on fourth semester of Software Engineering.

## Exercise 1

Not to be submitted

1. Successor nodes are inserted at front of the fringe (successor list) as
   a node is expanded. Is this a breadth (FIFO) or depth first search (LIFO)?

2. For goal J, give the fringe (successor list) after expanding each node.

3. What is the effect of inserting successor nodes at the end of the
   fringe as a node is expanded? A depth or breadth first search?

4. For goal J, give the fringe (successor list) after expanding each node.

## Exercise 2

To be submitted

Use your search program to solve the vacuum world problem. Hint: one way to
represent the state space in Python is by a dictionary where the current state is a
tuple:(location, A status, B status) and a list holds successor states for each action.
[(location, A status, B status), (location, A status, B status), (location, A status, B
status)]

For example:
('A', 'Dirty', 'Dirty’): [('A', 'Clean', 'Dirty'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')]

## Homework

To be submitted

Modify
your search program to solve the following problem A farmer has a goat, a cabbage and a wolf to move across a river with a boat that can only hold himself and one other passenger If the goat and wolf are alone, the wolf will eat the
goat If the goat and cabbage are alone, the goat will eat the cabbage Define the state space for the problem Hint Use a tuple to represent the side of the river each is located for example (' W',' E',' W',' can represent the ( wolf, goat,
cabbage) locations Use a list of tuples for the successor states Include successor states that violate the problem constraints, that is (' W',' W',' E',' which is the goat is alone with the cabbage don't violate requirement that the boat can hold only two passengers e.g all four passengers cannot move from one side to another at once, that is (' W','
' W',' cannot become (' E',' E',' E',' Define successor_fn to return a list of states that do not violate the problem constraints
