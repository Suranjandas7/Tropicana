# Corporate Finance Module

import math
import commons
import numpy as np

class corporate_finance_module:

    # self.model identifies which model to use
    # self.data is the data provided, ideally in a csv format for all models.

    def __init__(self, model, data_model):
        print 'Running module : Corporate_Finance'
        self.model = model
        self.data_model = data_model

    def net_present_value(self, mode):

        def get_pv_list(mode):
            x=0
            list_pv = []
            for cf in self.data_model.cash_flows:
                pv = round(
                float(cf)/(math.pow((1 + float(self.data_model.discount_rate)),
                int(x))),2)
                list_pv.append(pv)
                if mode == 'full':
                    print "\t {y} \t {cf} \t {pv}".format(y = str(x), cf = str(cf),
                    pv=pv)
                x += 1
            return list_pv

        if mode == "full":
            commons.render_to_main(
                [
                    'NET PRESENT VALUE',
                    """Value of future Cash
Flows discounted with
cost of asset adjusted.""",
                    {
                        'discount_rate':self.data_model.discount_rate,
                        'No of years':self.data_model.no_of_years
                    }
                ]
            )

            print "\t CASH FLOWS PER YEAR : "
            pv_list = []
            x = 0

            print "\t Year \t CF \t PV"

            pv_list = get_pv_list(mode)

            npv = 0.00

            for pv in pv_list:
                npv += pv

            print """


            Net Present Value : {}


            """.format(npv)

        else:

            x = 0
            pv_list = []

            pv_list = get_pv_list(mode)

            npv = 0.00

            for pv in pv_list:
                npv += pv

            print "NPV = {} ".format(npv)
            return npv

    def net_present_value_annuity(self, mode):
        part_a = math.pow(float(1) +
        self.data_model.discount_rate,
        self.data_model.no_of_future_paid)

        part_b = float(1) / part_a
        part_c = float(1) - part_b
        part_d = part_c / self.data_model.discount_rate
        value = self.data_model.periodic_payment * part_d

        if mode == 'full':
            commons.render_to_main(
                [
                    """NET PRESENT VALUE
OF AN ANNUITY""",
                    """Present Value of a fixed
annuity payment.""",
                    {
                        'discount_rate':self.data_model.discount_rate,
                        'No of future years paid':self.data_model.no_of_future_paid,
                        'Periodic Payment':self.data_model.periodic_payment,
                    }
                ]
            )
            print "NPV_A = {}".format(value)
        else:
            print "NPV_A = {}".format(value)
            return value

    def passthrough_pmt(self, mode):

        # numpy function called

        value = np.pmt(self.data_model.interest_rate,
        self.data_model.loan_term, -self.data_model.principle)

        if mode == 'full':
            commons.render_to_main(
                [
                    """FIAT PAYMENT SCHEDULE""",
                    """An annual payment that pays off
the interest and the principle by the end of the loan
term""",
                    {
                        'Princple':self.data_model.principle,
                        'Interest_Rate':self.data_model.interest_rate,
                        'Loan Term':self.data_model.loan_term,
                        'Passthrough Function':'numpy.pmt',
                    }
                ]
            )
            print "\nPMT = {}".format(value)
        else:
            print "\nPMT = {}".format(value)
            return value

    def passthrough_fv(self, mode):

        # numpy function called

        value = np.fv(self.data_model.rate,
        self.data_model.nper, self.data_model.pmt, self.data_model.when)

        if mode == 'full':
            commons.render_to_main(
                [
                    """FUTURE VALUE""",
                    """The Future Value of Money asuming
a rate of interest and regular payments""",
                    {
                        'Princple':-self.data_model.pmt,
                        'Interest_Rate':self.data_model.rate,
                        'Loan Term':self.data_model.nper,
                        'Passthrough Function':'numpy.fv',
                    }
                ]
            )
            print "\nFV = {}".format(value)
        else:
            print "\nFV = {}".format(value)
            return value
