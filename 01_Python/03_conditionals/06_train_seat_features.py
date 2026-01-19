# ============================================
# Match-Case Statement (Python 3.10+)
# ============================================
# KEY POINTS:
# - match-case is Python's version of switch statement
# - More readable than long if-elif chains
# - Underscore (_) is the wildcard pattern (like default)
# - Available in Python 3.10 and above
# ============================================

seat_type = input("Enter seat type (sleeper/general/AC/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat: No AC, only beds available.")
    case "general":
        print("General seat: Average seating arrangement.")
    case "ac":
        print("AC seat: Air-conditioned clean seats.")
    case "luxury":
        print("Luxury seat: Premium seats plus extra services.")
    case _:
        print("Invalid seat type entered.")