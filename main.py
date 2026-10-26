from numpy import random
import numpy as np
import pandas as pd

random.seed(42)

measurements_nominal_and_tolerance = {
    "x_01": (10, 0.02),
    "x_02": (15, 0.05),
    "x_03": (22.5, 0.03),
    "x_04": (8, 0.02),
    "x_05": (12.5, 0.05),
    "x_06": (30, 0.1),
    "x_07": (6, 0.02),
    "x_08": (18, 0.05),
    "x_09": (25, 0.03),
    "y_01": (14, 0.05),
    "y_02": (9.5, 0.02),
    "z_01": (4, 0.02),
}

extra_range = 0.02

results = []
acceptable = True

for i in measurements_nominal_and_tolerance:
    min_value = measurements_nominal_and_tolerance[i][0] - measurements_nominal_and_tolerance[i][1]
    max_value = measurements_nominal_and_tolerance[i][0] + measurements_nominal_and_tolerance[i][1]
    random_min = min_value - extra_range
    random_max = max_value + extra_range
    measurements = np.random.uniform(random_min, random_max, size=3)
    measurements = np.round(measurements, 2)
    print(f"{i}: {measurements}")
    out_of_tolerance_count = 0
    for j in measurements:
        if j < min_value or j > max_value:
            print(f"WARNING! Measurement {j} for {i} is out of tolerance range ({min_value}, {max_value}).")
            out_of_tolerance_count += 1

    if out_of_tolerance_count < 2:
            print(f"It is acceptable. {out_of_tolerance_count} out-of-tolerance measurements out of {len(measurements)}")
            acceptable = True
    else:
        print(f"WARNING! {out_of_tolerance_count} out-of-tolerance measurements out of {len(measurements)}. This is not acceptable.")
        acceptable = False

    results.append((i, measurements_nominal_and_tolerance[i][0], measurements_nominal_and_tolerance[i][1], measurements, measurements.mean(), measurements.max()-measurements.min(), out_of_tolerance_count, acceptable))

df_results = pd.DataFrame(results, columns=["Parameter", "Nominal", "Tolerance", "Measurements", "Mean", "Range", "Out_of_Tolerance_Count", "Acceptable"])


print("\nSummary of Out-of-Tolerance Measurements:")
print(df_results)
print(df_results["Acceptable"].all())
