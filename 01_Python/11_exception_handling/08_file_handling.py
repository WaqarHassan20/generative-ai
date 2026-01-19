# This is the old and length way of handling files with explicit open and close

try:
    file = open("order.txt", "w")
    file.write("Chai Order: 250 ml Lemon Chai\n")
    print("Order written to file successfully.")

except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

finally:
    file.close()
    print("File closed.")
    
    
# This is the preferred way of handling files using 'with' statement

with open("newOrder.txt", "w") as file:
    file.write("Chai Order: 300 ml Honey Chai\n")
    print("Order written to file successfully.")