#!/usr/bin/env python
# coding: utf-8

# In[15]:


import imageio
get_ipython().run_line_magic('cd', '/home/theghub/sgoliber/simpleice')


# In[16]:


get_ipython().run_line_magic('cd', '/home/theghub/sgoliber/simpleice')


# In[17]:


smb_steps = ['-20','-10','0','10','20']
for smb in smb_steps:
    
    for fps in [1,2,4]:
    
        frames = []

        for i in range(1,100,1):
            image = imageio.imread('plots/smb_step_'+smb+'_'+str(i)+'.png')
            frames.append(image)


        imageio.mimsave('gifs/smb_step_'+smb+'_'+str(fps)+'_.gif', # output gif
                    frames,          # array of input frames
                    fps = fps,
                    loop = 2)         # optional: frames per second


# In[ ]:




