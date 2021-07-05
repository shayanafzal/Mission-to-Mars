#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[77]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[78]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[79]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[80]:


slide_elem.find('div', class_='content_title')


# In[81]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[82]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[83]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[84]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[85]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[86]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[87]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[88]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[89]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[90]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[91]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[92]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
h_img_soup = soup(html, 'html.parser')
h_img_soup

for i in range(4): 
    h_info = {}
    
    h_info['title'] = h_img_soup.find_all('h3')[i].text
    browser.find_by_css("a.product-item h3")[i].click()
    
    img_url = browser.links.find_by_text("Sample")
    h_info['image_url'] = img_url['href']
    hemisphere_image_urls.append(h_info)
    
    browser.back()    


# In[93]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[94]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




