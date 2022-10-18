# Define constant for pack size.
CANS_PER_PACK = 6

# Obtain price per pack and can volume.
userInput = input("Please enter the price for a six-pack: ")
packPrice = float(userInput)

userInput = input("Please enter the volume for each can (in ml): ")
canVolume = float(userInput)

# Compute pack volume.
packVolume = canVolume * CANS_PER_PACK

# Compute and print price per Liter.
pricePerLiter = packPrice / (packVolume/1000)
print("Price per Liter: %8.2f" % pricePerLiter)