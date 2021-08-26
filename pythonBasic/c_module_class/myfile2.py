# myfile2.py

# from c_module_class.mypackage.exam import mymodule
#
# print('날씨:', mymodule.get_weather())

from mypackage.exam import mymodule
print('날씨:', mymodule.get_weather())

from mypackage.exam.mymodule import *
print('요일:', get_date())


