lista_v0 = ['ano','indice_area_citros','area_citros']

#list_v1 original list - contains all of the available features
lista_v1 = ['ano','area_citros','indice_area_citros','percentual_v123','T_15',
       'Tmin_15', 'Tmax_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100', 'indice_area_citros', 'area_citros', 
       'T_15_d1', 'Trange_15_d1', 'Tabsmin_15_d1', 'Tabsmax_15_d1',
       'Tmin_15_d1', 'Tmax_15_d1', 'T_15_d2', 'Trange_15_d2', 'Tabsmin_15_d2',
       'Tabsmax_15_d2', 'Tmin_15_d2', 'Tmax_15_d2', 'T_15_d3', 'Trange_15_d3',
       'Tabsmin_15_d3', 'Tabsmax_15_d3', 'Tmin_15_d3', 'Tmax_15_d3', 'T_15_d4',
       'Trange_15_d4', 'Tabsmin_15_d4', 'Tabsmax_15_d4', 'Tmin_15_d4',
       'Tmax_15_d4', 'T_15_d5', 'Trange_15_d5', 'Tabsmin_15_d5', 'Tabsmax_15_d5', 'Tmin_15_d5', 'Tmax_15_d5', 'T_15_d6',
       'Trange_15_d6', 'Tabsmin_15_d6', 'Tabsmax_15_d6', 'Tmin_15_d6',
       'Tmax_15_d6', 'T_15_d7', 'Trange_15_d7', 'Tabsmin_15_d7',
       'Tabsmax_15_d7', 'Tmin_15_d7', 'Tmax_15_d7', 'T_15_d8', 'Trange_15_d8',
       'Tabsmin_15_d8', 'Tabsmax_15_d8', 'Tmin_15_d8', 'Tmax_15_d8',
       'prec_15_d1', 'prec_15_d2', 'prec_15_d3', 'prec_15_d4', 'prec_15_d5',
       'prec_15_d6', 'prec_15_d7', 'prec_15_d8', 'balanco_h_cad100_d1', 'balanco_h_cad100_d2',
       'balanco_h_cad100_d3', 'balanco_h_cad100_d4', 'balanco_h_cad100_d5',
       'balanco_h_cad100_d6', 'balanco_h_cad100_d7', 'balanco_h_cad100_d8']

#list_v2 contains only absolute minimum ans maximum temperature values
lista_v2 = ['ano','gravidade_ano_anterior_4_meso','percentual_v123','total_armadilhas',
            'prop_manejos_4_meso','razao_total','area_citros','indice_area_citros',
            'T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100', 
       'T_15_d1', 'Trange_15_d1', 'Tabsmin_15_d1', 'Tabsmax_15_d1',
       'T_15_d2', 'Trange_15_d2', 'Tabsmin_15_d2',
       'Tabsmax_15_d2','T_15_d3', 'Trange_15_d3',
       'Tabsmin_15_d3', 'Tabsmax_15_d3', 'T_15_d4',
       'Trange_15_d4', 'Tabsmin_15_d4', 'Tabsmax_15_d4',
       'T_15_d5', 'Trange_15_d5', 'Tabsmin_15_d5', 'Tabsmax_15_d5','T_15_d6',
       'Trange_15_d6', 'Tabsmin_15_d6', 'Tabsmax_15_d6',
       'T_15_d7', 'Trange_15_d7', 'Tabsmin_15_d7',
       'Tabsmax_15_d7','T_15_d8', 'Trange_15_d8',
       'Tabsmin_15_d8', 'Tabsmax_15_d8',
       'prec_15_d1', 'prec_15_d2', 'prec_15_d3', 'prec_15_d4', 'prec_15_d5',
       'prec_15_d6', 'prec_15_d7', 'prec_15_d8', 'balanco_h_cad100_d1', 'balanco_h_cad100_d2',
       'balanco_h_cad100_d3', 'balanco_h_cad100_d4', 'balanco_h_cad100_d5',
       'balanco_h_cad100_d6', 'balanco_h_cad100_d7', 'balanco_h_cad100_d8']

#list_v3 is equal to list_v2 but without the delayed features
lista_v3 = ['ano','gravidade_ano_anterior_4_meso','percentual_v123','total_armadilhas',
            'prop_manejos_4_meso','razao_total','area_citros','indice_area_citros',
            'T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100']

#list_v4 is super simplified, equals list_v3 but without 'grav_anterior', 'percentual_v123' and 'total_armadilhas'
lista_v4 = ['ano','indice_area_citros','area_citros','razao_total','prop_manejos_4_meso',
            'T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100']

#list_v5 contains only current climate features, without citrus related features
lista_v5 = ['ano','T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100']

#list_v6 contains only climate features, including current and delayed
lista_v6 = ['ano','T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100', 
       'T_15_d1', 'Trange_15_d1', 'Tabsmin_15_d1', 'Tabsmax_15_d1',
       'T_15_d2', 'Trange_15_d2', 'Tabsmin_15_d2',
       'Tabsmax_15_d2','T_15_d3', 'Trange_15_d3',
       'Tabsmin_15_d3', 'Tabsmax_15_d3', 'T_15_d4',
       'Trange_15_d4', 'Tabsmin_15_d4', 'Tabsmax_15_d4',
       'T_15_d5', 'Trange_15_d5', 'Tabsmin_15_d5', 'Tabsmax_15_d5','T_15_d6',
       'Trange_15_d6', 'Tabsmin_15_d6', 'Tabsmax_15_d6',
       'T_15_d7', 'Trange_15_d7', 'Tabsmin_15_d7',
       'Tabsmax_15_d7','T_15_d8', 'Trange_15_d8',
       'Tabsmin_15_d8', 'Tabsmax_15_d8',
       'prec_15_d1', 'prec_15_d2', 'prec_15_d3', 'prec_15_d4', 'prec_15_d5',
       'prec_15_d6', 'prec_15_d7', 'prec_15_d8', 'balanco_h_cad100_d1', 'balanco_h_cad100_d2',
       'balanco_h_cad100_d3', 'balanco_h_cad100_d4', 'balanco_h_cad100_d5',
       'balanco_h_cad100_d6', 'balanco_h_cad100_d7', 'balanco_h_cad100_d8']

#list_v7 is equal to list_v2 but without 'gravidade_ano_anterior_4_meso','percentual_v123','total_armadilhas' and 'prop_manejos_4_meso'
lista_v7 = ['ano','razao_total','area_citros','indice_area_citros',
            'T_15', 'Trange_15', 'Tabsmin_15', 'Tabsmax_15', 'prec_15', 'balanco_h_cad100', 
       'T_15_d1', 'Trange_15_d1', 'Tabsmin_15_d1', 'Tabsmax_15_d1',
       'T_15_d2', 'Trange_15_d2', 'Tabsmin_15_d2',
       'Tabsmax_15_d2','T_15_d3', 'Trange_15_d3',
       'Tabsmin_15_d3', 'Tabsmax_15_d3', 'T_15_d4',
       'Trange_15_d4', 'Tabsmin_15_d4', 'Tabsmax_15_d4',
       'T_15_d5', 'Trange_15_d5', 'Tabsmin_15_d5', 'Tabsmax_15_d5','T_15_d6',
       'Trange_15_d6', 'Tabsmin_15_d6', 'Tabsmax_15_d6',
       'T_15_d7', 'Trange_15_d7', 'Tabsmin_15_d7',
       'Tabsmax_15_d7','T_15_d8', 'Trange_15_d8',
       'Tabsmin_15_d8', 'Tabsmax_15_d8',
       'prec_15_d1', 'prec_15_d2', 'prec_15_d3', 'prec_15_d4', 'prec_15_d5',
       'prec_15_d6', 'prec_15_d7', 'prec_15_d8','balanco_h_cad100_d1', 'balanco_h_cad100_d2',
       'balanco_h_cad100_d3', 'balanco_h_cad100_d4', 'balanco_h_cad100_d5',
       'balanco_h_cad100_d6', 'balanco_h_cad100_d7', 'balanco_h_cad100_d8']

#list_v8 contains the top 30 features according to the feature importance estimated by training the model with list_v7
lista_v8 = ['ano','T_15_d4', 'balanco_h_cad100_d3', 'Tabsmax_15_d7', 'Tabsmax_15_d6', 'Tabsmin_15_d1', 'prec_15_d3', 
            'Trange_15_d1', 'Tabsmax_15_d1', 'T_15_d5', 'Tabsmax_15', 'Tabsmin_15_d4', 'Trange_15', 'Tabsmin_15_d3', 
            'Trange_15_d8', 'Trange_15_d2', 'Tabsmax_15_d8', 'Tabsmin_15_d7', 'T_15_d7', 'Tabsmin_15_d5', 'T_15_d6', 
            'Tabsmin_15_d8', 'Trange_15_d5', 'Trange_15_d3', 'Trange_15_d4', 'T_15_d8', 'Tabsmin_15_d6', 'razao_total', 
            'area_citros', 'indice_area_citros']
