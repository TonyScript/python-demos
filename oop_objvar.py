#/usr/local/bin/python3
# coding=UTF-8

class Robot:
    """This is Class Robot

    展示类变量与对象变量的区别
    """

    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        """function die

        打印出剩余的对象数量
        """

        print("{} is being destoryed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """function say_hi

        打印出当前对象的名称
        """

        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """装饰器修饰的方法 function how_may

        打印出当前的对象数量
        """

        print("We have {:d} robots.".format(cls.population))


droidOne = Robot("R2-D2")
droidOne.say_hi()
droidOne.how_many()

droidTwo = Robot("C-3PO")
droidTwo.say_hi()
droidTwo.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destory them.")

droidOne.die()
droidTwo.die()
Robot.how_many()
