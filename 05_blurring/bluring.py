import os
import cv2

image=cv2.imread(os.path.join("..","About_Image","rabbit.png"))
recized_image=cv2.resize(image,(image.shape[1]//2,image.shape[0]//2))

k_size=7
blurred_image=cv2.blur(recized_image,(k_size,k_size))
gaussain_blurred_image=cv2.GaussianBlur(recized_image,(k_size,k_size),5)
median_blurred_image=cv2.medianBlur(recized_image,k_size)


cv2.imshow("img",recized_image)
cv2.imshow("blurred_image",blurred_image)
cv2.imshow("gaussain_blurred_image",gaussain_blurred_image)
cv2.imshow("median_blurred_image",median_blurred_image)
cv2.waitKey(0)







# Yes — that idea is almost correct, just one small clarification.

# Core Idea

# When you write:

# cv2.blur(image, (7,7))

# OpenCV does this:

# Take a 7 × 7 square region (kernel) around the pixel.

# Compute the average of all pixels inside that square.

# Replace the center pixel with that average value in the output image.

# Visual Intuition

# Imagine a 7×7 window centered on a pixel:

# □ □ □ □ □ □ □
# □ □ □ □ □ □ □
# □ □ □ □ □ □ □
# □ □ □ X □ □ □
# □ □ □ □ □ □ □
# □ □ □ □ □ □ □
# □ □ □ □ □ □ □

# X = the pixel currently being processed

# The square contains 49 pixels (7×7)

# OpenCV calculates:

# New value of X = average of all 49 pixels

# Then it moves this 7×7 window to the next pixel and repeats the process across the whole image.

# Important Detail

# The original pixel is included in the averaging.

# So the calculation is:

# NewPixel = (sum of 49 pixels) / 49
# How the Kernel Moves

# The grid slides across the image like this:

# [7×7 window] → → →
#                ↓
# → → → → → → → →
#                ↓
# → → → → → → → →

# For every pixel, OpenCV computes a new averaged value.

# Why This Causes Blur

# Averaging mixes nearby colors:

# Example:

# Original pixels
# 10 20 30
# 40 200 60
# 70 80 90

# After averaging, the center pixel (200) becomes closer to surrounding values, making the image smoother and less sharp.

# Simple One-Line Intuition
# 7×7 blur = replace each pixel with the average color of a 7×7 neighborhood around it