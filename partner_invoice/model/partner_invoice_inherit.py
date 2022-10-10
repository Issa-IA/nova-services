from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PartnerInvoiceHerit(models.Model):
    _inherit = 'res.partner'

    pfr = fields.Monetary('PFR', default=20)
    code_service = fields.Char('Code service')
    augmentation_sav = fields.Float(string='Augmentation SAV', default=0.05)
    augmentation_sav_bool= fields.Boolean(string="Augmentation SAV", default=True)
    type_facture = fields.Selection([('par_dossier', 'facture par dossier'),('tout_dossiers', 'facturer tout les dossiers')],default='par_dossier' )
    moyen_de_paiement= fields.Selection([('prelevement', 'Prélèvement'),('chorus', 'Chorus'),('autres', 'Autres')],default='prelevement')
    goup_commerc_ok = fields.Char('Type Facture', compute="compute_type_facture")
    goup_commerc_ok_1 = fields.Char('KDFM', compute="compute_type_kdfm")
    
    
    @api.depends('x_studio_kdfm')
    def compute_type_kdfm(self):
        for rec in self:
            rec.goup_commerc_ok_1 = str(rec.x_studio_kdfm)
    @api.depends('type_facture')
    def compute_type_facture(self):
        for rec in self:
            if rec.type_facture == 'par_dossier':
                rec.goup_commerc_ok = "facture par dossier"
            elif rec.type_facture == 'tout_dossiers':
                rec.goup_commerc_ok = "facturer tout les dossiers"
            else:
                rec.goup_commerc_ok = False
    
 
