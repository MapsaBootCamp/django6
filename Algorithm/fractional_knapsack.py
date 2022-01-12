from typing import Dict, List, Tuple


test_data = [(3, 8), (5, 12), (1, 6), (5, 2), (5, 2)]  #(value, weight)

def _density_sorted(val_weight: List[Tuple]):
    """
    @params: [(value, weight)]
    @return: [(val, weight)] sorted
    """
    result_ = []
    for elm in val_weight:
        result_.append((elm, elm[0]/elm[1]))
    result_ = sorted(result_, key=lambda x: x[1], reverse=True)
    result = [elm[0] for elm in result_]
    return result


def fractional_knapsack(val_weight: List[Tuple], capacity) -> Dict:
    """
    @return: [((val, weight), fraction)]
    """
    val_weight_density_sorted = _density_sorted(val_weight)

    val = 0
    result = []
    for elm in val_weight_density_sorted:
        if capacity >= elm[1]:
            result.append((elm, 1))
            val += elm[0]
            capacity -= elm[1]
        else:
            result.append((elm, capacity/elm[1]))
            val += (capacity/elm[1]) * elm[0]
            capacity = 0

    return result, val


print(fractional_knapsack(test_data, 27))
