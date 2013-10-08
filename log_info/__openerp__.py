# -*- coding: utf-8 -*-                                                            
##############################################################################  
#                                                                                  
#    OpenERP, Open Source Management Solution                                      
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).                         
#                                                                                  
#    This program is free software: you can redistribute it and/or modify          
#    it under the terms of the GNU Affero General Public License as                
#    published by the Free Software Foundation, either version 3 of the            
#    License, or (at your option) any later version.                               
#                                                                                  
#    This program is distributed in the hope that it will be useful,               
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 
#    GNU Affero General Public License for more details.                           
#                                                                                  
#    You should have received a copy of the GNU Affero General Public License   
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.         
#                                                                                  
##############################################################################  
{                                                                                  
    'name' : 'Server Log Info',
    'version' : '0.1',                                                             
    'author' : 'Vauxoo',                                                      
    'category' : '',                                                          
    'description' : """                                                            
                                                                                   
    """,                                                                           
    'website': 'http://www.vauxoo.com',                                            
    'images' : [],                                                                 
    'depends' : [
        'web_bootstrap3',
        'web_fontawesome',
    ],                                                                
    'data': [                                                                      
        'view/log_info_view.xml',
        'wizard/log_info_view.xml',
    ],                                                                                 
    'js': [                                                                        
    'static/src/js/log_info.js',
    ],                                                                                 
    'qweb' : [                                                                     
        'static/src/xml/log_info.xml',
    ],                                                                                 
    'css':[                                                                        
        'static/src/css/log_info.css',
    ],                                                                                 
    'demo': [                                                                      
    ],                                                                                 
    'test': [                                                                      
    ],                                                                                                                                                                                                  
    'installable': True,                                                           
    'auto_install': False,                                                         
}                                                                                  
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: 

