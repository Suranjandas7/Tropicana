# Corporate Finance Module

import math
import commons
import numpy as np
from scipy import stats

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
            value_dict = commons.render_to_main(
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

            value_dict['NPV'] = npv
            return [value, value_dict]

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
            value_dict = commons.render_to_main(
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
            value_dict['NPV_A'] = value
            return [value, value_dict]
        else:
            print "NPV_A = {}".format(value)
            return value

    def passthrough_pmt(self, mode):

        # numpy function called

        value = np.pmt(self.data_model.interest_rate,
        self.data_model.loan_term, -self.data_model.principle)

        if mode == 'full':
            value_dict = commons.render_to_main(
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
            value_dict['PMT'] = value
            return [value, value_dict]
        else:
            print "\nPMT = {}".format(value)
            return value

    def passthrough_fv(self, mode):

        # numpy function called

        value = np.fv(self.data_model.rate,
        self.data_model.nper, self.data_model.pmt, self.data_model.when)

        if mode == 'full':
            value_dict = commons.render_to_main(
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
            value_dict['FV'] = value
            return [value, value_dict]
        else:
            return value

    def gordon_equity_cost(self, mode):

        value = (
        self.data_model.current_dividend * ((
        1 + self.data_model.growth_rate)/self.data_model.current_share_price
        )) + self.data_model.growth_rate

        if mode == 'full':
            value_dict = commons.render_to_main(
                [
                    """Gordon Equity Cost Model""",
                    """The value of a share is the present value
of the future anticipated dividend stream from the share, where
the future anticipated dividends are discounted at the appropriate
risk-adjusted cost of equity.""",
                    {
                        'Current Share Price':self.data_model.current_share_price,
                        'Current Dividend':self.data_model.current_dividend,
                        'Anticipated Growth Rate':self.data_model.growth_rate,
                    }
                ]
            )
            print "\nCost of Equity  = {}".format(value)
            value_dict['Cost of Equity '] = value
            return [value, value_dict]
        else:
            return value

    def passthrough_reg_line(self, mode):
        series_A = self.data_model.series_A
        series_B = self.data_model.series_B

        slope, intercept, r_value, p_value, stderr = stats.linregress(
        series_A, series_B
        )

        if mode == 'full':
            value_dict = commons.render_to_main(
                [
                    """Regression Line""",
                    """Creates a least-squares regression line
for two sets of measurements.""",
                    {
                        'slope':slope,
                        'intercept':intercept,
                        'r-value':r_value,
                        'p-value':p_value,
                        'std_err':stderr,
                        'Passthrough Function':'scipy.stats.linregress'
                    }
                ]
            )
            return [slope, value_dict]
        else:
            return slope

    def CAPM_classic(self, mode):

        value = self.data_model.rf_rate + (
        self.data_model.beta * (
        self.data_model.expected - self.data_model.rf_rate
        ))

        if mode == 'full':
            value_dict = commons.render_to_main(
                [
                    """CAPM Classic""",
                    """Classic CAPM model that ignores taxes.""",
                    {
                        'beta':self.data_model.beta,
                        'risk free rate':self.data_model.rf_rate,
                        'expected market rate':self.data_model.expected,
                    }
                ]
            )
            value_dict['Expected Return'] = value
            print "\nExpected Return = {}".format(value)
            return [value, value_dict]
        else:
            return value

    def CAPM_taxadj(self, mode):
        ta_rate = self.data_model.rf_rate * (1 - self.data_model.tax_rate)
        value = ta_rate + (
        self.data_model.beta * (
        self.data_model.expected - ta_rate
        ))

        if mode == 'full':
            value_dict = commons.render_to_main(
                [
                    """CAPM Tax Adjusted""",
                    """CAPM model that includes taxes
in its calculation.""",
                    {
                        'beta':self.data_model.beta,
                        'risk free rate':self.data_model.rf_rate,
                        'expected market rate':self.data_model.expected,
                        'tax rate':self.data_model.tax_rate,
                    }
                ]
            )
            value_dict['Expected Return'] = value
            return [value, value_dict]
        else:
            return value
