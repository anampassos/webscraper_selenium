#!/usr/bin/env python
# coding: utf-8

# In[17]:


from selenium import webdriver

driver = webdriver.Chrome()
# driver = navegador

#another way to do it is to tell python the path to the chromedriver file 
# servico = Service(r'path_to_file)
# driver = webdriver.Chrome(service = servico)

# to ensure you will always have the latest chromedriver version, you can download the webdriver each time the code is run
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# servico = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = Servico)


# In[18]:


# to ensure you will always have the latest chromedriver version, you can download the webdriver each time the code is run
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


# ## Open Pages from the Internet

# In[20]:


import os

caminho = os.getcwd() 
arquivo = caminho + r"\Pagina Hashtag.html"
# (cwd = current working directory)
# print(caminho)
# navegador.get(arquivo)

driver.get("https://www.hashtagtreinamentos.com/")


# In[5]:


from selenium.webdriver.common.by import By

# nevagador.find_element -> 1 item
# navegador.find_elements > lista
driver.find_element(By.ID, 'firstname').send_keys('Ana Maria')
driver.find_element(By.ID, 'email').send_keys('teste@gmail.com')
driver.find_element(By.CLASS_NAME, 'botao-formulario').send_keys('teste@gmail.com')


# ## Selecionar vários elementos

# In[6]:


lista_elementos = driver.find_elements(By.CLASS_NAME, 'nav-link')

#não preciso saber a posição do elemento, posso pegar pelo texto do item
for elementos in lista_elementos:
    if "blog" in elementos.text.lower():
        elementos.click()
        break


# ## Pegando atributos de um elemento
# ##### Ex1: Link do Whatsapp

# In[7]:


texto = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/div[2]/div[5]/div[2]/a').get_attribute('href')
print(texto)


# ##### Ex2: Imagens dos cursos

# In[8]:


link = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div[1]/a').get_attribute('href')
print(link)


# ### Pegar todos os links das imagens

# In[16]:


lista_elementos = driver.find_elements(By.CLASS_NAME,'dados') #lista de figures
for elemento in lista_elementos:
    try:
        link = elemento.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(link)
    except:
        continue


# ### Preenchendo Formulários

# In[ ]:




