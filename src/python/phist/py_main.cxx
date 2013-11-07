#define PY_ARRAY_UNIQUE_SYMBOL phist_PyArray_API

//#include <Python.h>
#include <boost/python.hpp>
#include <vigra/numpy_array_converters.hxx>

#include "phist/phist_python.hxx"


#include "py_histogram.hxx"


BOOST_PYTHON_MODULE_INIT(_phist) {
    //using namespace boost::python;
    //using namespace vigra;


    import_array();
    //boost::python::array::set_module_and_type("numpy", "ndarray");

    vigra::import_vigranumpy();



    // image processing related functions and classes 
    cgp2d::export_histogram();


}
