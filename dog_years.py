# program will let us know the equivalent of one dog year into human years
class Dog:
  dog_time_dilation = 7
  
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pitbull = Dog()
pitbull.time_explanation()