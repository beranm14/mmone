# mmone

M/M/1 queue theory thoughts in monitoring with integration on statusdroid.

Naive idea is to parse your nginx/apache access logs, presume Poisson distribution (it is very strong assumption) and count basic values from M/M/1 queue thoery.

Example of output:

```
python3 mmone.py  -c config.yml 
Description                                  Value
-------------------------------------------  ---------------------
Mu - intensity of serve per minute:          233.05968175906384
Lambda - insensity of messages per minute:   13.383333333333333
Rho expected occupacy per minute:            0.057424489865943305
System is:                                   stable
Expected count of tasks in the queue:        0.0035100445094311218
Expected count of tasks in system:           0.060934534375374425
Expected time to serve the task:             0.004290746440792775
Expected time to the task to wait in queue:  0.0002622698263584898
Expected time of task in whole system:       0.0045530162671512655
```

### Resources


Math related stuff:
 * http://homen.vsb.cz/~s1i95/MaSvD/SHO_1.pdf


#### Statusdroid example

You can get some stats from api by calling it with page guid. That is stated on status page, e.g.:

```
curl 'https://www.statusdroid.com/api/statistics/response-time/?range_hours=24&user_website_guid=551bf0d2-88aa-430b-a35a-589ecf9409c0&region=europe'
```
