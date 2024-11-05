import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder


class Categorical_encoder:
    def __init__(self,columns_to_onehot:list=['subtype_of_property','postal_code']) -> None:
        self.df = pd.read_csv('data/clean_data_no_outliers.csv')
        self.columns_to_onehot = columns_to_onehot

    def kitchen_type_ordinal_encode(self):
        self.df.equipped_kitchen = self.df.apply(lambda x: x.equipped_kitchen.replace('USA_INSTALLED','INSTALLED'),axis = 1 )
        self.df.equipped_kitchen = self.df.apply(lambda x: x.equipped_kitchen.replace('USA_SEMI_EQUIPPED','SEMI_EQUIPPED'),axis = 1 )
        self.df.equipped_kitchen = self.df.apply(lambda x: x.equipped_kitchen.replace('USA_UNINSTALLED','NOT_INSTALLED'),axis = 1 )
        self.df.equipped_kitchen = self.df.apply(lambda x: x.equipped_kitchen.replace('USA_HYPER_EQUIPPED','HYPER_EQUIPPED'),axis = 1 )
        encoder = OrdinalEncoder(categories=[['NOT_INSTALLED','SEMI_EQUIPPED','UNKNOWN','INSTALLED','HYPER_EQUIPPED']])
        self.df.equipped_kitchen = encoder.fit_transform(self.df.equipped_kitchen.to_numpy().reshape(-1,1),)
    
    def state_of_building_ordinal_encode(self):
        state_of_building_encoder = OrdinalEncoder(categories=[['TO_RESTORE','TO_RENOVATE','TO_BE_DONE_UP','UNKNOWN','JUST_RENOVATED','GOOD','AS_NEW']])
        self.df.state_of_building  = state_of_building_encoder.fit_transform(self.df.state_of_building.to_numpy().reshape(-1,1))    
    
    def custom_combiner(obj,feature,category):
        return str(category)

    def column_one_hot_encode(self,column_name:str):
        arg = self.df[column_name].to_numpy()
        encoder = OneHotEncoder(drop='first',feature_name_combiner=self.custom_combiner,sparse_output=False)
        a = encoder.fit_transform(arg.reshape(-1,1))
        b = encoder.get_feature_names_out()
        new_df = pd.DataFrame(a,columns=b)
        self.df = self.df.reset_index(drop=True)
        new_df = new_df.reset_index(drop=True)
        self.df = self.df.join(new_df)
        self.df.drop([column_name],axis=1,inplace=True)

    def postal_code_preprocessing(self):
        test_df = self.df.groupby('postal_code').postal_code.value_counts()
        sum = 0
        to_small_pc_list=[]
        for i in range(len(test_df)):
            if test_df.iloc[i] < 5:
                sum+=test_df.iloc[i]
                to_small_pc_list.append(test_df.keys()[i])
        for i in to_small_pc_list:
            test_df = self.df[self.df.postal_code == i]
            for row in test_df.property_id:
                index = self.df.property_id == row
                self.df.loc[index,'postal_code'] = 9999
        

    def one_hot_all_columns(self):
        for column in self.columns_to_onehot:
            self.column_one_hot_encode(column)    



    def save_to_csv(self):
        mask = self.df.number_of_rooms == 0
        self.df = self.df[~mask]
        self.df.drop(['Unnamed: 0','facades','property_id','type_of_property','province'],axis=1,inplace=True)
        self.df.to_csv('data/encoded_data.csv')

    def encode_df(self):
        self.kitchen_type_ordinal_encode()
        self.state_of_building_ordinal_encode()
        self.postal_code_preprocessing()
        self.one_hot_all_columns()
        self.save_to_csv()
