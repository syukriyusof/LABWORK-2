"""
 Program Purpose: To ask user to input data for booking room at Hotel Ceria and calculation the cost with available discount.
 Programmer: MUHAMMAD SYUKRI BIN MHD YUSOF (AM2307013981)
 Date: 23 February 2024
"""

# Define nightly rates for each room type
hotelrates = {
    'Single': 100,
    'Double': 150,
    'Suite': 250
}

# Function to calculate total cost with discounts
def calculate_total_cost(RoomType, RoomsNum, NightsNum):
    if RoomType not in hotelrates:
        return None, "Invalid room type"

    if RoomsNum <= 0 or NightsNum <= 0:
        return None, "Invalid value inserted, please enter again!"

    rate = hotelrates[RoomType]
    total_cost = rate * RoomsNum * NightsNum

    if RoomsNum > 5:
        total_cost *= 0.9  # 10% discount for more than 5 rooms
        print("Congratulations! You got 10% discount.")

    if RoomType == 'Single' and NightsNum > 7:
        print("Nice deal! You got a complimentary breakfast voucher.")

    if RoomType == 'Suite' and NightsNum < 3:
        return None, "Minimum stay for a Suite is 3 nights"

    return total_cost, None


# Main program
print("Welcome to Hotel Ceria!")

while True:
    RoomType = input("Enter room type (Single, Double, Suite): ").capitalize()
    RoomsNum = int(input("Enter number of rooms to reserve: "))
    NightsNum = int(input("Enter number of nights to stay: "))

    total_cost, error = calculate_total_cost(RoomType, RoomsNum, NightsNum)
    if error:
        print(error)
        continue

    print(f"Total cost for your reservation: RM {total_cost:.2f}")
    break
