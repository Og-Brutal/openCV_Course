import os
import cv2

webcam=cv2.VideoCapture(0)

while(True):
    ret,frame=webcam.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0xFF==ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()





# 1️⃣ cv2.waitKey(40)
# cv2.waitKey(40)
# What it does

# Waits 40 milliseconds for a key press.

# Returns the ASCII code of the pressed key.

# If no key is pressed, it returns -1.

# Example return values:

# Key Pressed	Returned Value
# q	113
# a	97
# ESC	27
# nothing	-1

# So this function captures keyboard input.

# 2️⃣ & 0xFF
# cv2.waitKey(40) & 0xFF
# Why this is used

# waitKey() sometimes returns extra bits depending on the system, especially on Windows.

# 0xFF in hexadecimal equals:

# 255

# Binary form:

# 11111111

# Using:

# value & 0xFF

# keeps only the lowest 8 bits (the actual key code).

# Example:

# Returned value = 1048689
# 1048689 & 255 → 113

# which is the ASCII code of 'q'.

# So & 0xFF ensures consistent key detection across platforms.

# 3️⃣ ord("q")
# ord("q")

# ord() converts a character to its ASCII number.

# Example:

# Character	ASCII
# q	113
# a	97
# A	65

# So:

# ord("q") = 113
# 4️⃣ Full Condition
# cv2.waitKey(40) & 0xFF == ord("q")

# This means:

# Wait 40ms → check key press → if key pressed is q, return True.