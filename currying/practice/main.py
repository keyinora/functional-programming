# Remember, currying is when we take a function that accepts multiple arguments:
# final_volume = box_volume(3, 4, 5)
# print(final_volume)
# 60

# And convert it into a series of functions that each accept a single argument:
# final_volume = box_volume(3)(4)(5)
# print(final_volume)
# 60

'''
box_volume(3) returns a new function that accepts a single integer and returns a new function
box_volume(3)(4) returns another new function that accepts a single integer and returns a new function
box_volume(3)(4)(5) returns the final result

Here's another way of calling it, where each function is stored in a variable before being called:
'''
# Here are the function definitions:
def box_volume(length):
  def box_volume_with_len(width):
    def box_volume_with_len_width(height):
      return length * width * height
    return box_volume_with_len_width
  return box_volume_with_len

with_length_3 = box_volume(3)
with_len_3_width_4 = with_length_3(4)
final_volume = with_len_3_width_4(5)
print(final_volume)
# 60
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.split("\n")
            num_lines = 0
            for line in lines:
                if sequence in line:
                    num_lines += 1
            return num_lines

        return with_length

    return with_char

