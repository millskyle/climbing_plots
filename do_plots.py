from plot import *

urllib.request.urlretrieve("http://kylemills.ca/climbing/dump.php?u=kmills&report_id=1&y=6", '/tmp/out.txt')
df = pd.read_csv("/tmp/out.txt")
df['date']= pd.to_datetime(df['date']) 
 
success_ratio(df).savefig('1.png')
plot_cum_frac(df, attempt=0).savefig('2.png')
plot_cum_frac(df, attempt=1).savefig('3.png')
climbing_score(df).savefig('4.png')


urllib.request.urlretrieve("http://kylemills.ca/climbing/dump.php?u=kmills", '/tmp/out.txt')
df = pd.read_csv("/tmp/out.txt")
df['date']= pd.to_datetime(df['date']) 

scatterplotclimbs(df, attempt=1).savefig('5.png')
scatterplotclimbs(df, attempt=0).savefig('6.png')
climbing_trends(df).savefig('7.png')
