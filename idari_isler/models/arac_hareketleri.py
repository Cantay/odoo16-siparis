from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
class AracHareketleri(models.Model):
    _name = 'arac.hareketleri'
    _description = 'Araç Hareketleri Modeli'

    #arac_id = fields.Many2one('arac.tanim', string='Plaka', required=True)
    arac_id = fields.Many2one('arac.tanim', string='Araç', required=True)
    sofor = fields.Many2one('hr.employee', string='Şoför', required=True)
    hareket_tarihi = fields.Date(string='Tarih', default=fields.Date.today)
    cikis_saati = fields.Datetime(string='Çıkış Saati')
    giris_saati = fields.Datetime(string='Giriş Saati')
    cikis_km = fields.Integer(string='Çıkış Km', related="arac_id.km")
    haraket_cikis_km = fields.Integer(string='Haraket Cıkış KM', readonly=True, store=True)
    giris_km = fields.Integer(string='Giriş Km', required=True)
    # Yapılan KM alanı (computed)
    yapilan_km = fields.Integer(string='Yapılan Km', default=0, readonly=True)
   
    durum = fields.Selection(
        string='Hareket Durumu',
        selection=[('deger_1', 'Dışarda'), ('deger_2', 'Geldi')],
        default='deger_1',  # Varsayılan değer
        help="Bu alanda iki seçenekten biri seçilebilir"
    )
    aciklama = fields.Text(string='Açıklama')

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        
        for record in records:
            record.write(
                {'haraket_cikis_km': record.cikis_km,
                 'yapilan_km': record.giris_km - record.cikis_km
                 }
            )
        return records

        
    # @api.onchange('arac_id')
    # def _onchange_arac_id(self):
    #     #Araç seçildiğinde çıkış km'yi aracın mevcut km'siyle güncelle"""
    #     if self.arac_id:
    #         self.cikis_km = self.arac_id.km  # arac.tanim modelindeki km'yi al   
            
    @api.model
    def _get_default_time(self):
        # Şu anki saati alıp 'HH:MM' formatına dönüştürme
        now = datetime.now()
        return now.strftime('%H:%M')

    # @api.onchange('giris_km')
    # def _onchange_km(self):
    #     if self.giris_km and self.cikis_km:
    #         if self.giris_km < self.cikis_km:
    #             self.giris_km = 10  # Giriş kilometresi sıfırlanıyor
    #             raise UserError("Giriş kilometresi, çıkış kilometresinden küçük olamaz. Lütfen doğru bir değer girin!")
    #         else:
    #             self.yapilan_km = self.giris_km - self.cikis_km
                
                       
    # @api.model
    # def write(self, vals):
    #     if 'giris_km' in vals and 'giris_saati' in vals:
    #         if vals['giris_km'] and vals['giris_saati']:
    #             vals['durum'] = 'deger_2'  # 'Geldi' durumuna çekiliyor
    #     return super(AracHareketleri, self).write(vals)

    # @api.depends('giris_km', 'cikis_km')
    # def _compute_yapilan_km(self):
    #     for record in self:
    #         if record.giris_km and record.cikis_km:
    #             record.yapilan_km = record.giris_km - record.cikis_km
    #         else:
    #             record.yapilan_km = 0    
    # @api.depends('giris_km', 'cikis_km')
    # def _compute_yapilan_km(self):
    #     for record in self:
    #         if (record.giris_km and record.cikis_km) and record.giris_km > 0:
    #             record.yapilan_km = record.giris_km - 10
    #         else:
    #             record.yapilan_km = 0    
    
        
 
    
    
            

                
            
