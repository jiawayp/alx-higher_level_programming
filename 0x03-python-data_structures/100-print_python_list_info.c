#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	long int size = PyList_size(p);
	PyListObject *obj = (PListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	prinf("[*} Allocated = %li\n", obj->allocated);

	while (i < size)
	{
		printf("Element %d: %s\n", i, Py_TYPE(obj->obj_item[i])->tp_name);
		++i;
	}
}
