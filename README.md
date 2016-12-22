# rasp-info-display
Small project which will be built mostly in Python (Backend) and React.js (Frontend).

This is the repo for my little rasp-info-display-project. I want to display stuff like the current weather, when to leave to catch the next tram and other shizzle.

The rasp + display will be put up next to my frontdoor.

# basic concept idea

* backend/
	* config.py // basic config
	* widgets/
		* calender/
		* cats/
		* todo/
		* tram/
		* weather/
		* ...
* frontend/
	* index.html // view for the rasp display, gets
				 generated based on admin
	* admin/
		* index.html // configure the index.html within
					 fe-root to look like you want it, 
					 based on the widgets + configure 
					 them here