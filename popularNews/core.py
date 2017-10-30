from analytics import Analytics
from processor import Processor


def main():
    file_name = "OnlineNewsPopularity/OnlineNewsPopularity.csv"
    an = Analytics(Processor(file_name).run())
    an.random_forest_classfier()

if __name__ == "__main__":
    main()
