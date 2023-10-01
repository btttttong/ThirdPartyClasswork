# def most_frequent_item_count(collection):
#     # Do your magic. :)
#
#     tmp = {}
#     for num in collection:
#         if num not in tmp:
#             tmp[num] = 1
#         else :
#             tmp[num] += 1
#
#     sorted_num_by_value = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
#     converted_dict = dict(sorted_num_by_value)
#     list_convert_dict = []
#     print(converted_dict)
#     print(list(converted_dict.values())[0])
#
# most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])

from collections import Counter
def most_frequent_item_count(collection):
    if not collection:
        return 0
    counter = Counter(collection)
    most_common = counter.most_common(5)[0]
    return most_common

print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
