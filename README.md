# TROPICANA

A financial calculator and an intro to numpy for begginers.

## Structure

'''
import Tropicana as tr
module = tr.module(module_name, model_name, data_source)

'''

module_name is the name of the module you want to access (right now, there's only cf). model_name is the name of the model in the module, data_source is the source of your data. All params are strings. data_source can be a csv file or a string containing csv data. If you want it to read the default data.csv, data_source should be 'd'.

Once the model object is initialized, you can access the results by

'''
mod.module_name.model_name(view_option)
'''

if view_option is 'full', the display would be nicer. Put any other string to just get the result as a value. For example ->

'''
value = mod.module_name.model_name('')

'''
