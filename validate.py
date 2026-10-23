"""Supporting verification for the existing Tableau dashboard; no workbook edits."""
from pathlib import Path
import json
import pandas as pd

root = Path(__file__).resolve().parent
df = pd.read_excel(root / 'Coffee_Sales_Dataset.xlsx')
assert len(df) == 3636
assert df.duplicated().sum() == 0
assert df.drop(columns='card').notna().all().all()
assert df.loc[df.cash_type.eq('card'), 'card'].notna().all()
assert df.loc[df.cash_type.eq('cash'), 'card'].isna().all()
assert df.money.gt(0).all()
assert df['date'].dt.normalize().equals(df.datetime.dt.normalize())
assert round(df.money.sum(), 2) == 115431.58
out = root / 'results'
out.mkdir(exist_ok=True)
revenue = df.money.sum()
metrics = {'cups':len(df), 'revenue':round(revenue,2),
 'average_price_per_cup':round(df.money.mean(),2),
 'card_revenue_share_pct':round(df.loc[df.cash_type.eq('card'),'money'].sum()/revenue*100,2),
 'card_cup_share_pct':round(df.cash_type.eq('card').mean()*100,2),
 'start':str(df.date.min().date()), 'end':str(df.date.max().date()),
 'expected_blank_cash_card_ids':int(df.card.isna().sum())}
(out/'kpis.json').write_text(json.dumps(metrics,indent=2)+'\n')
for name, key in [('coffee',df.coffee_name),('payment',df.cash_type),('month',df.datetime.dt.to_period('M')),('hour',df.datetime.dt.hour)]:
 t=df.groupby(key).money.agg(revenue='sum',cups='size')
 t['revenue_share_pct']=t.revenue/revenue*100
 t.round(2).to_csv(out/f'{name}.csv')
h=df.datetime.dt.hour
df['time_slot']=h.map(lambda x:'Morning' if 6<=x<=12 else 'Afternoon' if 12<x<=16 else 'Evening' if 16<x<=18 else 'Night')
t=df.groupby('time_slot').money.agg(revenue='sum',cups='size');t['revenue_share_pct']=t.revenue/revenue*100
t.round(2).to_csv(out/'time_slot.csv')
print(json.dumps(metrics,indent=2));print(t.round(2).to_string())
