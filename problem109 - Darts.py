#
# Created by 14chanwa on 2017.02.23
#

# Project Euler - Problem 109
# Darts

singles = list(range(1, 21))
doubles = [2 * i for i in singles]
triples = [3 * i for i in singles]
singles.append(25)
doubles.append(50)

merged = sorted(singles + doubles + triples)

print(singles)
print(doubles)
print(triples)


def recursive_count_no_double(remaining_amount, remaining_hits, history, banned_indexes=[], merged=merged):
    count = 0

    if remaining_amount <= 0:
        return 0
    if remaining_hits == 0:
        return 0

    # Remove any relevant amount among singles, doubles, triples
    available_amounts_indexes = [i for i in range(len(merged)) if i not in banned_indexes]

    for index in range(0, len(available_amounts_indexes)):
        amount = merged[available_amounts_indexes[index]]

        # Check history
        if remaining_amount - amount in history.keys():
            count += history[remaining_amount - amount]
        else:
            # Else, compute
            if remaining_amount - amount < 0:
                break
            elif remaining_amount - amount == 0:
                count += 1
            else:
                banned_indexes_copy = list(banned_indexes)
                banned_indexes_copy.append(available_amounts_indexes[index])
                count += recursive_count_no_double(remaining_amount - amount, remaining_hits - 1, history,
                                                   banned_indexes_copy, merged)

    history[remaining_amount] = count

    return count


total_count = 0
history = {}
for i in range(6, 7):
    # print(i)
    for d in doubles:
        total_count += recursive_count_no_double(i - d, 2, history)

print(history)
print(total_count)

# def recursive_count(remaining_amount, history, start=True, max_authorized=max(merged), doubles=doubles,
# merged=merged):
#     count = 0
#     if start:
#         # Remove a double from the remaining amount
#         for amount in doubles:
#             if remaining_amount - amount < 0:
#                 break
#             elif remaining_amount - amount == 0:
#                 count += 1
#             else:
#                 count += recursive_count(remaining_amount - amount, history, False,
#                                          min(max_authorized, amount), doubles, merged)
#     else:
#         count += recursive_count_no_double(remaining_amount, history, max_authorized, doubles, merged)
#         # # Remove any relevant amount among singles, doubles, triples
#         # for amount in [i for i in merged if i <= max_authorized]:
#         #     if remaining_amount - amount < 0:
#         #         break
#         #     elif remaining_amount - amount == 0:
#         #         count += 1
#         #     else:
#         #         count += recursive_count(remaining_amount - amount, history, False,
#         #                                  min(max_authorized, amount), doubles, merged)
#     return count
