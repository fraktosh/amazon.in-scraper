import new
import csv
import requests
from bs4 import BeautifulSoup
import pandas
# URL to scrape
url = "https://www.amazon.in/gp/bestsellers/"+new.af

headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
# Make a request to the website
response = requests.get(url, headers=headers)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the best sellers on the page
best_sellers = soup.find_all('div', {'class': 'p13n-gridRow _cDEzb_grid-row_3Cywl'})
#print(best_sellers)
# Print the titles of each best seller
for best_seller in best_sellers:
    string= best_seller.text.strip()

array= [i.split('₹') for i in string.split('#')]
a = array.pop(0)
print(array)
for x in range(0,len(array)-1):
    temp= array[x][0]
    array[x][0]="#" + temp
    #temp1 = array[x][1]
    #array[x][]="₹" + temp1
csv_filename=new.af+".csv"
pandas.DataFrame(array).to_csv(csv_filename)  


#with open('amazon_bestsellers.csv', mode='w', newline='', encoding='utf-8') as file:
   #writer = csv.writer(file)
    #writer.writerow(['Title', 'Author', 'Price'])

    # Write each best seller to the CSV file
 #   for best_seller in best_sellers:
        #title = best_seller.find('div', {'class': '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1'}).text.strip()
        #ratings = best_seller.find('div', {'class': 'a-icon-row'}).text.strip()
        #price = best_seller.find("a", {'class': 'a-size-base a-color-price'})

  #      writer.writerow([best_seller.find_all('div', {'class': '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1'}).text.strip(), best_seller.find_all('div', {'class': 'a-icon-row'}).text.strip(),best_seller.find('span', {'class': '_cDEzb_p13n-sc-price_3mJ9Z'}).text.strip()])
        #print(best_seller.find('span', {'class': '_cDEzb_p13n-sc-price_3mJ9Z'}).text.strip())