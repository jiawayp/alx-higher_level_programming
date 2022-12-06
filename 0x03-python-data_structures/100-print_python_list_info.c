#include "/usr/include/python3.4/Python.h"
#include "usr/include/python3.4/listobject.h"
#include "usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0, list_len = 0;
	PyOject *item;
	PyListObject *clone = (PyListObject *) p;

	list_len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	prinf("[*} Allocated = %d\n", (int) clone->allocated);

	while (i < list_len)
	{
		item = PyList_GET-ITEM(p, i);
		printf("Element %d: %s\n", item->ob_type->tp_name);
		++i;
	}
	return;
}
