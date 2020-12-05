# VISION meeting presentation
# Plotting the VENN diagrams for TFs FoxA1, Ascl1 and Hoxc6

import matplotlib
matplotlib.use('Agg')
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt

# Hoxc6 Data from PMID:33028607
cell_type_mn = 9037
cell_type_es = 9224
shared = 1068
out = venn2(subsets=(cell_type_es, cell_type_mn, shared),
            set_labels=('', ''),
            set_colors=('#03506f', '#bbbbbb'),
            alpha=0.7)
venn2_circles(subsets=(cell_type_es, cell_type_mn, shared),
              color='#1c2b2d')
for text in out.subset_labels:  #change number size
    text.set_fontsize(14)
plt.savefig('Venn_hoxc6.pdf')

# Ascl1 data: ~/group/lab/divyanshi/projects/iEB/EB-20180530/misc/diffBind/Ascl1/Ascl1/paint
fig, ax = plt.subplots()
cell_type_mef = 9654
cell_type_es = 8744
shared = 7714
out = venn2(subsets=(cell_type_es, cell_type_mef, shared),
            set_labels=('', ''),
            set_colors=('#c05555', '#ffc85c'),
            alpha=0.7)
venn2_circles(subsets=(cell_type_es, cell_type_mef, shared),
              color='#1c2b2d')
for text in out.subset_labels:  #change number size
    text.set_fontsize(14)
plt.savefig('Venn_ascl1.pdf')

# FoxA1
# Data from PMID: 18358809
cell_type_mcf7 = 1179
cell_type_lncap = 1898
shared = 855
fig, ax = plt.subplots()
out = venn2(subsets=(cell_type_mcf7, cell_type_lncap, shared),
            set_labels=('', ''),
            set_colors=('#c05555', '#ffc85c'),
            alpha=0.7)
for text in out.subset_labels:  #change number size
    text.set_fontsize(14)
venn2_circles(subsets=(cell_type_mcf7, cell_type_lncap, shared),
              color='#1c2b2d')
plt.savefig('Venn_foxa1.pdf')



