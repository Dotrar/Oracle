# Oracle
Part Finding using computer vision and AWS sagemaker.

## Layout:

#### s3: 

* oracle-inputstage
	* for uploading new pictures

* oracle-reference-images
	* for classified images

* sagemaker-ap-southeast-2-349967396867
	* Stores model / artifiacts.

#### Sagemaker:
	
* Notebook Instance: [oracle](https://ap-southeast-2.console.aws.amazon.com/sagemaker/home?region=ap-southeast-2#/notebook-instances/openNotebook/oracle?view=classic)

* Trainer Notebooks in notebook directory

#### Lamba:

* `createTrainData`:
	* trigger: s3 `oracle-inputstage` upload
	* function: modify images and move to `oracle-reference-images`
	 


