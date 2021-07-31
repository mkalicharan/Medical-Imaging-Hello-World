import pydicom
import matplotlib.pyplot as plt

ds = pydicom.dcmread("SampleDICOM files/1.2.840.113619.2.55.3.2831216128.32632.1118949199.255.1.dcm")
print(ds)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()
