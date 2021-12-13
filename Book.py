import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# returns true if the seat button is clickable
def checkIfAvailable(seatID):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, seatID))
    )
    classContent = element.get_attribute('class').split(" ")
    if "available" in classContent:
        return True
    return False

# returns "safeNumberOfSeats" number of seats to be booked
def getFinalSeats(seatIDs, safeNumberOfSeats):
    final = []
    for seat in seatIDs:
        if checkIfAvailable(seat):
            final.append(seat)
        if len(final) == safeNumberOfSeats:
            break
    return final 

def selectSeat(seatID):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, seatID))
    )
    element.click()

def fillForm(id, data):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id))
    )
    element.send_keys(data) 

def pressButton(path):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    element.click()


def main():
    # Start webdriver
    s=Service(ChromeDriverManager().install())
    global driver
    driver = webdriver.Chrome(service=s)

    seatMap = {'A18': '3834', 'B18': '3835', 'C18': '3836', 'D18': '3837', 'E18': '3838', 'F18': '3839', 'G18': '3840', 'H18': '3841', 'I14': '3842', 'A17': '3843', 'B17': '3844', 'C17': '3845', 'D17': '3846', 'E17': '3847', 'F17': '3848', 'G17': '3849', 'H17': '3850', 'I13': '3851', 'A16': '3852', 'B16': '3853', 'C16': '3854', 'D16': '3855', 'E16': '3856', 'F16': '3857', 'G16': '3858', 'H16': '3859', 'I12': '3860', 'A15': '3861', 'B15': '3862', 'C15': '3863', 'D15': '3864', 'E15': '3865', 'F15': '3866', 'G15': '3867', 'H15': '3868', 'I11': '3869', 'A14': '3870', 'B14': '3871', 'C14': '3872', 'D14': '3873', 'E14': '3874', 'F14': '3875', 'G14': '3876', 'H14': '3877', 'I10': '3878', 'A13': '3879', 'B13': '3880', 'C13': '3881', 'D13': '3882', 'E13': '3883', 'F13': '3884', 'G13': '3885', 'H13': '3886', 'I9': '3887', 'A12': '3888', 'B12': '3889', 'C12': '3890', 'D12': '3891', 'E12': '3892', 'F12': '3893', 'G12': '3894', 'H12': '3895', 'I8': '3896', 'A11': '3897', 'B11': '3898', 'C11': '3899', 'D11': '3900', 'E11': '3901', 'F11': '3902', 'G11': '3903', 'H11': '3904', 'A10': '3906', 'B10': '3907', 'C10': '3908', 'D10': '3909', 'E10': '3910', 'F10': '3911', 'G10': '3912', 'H10': '3913', 'A9': '3915', 'B9': '3916', 'C9': '3917', 'D9': '3918', 'E9': '3919', 'F9': '3920', 'G9': '3921', 'H9': '3922', 'A8': '3924', 'B8': '3925', 'C8': '3926', 'D8': '3927', 'E8': '3928', 'F8': '3929', 'G8': '3930', 'H8': '3931', 'A7': '3933', 'B7': '3934', 'C7': '3935', 'D7': '3936', 'E7': '3937', 'F7': '3938', 'G7': '3939', 'H7': '3940', 'I7': '3941', 'A6': '3942', 'B6': '3943', 'C6': '3944', 'D6': '3945', 'E6': '3946', 'F6': '3947', 'G6': '3948', 'H6': '3949', 'I6': '3950', 'A5': '3951', 'B5': '3952', 'C5': '3953', 'D5': '3954', 'E5': '3955', 'F5': '3956', 'G5': '3957', 'H5': '3958', 'I5': '3959', 'A4': '3960', 'B4': '3961', 'C4': '3962', 'D4': '3963', 'E4': '3964', 'F4': '3965', 'G4': '3966', 'H4': '3967', 'I4': '3968', 'A3': '3969', 'B3': '3970', 'C3': '3971', 'D3': '3972', 'E3': '3973', 'F3': '3974', 'G3': '3975', 'H3': '3976', 'I3': '3977', 'A2': '3978', 'B2': '3979', 'C2': '3980', 'D2': '3981', 'E2': '3982', 'F2': '3983', 'G2': '3984', 'H2': '3985', 'I2': '3986', 'A1': '3987', 'B1': '3988', 'C1': '3989', 'D1': '3990', 'E1': '3991', 'F1': '3992', 'G1': '3993', 'H1': '3994', 'I1': '3995'}
    website = "https://www.cinema.mv/movie/spider-man-no-way-home"
    safeNumberOfSeats = 10 
    delay = 10
    showing = f'//*[@id="container"]/div[2]/div/div[4]/ul/li[{sys.argv[4]}]/a'

    # attempt to get first screening of the movie every "delay" number of seconds
    while True:
        try:
            driver.get(website)
            link = driver.find_element(By.XPATH, showing)
            link.click()
            break
        except NoSuchElementException:
            time.sleep(delay)

    try:
        # Choosing seats
        seatIDs = [seatMap[seat] for seat in sys.argv[5].split(",")] # convert sys.argv[4] = "C6,C9,C12,B9,D9" -> ['3926','3917','3908']

        finalSeats = getFinalSeats(seatIDs, safeNumberOfSeats)

        for id in finalSeats:
            selectSeat(id)

        # Fill booking details        
        fillForm('name', sys.argv[1])
        fillForm('email', sys.argv[2]) 
        fillForm('phone', sys.argv[3])
        
        # Clicking book
        pressButton('//*[@id="scrolled-area"]/div[3]/div/div[4]/a[1]')

        # Confirming book
        pressButton('//*[@id="scrolled-area"]/div[2]/form/div/div[4]/input')

    except:
        driver.quit()

if __name__ == "__main__":
    main()