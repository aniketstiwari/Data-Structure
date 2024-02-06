require 'pry'

# arr = [2,7,4,1,5,2,7,4]
# sum = 0
# window_size = 3
# i = 0
# final_sum = []

# while i < arr.length - window_size + 1 do
#     j = i
#     while i == 0 && j < i + window_size do
#         sum += arr[j]
#         j += 1
#     end
#     if i != 0
#         sum = sum + arr[j + window_size - 1] - arr[i - 1]
#     end
#     final_sum << sum
#     i += 1
# end

# puts final_sum.max

arr = [2,7,4,1,5,2,7,4]
sum = 0
k = 3 # window size
i = 0
j = 0

while j < k do
    sum  += arr[j]
    j += 1
end

temp_sum = sum
i = k

while i < arr.length do
    puts i
    temp_sum += arr[i] - arr[i-k]
    sum = [temp_sum, sum].max
    i += 1
end

puts sum
