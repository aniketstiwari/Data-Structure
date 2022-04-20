# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

# -8, 1, 4, 6, 10, 45
# 16

# sorting two pointer technique

# def pair_with_sum_x(arr, sum)
# 	size = arr.length
# 	left = 0 
# 	right = size - 1
# 	arr = arr.sort
# 	while left < right do
# 		if arr[left] + arr[right] == sum
# 			return 1
# 		elsif arr[left] + arr[right] < sum
# 			left += 1
# 		else
# 			right -= 1
# 		end
# 	end
# 	return -1
# end

# p pair_with_sum_x([1, 4, 45, 6, 10, -8], 16)

# Time Complexity

# If Merge Sort or Heap Sort is used then (-)(nlogn) in the worst case.
# If Quick Sort is used then O(n^2) in the worst case.

# Auxiliary Space

# This too depends on sorting algorithm. The auxiliary space is O(n) for merge sort and O(1) for Heap Sort.


##########################################################################


# 2nd Approach

def pair_with_sum_x(arr, sum)
	hsh = {}
	arr.each_with_index do |elem, index|
		temp = sum - arr[index]
		if hsh.has_key?(temp)
			puts "#{sum} is available #{temp} #{arr[index]}"
		end
		hsh[arr[index]] = index
	end
end

pair_with_sum_x([1, 4, 45, 6, 10, -8, 12], 16)