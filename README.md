# Oracle
Part Finding using computer vision and AWS sagemaker.

Front-end code is in `eye`

## Frontend
Recently Converted to a 800x480 landscape format 

Generally, Takes 3 snapshots of the part being analysed and sends them to the server to be recognised.
Server returns 1 of 3 responses:
* Sure
	* It is differently this singular product
* Maybe
	* It could be one of these 3 options
* Unsure
	* I'm not sure, find the product manually and tell me what it is

There will be a global url-cache for every eye to download; this will have pictures and descriptions for things.


## System Layout:

#### s3: 

| Bucket | Description |
| --- | --- | 
`oracle-inputstage` | for uploading new pictures
`oracle-reference-images` | for classified images
`sagemaker-ap-southeast-2-349967396867` | Stores model / artifiacts.

#### Sagemaker:
	
Notebook has been replicated into notebook folder; it is unnessercary to run a notebook on that server; instead, run it on local servers to save a touch of time and money.

*(NB: I was billed $470/pm for leaving it on )*

* Notebook Instance: [oracle](https://ap-southeast-2.console.aws.amazon.com/sagemaker/home?region=ap-southeast-2#/notebook-instances/openNotebook/oracle?view=classic)

#### Lamba:

In the process of building functions as switches for business logic:

- [ ] `createTrainData`:
	* trigger: s3 `oracle-inputstage` upload
	* function: modify images and move to `oracle-reference-images`
- [x] `turnOffOracle`:
	* trigger: 6pm AWST *Western Australia*
	* function: turns off the servers to save money overnight; this can cut costs by 2/3rds in best case maths
- [ ] `turnOnOracle`:
	* trigger: 8am AEST 
	* function: fires up the server, ready for a batch of problem-solving


