try:
    from salesforce_bulk import SalesforceBulk
    from csv_adapter import CsvDictsAdapter
except ImportError:
    # Python 3
    from .salesforce_bulk import SalesforceBulk
    from .csv_adapter import CsvDictsAdapter

__version__ = '1.1.0'
