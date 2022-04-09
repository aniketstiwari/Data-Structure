def next_greatest_element(arr)
	stack = []
	output = []
	len = arr.length - 1
	arr.to_enum.with_index.reverse_each do |elem, index|
		if stack.length == 0
			output << -1
		elsif stack.length > 0 && stack.last > elem
			output << stack.last
		elsif stack.length > 0 && stack.last < elem
			while stack.length > 0 && stack.last <= elem do
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
	return output.reverse
end


p next_greatest_element([1,3,2,4])