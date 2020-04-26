from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import os
import requests as rq #to download the images
my_url='https://www.imdb.com/list/ls068010962/'
uclient = ureq(my_url) #it will download the whole webpage and store it in uclient(variable)
page_html=uclient.read() #as uclient.read wud dump the data uclient has so we storing it in page_html because this is just the raw preprocessed html code 
uclient.close() #this is done as this is an open internet connection so our client can go anywherfe berserk
page_soup=soup(page_html, "html.parser") #it will parse the webpage and we will store it in page-soup again as a html file format

my_url2='https://www.imdb.com/list/ls073889754/'
uclient2 = ureq(my_url2) #it will download the whole webpage and store it in uclient(variable)
page_html2=uclient2.read() #as uclient.read wud dump the data uclient has so we storing it in page_html because this is just the raw preprocessed html code 
uclient2.close() #this is done as this is an open internet connection so our client can go anywherfe berserk
page_soup2=soup(page_html2, "html.parser") #it will parse the webpage and we will store it in page-soup again as a html file format


my_url3='https://www.imdb.com/list/ls062161896/'
uclient3 = ureq(my_url3) #it will download the whole webpage and store it in uclient(variable)
page_html3=uclient3.read() #as uclient.read wud dump the data uclient has so we storing it in page_html because this is just the raw preprocessed html code 
uclient3.close() #this is done as this is an open internet connection so our client can go anywherfe berserk
page_soup3=soup(page_html3, "html.parser") #it will parse the webpage and we will store it in page-soup again as a html file format

# my_url, my_url2 & my_url3 contains address of 3 sites 
containerss = page_soup.findAll("div",{"class":"lister-item mode-detail"}) #grabs all list of actors
containerss2= page_soup2.findAll("div",{"class":"lister-item mode-detail"}) #grabs all list of new actors
containerss3= page_soup3.findAll("div",{"class":"lister-item mode-detail"}) #grabs all list of south indian  actors
os.mkdir("ActorPhotos")
filename="actors.csv"
f=open(filename,"w")
headers = "ACTOR NAME,PERSONALITY_TRAITS(1),PERSONALITY TRAITS(2),PERSONALITY TRAITS(3) \n"
f.write(headers)



#FOR BOLLYWOOD ACTORS AND ACTRESSES
for container in containerss:
		actor_name=container.div.a.img["alt"]
		

		image= container.div.img["src"]	# image conatains the links of the images of each container i.e actor
		img_data=rq.get(image).content
		with open("ActorPhotos\\"+str(actor_name)+'.jpg','wb+') as f1:
			f1.write(img_data)
		

		linked=container.div.a["href"]
		linked="https://www.imdb.com"+linked+"bio?ref_=nm_dyk_tm_sm#trademark"
		clients=ureq(linked)
		page1_html=clients.read()
		clients.close()
		page1_soup=soup(page1_html, "html.parser")
		
		for em in page1_soup('em'):  #to remove all the sources links under em tag
			em.decompose()
		for td in page1_soup('td'):	#to remove all the td tags containing the heights and birth dates
			td.decompose()
		

		a = page1_soup.findAll("h4",{"class":"li_group"}) 
		i=10
		t=['li_group']
		
		traits=[]
		
		try:
			for sibling in a[3].next_siblings:
				if(sibling!='\n' and  sibling.get('class')!=t):   #to remove all headings like Mini Bio ,etc
					traits.append(sibling)
				i=i-1
				if(i==0):
					break
		except :
			i=8
			for sibling in a[0].next_siblings:
				if(sibling!='\n' and sibling.get('class')!=t):
					traits.append(sibling)
				i=i-1
				if(i==0):
					break
		
		final_traits_bolly=[]
		
		for j in traits:
			final_traits_bolly.append(j.text.strip())
		
		
		
		p_trait_bolly1=final_traits_bolly[0]
		p_trait_bolly2=final_traits_bolly[1]
		p_trait_bolly3=final_traits_bolly[2]
		
    
    
		
		print("Actor Name: ", actor_name)
		print("Personality Traits1 : ",p_trait_bolly1) 
		print("Personality Traits2 : ",p_trait_bolly2)
		print("Personality Traits3 : ",p_trait_bolly3)

		f.write(actor_name+","+ p_trait_bolly1+ ","+p_trait_bolly2+","+p_trait_bolly3+'\n')
		
#FOR NEWCOMERS OF BOLLYWOOD
for container in containerss2:
	actor_name=container.div.a.img["alt"]
		

	image= container.div.img["src"]	# image conatains the links of the images of each container i.e actor
	img_data=rq.get(image).content
	with open("ActorPhotos\\"+str(actor_name)+'.jpg','wb+') as f2:
		f2.write(img_data)
		

	linked1=container.div.a["href"]
	linked1="https://www.imdb.com"+linked1+"bio?ref_=nm_ov_bio_sm"
	clients1=ureq(linked1)
	page2_html=clients1.read()
	clients1.close()
	page2_soup=soup(page2_html, "html.parser")
		
	for em in page2_soup('em'):  #to remove all the sources links under em tag
		em.decompose()
	for td in page2_soup('td'):	#to remove all the td tags containing the heights and birth dates
		td.decompose()
		

	a1 = page2_soup.findAll("h4",{"class":"li_group"}) 
	i=10
	t=['li_group']
		
	traits1=[]
		
	try:
		for sibling in a1[1].next_siblings:
			if(sibling!='\n' and  sibling.get('class')!=t):   #to remove all headings like Mini Bio ,etc
				traits1.append(sibling)
			i=i-1
			if(i==0):
				break
	except :
		i=8
		for sibling in a1[0].next_siblings:
			if(sibling!='\n' and sibling.get('class')!=t):
				traits1.append(sibling)
			i=i-1
			if(i==0):
				break
		
	final_traits_newbolly=[]
		
	for j in traits1:
		final_traits_newbolly.append(j.text.strip())
		
		
	p_trait_newbolly1=final_traits_newbolly[0]
	p_trait_newbolly2=final_traits_newbolly[1]
	p_trait_newbolly3=final_traits_newbolly[2]
		
    
    
		
	print("Actor Name: ", actor_name)
	print("Personality Traits1 : ",p_trait_newbolly1) 
	print("Personality Traits2 : ",p_trait_newbolly2)
	print("Personality Traits3 : ",p_trait_newbolly3)

	f.write(actor_name+","+ p_trait_newbolly1+ ","+p_trait_newbolly2+","+p_trait_newbolly3+'\n')


#FOR SOUTH INDIAN ACTORS AND ACTRESSES
for container in containerss3:
	actor_name=container.div.a.img["alt"]
		

	image= container.div.img["src"]	# image conatains the links of the images of each container i.e actor
	img_data=rq.get(image).content
	with open("ActorPhotos\\"+str(actor_name)+'.jpg','wb+') as f3:
		f3.write(img_data)
		

	linked2=container.div.a["href"]
	linked2="https://www.imdb.com"+linked2+"bio?ref_=nm_ov_bio_sm#trademark"
	clients2=ureq(linked2)
	page3_html=clients2.read()
	clients2.close()
	page3_soup=soup(page3_html, "html.parser")
		
	for em in page3_soup('em'):  #to remove all the sources links under em tag
		em.decompose()
	for td in page3_soup('td'):	#to remove all the td tags containing the heights and birth dates
		td.decompose()
		

	a2 = page3_soup.findAll("h4",{"class":"li_group"}) 
	i=10
	t=['li_group']
		
	traits2=[]
		
	try:
		for sibling in a2[3].next_siblings:
			if(sibling!='\n' and  sibling.get('class')!=t):   #to remove all headings like Mini Bio ,etc
				traits2.append(sibling)
			i=i-1
			if(i==0):
				break
	except :
		i=8
		for sibling in a2[0].next_siblings:
			if(sibling!='\n' and sibling.get('class')!=t):
				traits2.append(sibling)
			i=i-1
			if(i==0):
				break
	
	
	final_traits_south=[]
		
	for j in traits2:
		final_traits_south.append(j.text.strip())
		
		
		
		
	p_trait_south1=final_traits_south[0]
	p_trait_south2=final_traits_south[1]
	p_trait_south3=final_traits_south[2]
		
    
    
		
	print("Actor Name: ", actor_name)
	print("Personality Traits1 : ",p_trait_south1) 
	print("Personality Traits2 : ",p_trait_south2)
	print("Personality Traits3 : ",p_trait_south3)

	f.write(actor_name+","+ p_trait_south1+ ","+p_trait_south2+","+p_trait_south3+'\n')
	
			

f1.close()