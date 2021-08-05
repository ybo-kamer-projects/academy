# -*- coding: utf-8 -*-
# from odoo import http



# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })


from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        return res






class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Contacts = http.request.env['academy.contacts']
        return http.request.render('academy.index', {'contacts': Contacts.search([], orderby=False)
                                                     })

    @http.route('/academy/resultat2', auth='public', website=True)
    def resultat2(self, **kw):

        return http.request.render('academy.resultat2')

    @http.route('/academy/<model("academy.contacts"):contact>/', auth="public", website=True)
    def contact(self, contact):
        return http.request.render('academy.biography', {
            'person': contact
        })




    # Recherche avancée


    @http.route('/academy/rechercheavancee/', auth='public', website=True)
    def rechercheavancee(self, **post):
        name = post.get('name')
        profession = post.get('profession')
        quartier = post.get('quartier')
        ville = post.get('ville')
        region = post.get('region')
        codepostal = post.get('codepostal')
        Contacts = http.request.env['res.partner']

        # search

        domain = [('name', 'ilike', name), ('state_id', 'ilike', region), ('district', 'ilike', quartier),
                  ('function', 'ilike', profession), ('city', 'ilike', ville)]

        customers = request.env['res.partner'].search(domain, order='id asc')
        longueur = len(customers)

        values = {
            'customers': customers,
            'length': longueur,

            'contacts': Contacts.search([]),
            'valeur': name,

        }
        return http.request.render('academy.rechercheavancee', values)




    #  Détails du profil


    @http.route('/academy/resultats/<model("res.partner"):customer>/', type='http', auth='public', website=True,
                sitemap=True)
    def customer(self, customer):
        messages = http.request.env['mail.thread']

        return http.request.render('academy.detailsduprofil', {
            'customer': customer,
            'messages': messages,
        })




    # Avis et commentaires


    @http.route('/academy/evaluationetcommentaire/', auth='public', website=True)
    def evaluationetcommentaire(self, **kw):
        Contacts = http.request.env['academy.contacts']
        return http.request.render('academy.evaluationetcommentaire', {'contacts': Contacts.search([])
                                                                       })



    # Facturation et paiement


    @http.route('/academy/paiement/', auth='public', website=True)
    def paiement(self, **kw):
        Contacts = http.request.env['academy.contacts']
        return http.request.render('academy.paiement', {'contacts': Contacts.search([])
                                                        })

    @http.route('/academy/facturation/', auth='public', website=True)
    def facturation(self, **kw):
        Contacts = http.request.env['academy.contacts']
        return http.request.render('academy.facturation', {'contacts': Contacts.search([])
                                                           })





    # Pages blanches




    @http.route(['/academy/pagesblanches/'], auth='public', website=True,
                type="http")
    def pagesblanches(self, **post):
        name = post.get('namepg')
        domain = [ ('name', 'ilike', name)]
        customers = request.env['res.partner'].search(domain, order='id asc')
        values = {
            'customers': customers,
            'taille': len(customers),
            'recherche': name,
                    }
        return request.render('academy.pagesblanches', values)




    # Page d'accueil


    @http.route(['/academy/pageaccueil/'], type='http', auth="public", website=True)
    def pageaccueil(self, **post):

        return request.render("academy.pageaccueil", {})

   # Résultats

    @http.route(['/academy/resultats/submit', '/academy/resultats/submit/page/<int:page>'], type='http', auth="public", website=True)
    def resultats(self, page=0, **post):
        name = post.get('name')
        category = post.get('name')
        namepg = post.get('namepg')
        place = post.get('place')
        Contacts = http.request.env['res.partner']
        Companies = http.request.env['res.partner'].search([('is_company', '=', 'True')])

        # recherche

        domain = ['|', ('name', 'ilike', name),  ('function', 'ilike', name), ('city', 'ilike', place)]
        domain1 = ['|', ('category_id.name', 'ilike', category), ('city', 'ilike', place)]
        domainpg = [('name', 'ilike', namepg)]

        total_customers = request.env['res.partner'].search(domain)
        total_count = len(total_customers)
        per_page = 12
        pager = request.website.pager(url='/academy/resultats/submit', total=total_count, page=page, step=per_page, scope=3,
                                      url_args=None)
        customers = request.env['res.partner'].search(domain,  order='id asc')
        customerspg = request.env['res.partner'].search(domainpg, limit=per_page, offset=pager['offset'], order='id asc')
        longueur = len(customers)

        values = {
            'customers': customers,
            'customerspg':customerspg,
            'length': longueur,
            'contacts': Contacts.search([]),
            'valeur': name,
            'companies': Companies.search([]),
            'pager': pager,
            

        }
        return http.request.render('academy.resultat', values)

    @http.route(['/academy/pagesblanches/submit'], type='http', auth="public", website=True)
    def resultatspg(self, page=0, **post):

        namepg = post.get('namepg')


        # recherche

        domainpg = [('name', 'ilike', namepg)]


        customerspg = request.env['res.partner'].search(domainpg, order='id asc')

        values = {
            'customerspg': customerspg,
            'valeur': namepg,
        }
        return http.request.render('academy.resultatpg', values)

    #Inscription


    @http.route(['/academy/inscription/form'], type='http', auth="public", website=True)
    # mention a url for redirection.
    # define the type of controller which in this case is ‘http’.
    # mention the authentication to be either public or user.
    def partner_form(self, **post):
        # create method
        # this will load the form webpage
        return request.render("academy.tmp_customer_form", {})

    @http.route(['/academy/inscription/form/submit'], type='http', auth="public", website=True)
    # next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        confirm_pass = post.get('pass')
        password = post.get('password')
        if confirm_pass == password:
            partner = request.env['res.users'].create({
                'name': post.get('name'),
                'login': post.get('email'),
                'phone': post.get('phone'),
                'password': post.get('password'),
            })
            vals = {
                'partner': partner,
            }
        # inherited the model to pass the values to the model from the form#
        return request.render("academy.tmp_customer_form_success", vals)
        # finally send a request to render the thank you page#


"""@http.route(['/academy/resultats', '/academy/resultats/page/<int:page>'], auth='public', website=True, type="http")
    def resultat(self, page=0, search=''):
        Contacts = http.request.env['res.partner']


         # search

        domain = []

        if search:
            domain = [('name', 'ilike', search)]



        total_customers = request.env['res.partner'].search(domain)

        total_count = len(total_customers)
        per_page = 12
        pager = request.website.pager(url='/academy/resultats', total=total_count, page=page, step=per_page, scope=3, url_args=None)
        customers = request.env['res.partner'].search(domain, limit=per_page, offset=pager['offset'], order='id asc')

        values = {
            'customers': customers,
            'pager': pager,
            'contacts': Contacts.search([]),
            'valeur': search,

        }


        return request.render('academy.resultat', values) """

"""@http.route(['/academy/pageaccueil/', '/academy/pageaccueil/page1/<int:page>'], auth='public', website=True,
            type="http")


def pageaccueil(self, **post):
    name = post.get('name')
    profession = post.get('category')
    Contacts = http.request.env['res.partner']

    # search

    domain = [('name', 'ilike', name), ('function', 'ilike', profession)]

    customers = request.env['res.partner'].search(domain, order='id asc')
    longueur = len(customers)

    values = {
        'customers': customers,
        'length': longueur,
        'contacts': Contacts.search([]),
        'valeur': name,

    }
    return http.request.render('academy.pageaccueil', values)"""
