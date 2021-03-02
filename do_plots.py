from plot import *
from hashlib import sha256

urllib.request.urlretrieve("http://kylemills.ca/climbing/dump.php?u=kmills&report_id=1&y=6", '/tmp/out.txt')
hasher = sha256()

"""Hash the newly downloaded file and compare to last run's hash on disk"""
"""Only plot if data changed on server"""
plot=False
with open("/tmp/out.txt", 'rb') as f:
   buf = f.read()
   hasher.update(buf)
try:
   with open("/tmp/kylemillsnetclimbinghash.txt", "r") as f:
      refhash = f.readlines()
  
   if hasher.hexdigest()==refhash[0]:
      print("Hash matches. No new plotting required")
   else:
      print(f"Hash on disk: {refhash[0]}")
      print(f"New hash: {hasher.hexdigest()}")
      raise
except Exception as E:
      print(E)

      print("Hash does not match. Saving has to file and plotting...")
      with open("/tmp/kylemillsnetclimbinghash.txt","w") as f:
         f.write(hasher.hexdigest())
      plot=True

if plot:

   df = pd.read_csv("/tmp/out.txt")
   df['date']= pd.to_datetime(df['date']) 
    
   success_ratio(df).savefig('1.png', transparent=True)
   plot_cum_frac(df, attempt=0).savefig('2.png', transparent=True)
   plot_cum_frac(df, attempt=1).savefig('3.png', transparent=True)
   climbing_score(df).savefig('4.png', transparent=True)
   
   
   urllib.request.urlretrieve("http://kylemills.ca/climbing/dump.php?u=kmills", '/tmp/out.txt')
   df = pd.read_csv("/tmp/out.txt")
   df['date']= pd.to_datetime(df['date']) 
   
   scatterplotclimbs(df, attempt=1).savefig('5.png', transparent=True)
   scatterplotclimbs(df, attempt=0).savefig('6.png', transparent=True)
   climbing_trends(df).savefig('7.png', transparent=True)



