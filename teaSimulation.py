#sarahwardlow
class teaMug:
    """Represents the amount of tea in a mug"""
myMug = teaMug()

myMug.color = "blue"
myMug.size = "12 ounce"
myMug.shape = "heart"
myMug.amount = 12


def tea_drinking_simulation(t, time):
    tea_rem = myMug.amount - 2*time
    result = "My %s, %s %s shaped mug has" % (myMug.color, myMug.size, myMug.shape), tea_rem, "ounces left after", time, "minutes"
    print(result)

tea_drinking_simulation(myMug, 4)
