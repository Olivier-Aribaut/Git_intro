from isa import density, temperature, pressure

print("At 0 m:")
print("Density:", density(0), "kg/m^3")
print("Temperature:", temperature(0), "K")
print("Pressure:", pressure(0), "Pa")

print("\nAt 5000 m:")
print("Density:", density(5000), "kg/m^3")
print("Temperature:", temperature(5000), "K")
print("Pressure:", pressure(5000), "Pa")

print("\nAt 10000 m:")
print("Density:", density(10000), "kg/m^3")
print("Temperature:", temperature(10000), "K")
print("Pressure:", pressure(10000), "Pa")