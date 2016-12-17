## a simple script that generates random levels for use in the FPGA

import random

top = []
for i in range(64):
    top.append(random.randint(0,5))

bot = []
for i in top:
    x = random.randint(1,2)
    bot.append(i+x)

# in mojo-arrays are reverse indexed
top.reverse()
bot.reverse()

# prints out the levels in the format accepted by Mojo
def create(input):
    string = "{"
    for i in input:
        string += "3b{:03b}".format(i)
        string += ", "
    string = string[:-2]
    string += "}"
    print(string)

create(top)
create(bot)
