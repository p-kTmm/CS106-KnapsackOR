import os
import shutil

current_path = os.getcwd()

kplib_path = os.path.join(current_path, "kplib")
mytest_path = os.path.join(current_path, "MyTest")

if not os.path.exists(mytest_path):
    os.makedirs(mytest_path)

testgroups = ['n00050', 'n00100', 'n00200', 'n00500', 'n01000']
Rtestgroups = ['R01000', 'R10000']
groupnames = ['00Uncorrelated', '01WeaklyCorrelated', '02StronglyCorrelated', '03InverseStronglyCorrelated',
              '04AlmostStronglyCorrelated', '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated',
              '08SpannerWeaklyCorrelated', '09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated',
              '11ProfitCeiling', '12Circle']
filenames = ['s000.kp']
for groupname in groupnames:
    for testgroup in testgroups:
        for Rtestgroup in Rtestgroups:
            for suffix in filenames:
                filepath = os.path.join(kplib_path, groupname, testgroup, Rtestgroup, suffix)
                if os.path.exists(filepath):
                    newfilepath = os.path.join(mytest_path, f"{groupname}_{testgroup}_{Rtestgroup}_{suffix}")
                    shutil.copy(filepath, newfilepath)
