# 4 5 2 10 3

# stack

#  5 
#  4

# output

#output => -1

def next_smaller_element_to_left(arr)
	stack = []
	output = []
	len = arr.length - 1
	arr.each do |elem, index|
		if stack.length == 0
			output << -1
		elsif stack.length > 0 && stack.last < elem
			output << stack.last
		elsif stack.length > 0 && stack.last > elem
			while stack.length > 0 && stack.last >= elem do
				stack.pop
			end
			if stack.length == 0 
				output << -1
			else
				output << stack.last
			end
		end
        stack << elem
	end
	return output
end


p next_smaller_element_to_left([4,5,2,10,3])

#output => -1 4 -1 2 2