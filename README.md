# Flappy Bit

![flappy-bit](/flappy-bit.jpg)

A hardware implementation of the famous mobile game flappy bird. Makes use of the [Mojo V3](https://embeddedmicro.com/products/mojo-v3.html) FGPA development board.

####Gameplay
The yellow LEDs represent the bird's level while the red LEDs corresponds to top and bottom boundaries. The aim of the game is to make sure the bird is between the boundaries when the countdown timer reaches 0. The bird rises when the button is pressed and falls naturally otherwise.

As your score increases, the countdown timer becomes faster, increasing the difficulty. The score is displayed on the left seven-segment-display while the max score for the session is stored on the right seven-segment-display

#### FPGA Design

![](/schematics1.jpg)
![](/schematics2.jpg)
![](/schematics3.jpg)

#### Physical circuitry

There are 8 output pins for the red LED rows, 4 for the counter, 7+4 output pins for each seven-segment-display and 1 input pin for the button.

It would have been impractical to have an output pin for each of the yellow LEDs (32), thus 5 [74HC238](http://www.nxp.com/documents/data_sheet/74HC_HCT238.pdf) 3to8 decoders are used to decode 5 output pins into the corresponding yellow LED.

![](/physicalschematics.jpg)


