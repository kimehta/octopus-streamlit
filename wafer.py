import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import cv2
import numpy
import streamlit as st
from keras.models import load_model

def get_circle_defects(pattern:str, r:int=50):
    pattern = pattern.lower()
    def get_defects(low:float = 0.0, high:float = 1.0, p:float = 1.0):
        # simulate defect density wafer map
        #low: minimum % of defects per die location
        #high: maximum % of defects per die location
        #p: 0...1 random change of finding defect each die(separate from random count at the given die)
        
        # random 0...1 (simulating defect in this place found in % of wafers)
        square = numpy.random.uniform(low, high, (r*2, r*2))
        
        # discard defects of some places based on random probability p
        dropper = lambda t: 0.0 if (random.random() > p) else float(t)
        square = numpy.vectorize(dropper)(square)
        
        # square => circle
        circle = numpy.zeros_like(square)
        cv2.circle(circle,(r, r), r, 1, -1)
        result = circle * square
        return result
        
    if pattern == 'minimal':
        result = get_defects(0, 0.05, 0.03)
    
        return result
    if pattern == 'random':
        result = get_defects(0.3, 1, 0.03)
        return result
    
    if pattern == 'ring edge':
        thickness = random.randint(2,6)
        minimal_pattern = get_circle_defects('minimal', r)
        random_pattern = get_defects(0, 1, random.uniform(0.03,1))
        
        circle = numpy.zeros_like(random_pattern)
        cv2.circle(circle,(r, r), r, 1, thickness)
        result = circle * random_pattern
        
        result = result + minimal_pattern
        
        return result
    
    if pattern == 'right edge':
        thickness = random.randint(2,6)
        density = random.uniform(5/thickness*0.2,1)
        
        minimal_pattern = get_circle_defects('minimal', r)
        random_pattern = get_defects(0.3, 1, density)
        
        circle = numpy.zeros_like(random_pattern)
        # cv2.ellipse(circle, (r, r), (r, r), 0, random.randint(-45,45), random.randint(-45,45), 1, random.randint(1,6))
        cv2.ellipse(circle, (r, r), (r, r), 0, random.randint(-75,-15), random.randint(15,75), 1, thickness)
        result = circle * random_pattern
        
        result = result + minimal_pattern
        
        return result
    
    if pattern == 'left edge':
        thickness = random.randint(2,6)
        density = random.uniform(5/thickness*0.2,1)
        
        minimal_pattern = get_circle_defects('minimal', r)
        random_pattern = get_defects(0.3, 1, density)
        
        circle = numpy.zeros_like(random_pattern)
        cv2.ellipse(circle, (r, r), (r, r), 0, random.randint(105,165), random.randint(195,255), 1, thickness)
        result = circle * random_pattern
        
        result = result + minimal_pattern
        
        return result   
    
    if pattern == 'line':
        thickness = random.randint(2,4)
        density = random.uniform(5/thickness*0.2,1)
        
        minimal_pattern = get_circle_defects('minimal', r)
        random_pattern = get_defects(0.3, 1, density)
        
        circle = numpy.zeros_like(random_pattern)
        # p1 = (random.getrandbits(1)*r*2,random.getrandbits(1)*r*2)
        # p2 = (random.randint(r/2,r+r/2),random.randint(r/2,r+r/2))
        p1,p2 = (random.randint(0,r*2),random.randint(0,r*2)),(random.randint(0,r*2),random.randint(0,r*2))
        cv2.line(circle, p1, p2, 1, random.randint(1,thickness))
        result = circle * random_pattern
        
        result = result + minimal_pattern
        
        return result  
    
    if pattern == 'test':
        return  get_defects(1, 1, 1)

# x = get_circle_defects('left-edge')
# plt.imshow(x, cmap="Oranges", norm=mcolors.TwoSlopeNorm(.03)) 

# fig, ax = plt.subplots()
# ax.imshow(x, cmap="Oranges", norm=mcolors.TwoSlopeNorm(.03)) 
# ax.axis('off')
# st.pyplot(fig, clear_figure=True)

@st.experimental_singleton
def get_model():
    return load_model('wafer_model.h5')
