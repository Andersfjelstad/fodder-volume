from typing import List


def fodder_volume(height: List[int]) -> int:
    max_floor = max(height)

    first_list = height[: height.index(max_floor)]
    second_list = list(reversed(height[height.index(max_floor) + 1 :]))

    fodder1 = get_fodder(first_list, max_floor)
    fodder2 = get_fodder(second_list, max_floor)

    return fodder1 + fodder2


def get_fodder(food_list: List[int], max_floor: int) -> int:
    fodder = 0
    under_max_floor = max_floor - 1
    for idx in range(len(food_list) - 1):
        if food_list[idx + 1] < food_list[idx]:
            fodder += under_max_floor - food_list[idx + 1]
    return fodder
