#dates = ['2012-02-10', '2012-02-11', '2012-02-13', '2012-02-14', '2012-02-15', '2012-02-16', '2012-02-17','2012-02-18', '2012-02-19', '2012-02-20', '2012-02-21',  '2012-02-22']
dates = ['2011-12-06', '2011-12-07', '2011-12-08', '2011-12-09', '2011-12-10', '2011-12-11', '2011-12-12', '2011-12-13', '2011-12-14', '2011-12-15', '2011-12-16', '2011-12-17', '2011-12-18', '2011-12-19', '2011-12-20', '2011-12-21', '2011-12-22', '2011-12-23', '2011-12-24', '2011-12-25', '2011-12-26', '2011-12-27', '2011-12-28', '2011-12-29', '2011-12-30', '2011-12-31', '2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04', '2012-01-05', '2012-01-06', '2012-01-07', '2012-01-08', '2012-01-09', '2012-01-10', '2012-01-11', '2012-01-12', '2012-01-13', '2012-01-14', '2012-01-15', '2012-01-16', '2012-01-17', '2012-01-18', '2012-01-19', '2012-01-20', '2012-01-21', '2012-01-22', '2012-01-23', '2012-01-24', '2012-01-25', '2012-01-26', '2012-01-27', '2012-01-28', '2012-01-29', '2012-01-30', '2012-01-31', '2012-02-01', '2012-02-02', '2012-02-03', '2012-02-04', '2012-02-05', '2012-02-06', '2012-02-07', '2012-02-08', '2012-02-09', '2012-02-10', '2012-02-11', '2012-02-12', '2012-02-13', '2012-02-14', '2012-02-15', '2012-02-16', '2012-02-17', '2012-02-18', '2012-02-19', '2012-02-20', '2012-02-21', '2012-02-22', '2012-02-23', '2012-02-24', '2012-02-25', '2012-02-26', '2012-02-27', '2012-02-28']

import pickle
import numpy as np
from radiono import rm
from radiono import utils as ut

lat, lon = '30d43m17.5ss', '21d25m41.9se'
IM = rm.IonoMap(lat,lon,dates)
ras,decs = ut.nsideToRaDec(16)

print 'Calculating...'
IM.calc_radec_RM(ras,decs)

print 'Saving to dict structure'
datadict = {}
datadict['lat'] = lat
datadict['lon'] = lon 
datadict['lsts'] = IM.lst

for dayindex,day in enumerate(dates):
    datadict[day] = {}
    for ut in range(24): datadict[day][ut] = IM.RMs[dayindex,ut,:] 
outname = 'radec_maps_%s_to_%s.pkl'%(dates[0],dates[-1])

#pickle it up
output = open(outname,'wb')
pickle.dump(datadict,output)
output.close()
