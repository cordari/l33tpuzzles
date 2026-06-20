"""
Given 2 lists of size N. The first list is the labor cost of each worker, and the second list indicates the skills each worker has. 

e.g. 

labor_cost = [100, 200, 50, 3]

skills = ["0", "1", "2", "3"]

"0" - the worker has no special skill
"1" - the worker has specialized skill A
"2" - the worker has specialized skill B
"3" - the worker has specialized skills in both A and B

A task group satisfying threshold X is a group formed from the workers so there are at least X workers have specialized skill A, and also at least X workers have specialized skill B

write a function to calculate the minimum labor costs of forming tasks groups satisfying thresholds x for each x between 1 and N, and put the costs in a list. if the worker pool
cannot satisfy a certain threshold, output -1 for that threshold

"""

from math import inf
from typing import List

"""
not 100% sure of the correctness of the solution, as I didn't do well during the OA session and now I don't have the test cases to verify.

the idea is we want to calculate the labor cost of having X A-skill and X B-skill. If there is no worker with both A and B skills, then the problem is simple - we just separate
the workers with their skill into A and B list, and sort by their labor cost, and then pair them up to get the total cost of having A and B skills. The cost of having m A workers
and m B workers, is the cost of having (m-1) A and B workers plus the cost of mth combined cost of A worker and B worker.

but now with workers having both skills, we are just trying to replace a pair of A worker and B worker with a AB worker IF the cost ends up lower. Since cost is always positive,
when a A worker is replaced by a AB worker, we should remove a B worker to further reduce the cost. So it is always a AB worker or a pair of A and a B worker. We just compute the
cost of having 1 A skill and 1 B skill, and sort them, and select them from the lowest to highest.

this is my algorithm:


1. separate the A-only cost, B-only cost, and AB costs into their own list
2. sort A-only cost and B-only cost
3. use the shorter of the two to add A-only cost and B-only cost from lowest
4. add in the AB costs
5. sort the list so the cost of having A and B is from lowest to highest
6. the output list is the running sum of the list
7. if the output list size is under the target size, fill the rest with -1 because these cannot be satisfied



"""

def task_group_min_cost(cost: List[int], skills: List[str]) -> List[int]:
    a_only_cost: List[int] = []
    b_only_cost: List[int] = []
    both_cost: List[int] = []

    for i in range(0, len(cost)):
        c = cost[i]
        s = skills[i]
        if s == "1":
            a_only_cost.append(c)
        elif s == "2":
            b_only_cost.append(c)
        elif s == "3":
            both_cost.append(c)

    a_only_cost.sort()
    b_only_cost.sort()


    for i in range(0, min(len(a_only_cost), len(b_only_cost))):
        both_cost.append(a_only_cost[i] + b_only_cost[i])

    both_cost.sort()
    combined_accumulate_cost = []
    sum = 0
    for i in range(0, len(both_cost)):
        sum += both_cost[i]
        combined_accumulate_cost.append(sum)

    output = []
    for i in range(0, min(len(cost), len(combined_accumulate_cost))):
        output.append(combined_accumulate_cost[i])

    length = len(output)
    for i in range(length, len(cost)):
        output.append(-1)

    return output


