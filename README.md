# Oracle
Part Finding using computer vision and AWS sagemaker.

* Frontend code is in `eye`
* `partfinder.stl` is the original bowl design, [view in github](./partfinder.stl)


## System overview

Generally, Takes 3 snapshots of the part being analysed and sends them to the server to be recognised.
Server returns 1 of 3 responses:
* Sure
	* It is differently this singular product
* Maybe
	* It could be one of these 3 options
* Unsure
	* I'm not sure, find the product manually and tell me what it is
	

There will be a global url-cache for every eye to download; this will have pictures and descriptions for things. Designed to be linked with a backend that would show the particular product's image ( for human confirmation ) as well as pricing and details.

### Other components:

* `eye` for front-end interaction on a 800x460 touch screen interface.
* lambda functions for business logic (scheduling model rebuilds, shut-off periods, controlling the rpi authorising system)
* AWS sagemaker for actual model training (original notebook in notebook folder)

