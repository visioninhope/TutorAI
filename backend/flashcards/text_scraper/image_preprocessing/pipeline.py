
import image_filter as imF
import cv2



class PipelineFactory:
    def __init__(self, image):
        self.image = image
    
    def create_pipeline(self, pipeline_type):
        match pipeline_type:
            case 1:
                return Pipe1(self.image)
            case 2:
                return Pipe2(self.image)
            case 3:
                return Pipe3(self.image)
            case _:
                print("Invalid pipeline type")
                return None



from abc import abstractmethod
class Pipeline:
    
    @abstractmethod
    def pipe(self):
        pass
    

class Pipe1(Pipeline):
    
    def __init__(self, image):
        self.image = image
        self.filter = imF.Filter()
        
    def get_image(self):   
        return self.image

    
    def pipe(self):
        print("Pipe1")
        self.image = self.filter.invert_image(self.image)
        
        
        
    
class Pipe2(Pipeline):
    
    def __init__(self, image):
        self.image = image
        self.filter = imF.Filter()
    
    def pipe(self):
        print("Pipe2")
        self.image = self.filter.remove_noise(self.image)
        
class Pipe3(Pipeline):
    
    def __init__(self, image):
        self.image = image
        self.filter = imF.Filter()
    
    def pipe(self):
        print("Pipe3")

import PIL.Image as Image 

if __name__=="__main__":
    image_file = "TutorAI/backend/flashcards/text_scraper/assets/page_01_rotated.jpg"
    image = cv2.imread(image_file)
    factory = PipelineFactory(image)
    pipe = factory.create_pipeline(1)
    pipe.pipe()
    filtered_image = pipe.get_image() 
    
    filter = imF.Filter() 
    filter.display(filtered_image)
    
    
    #kan endre arkitekturen, slik at filter får inn bildet, og pipe får inn filter, eller så må filter ikke ta inn et bilde, men pipeline gjør det. Tror det er det beste. 
    
    
    
    
    
    
    
    