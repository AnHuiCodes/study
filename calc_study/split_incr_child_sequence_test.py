from collections import defaultdict


def isPossible(lst: list) -> bool:
    lst.sort()
    default_dict = defaultdict(int)
    for num in lst:
        default_dict[num] += 1
    result = []
    tmp_lst = []
    while True:
        num = lst.pop(0)
        num_count = default_dict.get(num, 0)
        if num_count >= 2:
            pass
        if len(result) >= 3 and num_count <= 1:
            break
        if num in result:
            tmp_lst.append(num)
            continue
        if not result:
            result.append(num)
            continue
        tmp_int = result[-1]
        if num - tmp_int == 1:
            result.append(num)
            continue
        tmp_lst.append(num)
    if len(result) < 3:
        return False
    if tmp_lst:
        return isPossible(tmp_lst)
    return True


if __name__ == '__main__':
    nums = [1, 4, 2, 5, 3, 3]
    print(isPossible(nums))
