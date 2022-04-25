def  balance_paranthesis(expression)
	stack = []
	expression.chars.each do |elem|
		if ["(", "[", "{"].include?(elem)
			stack << elem
		else
			if stack.empty?
				return false
			end
			pop_elem = stack.pop
			if elem == "("
				if pop_elem != ")"
					return false
				end
			elsif elem == "["
				if pop_elem != "]"
					return false
				end
			elsif elem == "{"
				if pop_elem != "}"
					return false
				end
			end
		end
	end
	if !stack.empty?
		return false
	end
	return true
end

puts balance_paranthesis("}}}")

puts balance_paranthesis("{[(}])")

puts balance_paranthesis("{(})")

puts balance_paranthesis("{")

puts balance_paranthesis("()")
