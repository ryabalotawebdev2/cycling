from django.urls import resolve
from django.test import TestCase
from LMList.views import home_page

from LMList.models import Item, List

from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):
    
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, home_page)
      
   
   
   def test_only_saves_items_when_necessary(self): 
      self.client.get('/')        
      self.assertEqual(Item.objects.count(), 0)
      
class ListViewTest(TestCase):
 
   def test_uses_list_template(self):
      list_ = List.objects.create()        
      response = self.client.get(f'/LMList/{list_.id}/')
      self.assertTemplateUsed(response, 'registration.html')
     
   
   def test_displays_all_list_items(self):        
       list_ = List.objects.create()        
       Item.objects.create(npet='Leonalyn', list=list_)        
       Item.objects.create(npet='Maglines', list=list_)
   
   def test_passes_correct_list_to_template(self):       
       other_list = List.objects.create()        
       correct_list = List.objects.create()        
       response = self.client.get(f'/LMList/{correct_list.id}/')
       self.assertEqual(response.context['list'], correct_list)  
 
class NewListTest(TestCase):   

 
   def test_redirects_after_POST(self):        
       response = self.client.post('/LMList/new', data={'pet': 'A new pet','owner': 'A new owner','address':'A new address','breed': 'A new breed','birthday': 'A new birtday'})                     
       new_list = List.objects.first()        
       self.assertRedirects(response, f'/LMList/{new_list.id}/')
       

       
class NewItemTest(TestCase):
   def test_can_save_a_POST_request_to_an_existing_list(self):       
      other_list = List.objects.create()        
      correct_list = List.objects.create()        
      
      self.client.post(            
          f'/LMList/{correct_list.id}/add_item',            
          data={'pet': 'A new existing pet','owner': 'A new owner','address':'A new address','breed': 'A new breed','birthday': 'A new birtday'}
          ) 
      
      self.assertEqual(Item.objects.count(), 1)        
      new_item = Item.objects.first()        
      self.assertEqual(new_item.npet, 'A new existing pet')       
      self.assertEqual(new_item.list, correct_list)
      
   def test_redirects_to_list_view(self):        
      other_list = List.objects.create()        
      correct_list = List.objects.create()        
      response = self.client.post(            
          f'/LMList/{correct_list.id}/add_item',            
         data={'pet': 'A new pet','owner': 'A new owner','address':'A new address','breed': 'A new breed','birthday': 'A new birtday'})  
      self.assertRedirects(response, f'/LMList/{correct_list.id}/')
   
class ORM(TestCase):

   def test_saving_and_retrieving_items(self):
      list_ = List()        
      list_.save()
      
      first_item = Item()        
      first_item.npet = 'The first (ever) list item' 
      first_item.list = list_ 
      first_item.save()        
               
      second_item = Item()      
      second_item.npet = 'Item the second'
      second_item.list = list_         
      second_item.save()
       
       
      saved_list = List.objects.first()          
      self.assertEqual(saved_list, list_)
                 
      saved_items = Item.objects.all()
      self.assertEqual(saved_items.count(), 2)
       
      first_saved_item = saved_items[0]
      second_saved_item = saved_items[1]      	     
      self.assertEqual(first_saved_item.npet, 'The first (ever) list item')
      self.assertEqual(first_saved_item.list, list_)
      self.assertEqual(second_saved_item.npet, 'Item the second')
      self.assertEqual(second_saved_item.list, list_)





'''
def test_displays_only_items_for_that_list(self):
      correct_list = List.objects.create()
      Item.objects.create(npet='shana', list=correct_list)
      #Item.objects.create(npet='itemey 2', list=correct_list)
      other_list = List.objects.create()
      #Item.objects.create(npet='other list item 1', list=other_list)
      Item.objects.create(npet='other list item 2', list=other_list)        
      
      response = self.client.get(f'/LMList/{correct_list.id}/')
      
      self.assertContains(response, 'shana')
      #self.assertContains(response, 'itemey 2')
      self.assertNotContains(response, 'other list item 1')
      #self.assertNotContains(response, 'other list item 2') '''














'''
from django.test import TestCase
#from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import HttpRequest
#from django.urls import resolve


class HomePageTest(TestCase):

	#def test_root_url_resolve_to_homepage_view(self):
		#found = resolve('/')

	def test_homepage_returns_correct_views(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'owner': 'pet'})
		self.assertIn('pet', response.content.decode())
		#self.assertTemplateUsed(response,'homepage.html')


	


	def test_homepage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')



	def test_homepage_returns_correct_view(self):
		request = HttpRequest()
		response = HomePageTests(request)
		#html = response.content.decode('utf8')
		string_html = render_to_string('homepage.html')
		self.assertEqual(html, string_html)

	#def test_homepage_returns_correct_view(self):
		#request = HttpRequest()
		#reponse = HomePage(request)
		#html = response.content.decode('utf8')
		#string_html = render_to_string('homepage.html')
		#self.assertEqual(html, string_html)


		

	def test_save_POST_request(self):
		reponse = self.client.post('/', data={'pet': 'New entry'})
		newItem = Item.objects.first()
		self.assertEqual(newItemtext, 'New entry')
		self.assertIn('New entry', reponse.content.decode())
		self.assertTemplateUsed(reponse, 'homepage.html')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_save_POST_request(self):
		reponse = self.client.post('/', data={'pet': 'leo'}) 
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'leo')

	def test_redirects_POST(self):
		reponse = self.client.post('/', data={'pet': 'leo'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_template_display_list(self):
		Item.objects.create(text='List item 1')
		Item.objects.create(text='List item 2')
		response = self.client.get('/')
		self.assertIn('List item 1', response.content.decode())
		self.assertIn('List item 2', response.content.decode())
	

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')'''
