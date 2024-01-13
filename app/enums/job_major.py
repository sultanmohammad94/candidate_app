from enum import Enum

class JobMajor(str, Enum):
    """This class represents the job Majors."""
    
    COMPUTER_SCIENCE = "Computer Science"
    COMPUTER_INFORMATION_SYSTEMS = "Computer Information Systems"
    IT = "IT"
    SOFTWARE_DEVELOPMENT = "Software Development"
    ACCOUNTING = "Accounting"
    BUSINESS_ADMINISTRATION = "Business Administration"
    MANAGERIAL = "Managerial"