from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup
import re


def crawl_website(request):
    message = None
    error = None
    result = None  # Initialize result to None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']  # Correctly get the URL from the form
            
            # Crawl the property information
            try:
                response = requests.get(url)
                # print (response.text)
                
                soup = BeautifulSoup(response.text, 'html.parser')
              
                
                # Extract data
                title = soup.find('title').text if soup.find('title') else ''
                urls = [a['href'] for a in soup.find_all('a', href=True)]  # Extract all hrefs from anchor tags
                property_size = soup.find('div', class_='size').text if soup.find('div', class_='size') else ''
                price = soup.find('span', class_='price').text if soup.find('span', class_='price') else ''
                img_sources = [img['src'] for img in soup.find_all('img')]
                # Extract image sources within anchor tags
                a_img_sources = [img['src'] for a in soup.find_all('a') for img in a.find_all('img')]
                property_images = img_sources + a_img_sources
                # Search for categories using the 'card-categories' CSS selector
                property_categories = soup.select_one('.card-categories').text if soup.select_one('.card-categories') else ''

                # Regex pattern for email addresses
                email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
                email_matches = re.findall(email_pattern, soup.text)
                email = email_matches[0] if email_matches else ''  # Assuming the first match is the desired email

                # Regex pattern for location (customize the regex according to your needs)
                location_pattern = r'\d{1,3} [a-zA-Z ]+, [a-zA-Z ]+, [a-zA-Z ]+, \d{5}'
                location_matches = re.findall(location_pattern, soup.text)
                location = location_matches[0] if location_matches else ''  # Assuming the first match is the location
                
                # Save to database
                property_data = {
                    'urls': urls,
                    'title': title,
                    'size': property_size,
                    'location': location,
                    'price': price,
                    'images': property_images,
                    'categories': property_categories,
                    'emails': email,
                    'row': soup.find('body').text if soup.find('body') else 'No Content'
                }
                ScrapedData.objects.create(**property_data)
                result = property_data 
                message = f"Property information saved successfully!"
            except Exception as e:
               error = f"Error: {str(e)}"
    else:
        form = URLForm()
    return render(request, 'crawlers/crawlerForm.html',{
        'form': form,
        'message': message,
        'error': error,
        'result': result,
    })

# Optional results view for displaying saved data
# def results(request):
#     crawled_data = ScrapedData.objects.all()
#     return render(request, 'crawlers/results.html', {'data': crawled_data})
