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

Still missing 1 card:


	Karthus


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



 
