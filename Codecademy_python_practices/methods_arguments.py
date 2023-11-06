class DistanceConverter:
    """A class to convert miles to kilometers"""
    kms_in_miles = 1.609

    def how_many_kms(self, miles):
        return miles * self.kms_in_miles


converter = DistanceConverter()
print(converter.how_many_kms(5))
