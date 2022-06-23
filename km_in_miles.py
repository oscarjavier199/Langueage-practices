#program will let us know hom many KMs are in given miles

class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_55_miles = converter.how_many_kms(55)
print(kms_in_55_miles)