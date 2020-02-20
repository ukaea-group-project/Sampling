class Parameter:
    '''
    Holds name, acceptable values, (and sampling distribution) for an input parameter.
    '''

    def __init__(self, name, valuerange=[], values=[]):
        self.name = name
        if len(values) == 0:
            self.val = valuerange
            self.discrete = False
        else:
            self.val = values
            self.discrete = True

    def gen_uniform(self, num):
        '''
        Generates appropriate uniform random data (either discrete or cont) for parameter.
        '''

        from numpy.random import randint, uniform

        if self.discrete:
            scope = len(self.val)
            if num == 1:
                return self.val[randint(scope)]
            else:
                return [self.val[randint(scope)] for i in range(num)]

        else:
            return uniform(self.val[0], self.val[1], num)


class Domain:
    def __init__(self):
        '''
        Generates array of input parameters for model in use.
        '''
        FWT = Parameter('firstwall_thickness',
                        valuerange=[0, 20])
        FWAM = Parameter('firstwall_amour_material',
                         values=['tungsten'])
        FWSM = Parameter('firstwall_structural_material',
                         values=['SiC', 'eurofer'])
        FWCM = Parameter('firstwall_coolant_material]',
                         values=['H2O', 'He', 'D2O'])
        BSM = Parameter('blanket_structural_material',
                        values=['SiC', 'eurofer'])
        BBM = Parameter('blanket_breeder_material ',
                        values=['Li4SiO4', 'Li2TiO3'])
        BMM = Parameter('blanket_multiplier_material',
                        values=['Be', 'Be12Ti'])
        BCM = Parameter('blanket_coolant_material',
                        values=['H2O', 'He', 'D2O'])
        BBEF = Parameter(
            'blanket_breeder_li6_enrichment_fraction', valuerange=[0, 1])
        BBPF = Parameter('blanket_breeder_packing_fraction',
                         valuerange=[0, 1])
        BMPF = Parameter('blanket_multiplier_packing_fraction',
                         valuerange=[0, 1])
        BMF = Parameter('blanket_multiplier_fraction',
                        valuerange=[0, 1])
        BBF = Parameter('blanket_breeder_fraction',
                        valuerange=[0, 1])
        BSF = Parameter('blanket_structural_fraction',
                        valuerange=[0, 1])
        # BCF = 1 - BMF - BBF - BSF (blanket_coolant_fraction)

        self.params = [FWT, FWAM, FWSM, FWCM, BSM, BBM,
                       BMM, BCM, BBEF, BBPF, BMPF, BMF, BBF, BSF]
        self.numparams = len(self.params)

    def create_data_frame(self):
        from pandas import DataFrame
        return DataFrame(
            columns=[param.name for param in self.params]
        )
