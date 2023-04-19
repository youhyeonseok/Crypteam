import sys, os,pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname("backend"))))))
data = pd.read_csv("/Users/yuhyeonseog/졸작 연구/git/Crypteam-3/backend/ML/BTC_USDT_1d.csv")