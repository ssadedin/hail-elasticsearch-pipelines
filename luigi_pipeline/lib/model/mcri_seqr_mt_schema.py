from lib.model.base_mt_schema import BaseMTSchema, row_annotation


class SeqrGenetaleSchema(BaseMTSchema):

    @row_annotation(name='genetale_all_diseases')
    def genetaleAllDiseases(self):
        return self.mt.info['GT.All.Diseases']

    @row_annotation(name='genetale_all_inheritances')
    def genetaleAllInheritances(self):
        return self.mt.info['GT.All.Inheritances']

    @row_annotation(name='genetale_alt_res_flag')
    def genetaleAltResFlag(self):
        return self.mt.info['GT.Alt.Res.Flag']

    @row_annotation(name='genetale_flag')
    def genetaleFlag(self):
        return self.mt.info['GT.Flag']

    @row_annotation(name='genetale_gene_class_info')
    def genetaleGeneClassInfo(self):
        return self.mt.info['GT.GeneClass.Info']

    @row_annotation(name='genetale_gene_class')
    def genetaleGeneClass(self):
        return self.mt.info['GT.GeneClass']

    @row_annotation(name='genetale_previous')
    def genetalePrevious(self):
        return self.mt.info['GT.Previous']

    @row_annotation(name='genetale_var_class_num')
    def genetaleVarClassNum(self):
        return self.mt.info['GT.VarClass.Num']
