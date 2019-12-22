from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()


y = 0
for y in range(30):
    mc.setBlock(5, y, 5, 0)
    sleep(0.2)
    y = y + 1