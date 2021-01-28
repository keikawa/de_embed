# de_embed
 Python scripts for on-wafer de-embedding
 
## Requirement

- Python3
- scikit-rf 0.16.0

## Directory
.

├── main.py

├── deemb.py(Python module of various de-embedding methods)

├── output  (De-embedded touchstones are saved here)

├── dummy	(Measured touchstones of dummies)

└── raw		(Measured touchstones of DUT)

## Usage

1. Save the measured touchstones of the DUTs at the "raw" directory
2. Save the measured touchstones of the dummies, such as open or short, at the "dummy" directory
3. Set a de-embedding method in main.py, line 23, for example `method = 'open'`
4. Run main.py

## Contribution

We look forward to your pull request!  
Should you have any questions about fixes or improvements, please feel free to open an issue.

## Author

Keisuke Kawahara

## Licence

GPL-3.0 License