# -*- coding = utf-8 -*-
#!/usr/bin/env python
import os
import requests
import bs4

#下厨房的鱼香肉丝菜谱页面的url
url = 'https://m.xiachufang.com/category/40076/pop/'
os.makedirs('recipe_img', exist_ok=True)

#download the page
print('Downloading page %s...' % url)
# 使用request模块从下厨房下载鱼香肉丝菜谱文件
res = requests.get(url)

#emsure download successed
try:
    res.raise_for_status()
except Exception as e:
	print('There was a problem: %s' % (e))

soup = bs4.BeautifulSoup(res.text, 'lxml')

#从下载的菜谱文件中寻找img 元素
get_image = soup.select('.cover img')
recipe_list = []
for i in range(20):
    if get_image == []:
	    print('Could not found the img')
    else:
	    img_url = get_image[i].get('src')
	    recipe_list.append(img_url)

        #download the img
	    print('Downloading img %s...' % (recipe_list[i]))
	    res = requests.get(recipe_list[i])
	    res.raise_for_status()

	    file_path = os.path.join('recipe_img', os.path.basename(recipe_list[i]))
	    imgFile = open(file_path, 'wb')
	    for i in res.iter_content(100000):
	        imgFile.write(i)
	    imgFile.close()
	    

print('Done.')



        







