# coding=utf-8
from django.template import Library

register = Library()


@register.filter
def get_item(value_dict, key):
    '''get data from dictionary base on key'''
    return value_dict.get(key)

@register.filter
def get_rowData(value_dict, row):
    '''get row data of 2D dictionary'''
    rowData =[]
    for field in value_dict.keys():
        rowData.append(value_dict.get(field).get(row))
    return rowData

@register.filter
def get_fieldNbr(value_dict):
    '''get field number of 2D dictionary'''
    return len(value_dict)

@register.filter
def get_rowNbr(value_dict):
    '''get row number of 2D dictionary'''
    for field in value_dict.keys():
        #get row number from first field
        return len(value_dict.get(field))

@register.filter
def get_colData(value_dict):
    '''get row keys of 2D dictionary'''
    for field in value_dict.keys():
        #get row keys from first field
        return value_dict.get(field)
