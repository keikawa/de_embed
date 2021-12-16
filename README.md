# de_embed
 Python scripts for S-parameter deembedding
 
## Notice

scikit-rf has implemented a de-embedding class, and it is recommended to use it now.
https://scikit-rf.readthedocs.io/en/latest/tutorials/Deembedding.html
 
## Requirement

- Python3
- scikit-rf 0.16.0

## Directory
.

├── main.py

├── deemb.py (Python module of various de-embedding methods)

├── output  (De-embedded touchstones are saved here)

├── dummy	(Measured touchstones of dummies)

└── raw		(Measured touchstones of DUT)

## Usage

1. Save the measured touchstones of the DUTs at the "raw" directory
2. Save the measured touchstones of the dummies, such as open or short, at the "dummy" directory
3. Set a de-embedding method in main.py, line 23, for example `method = 'open'`
4. Run main.py

## Supported methods and these required dummy

- Open (Open only)
- Short (Short only)
- Open_short (Open and short)
- Short_open (Short and open)
- Split-I (Thru only)
- Split-Pi (Thru only)
- Split-T (Thru only)
- ICS-Y (Thru only) : also known as Mangan's method
- ICS-Z (Thru only)
- ICS-YZ (Thru only)
- ICS-ZY (Thru only)

!! Note that ICS (Imittance Cancellation by Swapping) methods are available for only symmetric (i.e. S11=S22 and S12=S21) DUTs

## Contribution

We look forward to your pull request!  
Should you have any questions about fixes or improvements, please feel free to open an issue.

## Author

Keisuke Kawahara

## Licence

GPL-3.0 License
