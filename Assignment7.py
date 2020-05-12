''' Write code using find() and string slicing (see section 6.10) to extract 
the number at the end of the line below. Convert the extracted value to a 
floating point number and print it out.'''

text = "X-DSPAM-Confidence:    0.8475";
dummy = text.find('0')
dummy1=text[dummy:]
dummy2=float(dummy1)
print(dummy2)