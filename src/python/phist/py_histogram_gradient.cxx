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
#include <cmath>

namespace python = boost::python;

namespace phist {





    void export_histogram_gradient(){

        /*
        python::def("_label_histogram_",vigra::registerConverters(&labelHistogram),
            (
                python::arg("img"),
                python::arg("sigma"),
                python::arg("r"),
                python::arg("outX")=python::object()
                python::arg("outY")=python::object()
            )
        );
        */
    }

}