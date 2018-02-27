# mmone

M/M/1 queue theory thoughts in monitoring with integration on statusdroid.

Naive idea is to parse your nginx/apache access logs, presume Poisson distribution (it is very strong assumption) and count basic values from M/M/1 queue thoery:

 * stability



### Resources


Math related stuff:
 * http://homen.vsb.cz/~s1i95/MaSvD/SHO_1.pdf


#### Statusdroid example

You can get some stats from api by calling it with page guid. That is stated on status page, e.g.:

```
curl 'https://www.statusdroid.com/api/statistics/response-time/?range_hours=24&user_website_guid=551bf0d2-88aa-430b-a35a-589ecf9409c0&region=europe'
```
