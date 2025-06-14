import splitfolders

splitfolders.ratio(
    "dataset",                     # Input folder with 'images' and 'labels'
    output="dataset_split",        # Output folder
    seed=1337,                     # Fix seed for reproducibility
    ratio=(0.8, 0.2),              # Train : Val split
    group_prefix=None,             # Not grouping by prefix
    move=True                      # Move files instead of copying (faster)
)
