from _phist import *
import numpy
import vigra






"""
def gaussianSmoothing1d(histograms,sigma):
  nHist = histograms.shape[0]
  nBins = histograms.shape[1]

  kernel=vigra.filters.Kernel1D()
  kernel.initDiscreteGaussian(sigma)

  smoothedHistograms=vigra.filters.convolveOneDimension(histograms, dim=1, kernel=kernel)

  return smoothedHistograms
"""
from scipy.ndimage.filters import  gaussian_filter as GaussainFilter


def histogram(image,dmin=None,dmax=None,bins=32,r=3,sigma=None,out=None):


    img       = numpy.require(image,dtype=numpy.float32)
    nChannels = img.shape[2]
    flat      = img.reshape([-1,nChannels])

    if dmin is None :
        dmin = numpy.require(numpy.min(flat,axis=0),dtype=numpy.float32)
    if dmax is None :
        dmax = numpy.require(numpy.max(flat,axis=0),dtype=numpy.float32)

    
    # computet the actual histogram
    rawHist  = _phist._batchHistogram_( img=img,dmin=dmin,dmax=dmax,bins=bins,r=r,out=out)



    if sigma is None :
        return rawHist

    else : 
        if isinstance(sigma,(float,int,long)):
            sigmas = [sigma]
        else :
            sigmas = sigma
        assert len(sigmas)<=2 


        if len(sigmas)==1 :
            # only smooth bins
            for c in range(nChannels):
                cHist = rawHist[:,:,c,:]
                kernel=vigra.filters.Kernel1D()
                kernel.initDiscreteGaussian(float(sigmas[0]))
                #kernel.setBorderTreatment()
                smoothedHistograms=vigra.filters.convolveOneDimension(cHist, dim=2, kernel=kernel)
                rawHist[:,:,c,:] = smoothedHistograms[:,:,:]
            return rawHist
        if len(sigmas)==2 :
            # smooth bins ans spatial
            for c in range(nChannels):
                cHist = rawHist[:,:,c,:]
                
                s = [sigmas[1]]*2 + [sigmas[0]]

                smoothedHistograms = GaussainFilter(cHist,sigma=s,order=0)#,mode='constant',cval=0.0)
                rawHist[:,:,c,:] = smoothedHistograms[:,:,:]
            return rawHist

    print rawHist.shape