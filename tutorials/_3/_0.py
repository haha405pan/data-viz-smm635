# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
   Stacked barchart
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk
        -- credits to the Matplotlib team

Dates: - created 
       - last change 

Notes: --

"""

# %% load libraries
# -----------------

import numpy as np
import matplotlib.pyplot as plt


# %% style
# --------

plt.style.use('fivethirtyeight')


# %% fake data
# ------------

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 50
x = np.random.normal(mu, sigma, size=100)


# %% figure
# ---------

# create
fig, ax = plt.subplots(figsize=(8, 4))

# plot the cumulative histogram
n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
                           cumulative=True, label='Empirical')

# Add a line showing the expected distribution.
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
y = y.cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

# Overlay a reversed cumulative histogram.
ax.hist(x, bins=bins, density=True, histtype='step', cumulative=-1,
        label='Reversed emp.')

# tidy up the figure
ax.grid(False)
ax.legend(loc='best')
ax.set_title('Cumulative step histograms')
ax.set_xlabel('Annual rainfall (mm)')
ax.set_ylabel('Likelihood of occurrence')

# save plot
plt.savefig('cumulative_historam.pdf')

# show plot
plt.show()
