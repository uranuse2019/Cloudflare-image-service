import requests


def get_all_images_list():
    # Use Token Created on Cloudflare
    headers = {
        "Authorization": "Bearer " + "API TOKEN",
        "Content-Type": "application/json"
    }
    account_id = "Account ID"
    all_time_entries = []
    # Cloudflare support Maximum of 100 Item per page so you need to calculate the Total Page number (default value:
    # 50 min value:10 max value:100)
    for page in range(1, 93):
        url = "https://api.cloudflare.com/client/v4/accounts/" + account_id + "/images/v1?page=" + str(
            page) + "&per_page=100"
        response = requests.get(url=url, headers=headers).json()
        # you can change the field as your requirements.
        for image in response['result']['images']:
            id_res = image['id'] + "," + image['filename']
            all_time_entries.append(id_res)
        page += 1
        print(page)
    return all_time_entries


# Create CSV File called Image List.csv which include Image ID and Image File Name
with open('image_list.csv', 'w') as outfile:
    # write a row to the csv file
    for row in get_all_images_list():
        outfile.write(row + "\n")

    outfile.close()
