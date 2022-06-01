import pandas as pd
import statistics 
import csv
df=pd.read_csv("data.csv")
height_list=df ["Height"].tolist()
weight_list=df ["Weight"].tolist()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print("mean,median,mode of the height is,{},{}and{}respectively".format(height_mean,height_median,height_mode))
print("mean,median,mode of the weight is,{},{}and{}respectively".format(weight_mean,weight_median,weight_mode))
height_std_dev=statistics.stdev(height_list)
weight_std_dev=statistics.stdev(weight_list)
height_first_std_dev_start,height_first_std_dev_end=height_mean-height_std_dev,height_mean+height_std_dev
height_second_std_dev_start,height_second_std_dev_end=height_mean-(2*height_std_dev),height_mean+(2*height_std_dev)
height_third_std_dev_start,height_third_std_dev_end=height_mean-(3*height_std_dev),height_mean+(3*height_std_dev)

weight_first_std_dev_start,weight_first_std_dev_end=weight_mean-weight_std_dev,weight_mean+weight_std_dev
weight_second_std_dev_start,weight_second_std_dev_end=weight_mean-(2*weight_std_dev),weight_mean+(2*weight_std_dev)
weight_third_std_dev_start,weight_third_std_dev_end=weight_mean-(3*weight_std_dev),weight_mean+(3*weight_std_dev)

height_listofdatawithin_1_stddev=[result for result in height_list if result>height_first_std_dev_start and result<height_first_std_dev_end]
height_listofdatawithin_2_stddev=[result for result in height_list if result>height_second_std_dev_start and result<height_second_std_dev_end]
height_listofdatawithin_3_stddev=[result for result in height_list if result>height_third_std_dev_start and result<height_third_std_dev_end]

weight_listofdatawithin_1_stddev=[result for result in weight_list if result>weight_first_std_dev_start and result<weight_first_std_dev_end]
weight_listofdatawithin_2_stddev=[result for result in weight_list if result>weight_second_std_dev_start and result<weight_second_std_dev_end]
weight_listofdatawithin_3_stddev=[result for result in weight_list if result>weight_third_std_dev_start and result<weight_third_std_dev_end]

print("{}% of data for height that lies within 1 standerd dev".format(len (height_listofdatawithin_1_stddev)*100.0/len(height_list)))
print("{}% of data for height that lies within 2 standerd dev".format(len (height_listofdatawithin_2_stddev)*100.0/len(height_list)))
print("{}% of data for height that lies within 3 standerd dev".format(len (height_listofdatawithin_3_stddev)*100.0/len(height_list)))

print("{}% of data for weight that lies within 1 standerd dev".format(len (weight_listofdatawithin_1_stddev)*100.0/len(weight_list)))
print("{}% of data for weight that lies within 2 standerd dev".format(len (weight_listofdatawithin_2_stddev)*100.0/len(weight_list)))
print("{}% of data for weight that lies within 3 standerd dev".format(len (weight_listofdatawithin_3_stddev)*100.0/len(weight_list)))