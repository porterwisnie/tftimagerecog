# tftimagerecog


game screenshots scaled to 1920 x 1080
the five squares of characters in the shop for processing have size of 193 x 144
(width x height)

positions of upper left corner from left to right are
1. 480 928
2. 681 928
3. 882 928
4. 1084 928
5. 1285 928

Still missing 0 cards!
	


After gathering all cards, attempting to minimize the number of pixels needed to be looked at to optimize recognition is the next step

For example:

	Every pixel has 4 numbers associated with it:
		Red
		Green
		Blue
		Alpha (opacity) ((I belive is always 255 in this case))


	if every character has a **unique** combination of pixel values at the same point,
	only that one pixel has to be examined in order to decide between all of the champions, 
	however this may not be the case and may require more than one pixel to make these determinations

Chosen pixels to be analyzed from the upper left corner are 170,85 and 51,44

Only one pixel was needed to make unique determination of character for a surprising number of pixels, but checking two
locations is a safer option
 
# Conclusion

After working on this project for a while, a few critical assumptions early on have created major issues

* I assumed that the characters shop cards were fully opaque, however, the background appears to have some effect on the colors of the individual pixels
	
* I was only using one card per charcter for matching, but this approach was extermely faulty due to the background effecting the coloration changes in the background
	
* If I were to refactor everything I would create an equation that does some sort of measurement on the background and measure the offset created by the cards
* This would allow increased accuracy with any of the backgrounds selectable with the game
	
	
In conclusion, this project failed to meet my goals, but it was very informative on what small assumptions can do to a larger project
