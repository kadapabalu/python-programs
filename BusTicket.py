seats=[1,2,3,4,5]
print("Available seats;",seats)
seat=int(input("Choose seat:"))
if seat in seats:
    seats.remove(seat)
    print("Seat booked")
else:
    print("Seat not available")
print("Remaining seats:",seats)
    
