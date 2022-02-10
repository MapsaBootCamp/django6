def update_file(n, k):
    hour = 0
    updated_computers = 1

    while updated_computers < n:
        temp = min(k, updated_computers)
        updated_computers += temp
        hour += 1

    return hour



if __name__ == "__main__":
    number_of_chalenges = int(input())
    inputs = []
    for i in range(number_of_chalenges):
        inputs.append(map(int, input().split()))
    for elm in inputs:
        print(update_file(*elm))
