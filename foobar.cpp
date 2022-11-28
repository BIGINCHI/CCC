#include <python3.10/Python.h>
#include <stdlib.h>
#include<string>
#include <boost/algorithm/algorithm.hpp>
#include <iostream>

using namespace boost::algorithm;
using namespace std;

int main()
{   //char x[]="/home/curtainmonkey/Downloads/open3d_gui/vulcantechs-3d/pipes_added_v2.ply";
    //char y[]="/home/curtainmonkey/Downloads/open3d_gui/vulcantechs-3d/pipes.ply";
   // Set PYTHONPATH TO working directory
   setenv("PYTHONPATH",".",1);
   std::string output;
   PyObject *pName, *pModule, *pDict, *pFunc, *pValue, *pValue1, *pValue2, *presult, *presult1, *presult2,*pFunc1, *pFunc2, *pResultstr, *pResultstr1;
    
   std::string x = "/home/curtainmonkey/Downloads/open3d_gui/vulcantechs-3d/pipes.ply";
   std::string y = "/home/curtainmonkey/Downloads/open3d_gui/vulcantechs-3d/pipes_added_v2.ply";
   // Initialize the Python Interpreter
   Py_Initialize();


   // Build the name object
   pName = PyUnicode_FromString((char*)"app");

   // Load the module object
   pModule = PyImport_Import(pName);


   // pDict is a borrowed reference 
   pDict = PyModule_GetDict(pModule);


   // pFunc is also a borrowed reference 
   pFunc = PyDict_GetItemString(pDict, (char*)"someFunction_cloud");

   if (PyCallable_Check(pFunc))
   {
       //pValue=Py_BuildValue("(z)",(char* )"helo");;
       pValue=Py_BuildValue("s",(x.c_str()));
       PyErr_Print();
       printf("FILE ONE UPLOAD :\n");
       //presult=PyObject_CallObject(pFunc,pValue);
       presult=PyObject_CallFunctionObjArgs(pFunc,pValue,NULL);
       PyErr_Print();
       
   } else 
   {
       PyErr_Print();
   }

   //newcode here start
   /////////////////////////////////////////////////////
   pFunc1 = PyDict_GetItemString(pDict, (char*)"someFunction_3d");

   if (PyCallable_Check(pFunc))
   {
       
       pValue1=Py_BuildValue("s",(y.c_str()));

       PyErr_Print();
        std:: string pass = "passed value";

       printf("FILE 2 UPLOAD :\n");
       
       presult1=PyObject_CallFunction(pFunc1,"s",y.c_str());

       pResultstr = PyObject_Repr(presult1);

       std::string returnedString = PyUnicode_AsUTF8(pResultstr);
       //std::cout << returnedString << std::endl;
       output = returnedString;
       //printf("Result is %c\n",PyUnicode_AsUTF8String(pResultstr));
       
       PyErr_Print();
       
   } else 
   {
       PyErr_Print();
   }


    pFunc2 = PyDict_GetItemString(pDict, (char*)"functionC3");

   if (PyCallable_Check(pFunc))
   {
       
       pValue2=Py_BuildValue("s",(x.c_str()));
       
       printf("FUNCTION TEST UPLOAD :\n");
       
       presult2=PyObject_CallFunctionObjArgs(pFunc2,pValue2,NULL);

       pResultstr1 = PyObject_Repr(presult2);

       std::string returnedString1 = PyUnicode_AsUTF8(pResultstr1);
       //std::cout << returnedString1 << std::endl;

              
   } else 
   {
       PyErr_Print();
   }

   /////////////////////////////////////////////////////
   //newcode here end



   //printf("Result is %ld\n",PyLong_AsLong(presult));
   printf("%s\n",output.c_str());
   
   Py_DECREF(pValue);

   // Clean up
   Py_DECREF(pModule);
   Py_DECREF(pName);
   Py_DECREF(presult1);
   Py_DECREF(pResultstr);
   
   // Finish the Python Interpreter
   Py_FinalizeEx();


    return 0;
}