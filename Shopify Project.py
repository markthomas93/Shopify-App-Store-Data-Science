import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apps = pd.read_csv('Shopify Project/apps.csv')
categories = pd.read_csv('Shopify Project/categories.csv')
plan_features = pd.read_csv('Shopify Project/plan_features.csv')
pricing_plans = pd.read_csv('Shopify Project/pricing_plans.csv')
reviews = pd.read_csv('Shopify Project/reviews.csv')

# First find out how many apps per category there are 
categories_cnt = categories['category'].value_counts()

# Apps per category percentages
categories_perc = categories_cnt/sum(categories_cnt) * 100

categories_cnt['Total'] = sum(categories_cnt)

# Pie Chart for Categories 
pi = categories_perc.plot.pie()