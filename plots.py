#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

# Define the scale range
scale_values = np.linspace(1, 32, 100)

# Define the original max position embeddings
original_max_position_embeddings = 4096

# Calculate the scaling factors
scaling_factor_su = np.sqrt(1 + np.log(scale_values) / np.log(original_max_position_embeddings))
scaling_factor_yarn = 0.1 * np.log(scale_values) + 1.0

# Set the default font size for all elements
plt.rcParams.update({'font.size': 12})  # Adjust this value as needed

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the scaling factors
ax.plot(scale_values, scaling_factor_su, label='Phi3SuScaledRotaryEmbedding', color='#419bf9')
ax.plot(scale_values, scaling_factor_yarn, label='Phi3YarnScaledRotaryEmbedding', color='#ee6723')

# Set labels and title with hex color #666666
ax.set_xlabel('Scale', color='#666666')
ax.set_ylabel('Scaling Factor', color='#666666')
ax.set_title('Comparison of Scaling Factors with original_max_position_embeddings = 4096', color='#666666')

# Customize the tick parameters
ax.tick_params(axis='x', colors='#666666')
ax.tick_params(axis='y', colors='#666666')

# Customize the spines (box) color
ax.spines['top'].set_color('#666666')
ax.spines['right'].set_color('#666666')
ax.spines['bottom'].set_color('#666666')
ax.spines['left'].set_color('#666666')

# Add a legend and set the text color to #666666
legend = ax.legend(framealpha=0.0, edgecolor='#666666')
plt.setp(legend.get_texts(), color='#666666')

# Save the plot as an SVG file with a transparent background
plt.savefig('scaling_factors_comparison.svg', format='svg', transparent=True)

# Display the plot
plt.show()


# In[ ]:




