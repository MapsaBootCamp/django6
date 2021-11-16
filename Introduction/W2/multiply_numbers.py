from time import time
from typing import List, Dict, Tuple
import logging

def multiple_offer_marzieh(input_data: Tuple, deviders: Tuple[int]):
    deviders = set(deviders)
    result = {"None": []}

    for item in deviders:
        if item==0:
            logging.error("taghsim be sefr nadarim")
            raise Exception("taghsim be sefr nadarim")

        result[str(item)] = []



    for item in input_data:
        flag = True
        for devide in deviders:
            if not item % devide:
                result[f"{devide}"].append(item)
                flag = False
        if flag:
            result["None"].append(item)

    return result

def multiple(input_data: Tuple) -> Dict:
    # result = {
    #     "2": [],
    #     "3": [],
    #     "5": [],
    #     "None": [],
    # }

    # for item in input_data:
    #     flag = True
    #     if not (item % 2):
    #         result["2"].append(item)
    #         flag = False
    #     if not (item % 3):
    #         result["3"].append(item)
    #         flag = False
    #     if not (item % 5):
    #         result["5"].append(item)
    #         flag = False
    #     if flag:
    #         result["None"].append(item)

    result = multiple_offer_marzieh(input_data, (2,3,5))
    return result



if __name__ == "__main__":
    
    FORMAT = '[%(asctime)s]-%(levelname)s-%(pathname)s-%(lineno)d: %(message)s'
    logging.basicConfig(format=FORMAT, filename="log.txt", datefmt="%Y-%m-%d %H:%M")
    test_data = (2, 3, 24, 25, 15, 30, 11, 10)
    print(multiple(test_data))
    print(multiple_offer_marzieh((2, 3, 24, 25, 15, 30, 11, 10), (2, 8, 5)))

