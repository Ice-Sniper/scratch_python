from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()


y = 0
for y in range(8):
    mc.setBlock(5, y, 5, 41)
    sleep(0.5)
    y = y + 1