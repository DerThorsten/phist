import vigra
import numpy
import phist
import scipy.ndimage
import pylab


img = vigra.readImage('108073.jpg')#[0:100,0:200,0:3]


"""

h0 = phist.histogram(image=img,r=3)
h1 = phist.histogram(image=img,sigma=1.0,r=3)
h2 = phist.histogram(image=img,sigma=[1.0,1.0],r=3)



h0 = h0.reshape([img.shape[0],img.shape[1],-1])
h1 = h1.reshape([img.shape[0],img.shape[1],-1])
h2 = h2.reshape([img.shape[0],img.shape[1],-1])


for x in range(0,h0.shape[2]):

	f = pylab.figure()

	f.add_subplot(2, 2, 1)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(img/255.0,0,1),cmap='jet')

	hImg = h0[:,:,x].copy()
	hImg-=hImg.min()
	hImg/=hImg.max()
	f.add_subplot(2, 2, 2)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(hImg,0,1),cmap='jet')


	hImg2 = h1[:,:,x].copy()
	hImg2-=hImg2.min()
	hImg2/=hImg2.max()
	f.add_subplot(2, 2, 3)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(hImg2,0,1),cmap='jet')


	hImg3 = h2[:,:,x].copy()
	hImg3-=hImg3.min()
	hImg3/=hImg3.max()
	f.add_subplot(2, 2, 4)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(hImg3,0,1),cmap='jet')

	pylab.title('Double image')
	pylab.show()





"""




































imgHist = phist.jointColorHistogram(
	img,
	tuple([0.0  ]*3),
	tuple([255.0]*3),
	tuple([5]*3),
	7
)


sigma = [0.2]*2 + [1.0]*3
smmothed = scipy.ndimage.filters.gaussian_filter(imgHist,sigma=sigma,order=0,mode='constant',cval=0.0)



h0 = imgHist.reshape( [imgHist.shape[0],imgHist.shape[1],-1   ])
h1 = smmothed.reshape( [smmothed.shape[0],smmothed.shape[1],-1   ])


# show the histogram

for x in range(0,h0.shape[2]):

	f = pylab.figure()

	f.add_subplot(1, 3, 1)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(img/255.0,0,1),cmap='jet')

	hImg = h0[:,:,x].copy()
	hImg-=hImg.min()
	hImg/=hImg.max()
	f.add_subplot(1, 3, 2)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(hImg,0,1),cmap='jet')


	hImg2 = h1[:,:,x].copy()
	hImg2-=hImg2.min()
	hImg2/=hImg2.max()
	f.add_subplot(1, 3, 3)  # this line outputs images side-by-side
	pylab.imshow(numpy.swapaxes(hImg2,0,1),cmap='jet')

	pylab.title('Double image')
	pylab.show()