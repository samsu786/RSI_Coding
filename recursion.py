import math
vector_1 = [3,5,8,12,9]
vector_2 = [4,4,12,11,10]
# calculate_similarity(vector_1,vector_2)

def calculate_similarity(vector_1, vector_2):
    result = 0
    for idx, v1 in enumerate(vector_1):
        result += (vector_2[idx] - v1) ** 2 
    print(math.sqrt(result))
    return math.sqrt(result)

calculate_similarity(vector_1, vector_2)