from ortools.algorithms.python import knapsack_solver
import os
import csv
import time
from itertools import islice

current_path = os.getcwd()
csv_file_path = os.path.join(current_path, 'result.csv')
testgroups = ['n00050', 'n00100', 'n00200', 'n00500', 'n01000']
Rtestgroups = ['R01000', 'R10000']
groupnames = ['00Uncorrelated', '01WeaklyCorrelated', '02StronglyCorrelated', '03InverseStronglyCorrelated',
              '04AlmostStronglyCorrelated', '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated',
              '08SpannerWeaklyCorrelated', '09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated',
              '11ProfitCeiling', '12Circle']
filenames = ['s000.kp']

with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Group Name', 'Size', 'Range', 'Filename', 'Total Value', 'Total Weight', 'Time', 'isOptimal'])

    for groupname in groupnames:
        for testgroup in testgroups:
            for Rtestgroup in Rtestgroups:
                for filename in filenames:
                    filepath = os.path.join(current_path, "MyTest", f"{groupname}_{testgroup}_{Rtestgroup}_{filename}")
                    if not os.path.exists(filepath):
                        continue
                    capacities = []
                    values = []
                    weights = [[]]
                    with open(filepath, 'r') as f:
                        lines = f.read().splitlines()

                    capacities.append(int(lines[2]))
                    for line in islice(lines, 4, None):
                        data = line.split()
                        values.append(int(data[0]))
                        weights[0].append(int(data[1]))

                    solver = knapsack_solver.KnapsackSolver(
                        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
                        "KnapsackExample",
                    )
                    time_limit = 200
                    solver.init(values, weights, capacities)
                    solver.set_time_limit(time_limit)
                    start = time.perf_counter()
                    computed_value = solver.solve()
                    end = time.perf_counter()
                    elapsed_time = end - start

                    packed_weights = [weights[0][i] for i in range(len(values)) if solver.best_solution_contains(i)]
                    total_weight = sum(packed_weights)
                    isOptimal = "Yes" if solver.is_solution_optimal() else "No"

                    writer.writerow([groupname, testgroup, Rtestgroup, filename, computed_value, total_weight, elapsed_time, isOptimal])

                    print(f'Group: {groupname} | Size: {testgroup} | Range: {Rtestgroup} | File: {filename} completed. Time: {elapsed_time:.8f} seconds, Is Optimal: {isOptimal}')

