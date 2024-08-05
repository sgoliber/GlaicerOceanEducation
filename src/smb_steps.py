#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

get_ipython().run_line_magic('cd', '/home/theghub/sgoliber/simpleice')


# In[4]:


smb_steps = ['-20','-10','0','10','20']
for smb in smb_steps:
    h = pd.read_csv('smbsteps/SMBsteps_'+smb+'pct_h.csv',header=None)
    bed = pd.read_csv('smbsteps/SMBsteps_'+smb+'pct_bed.csv',header=None)

    bedx = pd.read_csv('smbsteps/SMBsteps_'+smb+'pct_bedx.csv',header=None)
    bedx = bedx.iloc[0].to_numpy()
    bedx = bedx/1000

    bedz = pd.read_csv('smbsteps/SMBsteps_'+smb+'pct_bedz.csv',header=None)
    bedz = bedz.iloc[0].to_numpy()

    slope, _ = np.polyfit(bedx, bedz, 1)
    # Extend the line
    x_min = np.min(bedx)
    x_max = np.max(bedx)
    y_min = np.min(bedz)
    y_max = np.max(bedz)
    extension_factor = 1.5  # Adjust this factor to extend the line further
    extended_x = np.array([x_min - extension_factor * (x_max - x_min), x_max + extension_factor * (x_max - x_min)])
    extended_y = slope * extended_x

    # Create a figure and axes
    initial_pos = bed.iloc[1].to_numpy()[-1]*-1

    for i in range(1,100,1):
        fig, ax = plt.subplots(figsize=(10,6))
        ax.fill_between(extended_x, extended_y, y2 = -1000, color='peru',hatch="\\",edgecolor="sienna", zorder=1000)
        bed_p = bed.iloc[i].to_numpy()
        h_p = h.iloc[i].to_numpy()

        ax.fill_between(bed_p*-1,h_p*1000, y2=-1000, alpha=0.6,color='lightsteelblue', zorder=0)

        plt.savefig('plots/smb_step_'+smb+'_'+str(i)+'.png')

        ax.set_ylabel('Z (m)')
        ax.set_xlabel('X (km)')
        ax.set_title('Year = ' + str(i))

        ax.set_xlim(365,385)
        ax.set_ylim(-1000,1000)
        
        ax.tick_params(axis='x', labelrotation = 45)
                
        ax.vlines(x=initial_pos, ymin=-1000, ymax=1000, linewidth=1, color='r',zorder=500)
        ax.text(initial_pos+.1, -100, 'Initial Position', rotation = 'vertical',fontsize = '15')


        plt.savefig('plots/smb_step_'+smb+'_'+str(i)+'.png')
        plt.close()


# In[ ]:




