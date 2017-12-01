import cf
import models
import csv
from StringIO import StringIO
import commons

class module:
    def __init__(self, module_name, model_name, data_src):
        self.module_name = module_name
        self.model_name = model_name
        self.data_src = data_src

        self.read_data_status = self.update_data(self.data_src, self.model_name)

        try:
            if self.read_data_status[1] is True:
                print 'MSG : DATA.CSV READ'
                self.data_model = self.get_data_model(self.read_data_status[0])
                print 'MSG : DATA MODEL ACTUALIZED'
                print '=============================='

                if self.module_name == 'cf':
                    self.cf = cf.corporate_finance_module(
                    self.model_name, self.data_model)
                    print 'MSG: Accesing corporate_finace_module with model {}'.format(
                    self.model_name)
        except TypeError:
            print 'MSG : Something went wrong.'

    def read_data_source(self, data_src):
        if data_src == 'd':
            print 'MSG : USING DEFAULT DATA.CSV FILE.'
            with open('data.csv', 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter = ',')
                s =[]
                for row in reader:
                    s.append(row)
            return [s, True]
        else:
            f = StringIO(self.data_src)
            reader = csv.reader(f, delimiter=',')
            s = []
            for row in reader:
                s.append(row)
            return [s, True]

#REGISTER MODELS HERE
#MAKE THIS MORE ABSTRACT

    def get_data_model(self, data):
        try:
            if self.model_name == 'npv':
                data_model = models.net_present_value_model(data)
            if self.model_name == 'npva':
                data_model = models.net_present_value_annuity_model(data)
            if self.model_name == 'pmt':
                data_model = models.fiat_payment_schedule_model(data)
            if self.model_name == 'fv':
                data_model = models.future_value_model(data)
            if self.model_name == 'gordon_equity_cost':
                data_model = models.gordon_model_cost_equity_model(data)
            return data_model
        except UnboundLocalError:
            print 'MSG : {} Model not found.'.format(self.model_name)
            return False

#REGISTER MODULES HERE
#MAKE THIS MORE ABSTRACT

    def update_data(self, data_src, model_name):
        self.model_name = model_name
        ans = self.read_data_source(data_src)
        if self.module_name == 'cf':
            if ans[1] == True:
                self.data_model = self.get_data_model(ans[0])
                if self.data_model == False:
                    return
                self.cf = cf.corporate_finance_module(
                self.model_name, self.data_model)
            else:
                return null
        return ans
