# Cloudflare-image-service
Here are the sample code to make image list, delete image or upload images to Cloudflare Image Service

**API Token**

Create API Token According to [cloudflare optimazation doc](https://developers.cloudflare.com/images/cloudflare-images/upload-images/api-token/). Please Note that you need free accoutn on cloudflare.
As shortcut, you can [click Here](https://dash.cloudflare.com/profile/api-tokens) to directly go to API Token Generation Page.
for image optimization service you need to create Custom Token. all other setting filed will be completed easyly. Please, Wright Down the Generated Key. you could not view it again.

**Account ID**

Also, you need your Account ID in cloudflare. Log in to the Cloudflare dashboard, and select your account and website.
In Overview, scroll down to find your Account ID. also it's visible on URL (https://dash.cloudflare.com/### Your Account ID###)

**Image Listing**
For listing all of your image on Cloudflare, easily config and run imagelist.py.
please provide required info as describe in file.
Cloudflare Official Document ca be found [here](https://api.cloudflare.com/#cloudflare-images-list-images).
**Image Deletion**
For deleting Specific Image or bulk Delete Images, just put the Image ID (Cloudflare Image ID) in image_id_for_delete.csv and run the image delete.py
