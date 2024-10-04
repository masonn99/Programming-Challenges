# the trip
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
def theTrip(arr):
    # Convert to cents
    cents = [int(amount * 100) for amount in arr]
    total_cents = sum(cents)
    n = len(cents)
    
    # Calculate average in cents
    avg_cents = total_cents // n
    remainder = total_cents % n
    
    # Calculate the amount each person needs to pay or receive
    differences = [amount - avg_cents for amount in cents]
    
    # Distribute the remainder
    for i in range(remainder):
        differences[i] -= 1
    
    # Sum up positive differences (amount to be paid)
    total_transfer = sum(max(0, diff) for diff in differences)
    
    # Convert back to dollars and format
    return f"${total_transfer / 100:.2f}"

print(theTrip([10, 20, 30]))
print(theTrip([15.00, 15.01, 3.00, 3.01]))
