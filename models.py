#DATA_MODELS

class net_present_value_model:
    def __init__(self, data):
        self.name = "Net_Present_Value_Data_Model"
        self.module = 'Corporate_Finance'
        self.discount_rate = float(data[0][1])
        self.no_of_years = float(data[1][1])
        self.cash_flows = []
        for x in xrange(0, int(self.no_of_years)+1):
            self.cash_flows.append(data[2][x])

class net_present_value_annuity_model:
    def __init__(self, data):
        self.name = "Net_Present_Value_Annuity_Data_Model"
        self.module = 'Corporate_Finance'
        self.periodic_payment = float(data[0][1])
        self.no_of_future_paid = float(data[1][1])
        self.discount_rate = float(data[2][1])

#IRR_model

class fiat_payment_schedule_model:
    def __init__(self, data):
        self.module = 'Corporate_Finance'
        self.name = "Fiat_Payment_Data_Model"
        self.principle = float(data[0][1])
        self.interest_rate = float(data[1][1])
        self.loan_term = float(data[2][1])

class future_value_model:
    def __init__(self, data):
        self.module = 'Corporate_Finance'
        self.name = "Future_Value_Data_Model"
        self.rate = float(data[0][1])
        self.nper = float(data[1][1])
        self.pmt = float(data[2][1])
        self.when = float(data[3][1])

class gordon_model_cost_equity_model:
    def __init__(self, data):
        self.module = 'Corporate_Finance'
        self. name = "Gordon_Model_Cost_Equity_Model"
        self.current_share_price = float(data[0][1])
        self.current_dividend = float(data[1][1])
        self.growth_rate = float(data[2][1])

# class TwoStageGordon_model:
#     def __init__(self, data):
#         self.module = 'Corporate_Finance'
#         self.name = "TwoStageGordon_model"
#         self.Po = float(data[0][1])
#         self.Divo = float(data[1][1])
#         self.high_growth = float(data[2][1])
#         self.h_years = float(data[3][1])
#         self.n_growth = float(data[4][1])

class regression_line_model:
    def __init__(self, data):
        self.name = "Regression_Cof_Model"
        self.series_A = []
        self.series_B = []
        try:
            for d in data[0]:
                self.series_A.append(float(d))
        except IndexError:
            pass
        try:
            for d in data[1]:
                self.series_B.append(float(d))
        except IndexError:
            pass

class CAPM_classic_model:
    def __init__(self, data):
        self.name = "CAPM_Classic_Model"
        self.beta = float(data[0][1])
        self.rf_rate = float(data[1][1])
        self.expected = float(data[2][1])
