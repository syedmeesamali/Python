from keras.datasets.mnist import load_data

#Load the data
(train_digits, train_labels), (test_digits, test_labels) = load_data()

#dispaly 14 random images from dataset
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

rand_14 = np.random.randint(0, train_digits.shape[0], 14)
sample_digits = train_digits[rand_14]
sample_labels = train_labels[rand_14]

#View the images
num_rows, num_cols =  2,7 
f, ax = plt.subplots(num_rows, num_cols, figsize = (12,5), gridspec_kw = {'wspace': 0.03, 'hspace': 0.01}, squeeze = True)

for r in range(num_rows):
    for c in range(num_cols):
        image_index = r * 7 + c
        ax[r, c].axis("off")
        ax[r, c].imshow(sample_digits[image_index], cmap = 'gray')
        ax[r, c].set_title('No. %d' % sample_labels[image_index])

plt.show()
#plt.close()