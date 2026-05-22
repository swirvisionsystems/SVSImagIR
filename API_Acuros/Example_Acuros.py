from API_Acuros import Acuros
import traceback

try:
    #Connect to the first available camera
    cam = Acuros()
    
    # Configure any settings
    # GIC (GenICam) functions should be the focus before using FPGA_ or TEC_ functions.
    cam.GIC_DnucEnable.setValue(3) # (3) Offset On / Gain On
    texp = cam.GIC_ExposureTime.getValue() # ms
    print(f'Current exposure time is {texp}ms.')

    #Capture 10 images and grab them from the cam object
    num_imgs = 10
    cam.getImages(num_imgs)
    my_ims = cam.Images # np.array format
        
except Exception:
    print(traceback.format_exc())
    
finally:
    if 'cam' in locals():
        cam.release()
