import pandas as pd
import matplotlib.pyplot as plt


class Processor:

    def __init__(self, file_name):
        self.file_name = file_name
        self.weekend = None
        self.col_to_remove = None
        self.col_type = [' data_channel_is_lifestyle', ' data_channel_is_bus',
                         ' data_channel_is_world', ' data_channel_is_tech',
                         ' data_channel_is_socmed',
                         ' data_channel_is_entertainment']
        self.col_data_type = {v: k for k, v in enumerate(self.col_type)}
        self.df = None
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                'saturday', 'sunday']
        self.weekend = {' weekday_is_' + v: k for k, v in enumerate(days)}

    def __col_util(self):
        self.col_to_remove = ["url", " timedelta"]
        self.col_to_remove += self.weekend.keys()
        for v in self.col_to_remove:
            self.df.drop(v, 1, inplace=True)

    def __col_process(self):
        new_week = []
        new_col_data_type = []
        is_popular = []
        for _, row in self.df.iterrows():
            for v in self.weekend.keys():
                if row[v] == 1:
                    new_week.append(self.weekend[v])
                    break
            if row[' shares'] > 1400:
                is_popular.append(1)
            else:
                is_popular.append(0)

        self.df['weekday_type'] = pd.Series(new_week)
        self.df['is_popular'] = pd.Series(is_popular)

    def __reader(self):
        self.df = pd.read_csv(self.file_name)

    def __plot_data(self):
        plt.bar(self.df['weekday_type'], self.df[' shares'])
        plt.savefig('weekday.png')
        plt.show()

    def __get_df(self):
        #print self.df.head(1)
        #print self.df.groupby(['weekday_type'])[' shares'].count()
        return self.df

    def run(self):
        self.__reader()
        self.__col_process()
        #self.__plot_data()
        self.__col_util()
        return self.__get_df()

