
"""

given a list of accounts with current balances, and a threshold, output a list of transfers among the accounts so all account balances are at or above the threshold

if the condition cannot be satisfied, return None


input:

Acct1: 130
Acct2: 90
Acct3: 70
Acct4: 120


output:
Acct1 -> Acct2: 10
Acct1 -> Acct3: 20
Acct4 -> Acct3: 10



challenge: can this be optimized to use as few transfers as possible?

"""
from typing import Dict, List, Tuple, Optional

"""
naive approach:

for each account, find whether it has surplus or deficit against the threshold
put surplus account in one list, and deficit account in another list
meanwhile, adding up the surpluses and deficits to check if it is at or above 0. If it is below 0, there is no solution. return None

go through each surplus account
  for the surplus amount, as long as the remaining surplus is > 0, go through the accounts with deficit
    for the deficit, check if the surplus can zero out the deficit.
    if the surplus can zero out the deficit, then the surplus may be used for the next deficit account (when surplus is 0 as well is taken care by the loop condition)
    else if the surplus is not enough, surplus from the next account will be used.
    
    update the surplus amount for the account, and the deficit amount of the account

    caveat: must check if deficit is less than 0 - because the deficit could be updated to 0 and should be skipped. alternative is to remove the account with 0 deficit from the 
     deficit list, but need to be careful with the current index
"""
def plan_accounts(accounts: Dict[str, int], threshold: int) -> Optional[List[Tuple[str, str, int]]]:
    transfers: List[Tuple[str, str, int]] = []
    positive: List[Tuple[str, int]] = []
    negative: List[Tuple[str, int]] = []
    delta_sum = 0
    for acct in accounts.keys():
        amount = accounts[acct]
        diff = amount - threshold
        delta_sum += diff
        if diff > 0:
            positive.append((acct, diff))
        elif diff < 0:
            negative.append((acct, diff))

    # unable to satisfy the constraints
    if delta_sum < 0:
        return None

    for pos_idx, pos in enumerate(positive):
        neg_idx = 0
        surplus = pos[1]
        print(f"acct {pos[0]} has surplus of {surplus}")
        while surplus > 0 and neg_idx < len(negative):
            print(f"acct {pos[0]} has surplus of {surplus}")
            deficit = negative[neg_idx][1]
            print(f"acct {negative[neg_idx][0]} has deficit of {deficit}")
            transfer_amount = 0
            if deficit >= 0:
                neg_idx += 1
                continue
            if surplus + deficit < 0:
                negative[neg_idx] = (negative[neg_idx][0], surplus + deficit)
                transfer_amount = surplus
                surplus = 0
                positive[pos_idx] = (positive[pos_idx][0], 0)
                
                transfers.append((pos[0], negative[neg_idx][0], transfer_amount))
            elif surplus + deficit > 0:
                negative[neg_idx] = (negative[neg_idx][0], 0)
                surplus += deficit
                transfer_amount = -deficit
                positive[pos_idx] = (positive[pos_idx][0], surplus)
                transfers.append((pos[0], negative[neg_idx][0], transfer_amount))
                neg_idx += 1

            

    return transfers
"""
challenge/optimization: as few transfers as possible:
idea:
sort the list of accounts based on the balance, so the one with the biggest deficit will be at the head of the list, and account with biggest surplus at the end

we could use two pointers, one from biggest deficit to smallest; and the other from biggest surplus to smallest. But this won't work optimally when remaining
deficit and/or remaining surplus change as a result of balancing.

A better data structure to use is a min-heap. Or 2 min-heaps.

"""
import heapq

def plan_accounts_optimal(accounts: Dict[str, int], threshold: int) -> Optional[List[Tuple[str, str, int]]]:
    total_surplus = 0
    # Tuple: balance, account
    deficit_accounts: List[Tuple[int, str]] = []
    surplus_accounts: List[Tuple[int, str]] = []
    transfers: List[Tuple[str, str, int]] = []

    heapq.heapify(deficit_accounts)
    heapq.heapify(surplus_accounts)

    for acct in accounts.keys():
        acct_name = acct
        diff = accounts[acct] - threshold
        total_surplus += diff
        if diff < 0:
            heapq.heappush(deficit_accounts, (diff, acct_name))
        elif diff > 0:
            # use negative here because python doesn't provide max-heap, so have to multiple by -1 of the value
            heapq.heappush(surplus_accounts, (-diff, acct_name))

    if total_surplus < 0:
        # not enough surplus to satisfy the problem
        return None
    
    while len(deficit_accounts) > 0:
        def_acct = heapq.heappop(deficit_accounts)
        sur_acct = heapq.heappop(surplus_accounts)

        print(f"def_acct: {def_acct}")
        print(f"sur_acct: {sur_acct}")

        # the transfer amount would be the smaller amount between deficit and surplus.
        # because we flipped surplus to negative, so we use max instead of min
        # and we flip the value so the xfer_amount is positive
        xfer_amount = -max(def_acct[0], sur_acct[0])
        transfers.append((sur_acct[1], def_acct[1], xfer_amount))
        new_deficit = def_acct[0] + xfer_amount
        new_surplus = sur_acct[0] - xfer_amount

        if new_deficit < 0:
            heapq.heappush(deficit_accounts, (new_deficit, def_acct[1]))

        # surplus is expressed as a negative value to get max-heap
        if new_surplus < 0:
            heapq.heappush(surplus_accounts, (new_surplus, sur_acct[1]))

    return transfers




def main():
    print(plan_accounts_optimal({"Acct1": 100, "Acct2": 100, "Acct3": 100, "Acct4": 120}, 100))

main()