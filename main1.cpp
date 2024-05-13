#include <iostream>
#include <Python.h>
int test01()
{
	// 1、初始化python接口
	Py_Initialize();
	if (!Py_IsInitialized())
	{
		std::cout << "python init failed" << std::endl;
		return 1;
	}

	// 2、初始化python系统文件路径，保证可以访问到 .py文件
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('/home/book/work/cpp_python/script')");

	// 3、调用python文件名，不用写后缀
	PyObject *module = PyImport_ImportModule("test1");
	if (module == nullptr)
	{
		std::cout << "module not found: test1" << std::endl;
		return 1;
	}

	// 4、获取函数对象
	PyObject *func = PyObject_GetAttrString(module, "say");
	if (!func || !PyCallable_Check(func))
	{
		std::cout << "function not found: say" << std::endl;
		return 1;
	}

	// 5、调用函数
	PyObject_CallObject(func, nullptr);

	// 6、结束python接口初始化
	Py_Finalize();
	return 0;
}

int test02()
{
	// 1、初始化python接口
	Py_Initialize();
	if (!Py_IsInitialized())
	{
		std::cout << "python init failed" << std::endl;
		return 1;
	}

	// 2、初始化python系统文件路径，保证可以访问到 .py文件
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./../script')");

	// 3、调用python文件名，不用写后缀
	PyObject *module = PyImport_ImportModule("test2");
	if (module == nullptr)
	{
		std::cout << "module not found: test2" << std::endl;
		return 1;
	}

	// 4、调用函数
	PyObject *func = PyObject_GetAttrString(module, "add");
	if (!func || !PyCallable_Check(func))
	{
		std::cout << "function not found: add" << std::endl;
		return 1;
	}

	// 5、给 python 传递参数
	// 函数调用的参数传递均是以元组的形式打包的, 2表示参数个数
	// 如果函数中只有一个参数时，写1就可以了
	PyObject *args = PyTuple_New(2);

	// 0：第一个参数，传入 int 类型的值 1
	PyTuple_SetItem(args, 0, Py_BuildValue("i", 1));
	// 1：第二个参数，传入 int 类型的值 2
	PyTuple_SetItem(args, 1, Py_BuildValue("i", 2));

	// 6、使用C++的python接口调用该函数
	PyObject *ret = PyObject_CallObject(func, args);

	// 7、接收python计算好的返回值
	int result;
	// i表示转换成int型变量。
	// 在这里，最需要注意的是：PyArg_Parse的最后一个参数，必须加上“&”符号
	PyArg_Parse(ret, "i", &result);
	std::cout << "return is " << result << std::endl;

	// 8、结束python接口初始化
	Py_Finalize();
	return 0;
}

int test03()
{
	// 1、初始化python接口
	Py_Initialize();
	if (!Py_IsInitialized())
	{
		std::cout << "python init failed" << std::endl;
		return 1;
	}

	// 2、初始化python系统文件路径，保证可以访问到 .py文件
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./../script')");

	// 3、调用python文件名，不用写后缀
	PyObject *module = PyImport_ImportModule("test3");
	if (module == nullptr)
	{
		std::cout << "module not found: test3" << std::endl;
		return 1;
	}
	// 4、获取类
	PyObject *cls = PyObject_GetAttrString(module, "Person");
	if (!cls)
	{
		std::cout << "class not found: Person" << std::endl;
		return 1;
	}

	// 5、给类构造函数传递参数
	// 函数调用的参数传递均是以元组的形式打包的, 2表示参数个数
	// 如果函数中只有一个参数时，写1就可以了
	PyObject *args = PyTuple_New(2);

	// 0：第一个参数，传入 int 类型的值 1
	PyTuple_SetItem(args, 0, Py_BuildValue("s", "jack"));
	// 1：第二个参数，传入 int 类型的值 2
	PyTuple_SetItem(args, 1, Py_BuildValue("i", 18));

	// 6、根据类名实例化对象
	PyObject *obj = PyEval_CallObject(cls, args);

	// 7、根据对象得到成员函数
	PyObject *func = PyObject_GetAttrString(obj, "foo");
	if (!func || !PyCallable_Check(func))
	{
		std::cout << "function not found: foo" << std::endl;
		return 1;
	}

	// 8、使用C++的python接口调用该函数
	PyObject_CallObject(func, nullptr);

	// 9、结束python接口初始化
	Py_Finalize();
	return 0;
}

int main()
{
	return test01();
	return test02();
	return test03();
}