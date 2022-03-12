import requests
import csv
import asyncio

account_id = "Account ID"
# please not that cloudflare has rate limit for delete request so using async is not make change in deletion speed.
async def get_all_images_list(image_id):
    url_address = "https://api.cloudflare.com/client/v4/accounts/"+account_id+"/images/v1/"+image_id
    headers = {
        "Authorization": "Bearer " + "Your API Token",
        "Content-Type": "application/json"
    }
    print(url_address)
    response = requests.delete(url=url_address, headers=headers).json()
    return response


with open('image_id_for_delete.csv') as outfile:
    type(outfile)
    csvreader = csv.reader(outfile)
    rows = []
    loop = asyncio.new_event_loop()
    for row in csvreader:
        loop.run_until_complete(get_all_images_list(row[0]))
        print(row[0])

    outfile.close()
