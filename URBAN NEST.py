class Property:
    def __init__(self, address, price, bedrooms, bathrooms, area_sqft):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.area_sqft = area_sqft
        self.listed = True

    def display_details(self):
        print("Property Details:")
        print("Address:", self.address)
        print("Price:", self.price)
        print("Bedrooms:", self.bedrooms)
        print("Bathrooms:", self.bathrooms)
        print("Area (sqft):", self.area_sqft)
        print("Status: ", "Listed" if self.listed else "Sold")

    def mark_sold(self):
        self.listed = False


class RealEstateAgency:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def display_properties(self):
        if self.properties:
            print("Properties Listed:")
            for idx, property in enumerate(self.properties):
                print(f"Property {idx + 1}:")
                property.display_details()
                print()
        else:
            print("No properties listed.")

    def sell_property(self, property_index):
        if 0 <= property_index < len(self.properties):
            self.properties[property_index].mark_sold()
            print("Property marked as sold.")
        else:
            print("Invalid property index.")


# Example usage:
if __name__ == "__main__":
    agency = RealEstateAgency()

    # Adding properties
    property1 = Property("123 Main St", 250000, 3, 2, 2000)
    property2 = Property("456 Elm St", 350000, 4, 3, 3000)
    agency.add_property(property1)
    agency.add_property(property2)

    # Displaying properties
    agency.display_properties()

    # Selling a property
    agency.sell_property(0)

    # Displaying properties after sale
    agency.display_properties()
