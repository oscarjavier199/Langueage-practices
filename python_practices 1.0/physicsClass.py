# program will print some fundamental physical properties

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# here we will get the convertion of Fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
print("100 F to C:", f100_in_celsius)


# here we will ger the convertion of Celsius
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print("0 C to F:", c0_in_fahrenheit)


# here we will get how many Newtons of force a Train has
def get_force(mass, acceleration):
  return mass * acceleration
train_force = (train_mass * train_acceleration)
print("Train Force:", train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass, c = 3*10**8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")


