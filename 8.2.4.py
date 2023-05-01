# def preprocess(input, k):
#   count = [0] * (k+1)

#   for i in input:
#     count[i] += 1

#   return count

# def query(count, a, b):
#   return count[b] - count[a-1]

# # Example usage
# input = [1, 2, 3, 2, 1, 3, 0, 4, 1]
# k = 4

# count = preprocess(input, k)
# print(query(count, 1, 3))  



def preprocess(numbers, k):
  count = [0] * (k+1)

  for number in numbers:
    count[number] += 1

  return count

def query(count, a, b):
  if a == 1:
    return count[b]

  return count[b] - count[a-1]

