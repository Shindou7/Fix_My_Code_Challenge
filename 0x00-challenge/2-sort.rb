###
#
#  Sort integer arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
    # Skip if not an integer
    next if arg !~ /^-?\d+$/

    # Convert to integer
    i_arg = arg.to_i

    # Find the right position to insert the integer
    is_inserted = false
    i = 0
    while i < result.size
        if result[i] <= i_arg
            i += 1
        else
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    result << i_arg unless is_inserted
end

puts result
