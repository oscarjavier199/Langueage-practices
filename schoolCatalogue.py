# the program will print inforation about some fake schools
# using mostly getter and setter besides other python functions

class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getname(self):
      return self.name

  def getlevel(self):
      return self.level

  def getnumberOfStudents(self):
      return self.numberOfStudents
    
  def setnumberOfStudents(self, newNumberOfStudents):
      self.numberOfStudents = newNumberOfStudents
    
  def __repr__(self):
      return str(("A {level} school named {name} with {numberOfStudents} students\n".format(level = self.level, name = self.name, numberOfStudents = self.numberOfStudents)))

mySchool = School("Codecademy", "high", 100)
print(mySchool)

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy
   
    def getPickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "And the pickup polity is: {pickupPolicy}\n".format(pickupPolicy = self.pickupPolicy)

testSchool = PrimarySchool("Start Smart", 300, "Pickup Allowed!")
print(testSchool)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)

    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    parentRepr = super().__repr__()
    return parentRepr + "And we have great {sportsTeams} teams!".format(sportsTeams = self.sportsTeams)

c = HighSchool("Codecademy High", 500, "Tennis and Basketball")
print(c.getSportsTeams())