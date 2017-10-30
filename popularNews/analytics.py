from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


class Analytics:

    def __init__(self, df):
        self.df = df

        self.train, self.test = train_test_split(df, test_size=0.3)
        self.shares = self.df[' shares']
        #features = [' shares', 'is_popular']
        self.train.drop(' shares', 1, inplace=True)
        #self.train.to_csv('f.csv', sep='\t')

    def random_forest_classfier(self):
        features = self.train.columns[:-1]
        to_decide = self.train['is_popular']

        clf = RandomForestClassifier(n_jobs=2, random_state=0)
        clf.fit(self.train[features], to_decide)
        print " List of the features and their importance scores {}",\
            list(zip(self.train[features], clf.feature_importances_))

        test_shares = self.test[' shares']
        self.test.drop(' shares', 1, inplace=True)
        predict = clf.predict(self.test[features])
        #print clf.predict_proba(self.test[features])[0:10]
        for k, v in zip(test_shares, predict):
            print k, v






