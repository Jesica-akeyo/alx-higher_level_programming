#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

	/**
	 * Py_ssize_t size, alloc, idx;

	 * size = PyList_Size(p);
	 * alloc = ((PyListObject *)p)->allocated;
	 * printf("[*] Size of the Python List = %ld\n", size);
	 * printf("[*] Allocated = %ld\n", alloc);
	 * for (idx = 0; idx < size; idx++)
	 * {
		*printf("Element %ld: %s\n",
			*idx,
			*(PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	* }
	*/
