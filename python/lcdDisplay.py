# Segment representation for digits 0-9
DIGITS = [
    (1,1,1,0,1,1,1),  # 0
    (0,0,1,0,0,1,0),  # 1
    (1,0,1,1,1,0,1),  # 2
    (1,0,1,1,0,1,1),  # 3
    (0,1,1,1,0,1,0),  # 4
    (1,1,0,1,0,1,1),  # 5
    (1,1,0,1,1,1,1),  # 6
    (1,0,1,0,0,1,0),  # 7
    (1,1,1,1,1,1,1),  # 8
    (1,1,1,1,0,1,1)   # 9
]

def print_number(s, n):
    def h_segment(on):
        return ' ' + '-'*s + ' ' if on else ' '*(s+2)
    
    def v_segment(left_on, right_on):
        return ('|' if left_on else ' ') + ' '*s + ('|' if right_on else ' ')
    
    digits = [int(d) for d in str(n)]
    
    # Top segments
    print(' '.join(h_segment(DIGITS[d][0]) for d in digits))
    
    # Top vertical segments
    for _ in range(s):
        print(' '.join(v_segment(DIGITS[d][1], DIGITS[d][2]) for d in digits))
    
    # Middle segments
    print(' '.join(h_segment(DIGITS[d][3]) for d in digits))
    
    # Bottom vertical segments
    for _ in range(s):
        print(' '.join(v_segment(DIGITS[d][4], DIGITS[d][5]) for d in digits))
    
    # Bottom segments
    print(' '.join(h_segment(DIGITS[d][6]) for d in digits))

# Test
print_number(2, 12345)
print()  # Blank line between numbers
print_number(3, 67890)