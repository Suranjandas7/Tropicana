# Samle application writing using Tropicana

import Tropicana as tr
from Tropicana import commons
import csv

class CAPM_model_example:

    def read_file(self):
        with open('final_input.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            sensex = []
            tata_co = []
            for row in reader:
                sensex.append(row[1])
                tata_co.append(row[3])
        return [sensex, tata_co]

    def write_file(self):
        small_s = self.read_file()
        s =''
        l =''
        for d in small_s[0]:
            s = s+str(d) + ", "
        for d in small_s[1]:
            l = l+str(d) + ", "
        s = s[0:len(s) - 2]
        l = l[0:len(l) - 2]
        with open('data.csv', 'wb') as fil:
            fil.write(s)
            fil.write('\n')
            fil.write(l)

    def proc(self):
        module = tr.module('cf', 'reg_cof', 'd')
        beta = module.cf.passthrough_reg_line('')*100
        expected_rate = commons.average_this(module.data_model.series_A, 'MtoA')
        risk_free_rate = 6.964
        print beta, expected_rate, risk_free_rate
        data_model = """beta, {a}
rf_rate, {b}
expected, {c}""".format(a = str(beta), b = str(risk_free_rate), c = str(expected_rate))
        module.update_data(data_model, 'CAPM_classic')
        module.cf.CAPM_classic('full')

c = CAPM_model_example()
c.write_file()
c.proc()
