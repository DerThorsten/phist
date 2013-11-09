#define PY_ARRAY_UNIQUE_SYMBOL phist_PyArray_API
#define NO_IMPORT_ARRAY

#include <string>
#include <cmath>

#include <boost/python/suite/indexing/vector_indexing_suite.hpp>


#include <boost/array.hpp>



#include <vigra/numpy_array.hxx>
#include <vigra/numpy_array_converters.hxx>

#include "phist/phist.hxx"
#include "phist/phist_python.hxx"


namespace python = boost::python;

namespace phist {




    vigra::NumpyAnyArray labelHistogram(
        vigra::NumpyArray<3, vigra::Multiband<LabelType>  >         img,
        const LabelType                                             nLabels,
        const size_t                                                r,
        //output
        vigra::NumpyArray<4, float >    res = vigra::NumpyArray<4, float >()
    ){ 
        const size_t nChannels=img.shape(2);
        // allocate output
        typedef typename vigra::NumpyArray<4, float >::difference_type Shape4;
        Shape4 shape(img.shape(0),img.shape(1),nChannels,nLabels);
        res.reshapeIfEmpty(shape);
        std::fill(res.begin(),res.end(),0.0);


        // coordinate in the res array (pixel wise histogram)
        // (x,y,c,bin)
        Shape4 histCoord;
        const vigra::TinyVector<float, 2>  radius1(r+1,r+1);
  
        vigra::TinyVector<int,2>  start,end,c;

        for(histCoord[0]=0;histCoord[0]<img.shape(0);++histCoord[0])
        for(histCoord[1]=0;histCoord[1]<img.shape(1);++histCoord[1]){


            for(int d=0;d<2;++d){
                start[d]   = std::max(int(0),            int(histCoord[d]) - int(r));
                end[d]     = std::min(int(img.shape(d)), int(histCoord[d] + (r+1) )); 
            }


            for(c[0]=start[0];c[0]<end[0];++c[0])
            for(c[1]=start[1];c[1]<end[1];++c[1]){

                // iterate over all channels
                for(histCoord[2]=0;histCoord[2]<nChannels;++histCoord[2] ){

                    const LabelType label = img(c[0],c[1],histCoord[2]);

                   
                    histCoord[3] = label;

                    /*
                    std::cout<<"\n\n” channel "<<histCoord[2]<<"\n";
                    std::cout<<"value "<< value<<"\n";
                    std::cout<<"mi " << min(histCoord[2])<<"\n";
                    std::cout<<"ma " << max(histCoord[2])<<"\n";
                    std::cout<<"fa " << fac[histCoord[2]]<<"\n";
                    */

                    PHIST_ASSERT_OP(histCoord[3],<,nLabels);
                    // increment hist
                    res(histCoord[0],histCoord[1],histCoord[2],histCoord[3])+=1.0;
                }
            }
        }

        // normalize

        for(histCoord[0]=0;histCoord[0]<img.shape(0);++histCoord[0])
        for(histCoord[1]=0;histCoord[1]<img.shape(1);++histCoord[1])
        for(histCoord[2]=0;histCoord[2]<img.shape(2);++histCoord[2]){

            float sum=0.0;
            for(histCoord[3]=0;histCoord[3]<nLabels;++histCoord[3]){
                sum+=res(histCoord[0],histCoord[1],histCoord[2],histCoord[3]);
            }
            for(histCoord[3]=0;histCoord[3]<nLabels;++histCoord[3]){
                res(histCoord[0],histCoord[1],histCoord[2],histCoord[3])/=sum;
            }
        }
        return res;
    }



    void export_label_histogram(){



        python::def("_label_histogram_",vigra::registerConverters(&labelHistogram),
            (
                python::arg("img"),
                python::arg("nLabels"),
                python::arg("r"),
                python::arg("out")=python::object()
            )
        );

    }

}