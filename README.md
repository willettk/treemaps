# treemaps

Create treemap images for user distributions in Zooniverse projects. 

## Example for how to make a treemap in R for the Galaxy Zoo 2 users:

* Download counts of raw classifications from SQL table ```gz2_rawclicks```:

```sql
select id, classification_count from users
where classification_count > 0
order by `classification_count`
```

Save output to ```csv/gz2_users.csv```

* If the number of unique users is quite large (which makes visualizing it cumbersome), optionally select a random sub-sample of users with Python:

```python
import asciitable,random

n = 5000    # Number of users to select

gz2users = asciitable.read('csv/gz2_users.csv')
subsampled = random.sample(gz2users,n)
asciitable.write(subsampled,'csv/ss5000.csv')
```

* Generate the treemap diagram using the ```treemap``` package in R and save to a PDF file: 

```R
ss<-read.table('csv/ss5000.csv')
require('treemap')
treemap(ss, index='id', vSize='size', palette='RdBu', lowerbound.cex.labels=1, title='Galaxy Zoo 2 user distribution', fontsize.labels=200, aspRatio=1, algorithm='pivotSize', type='index', border.lwds=1)
quartz.save('~/Dropbox/treemap/gz2_RdBu_5000.pdf',type='pdf')
```

![GZ2 example treemap](https://raw.github.com/willettk/treemaps/master/images/gz2_example.png)
