class dict_helper:
    '''distionary helper to other data form '''

    #this decorator make posible to call method w/o instantiate class
    @classmethod
    #use cls instead of self
    def get_fields(cls, dictData):
        '''get fields of 2D dictionary, return list'''
        fields =[]
        for field in dictData.keys():
            fields.append(field)        
        return fields

    #this decorator make posible to call method w/o instantiate class
    @classmethod
    #use cls instead of self
    def to_list(cls, dictData): 
        '''get row data of 2D dictionary'''
        dataList=[]
        rowData =[]
        for field in dictData.keys():
            for row in dictData.get(field):
                rowData.append(dictData.get(field).get(row))
            
            #use copy for avoid resetting data
            dataList.append(rowData.copy())
            
            #reset/clear data, after saving
            rowData.clear()
        return dataList

    #this decorator make posible to call method w/o instantiate class
    @classmethod
    #use cls instead of self
    def get_row_data(cls, dictData, row):
        '''get row data of 2D dictionary, return list'''
        rowData =[]
        for field in dictData.keys():
            rowData.append(dictData.get(field).get(row))
        return rowData

    #this decorator make posible to call method w/o instantiate class
    @classmethod
    #use cls instead of self
    def to_pair_dict(cls,dictData):
        listPair=[]
        rowDict ={}
        dataList = cls.to_list(dictData)
        fields = cls.get_fields(dictData)
        rows = len(dataList[len(fields)-1])
        for row in range(rows):
            for fld in range(len(fields)):
                rowDict[fields[fld]]=dataList[fld][row]
            listPair.append(rowDict.copy())        
        return listPair
